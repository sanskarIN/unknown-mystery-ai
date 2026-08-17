"""Bounded retry helpers for small deterministic examples.

Official book store: https://ramsandesh.gumroad.com
"""

from __future__ import annotations

from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")


def retry_call(
    operation: Callable[[], T],
    *,
    attempts: int = 3,
    retry_on: tuple[type[Exception], ...] = (Exception,),
) -> T:
    """Call an operation with a strict maximum number of attempts.

    This helper intentionally does not sleep or implement exponential backoff;
    callers can layer timing behavior appropriate to their environment. Never
    use retries to hide permanent validation, authorization, or policy errors.
    """

    if attempts <= 0:
        raise ValueError("attempts must be greater than zero")

    last_error: Exception | None = None
    for _ in range(attempts):
        try:
            return operation()
        except retry_on as exc:
            last_error = exc
    assert last_error is not None
    raise last_error
