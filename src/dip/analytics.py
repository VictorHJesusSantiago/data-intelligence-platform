from __future__ import annotations

import time
from collections import defaultdict
from typing import Any

from .models import QueryResult


class AnalyticsEngine:
    """Small in-process OLAP engine for grouped measures and decision support."""

    def aggregate(self, rows: list[dict[str, Any]], dimensions: list[str], measure: str,
                  operation: str = "sum") -> QueryResult:
        started = time.perf_counter()
        groups: dict[tuple, list[float]] = defaultdict(list)
        for row in rows:
            value = row.get(measure)
            if isinstance(value, (int, float)):
                groups[tuple(row.get(dimension) for dimension in dimensions)].append(float(value))
        output = []
        for key, values in sorted(groups.items(), key=lambda item: str(item[0])):
            if operation == "sum": result = sum(values)
            elif operation == "avg": result = sum(values) / len(values)
            elif operation == "count": result = len(values)
            elif operation == "min": result = min(values)
            elif operation == "max": result = max(values)
            else: raise ValueError(f"unsupported operation: {operation}")
            output.append({**dict(zip(dimensions, key)), f"{operation}_{measure}": round(result, 4)})
        elapsed = (time.perf_counter() - started) * 1000
        return QueryResult(dimensions + [f"{operation}_{measure}"], output, elapsed, len(rows))

    def recommend(self, metrics: dict[str, float]) -> list[dict[str, Any]]:
        recommendations = []
        if metrics.get("quality_score", 1) < .95:
            recommendations.append({"priority": "high", "action": "Remediate failing quality rules", "reason": "Quality below 95%"})
        if metrics.get("pipeline_failures", 0) > 0:
            recommendations.append({"priority": "high", "action": "Inspect failed pipelines", "reason": "Failures detected"})
        if metrics.get("freshness_hours", 0) > 24:
            recommendations.append({"priority": "medium", "action": "Refresh stale datasets", "reason": "Freshness SLA exceeded"})
        return recommendations or [{"priority": "low", "action": "No intervention required", "reason": "All indicators healthy"}]
