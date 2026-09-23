from __future__ import annotations

import re
from collections import Counter
from typing import Any

from .embeddings import tokenize


SENTENCE = re.compile(r"(?<=[.!?])\s+")
EMAIL = re.compile(r"\b[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}\b")
PHONE = re.compile(r"(?<!\w)(?:\+?\d[\d ()-]{7,}\d)")
MONEY = re.compile(r"(?i)(?:R\$|US\$|€|£|\$)\s?\d[\d.,]*")
DATE = re.compile(r"\b(?:\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\d{4}-\d{2}-\d{2})\b")


class NLP:
    """Deterministic NLP for classification, sentiment, entities and summaries."""

    POSITIVE = {"bom", "boa", "excelente", "otimo", "great", "good", "love", "sucesso", "feliz", "recomendo"}
    NEGATIVE = {"ruim", "pessimo", "falha", "erro", "bad", "hate", "problema", "lento", "cancelar", "triste"}
    STOP = {"a", "o", "as", "os", "de", "da", "do", "e", "em", "para", "the", "a", "an", "of", "to", "and", "is"}

    def analyze(self, text: str, labels: dict[str, list[str]] | None = None) -> dict[str, Any]:
        if not text.strip():
            raise ValueError("text is required")
        tokens = tokenize(text)
        score = sum(token in self.POSITIVE for token in tokens) - sum(token in self.NEGATIVE for token in tokens)
        sentiment = "positive" if score > 0 else "negative" if score < 0 else "neutral"
        result: dict[str, Any] = {
            "language": self._language(tokens), "sentiment": {"label": sentiment, "score": score},
            "entities": self.entities(text), "keywords": self.keywords(text),
            "summary": self.summarize(text), "tokens": len(tokens),
        }
        if labels:
            label_scores = {label: sum(token in set(map(str.casefold, words)) for token in tokens)
                            for label, words in labels.items()}
            result["classification"] = max(label_scores, key=lambda item: (label_scores[item], item))
            result["classification_scores"] = label_scores
        return result

    def entities(self, text: str) -> list[dict[str, str]]:
        entities = []
        for kind, pattern in (("email", EMAIL), ("phone", PHONE), ("money", MONEY), ("date", DATE)):
            for match in pattern.finditer(text):
                if kind == "phone" and len(re.sub(r"\D", "", match.group(0))) < 10:
                    continue
                entities.append({"type": kind, "value": match.group(0)})
        return entities

    def keywords(self, text: str, limit: int = 8) -> list[dict[str, Any]]:
        counts = Counter(token for token in tokenize(text) if len(token) > 2 and token not in self.STOP)
        return [{"term": term, "count": count} for term, count in counts.most_common(limit)]

    def summarize(self, text: str, sentences: int = 2) -> str:
        parts = [part.strip() for part in SENTENCE.split(text.strip()) if part.strip()]
        if len(parts) <= sentences:
            return " ".join(parts)
        frequencies = Counter(token for token in tokenize(text) if token not in self.STOP)
        ranked = sorted(enumerate(parts), key=lambda item: (
            -sum(frequencies[token] for token in tokenize(item[1])) / max(1, len(tokenize(item[1]))), item[0]
        ))[:sentences]
        return " ".join(sentence for _, sentence in sorted(ranked))

    @staticmethod
    def _language(tokens: list[str]) -> str:
        portuguese = {"de", "que", "para", "com", "uma", "nao", "dados"}
        english = {"the", "that", "with", "from", "data", "this", "and"}
        pt_score, en_score = sum(token in portuguese for token in tokens), sum(token in english for token in tokens)
        return "pt" if pt_score > en_score else "en" if en_score > pt_score else "und"
