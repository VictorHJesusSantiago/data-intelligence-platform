from __future__ import annotations

import importlib
import pkgutil
from functools import lru_cache

from . import capabilities
from .sdk import Capability


@lru_cache(maxsize=1)
def discover() -> dict[str, Capability]:
    found: dict[str, Capability] = {}
    prefix = capabilities.__name__ + "."
    for module_info in pkgutil.walk_packages(capabilities.__path__, prefix):
        if module_info.ispkg:
            continue
        module = importlib.import_module(module_info.name)
        capability = getattr(module, "CAPABILITY", None)
        if isinstance(capability, Capability):
            if capability.code in found:
                raise ValueError(f"duplicate capability: {capability.code}")
            found[capability.code] = capability
    return found


def by_family(family: str) -> list[Capability]:
    return sorted((item for item in discover().values() if item.family == family), key=lambda item: item.code)


def execute(code: str, rows: list[dict], context: dict | None = None):
    try:
        capability = discover()[code]
    except KeyError as exc:
        raise KeyError(f"unknown capability: {code}") from exc
    return capability.execute(rows, context)
