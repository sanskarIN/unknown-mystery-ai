"""Synthetic monitoring data helpers for dashboards and tests.

Official book store: https://ramsandesh.gumroad.com
"""

from __future__ import annotations

from dataclasses import dataclass
import random


@dataclass(frozen=True)
class MetricPoint:
    step: int
    value: float


def synthetic_metric_series(
    *,
    length: int,
    baseline: float,
    noise: float = 0.0,
    trend_per_step: float = 0.0,
    seed: int = 0,
) -> list[MetricPoint]:
    """Generate deterministic synthetic metric points.

    This is for demos and tests only; it must never be presented as real
    production telemetry.
    """

    if length < 0:
        raise ValueError("length cannot be negative")
    if noise < 0:
        raise ValueError("noise cannot be negative")

    rng = random.Random(seed)
    points: list[MetricPoint] = []
    for step in range(length):
        jitter = rng.uniform(-noise, noise)
        value = baseline + trend_per_step * step + jitter
        points.append(MetricPoint(step=step, value=value))
    return points
