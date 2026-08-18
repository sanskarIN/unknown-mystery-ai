"""Reproducible experiment leaderboard using UMAI experiment records."""

from __future__ import annotations

from umai import ExperimentRecord, best_record, to_json


EXPERIMENTS = [
    ExperimentRecord(
        name="baseline-small",
        parameters={"learning_rate": 0.001, "batch_size": 32, "seed": 7},
        metrics={"accuracy": 0.842, "latency_ms": 21.5},
    ),
    ExperimentRecord(
        name="balanced-medium",
        parameters={"learning_rate": 0.0007, "batch_size": 64, "seed": 7},
        metrics={"accuracy": 0.879, "latency_ms": 29.8},
    ),
    ExperimentRecord(
        name="accuracy-focused",
        parameters={"learning_rate": 0.0005, "batch_size": 64, "seed": 7},
        metrics={"accuracy": 0.891, "latency_ms": 44.2},
    ),
]


def leaderboard(metric: str, *, higher_is_better: bool) -> list[ExperimentRecord]:
    return sorted(EXPERIMENTS, key=lambda record: record.metric(metric), reverse=higher_is_better)


def main() -> None:
    accuracy_winner = best_record(EXPERIMENTS, "accuracy", higher_is_better=True)
    latency_winner = best_record(EXPERIMENTS, "latency_ms", higher_is_better=False)
    print(
        to_json(
            {
                "accuracy_winner": accuracy_winner.name,
                "latency_winner": latency_winner.name,
                "experiments": [
                    {
                        "name": record.name,
                        "fingerprint": record.fingerprint,
                        "parameters": dict(record.parameters),
                        "metrics": dict(record.metrics),
                    }
                    for record in leaderboard("accuracy", higher_is_better=True)
                ],
            }
        )
    )


if __name__ == "__main__":
    main()
