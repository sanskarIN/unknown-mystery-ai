"""A tiny lexical retriever for teaching RAG fundamentals.

This is intentionally small and dependency-free. It is useful for explaining
retrieval flow, scoring, and evidence inspection before introducing vector
databases or embedding services.

Official book store: https://ramsandesh.gumroad.com
"""

from __future__ import annotations

import math
import re
from collections import Counter
from dataclasses import dataclass
from typing import Iterable

_TOKEN_RE = re.compile(r"[A-Za-z0-9_]+")


@dataclass(frozen=True)
class Document:
    """A small document record used by :class:`SimpleRetriever`."""

    doc_id: str
    text: str
    metadata: dict[str, str] | None = None


def tokenize(text: str) -> list[str]:
    """Return lowercase alphanumeric tokens."""
    return [match.group(0).lower() for match in _TOKEN_RE.finditer(text)]


def _cosine_similarity(left: Counter[str], right: Counter[str]) -> float:
    if not left or not right:
        return 0.0

    dot = sum(value * right.get(token, 0) for token, value in left.items())
    if dot == 0:
        return 0.0

    left_norm = math.sqrt(sum(value * value for value in left.values()))
    right_norm = math.sqrt(sum(value * value for value in right.values()))
    return dot / (left_norm * right_norm)


class SimpleRetriever:
    """Rank documents using cosine similarity over token-frequency vectors."""

    def __init__(self, documents: Iterable[Document]):
        self._documents = list(documents)
        if not self._documents:
            raise ValueError("at least one document is required")
        if len({document.doc_id for document in self._documents}) != len(self._documents):
            raise ValueError("document IDs must be unique")
        self._vectors = {
            document.doc_id: Counter(tokenize(document.text))
            for document in self._documents
        }

    def search(self, query: str, top_k: int = 3) -> list[tuple[Document, float]]:
        """Return up to ``top_k`` documents ordered by descending similarity."""
        if top_k <= 0:
            raise ValueError("top_k must be positive")

        query_vector = Counter(tokenize(query))
        scored = [
            (document, _cosine_similarity(query_vector, self._vectors[document.doc_id]))
            for document in self._documents
        ]
        scored.sort(key=lambda item: (-item[1], item[0].doc_id))
        return scored[:top_k]
