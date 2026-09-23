from __future__ import annotations

import math
import time
from statistics import mean
from typing import Any

from ..models import new_id, utc_now
from ..storage import Storage


def _number(value: Any, field: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"feature {field!r} must be numeric")
    result = float(value)
    if not math.isfinite(result):
        raise ValueError(f"feature {field!r} must be finite")
    return result


def _matrix(rows: list[dict[str, Any]], features: list[str]) -> list[list[float]]:
    if not rows or not features:
        raise ValueError("training rows and features are required")
    return [[_number(row.get(field), field) for field in features] for row in rows]


def _standardize(matrix: list[list[float]]) -> tuple[list[list[float]], list[float], list[float]]:
    columns = list(zip(*matrix))
    centers = [mean(column) for column in columns]
    scales = [math.sqrt(mean((value - center) ** 2 for value in column)) or 1.0
              for column, center in zip(columns, centers)]
    normalized = [[(value - centers[index]) / scales[index] for index, value in enumerate(row)]
                  for row in matrix]
    return normalized, centers, scales


def _linear_train(x: list[list[float]], y: list[float], logistic: bool,
                  iterations: int = 800, learning_rate: float = 0.08) -> tuple[list[float], float]:
    weights, bias = [0.0] * len(x[0]), 0.0
    for _ in range(iterations):
        weight_gradient, bias_gradient = [0.0] * len(weights), 0.0
        for row, target in zip(x, y):
            raw = bias + sum(weight * value for weight, value in zip(weights, row))
            predicted = 1.0 / (1.0 + math.exp(-max(-30.0, min(30.0, raw)))) if logistic else raw
            error = predicted - target
            bias_gradient += error
            for index, value in enumerate(row):
                weight_gradient[index] += error * value
        size = len(x)
        bias -= learning_rate * bias_gradient / size
        weights = [weight - learning_rate * gradient / size
                   for weight, gradient in zip(weights, weight_gradient)]
    return weights, bias


def _distance(left: list[float], right: list[float]) -> float:
    return sum((a - b) ** 2 for a, b in zip(left, right))


class ModelPlatform:
    """AutoML, model registry, serving, drift checks and LLMOps metadata."""

    TASKS = {"regression", "binary_classification", "clustering"}

    def __init__(self, storage: Storage):
        self.storage = storage

    def automl(self, name: str, rows: list[dict[str, Any]], target: str,
               owner: str = "system", description: str = "") -> dict[str, Any]:
        """Infer a supervised task and usable numeric features, then train it."""
        if not rows or target not in rows[0]:
            raise ValueError("rows and a valid target are required")
        features = [field for field, value in rows[0].items()
                    if field != target and isinstance(value, (int, float)) and not isinstance(value, bool)
                    and all(isinstance(row.get(field), (int, float)) and not isinstance(row.get(field), bool)
                            for row in rows)]
        if not features:
            raise ValueError("AutoML did not find complete numeric features")
        unique_targets = {str(row.get(target)) for row in rows}
        task = "binary_classification" if len(unique_targets) == 2 else "regression"
        if task == "regression" and not all(
            isinstance(row.get(target), (int, float)) and not isinstance(row.get(target), bool) for row in rows
        ):
            raise ValueError("AutoML supports binary labels or numeric regression targets")
        result = self.train(name, task, rows, features, target, owner, description)
        result["automl"] = {"inferred_task": task, "selected_features": features}
        return result

    def train(self, name: str, task: str, rows: list[dict[str, Any]], features: list[str],
              target: str | None = None, owner: str = "system", description: str = "",
              clusters: int = 3) -> dict[str, Any]:
        if task not in self.TASKS:
            raise ValueError(f"task must be one of {sorted(self.TASKS)}")
        matrix, centers, scales = (*_standardize(_matrix(rows, features)),)
        normalized = matrix
        if task == "clustering":
            if not 2 <= clusters <= min(20, len(rows)):
                raise ValueError("clusters must be between 2 and the number of rows")
            centroids = [normalized[index * len(normalized) // clusters][:] for index in range(clusters)]
            assignments = [0] * len(normalized)
            for _ in range(50):
                updated = [min(range(clusters), key=lambda index: _distance(row, centroids[index]))
                           for row in normalized]
                if updated == assignments:
                    break
                assignments = updated
                for cluster in range(clusters):
                    members = [row for row, assignment in zip(normalized, assignments) if assignment == cluster]
                    if members:
                        centroids[cluster] = [mean(column) for column in zip(*members)]
            inertia = sum(_distance(row, centroids[assignment])
                          for row, assignment in zip(normalized, assignments))
            artifact = {"features": features, "centers": centers, "scales": scales,
                        "centroids": centroids}
            metrics = {"inertia": round(inertia, 8), "clusters": clusters}
            algorithm = "kmeans"
        else:
            if not target:
                raise ValueError("target is required for supervised learning")
            if task == "binary_classification":
                labels = sorted({str(row.get(target)) for row in rows})
                if len(labels) != 2:
                    raise ValueError("binary classification requires exactly two target labels")
                y = [float(str(row.get(target)) == labels[1]) for row in rows]
                weights, bias = _linear_train(normalized, y, True)
                probabilities = [self._score(row, weights, bias, True) for row in normalized]
                predicted = [labels[int(value >= 0.5)] for value in probabilities]
                accuracy = mean(float(value == str(row.get(target))) for value, row in zip(predicted, rows))
                artifact = {"features": features, "target": target, "centers": centers, "scales": scales,
                            "weights": weights, "bias": bias, "labels": labels}
                metrics = {"accuracy": round(accuracy, 8)}
                algorithm = "logistic_regression"
            else:
                y = [_number(row.get(target), target) for row in rows]
                weights, bias = _linear_train(normalized, y, False, learning_rate=0.04)
                predicted = [self._score(row, weights, bias, False) for row in normalized]
                mse = mean((actual - estimate) ** 2 for actual, estimate in zip(y, predicted))
                variance = sum((actual - mean(y)) ** 2 for actual in y)
                r2 = 1 - sum((actual - estimate) ** 2 for actual, estimate in zip(y, predicted)) / variance if variance else 1.0
                artifact = {"features": features, "target": target, "centers": centers, "scales": scales,
                            "weights": weights, "bias": bias}
                metrics = {"mean_squared_error": round(mse, 8), "r2": round(r2, 8)}
                algorithm = "linear_regression"
        model = self.storage.one("SELECT * FROM ai_models WHERE name=?", (name,))
        if model and model["task"] != task:
            raise ValueError("an existing model cannot change task")
        if not model:
            model = {"id": new_id("mdl"), "name": name, "task": task}
            self.storage.execute("INSERT INTO ai_models VALUES (?,?,?,?,?,?)",
                                 (model["id"], name, task, description, owner, utc_now()))
        latest = self.storage.one(
            "SELECT COALESCE(MAX(version),0) AS version FROM ai_model_versions WHERE model_id=?",
            (model["id"],),
        )
        version = int(latest["version"]) + 1
        version_id = new_id("mvr")
        self.storage.execute("INSERT INTO ai_model_versions VALUES (?,?,?,?,?,?,?,?)", (
            version_id, model["id"], version, algorithm, self.storage.encode(artifact),
            self.storage.encode(metrics), len(rows), utc_now(),
        ))
        return {"model_id": model["id"], "name": name, "task": task, "version": version,
                "algorithm": algorithm, "metrics": metrics, "training_rows": len(rows)}

    @staticmethod
    def _score(row: list[float], weights: list[float], bias: float, logistic: bool) -> float:
        raw = bias + sum(weight * value for weight, value in zip(weights, row))
        return 1.0 / (1.0 + math.exp(-max(-30.0, min(30.0, raw)))) if logistic else raw

    def deploy(self, name: str, version: int | None = None, environment: str = "production",
               traffic: float = 1.0) -> dict[str, Any]:
        if not 0 < traffic <= 1:
            raise ValueError("traffic must be greater than 0 and at most 1")
        model = self._model(name)
        selected = self._version(model["id"], version)
        deployment_id = new_id("dep")
        self.storage.execute(
            "INSERT INTO ai_deployments VALUES (?,?,?,?,?,?,?) "
            "ON CONFLICT(model_id,environment) DO UPDATE SET version=excluded.version,status='active',"
            "traffic=excluded.traffic,created_at=excluded.created_at",
            (deployment_id, model["id"], selected["version"], environment, "active", traffic, utc_now()),
        )
        return {"model": name, "version": selected["version"], "environment": environment,
                "status": "active", "traffic": traffic}

    def predict(self, name: str, rows: list[dict[str, Any]], environment: str = "production",
                version: int | None = None) -> dict[str, Any]:
        started = time.perf_counter()
        model = self._model(name)
        if version is None:
            deployment = self.storage.one(
                "SELECT version FROM ai_deployments WHERE model_id=? AND environment=? AND status='active'",
                (model["id"], environment),
            )
            if not deployment:
                raise ValueError(f"model {name!r} is not deployed in {environment!r}")
            version = deployment["version"]
        selected = self._version(model["id"], version)
        artifact = self.storage.decode(selected["artifact_json"])
        matrix = _matrix(rows, artifact["features"])
        normalized = [[(value - artifact["centers"][index]) / artifact["scales"][index]
                       for index, value in enumerate(row)] for row in matrix]
        if model["task"] == "clustering":
            predictions = [{"cluster": min(range(len(artifact["centroids"])),
                                            key=lambda index: _distance(row, artifact["centroids"][index]))}
                           for row in normalized]
        elif model["task"] == "binary_classification":
            probabilities = [self._score(row, artifact["weights"], artifact["bias"], True)
                             for row in normalized]
            predictions = [{"label": artifact["labels"][int(probability >= 0.5)],
                            "probability": round(probability, 8)} for probability in probabilities]
        else:
            predictions = [{"value": self._score(row, artifact["weights"], artifact["bias"], False)}
                           for row in normalized]
        latency = (time.perf_counter() - started) * 1000
        self.storage.execute("INSERT INTO ai_predictions VALUES (?,?,?,?,?,?,?)", (
            new_id("prd"), model["id"], selected["version"], self.storage.encode(rows),
            self.storage.encode(predictions), latency, utc_now(),
        ))
        return {"model": name, "version": selected["version"], "predictions": predictions,
                "latency_ms": round(latency, 4)}

    def drift(self, name: str, rows: list[dict[str, Any]], version: int | None = None) -> dict[str, Any]:
        model = self._model(name)
        artifact = self.storage.decode(self._version(model["id"], version)["artifact_json"])
        matrix = _matrix(rows, artifact["features"])
        shifts = {}
        for index, field in enumerate(artifact["features"]):
            current = mean(row[index] for row in matrix)
            shifts[field] = round(abs(current - artifact["centers"][index]) / artifact["scales"][index], 6)
        maximum = max(shifts.values(), default=0.0)
        return {"model": name, "drift_detected": maximum >= 1.0, "maximum_shift": maximum,
                "feature_shifts": shifts}

    def list(self) -> list[dict[str, Any]]:
        models = self.storage.query(
            "SELECT m.*,COUNT(v.id) AS versions FROM ai_models m LEFT JOIN ai_model_versions v "
            "ON v.model_id=m.id GROUP BY m.id ORDER BY m.name"
        )
        for model in models:
            model["deployments"] = self.storage.query(
                "SELECT version,environment,status,traffic,created_at FROM ai_deployments WHERE model_id=?",
                (model["id"],),
            )
        return models

    def _model(self, name: str) -> dict[str, Any]:
        model = self.storage.one("SELECT * FROM ai_models WHERE name=?", (name,))
        if not model:
            raise ValueError(f"unknown model: {name}")
        return model

    def _version(self, model_id: str, version: int | None) -> dict[str, Any]:
        if version is None:
            record = self.storage.one(
                "SELECT * FROM ai_model_versions WHERE model_id=? ORDER BY version DESC LIMIT 1",
                (model_id,),
            )
        else:
            record = self.storage.one(
                "SELECT * FROM ai_model_versions WHERE model_id=? AND version=?", (model_id, version)
            )
        if not record:
            raise ValueError("model version does not exist")
        return record
