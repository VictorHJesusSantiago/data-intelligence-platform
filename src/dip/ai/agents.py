from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any, Callable

from .guardrails import Guardrails


@dataclass(frozen=True, slots=True)
class AgentTool:
    name: str
    description: str
    handler: Callable[[dict[str, Any]], Any]
    required: tuple[str, ...] = ()


class AgentRuntime:
    """Auditable agent runtime that invokes only explicitly registered tools."""

    def __init__(self, guardrails: Guardrails | None = None, max_steps: int = 6):
        self.guardrails = guardrails or Guardrails()
        self.max_steps = max_steps
        self.tools: dict[str, AgentTool] = {}

    def register(self, tool: AgentTool) -> None:
        if not re.fullmatch(r"[a-z][a-z0-9_]{1,40}", tool.name):
            raise ValueError("tool name must be snake_case")
        if tool.name in self.tools:
            raise ValueError(f"tool already registered: {tool.name}")
        self.tools[tool.name] = tool

    def run(self, goal: str, steps: list[dict[str, Any]]) -> dict[str, Any]:
        self.guardrails.require_safe(goal)
        if len(steps) > self.max_steps:
            raise ValueError(f"agent plan exceeds the {self.max_steps}-step limit")
        trace, memory = [], {}
        for number, step in enumerate(steps, 1):
            name, arguments = step.get("tool"), dict(step.get("arguments", {}))
            tool = self.tools.get(name)
            if not tool:
                raise ValueError(f"agent tool is not allowed: {name}")
            missing = [field for field in tool.required if field not in arguments]
            if missing:
                raise ValueError(f"missing arguments for {name}: {', '.join(missing)}")
            for key, value in list(arguments.items()):
                if isinstance(value, str) and value.startswith("$memory."):
                    arguments[key] = memory.get(value.removeprefix("$memory."))
            try:
                output = tool.handler(arguments)
                status = "succeeded"
            except Exception as exc:
                output, status = {"error": str(exc)}, "failed"
            save_as = step.get("save_as")
            if save_as:
                memory[save_as] = output
            trace.append({"step": number, "tool": name, "arguments": arguments,
                          "status": status, "output": output})
            if status == "failed" and not step.get("continue_on_error", False):
                break
        return {"goal": goal, "status": "succeeded" if trace and trace[-1]["status"] == "succeeded" else "failed",
                "steps": trace, "memory": memory}

    def catalog(self) -> list[dict[str, Any]]:
        return [{"name": tool.name, "description": tool.description,
                 "required": list(tool.required)} for tool in self.tools.values()]
