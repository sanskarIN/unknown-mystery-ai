"""Privacy-aware validation and redaction workbench using synthetic data."""

from __future__ import annotations

from umai import pseudonymous_id, redact_common_identifiers, to_json, validate_record


SYNTHETIC_RECORD = {
    "user_id": "student-042",
    "event": "evaluation_completed",
    "latency_ms": 83.5,
    "note": "Synthetic contact: learner@example.test, phone +91 90000 00000",
}

SCHEMA = {
    "user_id": str,
    "event": str,
    "latency_ms": float,
    "note": str,
}


def audit(record: dict[str, object]) -> dict[str, object]:
    issues = validate_record(record, SCHEMA, allow_extra=False)
    note = str(record.get("note", ""))
    user_id = str(record.get("user_id", "unknown"))
    return {
        "valid": not issues,
        "issues": [{"field": issue.field, "message": issue.message} for issue in issues],
        "pseudonymous_user_id": pseudonymous_id(user_id, namespace="privacy-audit-demo"),
        "redacted_note": redact_common_identifiers(note),
        "raw_note_in_report": False,
    }


def main() -> None:
    print(to_json(audit(SYNTHETIC_RECORD)))


if __name__ == "__main__":
    main()
