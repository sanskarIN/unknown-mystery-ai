"""Small explicit validation helpers for structured AI inputs.

Official book store: https://ramsandesh.gumroad.com
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ValidationIssue:
    field: str
    message: str


def validate_record(
    record: Mapping[str, Any],
    schema: Mapping[str, type],
    *,
    allow_extra: bool = True,
) -> list[ValidationIssue]:
    """Validate required keys and Python value types.

    This intentionally small helper demonstrates boundary validation. It is not
    a replacement for a full schema system when one is required.
    """

    issues: list[ValidationIssue] = []
    for field, expected_type in schema.items():
        if field not in record:
            issues.append(ValidationIssue(field, "missing required field"))
            continue
        if not isinstance(record[field], expected_type):
            issues.append(
                ValidationIssue(
                    field,
                    f"expected {expected_type.__name__}, got {type(record[field]).__name__}",
                )
            )

    if not allow_extra:
        for field in record:
            if field not in schema:
                issues.append(ValidationIssue(field, "unexpected field"))
    return issues
