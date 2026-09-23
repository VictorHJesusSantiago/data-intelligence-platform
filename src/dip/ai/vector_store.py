from __future__ import annotations

from typing import Any

from ..models import new_id, utc_now
from ..storage import Storage
from .embeddings import cosine, embed


class VectorStore:
    """Persistent vector database implemented on the platform control plane."""

    def __init__(self, storage: Storage, dimensions: int = 192):
        self.storage = storage
        self.dimensions = dimensions

    def upsert(self, collection: str, text: str, metadata: dict[str, Any] | None = None,
               document_id: str | None = None) -> dict[str, Any]:
        if not collection.strip() or not text.strip():
            raise ValueError("collection and text are required")
        identifier = document_id or new_id("vec")
        values = embed(text, self.dimensions)
        self.storage.execute(
            "INSERT OR REPLACE INTO vector_documents VALUES (?,?,?,?,?,?)",
            (identifier, collection, text, self.storage.encode(metadata or {}),
             self.storage.encode(values), utc_now()),
        )
        return {"id": identifier, "collection": collection, "dimensions": len(values)}

    def search(self, collection: str, query: str, limit: int = 5,
               filters: dict[str, Any] | None = None) -> list[dict[str, Any]]:
        if not 1 <= limit <= 100:
            raise ValueError("limit must be between 1 and 100")
        target = embed(query, self.dimensions)
        results = []
        for row in self.storage.query(
            "SELECT id,text,metadata_json,vector_json,created_at FROM vector_documents WHERE collection=?",
            (collection,),
        ):
            metadata = self.storage.decode(row["metadata_json"])
            if filters and any(metadata.get(key) != value for key, value in filters.items()):
                continue
            results.append({
                "id": row["id"], "text": row["text"], "metadata": metadata,
                "score": round(cosine(target, self.storage.decode(row["vector_json"])), 6),
                "created_at": row["created_at"],
            })
        return sorted(results, key=lambda item: (-item["score"], item["id"]))[:limit]

    def delete(self, collection: str, document_id: str) -> bool:
        return bool(self.storage.execute(
            "DELETE FROM vector_documents WHERE collection=? AND id=?", (collection, document_id)
        ))

    def collections(self) -> list[dict[str, Any]]:
        return self.storage.query(
            "SELECT collection,COUNT(*) AS documents FROM vector_documents GROUP BY collection ORDER BY collection"
        )
