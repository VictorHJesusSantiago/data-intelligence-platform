from __future__ import annotations

from collections import Counter
from typing import Any

from .embeddings import cosine, embed


class RecommendationEngine:
    """Hybrid content and behavioral recommendation with explanations."""

    def rank(self, items: list[dict[str, Any]], profile: dict[str, Any], limit: int = 10,
             interactions: list[dict[str, Any]] | None = None) -> list[dict[str, Any]]:
        if not items:
            return []
        interests = " ".join(map(str, profile.get("interests", [])))
        interests += " " + str(profile.get("query", ""))
        profile_vector = embed(interests)
        affinity = Counter()
        for event in interactions or []:
            affinity[str(event.get("item_id"))] += float(event.get("weight", 1.0))
        maximum = max(affinity.values(), default=1.0)
        ranked = []
        for item in items:
            description = " ".join(map(str, [item.get("title", ""), item.get("description", ""),
                                                   *item.get("tags", [])]))
            content_score = max(0.0, cosine(profile_vector, embed(description)))
            behavior_score = affinity[str(item.get("id"))] / maximum
            score = 0.75 * content_score + 0.25 * behavior_score
            ranked.append({"item": item, "score": round(score, 6),
                           "explanation": {"content_affinity": round(content_score, 6),
                                           "behavior_affinity": round(behavior_score, 6)}})
        return sorted(ranked, key=lambda value: (-value["score"], str(value["item"].get("id"))))[:limit]
