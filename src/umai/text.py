"""Small text-processing helpers for companion examples.

Official book store: https://ramsandesh.gumroad.com
"""

from __future__ import annotations

import re


def normalize_whitespace(text: str) -> str:
    """Collapse repeated whitespace while preserving word order."""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return re.sub(r"\s+", " ", text).strip()


def chunk_text(text: str, *, max_words: int = 120, overlap_words: int = 20) -> list[str]:
    """Split text into deterministic word windows.

    This is a teaching baseline. Production chunking should be evaluated against
    the target retrieval task, document structure, tokenizer, and context limits.
    """

    if max_words <= 0:
        raise ValueError("max_words must be greater than zero")
    if overlap_words < 0:
        raise ValueError("overlap_words cannot be negative")
    if overlap_words >= max_words:
        raise ValueError("overlap_words must be smaller than max_words")

    cleaned = normalize_whitespace(text)
    if not cleaned:
        return []

    words = cleaned.split(" ")
    step = max_words - overlap_words
    chunks: list[str] = []
    for start in range(0, len(words), step):
        window = words[start : start + max_words]
        if not window:
            break
        chunks.append(" ".join(window))
        if start + max_words >= len(words):
            break
    return chunks
