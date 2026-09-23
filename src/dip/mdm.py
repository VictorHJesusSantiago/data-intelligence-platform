from __future__ import annotations

from collections import Counter
from typing import Any

from .models import new_id, utc_now
from .storage import Storage


class MasterDataManager:
    def __init__(self, storage: Storage):
        self.storage = storage

    def merge(self, entity_type: str, natural_key: str, records: list[dict[str, Any]]) -> dict[str, Any]:
        if not records:
            raise ValueError("at least one source record is required")
        fields = sorted({key for row in records for key in row})
        golden = {}
        for field in fields:
            values = [row[field] for row in records if row.get(field) not in (None, "")]
            golden[field] = Counter(map(str, values)).most_common(1)[0][0] if values else None
        existing = self.storage.one("SELECT id FROM master_records WHERE entity_type=? AND natural_key=?", (entity_type, natural_key))
        record_id = existing["id"] if existing else new_id("mdm")
        self.storage.execute("INSERT OR REPLACE INTO master_records VALUES (?,?,?,?,?,?)",
                             (record_id, entity_type, natural_key, self.storage.encode(golden), len(records), utc_now()))
        return {"id": record_id, "entity_type": entity_type, "natural_key": natural_key,
                "golden": golden, "source_count": len(records)}
