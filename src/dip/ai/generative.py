from __future__ import annotations

from typing import Any

from ..models import new_id, utc_now
from ..storage import Storage
from .guardrails import Guardrails
from .providers import LanguageModel, LocalGroundedModel
from .vector_store import VectorStore


class Assistant:
    """Conversational RAG assistant with persisted history, citations and guardrails."""

    def __init__(self, storage: Storage, vectors: VectorStore,
                 model: LanguageModel | None = None, guardrails: Guardrails | None = None):
        self.storage = storage
        self.vectors = vectors
        self.model = model or LocalGroundedModel()
        self.guardrails = guardrails or Guardrails()

    def ask(self, question: str, collection: str = "knowledge",
            conversation_id: str | None = None, limit: int = 5) -> dict[str, Any]:
        self.guardrails.require_safe(question)
        if not conversation_id:
            conversation_id = new_id("con")
            self.storage.execute("INSERT INTO ai_conversations VALUES (?,?,?)",
                                 (conversation_id, question[:80], utc_now()))
        elif not self.storage.one("SELECT id FROM ai_conversations WHERE id=?", (conversation_id,)):
            raise ValueError("conversation does not exist")
        history = self.history(conversation_id)
        context = self.vectors.search(collection, question, limit)
        self._message(conversation_id, "user", question, {})
        answer = self.guardrails.redact(self.model.generate(question, context, history))
        citations = [{"id": item["id"], "score": item["score"], "metadata": item["metadata"]}
                     for item in context if item["score"] > 0]
        self._message(conversation_id, "assistant", answer,
                      {"model": self.model.name, "citations": citations})
        return {"conversation_id": conversation_id, "answer": answer, "citations": citations,
                "model": self.model.name, "grounded": bool(citations)}

    def history(self, conversation_id: str) -> list[dict[str, Any]]:
        rows = self.storage.query(
            "SELECT role,content,context_json,created_at FROM ai_messages "
            "WHERE conversation_id=? ORDER BY created_at,id", (conversation_id,)
        )
        for row in rows:
            row["context"] = self.storage.decode(row.pop("context_json"))
        return rows

    def _message(self, conversation_id: str, role: str, content: str, context: dict) -> None:
        self.storage.execute("INSERT INTO ai_messages VALUES (?,?,?,?,?,?)", (
            new_id("msg"), conversation_id, role, content, self.storage.encode(context), utc_now()
        ))
