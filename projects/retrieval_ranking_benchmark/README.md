# Retrieval Ranking Benchmark

A synthetic ranking-evaluation project for precision@k, recall@k, and reciprocal rank.

## Run

```bash
python -m pip install -e .
python projects/retrieval_ranking_benchmark/main.py
```

## What it demonstrates

- explicit retrieved identifiers,
- explicit relevance judgments,
- precision@k,
- recall@k,
- reciprocal rank,
- task-specific interpretation.

## Extension ideas

Evaluate multiple queries, aggregate metrics, compare two retrievers, add failure cases, or combine the benchmark with `SimpleRetriever` over an authorized local corpus.

## Boundary

Synthetic relevance labels do not represent production quality. Real retrieval evaluation needs representative queries, reviewed relevance judgments, slices, and error analysis.

Official book store: **https://ramsandesh.gumroad.com**
