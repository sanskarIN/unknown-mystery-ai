"""Deterministic allowlisted tool-routing sandbox."""

from __future__ import annotations

import argparse

from umai import to_json
from umai.agents import Tool, ToolRegistry, select_tool


def word_count(*, text: str) -> dict[str, int]:
    return {"words": len(text.split())}


def character_count(*, text: str) -> dict[str, int]:
    return {"characters": len(text)}


def uppercase(*, text: str) -> dict[str, str]:
    return {"text": text.upper()}


def build_registry() -> ToolRegistry:
    registry = ToolRegistry()
    registry.register(Tool("word_count", "Count whitespace-separated words.", word_count))
    registry.register(Tool("character_count", "Count characters.", character_count))
    registry.register(Tool("uppercase", "Convert text to uppercase.", uppercase))
    return registry


def route(message: str, text: str) -> dict[str, object]:
    registry = build_registry()
    rules = {
        "word": "word_count",
        "character": "character_count",
        "uppercase": "uppercase",
    }
    selected = select_tool(message, rules)
    if selected is None:
        return {"selected_tool": None, "available_tools": list(registry.names()), "result": None}
    return {
        "selected_tool": selected,
        "available_tools": list(registry.names()),
        "result": registry.invoke(selected, text=text),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Route a request to a tiny explicit local tool registry.")
    parser.add_argument("--message", default="Please count the words")
    parser.add_argument("--text", default="Transparent tools are easier to inspect and test.")
    args = parser.parse_args()
    print(to_json(route(args.message, args.text)))


if __name__ == "__main__":
    main()
