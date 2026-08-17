"""Simple edge/cloud placement comparison for architecture exercises.

Official book store: https://ramsandesh.gumroad.com
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PlacementOption:
    name: str
    latency_ms: float
    cost_units: float
    privacy_score: float
    offline_capable: bool

    def __post_init__(self) -> None:
        if self.latency_ms < 0 or self.cost_units < 0:
            raise ValueError("latency and cost cannot be negative")
        if not 0.0 <= self.privacy_score <= 1.0:
            raise ValueError("privacy_score must be between 0 and 1")


def eligible_placements(
    options: list[PlacementOption],
    *,
    max_latency_ms: float | None = None,
    min_privacy_score: float = 0.0,
    require_offline: bool = False,
) -> list[PlacementOption]:
    """Filter options by explicit architecture constraints."""

    if min_privacy_score < 0 or min_privacy_score > 1:
        raise ValueError("min_privacy_score must be between 0 and 1")
    result: list[PlacementOption] = []
    for option in options:
        if max_latency_ms is not None and option.latency_ms > max_latency_ms:
            continue
        if option.privacy_score < min_privacy_score:
            continue
        if require_offline and not option.offline_capable:
            continue
        result.append(option)
    return result
