from __future__ import annotations

from typing import Any

from .models import utc_now
from .storage import Storage


class Governance:
    RETENTION_DAYS = {"public": 3650, "internal": 1825, "confidential": 730, "restricted": 365}

    def __init__(self, storage: Storage):
        self.storage = storage

    def policy_for(self, classification: str) -> dict[str, Any]:
        if classification not in self.RETENTION_DAYS:
            raise ValueError(f"unknown classification: {classification}")
        return {"classification": classification, "retention_days": self.RETENTION_DAYS[classification],
                "encryption_required": classification in {"confidential", "restricted"},
                "approval_required": classification == "restricted"}

    def audit(self, actor: str, action: str, resource: str, details: dict[str, Any] | None = None) -> None:
        self.storage.execute("INSERT INTO audit_log(actor,action,resource,details_json,created_at) VALUES(?,?,?,?,?)",
                             (actor, action, resource, self.storage.encode(details or {}), utc_now()))
