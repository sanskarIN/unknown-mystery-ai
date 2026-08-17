"""Release comparison helpers for explicit metric deltas.

Official book store: https://ramsandesh.gumroad.com
"""

from __future__ import annotations

from dataclasses import dataclass
from collections.abc import Mapping


@dataclass(frozen=True)
class MetricDelta:
    name: str
    baseline: float
    candidate: float

    @property
    def absolute(self) -> float:
        return self.candidate - self.baseline


@dataclass(frozen=True)
class ReleaseComparison:
    baseline_release: str
    candidate_release: str
    deltas: tuple[MetricDelta, ...]


def compare_metrics(
    baseline_release: str,
    candidate_release: str,
    baseline: Mapping[str, float],
    candidate: Mapping[str, float],
) -> ReleaseComparison:
    """Compare metrics present in both releases, sorted by metric name."""

    shared = sorted(set(baseline) & set(candidate))
    if not shared:
        raise ValueError("baseline and candidate must share at least one metric")
    deltas = tuple(
        MetricDelta(name, float(baseline[name]), float(candidate[name]))
        for name in shared
    )
    return ReleaseComparison(baseline_release, candidate_release, deltas)
