"""Deprecation helpers for the stable companion API.

Official book store: https://ramsandesh.gumroad.com
"""

from __future__ import annotations

from dataclasses import dataclass
import warnings


@dataclass(frozen=True)
class DeprecatedFeature:
    name: str
    replacement: str | None = None
    removal_version: str | None = None

    def message(self) -> str:
        parts = [f"{self.name} is deprecated"]
        if self.replacement:
            parts.append(f"use {self.replacement} instead")
        if self.removal_version:
            parts.append(f"planned removal: {self.removal_version}")
        return "; ".join(parts)


def warn_deprecated(feature: DeprecatedFeature, *, stacklevel: int = 2) -> None:
    """Emit a standard `DeprecationWarning` with an actionable message."""

    if stacklevel <= 0:
        raise ValueError("stacklevel must be greater than zero")
    warnings.warn(feature.message(), DeprecationWarning, stacklevel=stacklevel)
