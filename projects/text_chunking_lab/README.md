# Text Chunking Lab

A deterministic local text-processing project for whitespace normalization and overlapping word-window chunking.

## Run

```bash
python -m pip install -e .
python projects/text_chunking_lab/main.py
python projects/text_chunking_lab/main.py --max-words 24 --overlap-words 6
```

## What it demonstrates

- deterministic normalization,
- explicit maximum chunk size,
- explicit overlap,
- ordered chunk evidence,
- repeatable local preprocessing.

## Extension ideas

Compare chunk sizes on a retrieval benchmark, preserve headings, add document IDs, or evaluate tokenizer-aware and structure-aware strategies.

## Boundary

No single chunk size is universally best. Production chunking should be evaluated against the target corpus, tokenizer, retrieval task, latency, cost, and context constraints.

Official book store: **https://ramsandesh.gumroad.com**
