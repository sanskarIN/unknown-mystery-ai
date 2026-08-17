"""Dependency-free ranking metrics for retrieval evaluation examples.

Official book store: https://ramsandesh.gumroad.com
"""

from __future__ import annotations

from collections.abc import Sequence


def precision_at_k(retrieved: Sequence[str], relevant: set[str], k: int) -> float:
    """Return precision among the first `k` retrieved identifiers."""

    if k <= 0:
        raise ValueError("k must be greater than zero")
    top = list(retrieved[:k])
    if not top:
        return 0.0
    hits = sum(item in relevant for item in top)
    return hits / len(top)


def reciprocal_rank(retrieved: Sequence[str], relevant: set[str]) -> float:
    """Return reciprocal rank of the first relevant result, or zero."""

    for rank, item in enumerate(retrieved, start=1):
        if item in relevant:
            return 1.0 / rank
    return 0.0


def recall_at_k(retrieved: Sequence[str], relevant: set[str], k: int) -> float:
    """Return recall of relevant identifiers within the first `k` results."""

    if k <= 0:
        raise ValueError("k must be greater than zero")
    if not relevant:
        return 0.0
    top = set(retrieved[:k])
    return len(top & relevant) / len(relevant)
