"""RAG evaluation capstone with retrieval, ranking, and regression checks."""

from __future__ import annotations

import json

from umai import (
    Document,
    RegressionCase,
    SimpleRetriever,
    evaluate_output,
    precision_at_k,
    recall_at_k,
    reciprocal_rank,
)


def main() -> int:
    documents = [
        Document("d1", "Retrieval quality depends on useful evidence and evaluation.", {"topic": "rag"}),
        Document("d2", "Release gates connect measured evidence to deployment decisions.", {"topic": "mlops"}),
        Document("d3", "Privacy review should minimize unnecessary personal information.", {"topic": "privacy"}),
        Document("d4", "Reranking can improve the order of retrieved evidence.", {"topic": "rag"}),
    ]
    retriever = SimpleRetriever(documents)
    results = retriever.search("retrieval evidence ranking", top_k=3)
    retrieved = [document.doc_id for document, _ in results]
    relevant = {"d1", "d4"}

    answer = "Retrieval quality should be evaluated using evidence and ranking metrics."
    regression = evaluate_output(
        RegressionCase(
            name="grounded-answer-contract",
            required_substrings=("evidence", "ranking"),
            forbidden_substrings=("guaranteed perfect",),
        ),
        answer,
    )

    payload = {
        "project": "RAG Evaluation Capstone",
        "query": "retrieval evidence ranking",
        "retrieved": [
            {"doc_id": document.doc_id, "score": round(score, 6), "topic": (document.metadata or {}).get("topic")}
            for document, score in results
        ],
        "metrics": {
            "precision_at_3": precision_at_k(retrieved, relevant, 3),
            "recall_at_3": recall_at_k(retrieved, relevant, 3),
            "reciprocal_rank": reciprocal_rank(retrieved, relevant),
        },
        "regression": {
            "passed": regression.passed,
            "missing": list(regression.missing),
            "forbidden_found": list(regression.forbidden_found),
        },
        "boundary": "This local lexical baseline does not claim production RAG quality.",
        "store": "https://ramsandesh.gumroad.com",
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
