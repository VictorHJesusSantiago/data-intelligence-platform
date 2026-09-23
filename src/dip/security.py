from __future__ import annotations

import hashlib
import hmac
import os
from dataclasses import dataclass

from .errors import AuthorizationError


ROLE_PERMISSIONS = {
    "viewer": {"read"},
    "analyst": {"read", "query", "report"},
    "engineer": {"read", "query", "report", "write", "operate"},
    "steward": {"read", "query", "govern", "write"},
    "admin": {"read", "query", "report", "write", "operate", "govern", "admin"},
}


@dataclass(frozen=True, slots=True)
class Principal:
    name: str
    role: str

    def require(self, permission: str) -> None:
        if permission not in ROLE_PERMISSIONS.get(self.role, set()):
            raise AuthorizationError(f"{self.name} lacks permission: {permission}")


def authenticate(candidate: str | None) -> Principal:
    configured = os.getenv("DIP_API_KEY", "development-key")
    if not candidate or not hmac.compare_digest(candidate, configured):
        raise AuthorizationError("invalid API key")
    return Principal("api-client", os.getenv("DIP_API_ROLE", "admin"))


def fingerprint(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()[:16]


def mask(value: object, visible: int = 4) -> str:
    text = str(value)
    return "*" * max(0, len(text) - visible) + text[-visible:]
