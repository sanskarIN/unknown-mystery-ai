"""Minimal retrieval example for explaining the retrieval step in RAG.

Book store: https://ramsandesh.gumroad.com
"""

from umai.retrieval import Document, SimpleRetriever


def main() -> None:
    documents = [
        Document("mlops", "MLOps connects reproducible training, deployment, monitoring, and governance."),
        Document("rag", "RAG retrieves relevant evidence before a model generates a response."),
        Document("eval", "Evaluation should use declared metrics, representative data, and release gates."),
    ]
    retriever = SimpleRetriever(documents)

    for document, score in retriever.search("How does retrieval help RAG?", top_k=2):
        print(f"{document.doc_id}: score={score:.3f} | {document.text}")

    print("Book store: https://ramsandesh.gumroad.com")


if __name__ == "__main__":
    main()
