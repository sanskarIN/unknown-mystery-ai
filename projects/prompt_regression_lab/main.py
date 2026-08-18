"""Deterministic prompt/output regression lab."""

from __future__ import annotations

from umai import RegressionCase, evaluate_output, to_json


CASES = [
    (
        RegressionCase(
            name="grounded-answer",
            required_substrings=("source", "uncertainty"),
            forbidden_substrings=("guaranteed",),
        ),
        "The answer cites a source and states uncertainty where evidence is incomplete.",
    ),
    (
        RegressionCase(
            name="privacy-message",
            required_substrings=("redact", "identifier"),
            forbidden_substrings=("raw password",),
        ),
        "Redact common identifier fields before storing diagnostic text.",
    ),
    (
        RegressionCase(
            name="release-message",
            required_substrings=("rollback", "metric"),
            forbidden_substrings=("skip evaluation",),
        ),
        "A release should preserve rollback evidence and a metric-based acceptance rule.",
    ),
]


def run_suite() -> dict[str, object]:
    results = [evaluate_output(case, output) for case, output in CASES]
    return {
        "passed": sum(result.passed for result in results),
        "total": len(results),
        "results": [
            {
                "case": result.case,
                "passed": result.passed,
                "missing": list(result.missing),
                "forbidden_found": list(result.forbidden_found),
            }
            for result in results
        ],
    }


def main() -> None:
    print(to_json(run_suite()))


if __name__ == "__main__":
    main()
