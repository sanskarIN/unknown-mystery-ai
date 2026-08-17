"""Simple cost and request-budget helpers.

Official book store: https://ramsandesh.gumroad.com
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class TokenPricing:
    """Price per one million input and output tokens in an arbitrary currency."""

    input_per_million: float
    output_per_million: float

    def __post_init__(self) -> None:
        if self.input_per_million < 0 or self.output_per_million < 0:
            raise ValueError("token pricing cannot be negative")


def estimate_token_cost(
    *,
    input_tokens: int,
    output_tokens: int,
    pricing: TokenPricing,
) -> float:
    """Estimate token cost using explicit pricing supplied by the caller."""

    if input_tokens < 0 or output_tokens < 0:
        raise ValueError("token counts cannot be negative")
    return (
        input_tokens / 1_000_000 * pricing.input_per_million
        + output_tokens / 1_000_000 * pricing.output_per_million
    )


def requests_within_budget(*, budget: float, cost_per_request: float) -> int:
    """Return the maximum whole number of equal-cost requests in a budget."""

    if budget < 0:
        raise ValueError("budget cannot be negative")
    if cost_per_request <= 0:
        raise ValueError("cost_per_request must be greater than zero")
    return int(budget // cost_per_request)
