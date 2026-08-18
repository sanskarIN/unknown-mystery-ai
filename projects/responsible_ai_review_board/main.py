"""Responsible-AI review-board capstone using explicit review evidence."""

from __future__ import annotations

import json

from umai import EvidenceBundle, evaluate_release_gates, redact_common_identifiers, validate_record


def main() -> int:
    system_card = {
        "intended_use": "synthetic customer-support intent triage",
        "human_oversight": "required for low-confidence or sensitive cases",
        "data_scope": "synthetic demonstration records only",
        "owner_contact": "review.owner@example.com",
    }
    schema = {
        "intended_use": str,
        "human_oversight": str,
        "data_scope": str,
        "owner_contact": str,
    }
    issues = validate_record(system_card, schema, allow_extra=False)

    checks = {
        "intended_use_documented": bool(system_card["intended_use"].strip()),
        "human_oversight_documented": bool(system_card["human_oversight"].strip()),
        "data_scope_documented": bool(system_card["data_scope"].strip()),
        "schema_valid": not issues,
        "privacy_review_recorded": True,
        "rollback_owner_named": True,
    }
    decision = evaluate_release_gates(checks)
    evidence = EvidenceBundle(
        release_id="responsible-ai-review-demo",
        source_commit="synthetic-review-revision",
        checks=checks,
        notes=(
            "This is a teaching checklist, not a legal or regulatory determination.",
            "Residual risk requires accountable human review.",
        ),
    )

    payload = {
        "project": "Responsible AI Review Board",
        "system_card": {
            **system_card,
            "owner_contact": redact_common_identifiers(system_card["owner_contact"]),
        },
        "validation_issues": [issue.__dict__ for issue in issues],
        "review": {
            "passed": decision.passed,
            "failed_gates": [item.name for item in decision.failed],
            "evidence_passed": evidence.passed,
        },
        "boundary": "Use domain experts and applicable organizational/legal review for real deployments.",
        "store": "https://ramsandesh.gumroad.com",
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
