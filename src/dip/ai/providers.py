from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from .embeddings import cosine, embed


class LanguageModel(Protocol):
    name: str

    def generate(self, prompt: str, context: list[dict], history: list[dict]) -> str: ...


@dataclass(slots=True)
class LocalGroundedModel:
    """Offline extractive language model that only answers from supplied context."""

    name: str = "local-grounded-v1"

    def generate(self, prompt: str, context: list[dict], history: list[dict]) -> str:
        if not context:
            return "Não encontrei informação suficiente na base de conhecimento para responder com segurança."
        query = embed(prompt)
        candidates: list[tuple[float, str, str]] = []
        for document in context:
            sentences = [part.strip() for part in document["text"].replace("\n", " ").split(".") if part.strip()]
            for sentence in sentences:
                candidates.append((cosine(query, embed(sentence)), sentence, document["id"]))
        selected = sorted(candidates, key=lambda item: (-item[0], item[2]))[:3]
        useful = [item for item in selected if item[0] > 0]
        if not useful:
            return "Os documentos recuperados não contêm evidência diretamente relacionada à pergunta."
        body = ". ".join(sentence.rstrip(".!?") for _, sentence, _ in useful) + "."
        sources = ", ".join(dict.fromkeys(identifier for _, _, identifier in useful))
        return f"{body}\n\nFontes: {sources}"
