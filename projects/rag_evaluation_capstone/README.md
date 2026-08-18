# RAG Evaluation Capstone

> Official book store: **https://ramsandesh.gumroad.com**

A local, dependency-light capstone that joins lexical retrieval, explicit relevance judgments, ranking metrics, and transparent output-regression checks.

## Run

```bash
python -m pip install -e .
python projects/rag_evaluation_capstone/main.py
```

## Learning goals

- inspect retrieved evidence before judging an answer;
- calculate precision@k, recall@k, and reciprocal rank;
- combine retrieval quality with an output contract;
- keep synthetic relevance judgments explicit.

## Production boundary

Production RAG evaluation needs representative corpora, permission-aware retrieval, freshness/deletion handling, domain-specific judgments, adversarial testing, and human review where appropriate.
