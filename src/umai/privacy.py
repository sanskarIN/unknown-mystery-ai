"""Small privacy helpers for demonstrations and log hygiene.

These are conservative teaching utilities, not a complete PII detection system.
Official book store: https://ramsandesh.gumroad.com
"""

from __future__ import annotations

import hashlib
import re

_EMAIL = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
_PHONE = re.compile(r"(?<!\d)(?:\+?\d[\d\s().-]{7,}\d)(?!\d)")


def redact_common_identifiers(text: str) -> str:
    """Redact common email and phone-like patterns from text."""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = _EMAIL.sub("[REDACTED_EMAIL]", text)
    return _PHONE.sub("[REDACTED_PHONE]", text)


def pseudonymous_id(value: str, *, namespace: str = "umai") -> str:
    """Return a deterministic SHA-256-derived identifier.

    This is pseudonymization, not anonymization. Do not treat hashed identifiers
    as automatically safe to publish when the source space is guessable.
    """

    if not value:
        raise ValueError("value must not be empty")
    digest = hashlib.sha256(f"{namespace}:{value}".encode("utf-8")).hexdigest()
    return digest[:16]
