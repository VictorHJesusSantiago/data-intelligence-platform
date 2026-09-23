from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from statistics import mean
from typing import Any, Callable


Rows = list[dict[str, Any]]


def _profile(rows: Rows, config: dict[str, Any]) -> dict[str, Any]:
    fields = sorted({key for row in rows for key in row})
    return {"rows": len(rows), "fields": fields, "nulls": {f: sum(r.get(f) is None for r in rows) for f in fields}}


def _filter(rows: Rows, config: dict[str, Any]) -> Rows:
    field = config["field"]
    return [row.copy() for row in rows if row.get(field) not in (None, "")]


def _project(rows: Rows, config: dict[str, Any]) -> Rows:
    fields = config.get("fields", [])
    return [{field: row.get(field) for field in fields} for row in rows]


def _derive(rows: Rows, config: dict[str, Any]) -> Rows:
    target = config.get("target", "derived_value")
    source = config.get("field", "value")
    factor = float(config.get("factor", 1))
    result = []
    for row in rows:
        item = row.copy()
        value = item.get(source, 0)
        item[target] = value * factor if isinstance(value, (int, float)) else str(value).upper()
        result.append(item)
    return result


def _aggregate(rows: Rows, config: dict[str, Any]) -> dict[str, Any]:
    field = config.get("field", "value")
    values = [float(row[field]) for row in rows if isinstance(row.get(field), (int, float))]
    return {"field": field, "count": len(values), "sum": sum(values), "average": mean(values) if values else 0}


def _validate(rows: Rows, config: dict[str, Any]) -> dict[str, Any]:
    field, minimum, maximum = config.get("field", "value"), config.get("minimum", 0), config.get("maximum", 1_000_000)
    invalid = [index for index, row in enumerate(rows) if not isinstance(row.get(field), (int, float)) or not minimum <= row[field] <= maximum]
    return {"passed": not invalid, "invalid_rows": invalid, "score": 1 - len(invalid) / max(1, len(rows))}


def _dedupe(rows: Rows, config: dict[str, Any]) -> Rows:
    field, seen, output = config.get("field", "id"), set(), []
    for row in rows:
        marker = row.get(field)
        if marker not in seen:
            seen.add(marker)
            output.append(row.copy())
    return output


def _mask(rows: Rows, config: dict[str, Any]) -> Rows:
    field = config.get("field", "email")
    output = []
    for row in rows:
        item = row.copy()
        if field in item:
            item[field] = "***" + str(item[field])[-4:]
        output.append(item)
    return output


def _classify(rows: Rows, config: dict[str, Any]) -> dict[str, Any]:
    sensitive = {"email", "phone", "document", "cpf", "ssn", "card"}
    fields = sorted({field for row in rows for field in row})
    return {field: ("restricted" if any(token in field.lower() for token in sensitive) else "internal") for field in fields}


def _timestamp(rows: Rows, config: dict[str, Any]) -> Rows:
    target = config.get("target", "processed_at")
    now = datetime.now(timezone.utc).isoformat()
    return [dict(row, **{target: now}) for row in rows]


HANDLERS: dict[str, Callable[[Rows, dict[str, Any]], Any]] = {
    "profile": _profile, "filter_not_null": _filter, "project": _project,
    "derive": _derive, "aggregate": _aggregate, "validate_range": _validate,
    "dedupe": _dedupe, "mask": _mask, "classify": _classify, "timestamp": _timestamp,
}


@dataclass(frozen=True, slots=True)
class Capability:
    code: str
    family: str
    title: str
    description: str
    operation: str
    configuration: dict[str, Any] = field(default_factory=dict)
    tags: tuple[str, ...] = ()

    def execute(self, rows: Rows, context: dict[str, Any] | None = None) -> Any:
        merged = {**self.configuration, **(context or {})}
        return HANDLERS[self.operation](rows, merged)

    def to_dict(self) -> dict[str, Any]:
        return {"code": self.code, "family": self.family, "title": self.title,
                "description": self.description, "operation": self.operation,
                "configuration": self.configuration, "tags": list(self.tags)}
