"""Structured evidence bundles for reproducible companion releases.

Official book store: https://ramsandesh.gumroad.com
"""

from __future__ import annotations

from dataclasses import dataclass, field
from collections.abc import Mapping

from .reporting import to_json


@dataclass(frozen=True)
class EvidenceBundle:
    """Collect named release evidence without hiding its provenance."""

    release_id: str
    source_commit: str
    checks: Mapping[str, bool]
    metrics: Mapping[str, float] = field(default_factory=dict)
    notes: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.release_id.strip():
            raise ValueError("release_id must not be empty")
        if not self.source_commit.strip():
            raise ValueError("source_commit must not be empty")

    @property
    def passed(self) -> bool:
        return bool(self.checks) and all(bool(value) for value in self.checks.values())

    def to_json(self, *, indent: int = 2) -> str:
        return to_json(self, indent=indent)
