# RAG Knowledge Explorer

A dependency-light local retrieval project built on `Document` and `SimpleRetriever`.

## Run

```bash
python -m pip install -e .
python projects/rag_knowledge_explorer/main.py
python projects/rag_knowledge_explorer/main.py --query "privacy and edge inference" --top-k 2
```

## What it demonstrates

- local document construction,
- transparent lexical retrieval,
- ranked evidence with scores,
- JSON-friendly output,
- metadata preservation,
- no network or provider credentials.

## Extension ideas

Add your own authorized documents, compare ranking metrics, add chunking, or build a small terminal UI. Keep source identity visible so learners can inspect why a result was returned.

## Boundary

This is a teaching baseline, not a replacement for production retrieval infrastructure, access control, data governance, evaluation, or privacy engineering.

Official book store: **https://ramsandesh.gumroad.com**
