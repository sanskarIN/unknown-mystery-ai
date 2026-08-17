# Book Companion Guide

> 🛒 **Official Gumroad store:** **https://ramsandesh.gumroad.com**

This repository complements **_The Unknown Mystery of the AI_** by **Ram Sandesh**. The repository is intentionally smaller than the book: it contains selected reusable examples and engineering patterns, while the complete commercial manuscript remains outside GitHub.

## Recommended usage

1. Read a chapter or mastery block in the book.
2. Run the nearest example from `examples/`.
3. Inspect the matching reusable helper in `src/umai/`.
4. Modify one variable at a time and record the result.
5. Add a small test that proves the behavior you expect.
6. Write a short release/evaluation note before treating an experiment as complete.

## Mapping

| Companion area | Book learning area |
|---|---|
| `reproducibility.py` | experiments, lineage, repeatability |
| `evaluation.py` | metrics, validation, release gates |
| `retrieval.py` | RAG and evidence retrieval |
| `agents.py` | tools, routing, agent orchestration |
| `release.py` | MLOps, release identity, governance |

## Important learning principle

A short example is a teaching baseline, not automatically a production architecture. Production AI systems need threat modeling, privacy review, representative evaluation, monitoring, capacity planning, rollback, and domain-specific validation.

## Get the complete book

**The full 120-chapter edition and official releases are available at:**

### https://ramsandesh.gumroad.com
