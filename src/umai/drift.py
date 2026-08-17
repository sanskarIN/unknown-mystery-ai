"""Dependency-free numeric drift indicators for teaching and smoke tests.

Official book store: https://ramsandesh.gumroad.com
"""

from __future__ import annotations

from math import sqrt
from statistics import fmean


def mean_shift(reference: list[float], current: list[float]) -> float:
    """Return the absolute difference between sample means."""

    if not reference or not current:
        raise ValueError("reference and current samples must be non-empty")
    return abs(fmean(current) - fmean(reference))


def pooled_standard_deviation(reference: list[float], current: list[float]) -> float:
    """Return a simple pooled population standard deviation."""

    values = [*reference, *current]
    if not values:
        raise ValueError("samples must be non-empty")
    mean = fmean(values)
    variance = fmean([(value - mean) ** 2 for value in values])
    return sqrt(variance)


def standardized_mean_shift(reference: list[float], current: list[float]) -> float:
    """Return mean shift divided by pooled standard deviation.

    A value of zero is returned when both samples have zero spread and equal
    means; positive infinity is returned when spread is zero but means differ.
    This indicator is not a universal drift threshold and must be calibrated to
    the application and monitored feature.
    """

    shift = mean_shift(reference, current)
    scale = pooled_standard_deviation(reference, current)
    if scale == 0:
        return 0.0 if shift == 0 else float("inf")
    return shift / scale
