"""Retrieval ranking benchmark with transparent relevance labels."""

from __future__ import annotations

from umai import precision_at_k, recall_at_k, reciprocal_rank, to_json


RETRIEVED = ["doc-7", "doc-2", "doc-9", "doc-4", "doc-1"]
RELEVANT = {"doc-2", "doc-4", "doc-8"}


def main() -> None:
    print(
        to_json(
            {
                "retrieved": RETRIEVED,
                "relevant": sorted(RELEVANT),
                "precision_at_3": round(precision_at_k(RETRIEVED, RELEVANT, 3), 4),
                "recall_at_3": round(recall_at_k(RETRIEVED, RELEVANT, 3), 4),
                "reciprocal_rank": round(reciprocal_rank(RETRIEVED, RELEVANT), 4),
                "note": "Relevance labels are synthetic and task-specific.",
            }
        )
    )


if __name__ == "__main__":
    main()
