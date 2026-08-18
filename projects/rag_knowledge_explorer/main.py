"""Local lexical RAG/search explorer for the UMAI companion repository."""

from __future__ import annotations

import argparse

from umai import Document, SimpleRetriever, to_json


def build_documents() -> list[Document]:
    return [
        Document(
            "rag",
            "Retrieval-augmented generation retrieves evidence before generating an answer. "
            "Good systems preserve source identity, scoring, and explicit context boundaries.",
            {"topic": "rag"},
        ),
        Document(
            "evaluation",
            "AI evaluation should define datasets, metrics, thresholds, slices, and failure cases. "
            "A single aggregate metric rarely explains every important behavior.",
            {"topic": "evaluation"},
        ),
        Document(
            "mlops",
            "MLOps connects reproducible training, artifact lineage, release gates, deployment, "
            "monitoring, rollback, and operational evidence.",
            {"topic": "mlops"},
        ),
        Document(
            "privacy",
            "Privacy-aware AI systems minimize unnecessary data, separate identifiers from payloads, "
            "and avoid logging raw sensitive content when aggregate telemetry is sufficient.",
            {"topic": "privacy"},
        ),
        Document(
            "edge",
            "On-device and edge inference trade cloud elasticity for fixed memory, battery, thermal, "
            "hardware compatibility, update, and observability constraints.",
            {"topic": "edge"},
        ),
    ]


def search(query: str, top_k: int) -> list[dict[str, object]]:
    retriever = SimpleRetriever(build_documents())
    return [
        {
            "doc_id": document.doc_id,
            "score": round(score, 4),
            "topic": (document.metadata or {}).get("topic", "unknown"),
            "text": document.text,
        }
        for document, score in retriever.search(query, top_k=top_k)
    ]


def main() -> None:
    parser = argparse.ArgumentParser(description="Explore a small local RAG knowledge base.")
    parser.add_argument("--query", default="How do AI releases use evaluation and monitoring?")
    parser.add_argument("--top-k", type=int, default=3)
    args = parser.parse_args()

    print(to_json({"query": args.query, "results": search(args.query, args.top_k)}))


if __name__ == "__main__":
    main()
