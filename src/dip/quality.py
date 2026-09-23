from __future__ import annotations

import re
from typing import Any

from .models import QualityRule, new_id, utc_now
from .storage import Storage


class QualityEngine:
    def __init__(self, storage: Storage):
        self.storage = storage

    def evaluate_rule(self, rows: list[dict[str, Any]], rule: QualityRule) -> dict[str, Any]:
        outcomes = []
        for index, row in enumerate(rows):
            value = row.get(rule.field)
            if rule.kind == "required":
                passed = value not in (None, "")
            elif rule.kind == "unique":
                passed = sum(item.get(rule.field) == value for item in rows) == 1
            elif rule.kind == "regex":
                passed = bool(re.fullmatch(rule.expression, str(value or "")))
            elif rule.kind == "minimum":
                passed = isinstance(value, (int, float)) and value >= rule.threshold
            elif rule.kind == "maximum":
                passed = isinstance(value, (int, float)) and value <= rule.threshold
            else:
                passed = False
            outcomes.append({"row": index, "passed": passed, "value": value})
        score = sum(item["passed"] for item in outcomes) / max(1, len(outcomes))
        return {"rule": rule.name, "kind": rule.kind, "field": rule.field,
                "score": round(score, 4), "passed": score >= rule.threshold if rule.kind not in {"minimum", "maximum"} else all(item["passed"] for item in outcomes),
                "failures": [item for item in outcomes if not item["passed"]]}

    def run(self, asset_id: str, rows: list[dict[str, Any]], rules: list[QualityRule]) -> dict[str, Any]:
        results = [self.evaluate_rule(rows, rule) for rule in rules]
        score = sum(item["score"] for item in results) / max(1, len(results))
        passed = all(item["passed"] for item in results)
        result = {"id": new_id("qrun"), "asset_id": asset_id, "score": round(score, 4),
                  "passed": passed, "results": results, "created_at": utc_now()}
        self.storage.execute("INSERT INTO quality_results VALUES (?,?,?,?,?,?)",
                             (result["id"], asset_id, score, int(passed), self.storage.encode(results), result["created_at"]))
        return result
