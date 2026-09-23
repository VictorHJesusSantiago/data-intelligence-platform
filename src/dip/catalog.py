from __future__ import annotations

from typing import Any

from .models import DataAsset
from .storage import Storage


class Catalog:
    def __init__(self, storage: Storage):
        self.storage = storage

    def register(self, asset: DataAsset) -> dict[str, Any]:
        self.storage.execute(
            "INSERT OR REPLACE INTO assets VALUES (?,?,?,?,?,?,?,?,?)",
            (asset.id, asset.name, asset.domain, asset.owner, asset.description,
             asset.classification, self.storage.encode(asset.schema),
             self.storage.encode(asset.tags), asset.created_at),
        )
        return asset.to_dict()

    def list(self, search: str = "", domain: str = "") -> list[dict[str, Any]]:
        clauses, params = [], []
        if search:
            clauses.append("(name LIKE ? OR description LIKE ? OR tags_json LIKE ?)")
            params.extend([f"%{search}%"] * 3)
        if domain:
            clauses.append("domain = ?")
            params.append(domain)
        where = " WHERE " + " AND ".join(clauses) if clauses else ""
        rows = self.storage.query("SELECT * FROM assets" + where + " ORDER BY name", tuple(params))
        for row in rows:
            row["schema"] = self.storage.decode(row.pop("schema_json"))
            row["tags"] = self.storage.decode(row.pop("tags_json"))
        return rows

    def get_by_name(self, name: str) -> dict[str, Any] | None:
        return next(iter(self.list(search=name)), None)

    def lineage(self) -> list[dict[str, Any]]:
        return self.storage.query("SELECT * FROM lineage_edges ORDER BY created_at DESC")
