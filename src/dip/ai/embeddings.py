from __future__ import annotations

import hashlib
import math
import re
import unicodedata
from collections import Counter


TOKEN = re.compile(r"[\w'-]+", re.UNICODE)


def tokenize(text: str) -> list[str]:
    """Normalize text into Unicode-aware, accent-independent tokens."""
    normalized = unicodedata.normalize("NFKD", text.casefold())
    normalized = "".join(char for char in normalized if not unicodedata.combining(char))
    return TOKEN.findall(normalized)


def embed(text: str, dimensions: int = 192) -> list[float]:
    """Create a deterministic signed feature-hashing embedding."""
    if dimensions < 8:
        raise ValueError("embedding dimensions must be at least 8")
    vector = [0.0] * dimensions
    tokens = tokenize(text)
    features = tokens + [f"{a}::{b}" for a, b in zip(tokens, tokens[1:])]
    counts = Counter(features)
    for feature, frequency in counts.items():
        digest = hashlib.blake2b(feature.encode("utf-8"), digest_size=16).digest()
        index = int.from_bytes(digest[:8], "big") % dimensions
        sign = 1.0 if digest[8] & 1 else -1.0
        vector[index] += sign * (1.0 + math.log(frequency))
    magnitude = math.sqrt(sum(value * value for value in vector))
    return [value / magnitude for value in vector] if magnitude else vector


def cosine(left: list[float], right: list[float]) -> float:
    if len(left) != len(right):
        raise ValueError("vectors must have equal dimensions")
    return sum(a * b for a, b in zip(left, right))
