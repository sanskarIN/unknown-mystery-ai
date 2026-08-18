"""Synthetic monitoring and drift lab for AI operations lessons."""

from __future__ import annotations

from statistics import fmean

from umai import mean_shift, standardized_mean_shift, synthetic_metric_series, to_json


def values(points: list[object]) -> list[float]:
    return [float(getattr(point, "value")) for point in points]


def main() -> None:
    reference_points = synthetic_metric_series(
        length=24,
        baseline=120.0,
        noise=4.0,
        trend_per_step=0.05,
        seed=11,
    )
    current_points = synthetic_metric_series(
        length=24,
        baseline=128.0,
        noise=5.0,
        trend_per_step=0.12,
        seed=12,
    )
    reference = values(reference_points)
    current = values(current_points)

    print(
        to_json(
            {
                "data_source": "deterministic synthetic telemetry",
                "reference_mean": round(fmean(reference), 3),
                "current_mean": round(fmean(current), 3),
                "mean_shift": round(mean_shift(reference, current), 3),
                "standardized_mean_shift": round(standardized_mean_shift(reference, current), 3),
                "interpretation": "Investigate with application-calibrated thresholds; this demo does not define a universal drift limit.",
            }
        )
    )


if __name__ == "__main__":
    main()
