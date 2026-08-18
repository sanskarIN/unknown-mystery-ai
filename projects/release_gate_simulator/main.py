"""Transparent release-gate simulator for AI deployment exercises."""

from __future__ import annotations

import argparse

from umai import evaluate_release_gates, to_json


def build_checks(*, evaluation: bool, privacy: bool, rollback: bool, observability: bool) -> dict[str, bool]:
    return {
        "evaluation_passed": evaluation,
        "privacy_reviewed": privacy,
        "rollback_ready": rollback,
        "observability_ready": observability,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate explicit AI release gates.")
    parser.add_argument("--fail-evaluation", action="store_true")
    parser.add_argument("--fail-privacy", action="store_true")
    parser.add_argument("--fail-rollback", action="store_true")
    parser.add_argument("--fail-observability", action="store_true")
    parser.add_argument("--strict", action="store_true", help="Return a non-zero exit code for a blocked release.")
    args = parser.parse_args()

    checks = build_checks(
        evaluation=not args.fail_evaluation,
        privacy=not args.fail_privacy,
        rollback=not args.fail_rollback,
        observability=not args.fail_observability,
    )
    decision = evaluate_release_gates(checks)
    payload = {
        "decision": "PASS" if decision.passed else "BLOCK",
        "failed": [result.name for result in decision.failed],
        "results": [
            {"name": result.name, "passed": result.passed, "detail": result.detail}
            for result in decision.results
        ],
    }
    print(to_json(payload))

    if args.strict and not decision.passed:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
