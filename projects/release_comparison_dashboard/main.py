"""Compare synthetic baseline and candidate release metrics."""

from __future__ import annotations

from umai import compare_metrics, to_json


BASELINE = {"accuracy": 0.872, "latency_ms": 46.0, "memory_mb": 610.0}
CANDIDATE = {"accuracy": 0.889, "latency_ms": 39.5, "memory_mb": 584.0}


def main() -> None:
    comparison = compare_metrics("1.0-baseline", "1.1-candidate", BASELINE, CANDIDATE)
    print(
        to_json(
            {
                "baseline_release": comparison.baseline_release,
                "candidate_release": comparison.candidate_release,
                "deltas": [
                    {
                        "metric": delta.name,
                        "baseline": delta.baseline,
                        "candidate": delta.candidate,
                        "absolute_delta": round(delta.absolute, 6),
                    }
                    for delta in comparison.deltas
                ],
                "note": "Metric direction must be interpreted per metric; positive is not universally better.",
            }
        )
    )


if __name__ == "__main__":
    main()
