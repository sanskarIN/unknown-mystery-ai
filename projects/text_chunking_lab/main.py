"""Deterministic text normalization and chunking lab."""

from __future__ import annotations

import argparse

from umai import chunk_text, normalize_whitespace, to_json


DEFAULT_TEXT = (
    "AI systems need reproducible inputs, explicit evaluation, and observable releases.   "
    "Retrieval pipelines also need chunking decisions that match document structure and task needs.\n"
    "A chunking strategy should be measured rather than assumed to be universally optimal. "
    "Overlap can preserve local context but also increases duplicated content and retrieval cost."
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Normalize and chunk local text deterministically.")
    parser.add_argument("--max-words", type=int, default=18)
    parser.add_argument("--overlap-words", type=int, default=4)
    args = parser.parse_args()

    normalized = normalize_whitespace(DEFAULT_TEXT)
    chunks = chunk_text(
        normalized,
        max_words=args.max_words,
        overlap_words=args.overlap_words,
    )
    print(
        to_json(
            {
                "normalized": normalized,
                "max_words": args.max_words,
                "overlap_words": args.overlap_words,
                "chunk_count": len(chunks),
                "chunks": [{"index": index, "text": chunk} for index, chunk in enumerate(chunks)],
            }
        )
    )


if __name__ == "__main__":
    main()
