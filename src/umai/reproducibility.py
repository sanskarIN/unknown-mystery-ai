"""Small reproducibility helpers used across the companion examples.

Official book store: https://ramsandesh.gumroad.com
"""

from __future__ import annotations

import hashlib
import json
import os
import random
from typing import Any


def seed_everything(seed: int = 42) -> int:
    """Seed Python's standard random generator and expose the seed to child code.

    This helper intentionally avoids pretending that one seed guarantees bit-for-bit
    reproducibility across every framework, device, compiler, or accelerator.
    Framework-specific determinism settings should be configured separately.
    """
    if not isinstance(seed, int):
        raise TypeError("seed must be an integer")

    random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    return seed


def canonical_json(value: Any) -> str:
    """Serialize JSON-compatible data using stable ordering and separators."""
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    )


def fingerprint_json(value: Any, algorithm: str = "sha256") -> str:
    """Return a stable cryptographic fingerprint for JSON-compatible data."""
    try:
        hasher = hashlib.new(algorithm)
    except ValueError as exc:
        raise ValueError(f"unsupported hash algorithm: {algorithm}") from exc

    hasher.update(canonical_json(value).encode("utf-8"))
    return hasher.hexdigest()
