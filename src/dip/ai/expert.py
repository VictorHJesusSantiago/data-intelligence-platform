from __future__ import annotations

from typing import Any


class ExpertSystem:
    """Explainable forward-chaining rules over structured facts."""

    OPERATORS = {
        "eq": lambda left, right: left == right,
        "ne": lambda left, right: left != right,
        "gt": lambda left, right: left is not None and left > right,
        "gte": lambda left, right: left is not None and left >= right,
        "lt": lambda left, right: left is not None and left < right,
        "lte": lambda left, right: left is not None and left <= right,
        "in": lambda left, right: left in right,
        "contains": lambda left, right: right in left if left is not None else False,
    }

    def evaluate(self, facts: dict[str, Any], rules: list[dict[str, Any]],
                 max_cycles: int = 20) -> dict[str, Any]:
        state, fired, explanations = dict(facts), set(), []
        for _ in range(max_cycles):
            changed = False
            for index, rule in enumerate(rules):
                name = str(rule.get("name", f"rule_{index + 1}"))
                if name in fired:
                    continue
                conditions = rule.get("when", [])
                if not all(self._match(state, condition) for condition in conditions):
                    continue
                assignments = rule.get("then", {})
                for field, value in assignments.items():
                    if state.get(field) != value:
                        state[field] = value
                        changed = True
                fired.add(name)
                explanations.append({"rule": name, "conditions": conditions, "asserted": assignments})
            if not changed:
                break
        return {"facts": state, "fired_rules": sorted(fired), "explanations": explanations}

    def _match(self, facts: dict[str, Any], condition: dict[str, Any]) -> bool:
        operator = condition.get("operator", "eq")
        if operator not in self.OPERATORS:
            raise ValueError(f"unknown expert-system operator: {operator}")
        return bool(self.OPERATORS[operator](facts.get(condition["field"]), condition.get("value")))
