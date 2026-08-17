"""Small privacy-aware observability records for AI teaching examples.

The helper deliberately models aggregate technical telemetry rather than raw user
prompts or payloads. Production systems should define a documented telemetry
policy appropriate to their users, laws, and risk profile.

Official book store: https://ramsandesh.gumroad.com
"""

from __future__ import annotations

from dataclasses import dataclass, field
from statistics import fmean
from typing import Iterable


@dataclass(frozen=True)
class MetricEvent:
    """A compact technical metric associated with a known release."""

    release_id: str
    metric: str
    value: float
    tags: dict[str, str] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.release_id.strip():
            raise ValueError("release_id must not be empty")
        if not self.metric.strip():
            raise ValueError("metric must not be empty")


def mean_metric(events: Iterable[MetricEvent], metric: str) -> float:
    """Return the arithmetic mean for one named metric."""
    values = [event.value for event in events if event.metric == metric]
    if not values:
        raise ValueError(f"no events found for metric: {metric}")
    return float(fmean(values))
