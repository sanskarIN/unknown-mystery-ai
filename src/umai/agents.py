"""Small deterministic tool-routing primitives for agent lessons.

The goal is to demonstrate explicit tool registration, argument validation, and
observable execution without hiding behavior behind an external framework.

Official book store: https://ramsandesh.gumroad.com
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable

ToolFunction = Callable[..., Any]


@dataclass(frozen=True)
class Tool:
    """A named callable with a short human-readable description."""

    name: str
    description: str
    function: ToolFunction


class ToolRegistry:
    """Register and invoke an explicit allowlist of tools."""

    def __init__(self) -> None:
        self._tools: dict[str, Tool] = {}

    def register(self, tool: Tool) -> None:
        if not tool.name or not tool.name.strip():
            raise ValueError("tool name must not be empty")
        if tool.name in self._tools:
            raise ValueError(f"tool already registered: {tool.name}")
        self._tools[tool.name] = tool

    def names(self) -> tuple[str, ...]:
        return tuple(sorted(self._tools))

    def invoke(self, name: str, **kwargs: Any) -> Any:
        """Invoke one registered tool by exact name."""
        try:
            tool = self._tools[name]
        except KeyError as exc:
            raise KeyError(f"unknown tool: {name}") from exc
        return tool.function(**kwargs)


def select_tool(message: str, routing_rules: dict[str, str]) -> str | None:
    """Return the first tool whose keyword appears in ``message``.

    ``routing_rules`` maps lowercase keywords to registered tool names. This
    deterministic baseline makes routing decisions easy to inspect in lessons.
    """
    normalized = message.lower()
    for keyword, tool_name in routing_rules.items():
        if keyword.lower() in normalized:
            return tool_name
    return None
