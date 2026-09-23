from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def new_id(prefix: str) -> str:
    return f"{prefix}_{uuid4().hex[:16]}"


@dataclass(slots=True)
class DataAsset:
    name: str
    domain: str
    owner: str
    description: str = ""
    classification: str = "internal"
    schema: dict[str, str] = field(default_factory=dict)
    tags: list[str] = field(default_factory=list)
    id: str = field(default_factory=lambda: new_id("ast"))
    created_at: str = field(default_factory=utc_now)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class PipelineDefinition:
    name: str
    source: str
    destination: str
    steps: list[dict[str, Any]]
    schedule: str = "manual"
    id: str = field(default_factory=lambda: new_id("pip"))

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class QualityRule:
    name: str
    kind: str
    field: str
    threshold: float = 1.0
    expression: str = ""
    id: str = field(default_factory=lambda: new_id("qlt"))


@dataclass(slots=True)
class QueryResult:
    columns: list[str]
    rows: list[dict[str, Any]]
    elapsed_ms: float
    scanned_rows: int

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
