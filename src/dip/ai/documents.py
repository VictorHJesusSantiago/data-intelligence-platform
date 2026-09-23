from __future__ import annotations

import csv
import html
import io
import json
import re
from typing import Any

from .nlp import NLP


TAG = re.compile(r"<[^>]+>")
KEY_VALUE = re.compile(r"(?m)^\s*([\w À-ÿ./-]{2,50})\s*[:=]\s*(.+?)\s*$")


class DocumentProcessor:
    """Intelligent document processing for text, HTML, JSON and CSV payloads."""

    def __init__(self, nlp: NLP | None = None):
        self.nlp = nlp or NLP()

    def process(self, content: str | bytes, media_type: str = "text/plain",
                fields: dict[str, str] | None = None) -> dict[str, Any]:
        if isinstance(content, bytes):
            content = content.decode("utf-8", errors="replace")
        text, structured = self._extract(content, media_type.split(";", 1)[0].lower())
        extracted = {match.group(1).strip(): match.group(2).strip() for match in KEY_VALUE.finditer(text)}
        for name, pattern in (fields or {}).items():
            match = re.search(pattern, text, re.IGNORECASE | re.MULTILINE)
            extracted[name] = match.group(1) if match and match.groups() else match.group(0) if match else None
        analysis = self.nlp.analyze(text) if text.strip() else {"entities": [], "keywords": [], "summary": "", "tokens": 0}
        return {
            "media_type": media_type, "text": text, "structured": structured,
            "fields": extracted, "entities": analysis["entities"],
            "summary": analysis["summary"], "keywords": analysis["keywords"],
            "confidence": 1.0 if "�" not in text else 0.8,
        }

    @staticmethod
    def _extract(content: str, media_type: str) -> tuple[str, Any]:
        if media_type in {"application/json", "text/json"}:
            value = json.loads(content)
            return json.dumps(value, ensure_ascii=False, indent=2), value
        if media_type in {"text/csv", "application/csv"}:
            rows = list(csv.DictReader(io.StringIO(content)))
            text = "\n".join("; ".join(f"{key}: {value}" for key, value in row.items()) for row in rows)
            return text, rows
        if media_type in {"text/html", "application/xhtml+xml"}:
            plain = html.unescape(TAG.sub(" ", content))
            return re.sub(r"\s+", " ", plain).strip(), None
        if media_type.startswith("text/") or media_type == "application/octet-stream":
            return content, None
        raise ValueError(f"unsupported media type: {media_type}")
