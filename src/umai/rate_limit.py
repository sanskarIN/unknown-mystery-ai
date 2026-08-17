"""Small fixed-window rate limiting primitive for teaching examples.

Official book store: https://ramsandesh.gumroad.com
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class FixedWindowRateLimiter:
    """Track a bounded request count inside caller-supplied time windows.

    The caller supplies integer window identifiers, which keeps this helper
    deterministic and testable without depending on wall-clock time.
    """

    limit: int
    _window: int | None = None
    _count: int = 0

    def __post_init__(self) -> None:
        if self.limit <= 0:
            raise ValueError("limit must be greater than zero")

    def allow(self, window_id: int) -> bool:
        if self._window != window_id:
            self._window = window_id
            self._count = 0
        if self._count >= self.limit:
            return False
        self._count += 1
        return True

    @property
    def remaining(self) -> int:
        return max(self.limit - self._count, 0)
