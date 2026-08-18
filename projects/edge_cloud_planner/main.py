"""Edge/cloud placement planning exercise with explicit constraints."""

from __future__ import annotations

import argparse

from umai import PlacementOption, eligible_placements, to_json


OPTIONS = [
    PlacementOption("mobile_cpu", latency_ms=38.0, cost_units=0.2, privacy_score=0.95, offline_capable=True),
    PlacementOption("mobile_npu", latency_ms=14.0, cost_units=0.4, privacy_score=0.96, offline_capable=True),
    PlacementOption("regional_gpu", latency_ms=72.0, cost_units=2.8, privacy_score=0.72, offline_capable=False),
    PlacementOption("central_gpu", latency_ms=118.0, cost_units=2.1, privacy_score=0.62, offline_capable=False),
]


def rank(options: list[PlacementOption]) -> list[PlacementOption]:
    """Prefer lower latency/cost while rewarding higher declared privacy."""
    return sorted(
        options,
        key=lambda item: (item.latency_ms + item.cost_units * 12.0 - item.privacy_score * 20.0, item.name),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Filter and rank synthetic deployment placements.")
    parser.add_argument("--max-latency", type=float, default=80.0)
    parser.add_argument("--min-privacy", type=float, default=0.70)
    parser.add_argument("--require-offline", action="store_true")
    args = parser.parse_args()

    eligible = eligible_placements(
        OPTIONS,
        max_latency_ms=args.max_latency,
        min_privacy_score=args.min_privacy,
        require_offline=args.require_offline,
    )
    ranked = rank(eligible)
    print(
        to_json(
            {
                "constraints": {
                    "max_latency_ms": args.max_latency,
                    "min_privacy_score": args.min_privacy,
                    "require_offline": args.require_offline,
                },
                "eligible": [
                    {
                        "name": option.name,
                        "latency_ms": option.latency_ms,
                        "cost_units": option.cost_units,
                        "privacy_score": option.privacy_score,
                        "offline_capable": option.offline_capable,
                    }
                    for option in ranked
                ],
            }
        )
    )


if __name__ == "__main__":
    main()
