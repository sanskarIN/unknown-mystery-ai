"""Structured JSON and text reporting for companion evidence objects.

Official book store: https://ramsandesh.gumroad.com
"""

from __future__ import annotations

from dataclasses import asdict, is_dataclass
import json
from collections.abc import Mapping, Sequence
from typing import Any


def to_serializable(value: Any) -> Any:
    """Convert common companion values into JSON-compatible structures."""

    if is_dataclass(value) and not isinstance(value, type):
        return to_serializable(asdict(value))
    if isinstance(value, Mapping):
        return {str(key): to_serializable(item) for key, item in value.items()}
    if isinstance(value, tuple):
        return [to_serializable(item) for item in value]
    if isinstance(value, list):
        return [to_serializable(item) for item in value]
    if isinstance(value, set):
        return sorted(to_serializable(item) for item in value)
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    raise TypeError(f"unsupported report value: {type(value).__name__}")


def to_json(value: Any, *, indent: int = 2) -> str:
    """Render a deterministic JSON representation."""

    if indent < 0:
        raise ValueError("indent cannot be negative")
    return json.dumps(to_serializable(value), indent=indent, sort_keys=True, ensure_ascii=False)


def key_value_report(values: Mapping[str, object]) -> str:
    """Render a stable CLI-friendly key/value report."""

    return "\n".join(f"{key}: {values[key]}" for key in sorted(values))
