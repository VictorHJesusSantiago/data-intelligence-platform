from __future__ import annotations

from typing import Any

from .models import utc_now
from .storage import Storage


class Observability:
    def __init__(self, storage: Storage):
        self.storage = storage

    def record(self, name: str, value: float, labels: dict[str, str] | None = None) -> None:
        self.storage.execute("INSERT INTO metrics VALUES (?,?,?,?)", (name, value, self.storage.encode(labels or {}), utc_now()))

    def health(self) -> dict[str, Any]:
        counts = {}
        for table in ("assets", "datasets", "pipelines", "jobs", "quality_results", "events", "alerts"):
            counts[table] = self.storage.one(f"SELECT COUNT(*) AS count FROM {table}")["count"]
        failed = self.storage.one("SELECT COUNT(*) AS count FROM jobs WHERE status='failed'")["count"]
        open_alerts = self.storage.one("SELECT COUNT(*) AS count FROM alerts WHERE status='open'")["count"]
        return {"status": "healthy" if not failed else "degraded", "counts": counts,
                "failed_jobs": failed, "open_alerts": open_alerts, "checked_at": utc_now()}
