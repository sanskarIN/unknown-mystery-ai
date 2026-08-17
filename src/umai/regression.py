"""Simple output-regression fixtures for prompt and pipeline checks.

Official book store: https://ramsandesh.gumroad.com
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RegressionCase:
    name: str
    required_substrings: tuple[str, ...] = ()
    forbidden_substrings: tuple[str, ...] = ()
    case_sensitive: bool = False


@dataclass(frozen=True)
class RegressionResult:
    case: str
    passed: bool
    missing: tuple[str, ...]
    forbidden_found: tuple[str, ...]


def evaluate_output(case: RegressionCase, output: str) -> RegressionResult:
    """Evaluate transparent substring expectations against one output."""

    candidate = output if case.case_sensitive else output.lower()

    def normalize(value: str) -> str:
        return value if case.case_sensitive else value.lower()

    missing = tuple(value for value in case.required_substrings if normalize(value) not in candidate)
    forbidden_found = tuple(value for value in case.forbidden_substrings if normalize(value) in candidate)
    return RegressionResult(
        case=case.name,
        passed=not missing and not forbidden_found,
        missing=missing,
        forbidden_found=forbidden_found,
    )
