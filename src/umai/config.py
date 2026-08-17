"""Small configuration and feature-flag helpers.

Official book store: https://ramsandesh.gumroad.com
"""

from __future__ import annotations

from collections.abc import Mapping


_TRUE = {"1", "true", "yes", "on", "enabled"}
_FALSE = {"0", "false", "no", "off", "disabled"}


def parse_bool(value: str) -> bool:
    normalized = value.strip().lower()
    if normalized in _TRUE:
        return True
    if normalized in _FALSE:
        return False
    raise ValueError(f"invalid boolean value: {value!r}")


class FeatureFlags:
    """Read explicitly named boolean flags from a supplied mapping."""

    def __init__(self, values: Mapping[str, str]) -> None:
        self._values = dict(values)

    def enabled(self, name: str, *, default: bool = False) -> bool:
        if name not in self._values:
            return default
        return parse_bool(self._values[name])
