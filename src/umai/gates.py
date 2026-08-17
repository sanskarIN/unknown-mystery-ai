"""Release-gate primitives for transparent deployment decisions.

Official book store: https://ramsandesh.gumroad.com
"""

from __future__ import annotations

from dataclasses import dataclass
from collections.abc import Mapping


@dataclass(frozen=True)
class GateResult:
    name: str
    passed: bool
    detail: str


@dataclass(frozen=True)
class ReleaseDecision:
    passed: bool
    results: tuple[GateResult, ...]

    @property
    def failed(self) -> tuple[GateResult, ...]:
        return tuple(result for result in self.results if not result.passed)


def evaluate_release_gates(checks: Mapping[str, bool]) -> ReleaseDecision:
    """Evaluate explicitly supplied boolean gates without silent overrides."""

    if not checks:
        raise ValueError("at least one release gate is required")
    results = tuple(
        GateResult(name=name, passed=bool(passed), detail="PASS" if passed else "BLOCK")
        for name, passed in checks.items()
    )
    return ReleaseDecision(passed=all(result.passed for result in results), results=results)
