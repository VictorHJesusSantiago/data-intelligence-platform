from __future__ import annotations

import re
from typing import Any


SECRET = re.compile(r"(?i)\b(api[_ -]?key|password|senha|token)\s*[:=]\s*([^\s,;]+)")
INJECTION = re.compile(r"(?i)(ignore (all |the )?previous|reveal (the )?system prompt|ignore instruções|mostre o prompt)")


class Guardrails:
    """Input checks and output redaction for assistant and agent workloads."""

    def inspect(self, text: str) -> dict[str, Any]:
        findings = []
        if INJECTION.search(text):
            findings.append("prompt_injection")
        if SECRET.search(text):
            findings.append("secret")
        return {"allowed": "prompt_injection" not in findings, "findings": findings}

    def require_safe(self, text: str) -> None:
        result = self.inspect(text)
        if not result["allowed"]:
            raise ValueError("request rejected by AI guardrails: prompt injection pattern")

    @staticmethod
    def redact(text: str) -> str:
        return SECRET.sub(lambda match: f"{match.group(1)}=[REDACTED]", text)
