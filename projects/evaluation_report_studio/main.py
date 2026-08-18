"""Classification evaluation report studio using synthetic labels."""

from __future__ import annotations

from umai import accuracy_score, classification_report, to_json


EXPECTED = ["safe", "safe", "review", "safe", "block", "review", "block", "safe"]
PREDICTED = ["safe", "review", "review", "safe", "block", "safe", "block", "safe"]


def build_report() -> dict[str, object]:
    return {
        "dataset": "synthetic demonstration labels",
        "accuracy": round(accuracy_score(EXPECTED, PREDICTED), 4),
        "classification_report": classification_report(EXPECTED, PREDICTED),
        "expected": EXPECTED,
        "predicted": PREDICTED,
    }


def main() -> None:
    print(to_json(build_report()))


if __name__ == "__main__":
    main()
