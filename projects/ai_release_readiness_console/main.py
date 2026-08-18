"""Integrated AI release-readiness capstone using stable UMAI utilities."""

from __future__ import annotations

import json

from umai import (
    EvidenceBundle,
    accuracy_score,
    evaluate_release_gates,
    pseudonymous_id,
    redact_common_identifiers,
    validate_record,
)


def main() -> int:
    record = {
        "project": "support-intent-demo",
        "owner_email": "demo.owner@example.com",
        "model_version": "demo-model-3",
    }
    schema = {"project": str, "owner_email": str, "model_version": str}
    issues = validate_record(record, schema, allow_extra=False)

    expected = ["billing", "technical", "billing", "account"]
    predicted = ["billing", "technical", "account", "account"]
    accuracy = accuracy_score(expected, predicted)

    checks = {
        "schema_valid": not issues,
        "evaluation_minimum": accuracy >= 0.75,
        "rollback_documented": True,
        "privacy_reviewed": True,
    }
    decision = evaluate_release_gates(checks)
    evidence = EvidenceBundle(
        release_id="readiness-demo-v1",
        source_commit="synthetic-demo-commit",
        checks=checks,
        metrics={"accuracy": accuracy},
        notes=("Synthetic/local demonstration only.",),
    )

    result = {
        "project": "AI Release Readiness Console",
        "record": {
            "project": record["project"],
            "owner": pseudonymous_id(record["owner_email"], namespace="readiness-demo"),
            "redacted_contact": redact_common_identifiers(record["owner_email"]),
            "model_version": record["model_version"],
        },
        "validation_issues": [issue.__dict__ for issue in issues],
        "metrics": {"accuracy": accuracy},
        "release": {
            "passed": decision.passed,
            "failed_gates": [item.name for item in decision.failed],
            "evidence_passed": evidence.passed,
        },
        "boundary": "Educational readiness evidence is not a substitute for organization-specific review.",
        "store": "https://ramsandesh.gumroad.com",
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
