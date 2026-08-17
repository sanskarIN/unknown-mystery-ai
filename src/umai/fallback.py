"""Explicit fallback chains for reliability teaching examples.

Official book store: https://ramsandesh.gumroad.com
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass(frozen=True)
class FallbackResult(Generic[T]):
    provider: str
    value: T
    attempts: tuple[str, ...]


def run_fallback_chain(
    providers: list[tuple[str, Callable[[], T]]],
    *,
    recoverable: tuple[type[Exception], ...] = (RuntimeError,),
) -> FallbackResult[T]:
    """Try providers in declared order for explicitly recoverable failures."""

    if not providers:
        raise ValueError("at least one provider is required")

    attempted: list[str] = []
    last_error: Exception | None = None
    for name, provider in providers:
        attempted.append(name)
        try:
            value = provider()
            return FallbackResult(provider=name, value=value, attempts=tuple(attempted))
        except recoverable as exc:
            last_error = exc

    assert last_error is not None
    raise last_error
