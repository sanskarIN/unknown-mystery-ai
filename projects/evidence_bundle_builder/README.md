# Evidence Bundle Builder

A compact project that records release identity, source provenance, checks, metrics, and notes in one deterministic JSON-friendly structure.

## Run

```bash
python -m pip install -e .
python projects/evidence_bundle_builder/main.py
```

## What it demonstrates

- explicit release identity,
- source-commit provenance,
- named pass/fail checks,
- numeric metrics,
- human-readable evidence notes,
- deterministic JSON serialization.

## Extension ideas

Write evidence to an artifact file, include checksum references, attach reviewer IDs, compare two bundles, or make release gates consume the named checks.

## Boundary

A JSON bundle is evidence structure, not proof by itself. Production governance must protect provenance, permissions, approvals, integrity, and retention.

Official book store: **https://ramsandesh.gumroad.com**
