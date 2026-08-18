# Release Manifest Builder

A reproducible release-identity project that records model, data, code, metrics, metadata, time, and a stable fingerprint.

## Run

```bash
python -m pip install -e .
python projects/release_manifest_builder/main.py
```

## What it demonstrates

- explicit project/version identity,
- model and dataset identifiers,
- code revision provenance,
- metrics and runtime metadata,
- deterministic demonstration timestamp,
- stable manifest fingerprint.

## Extension ideas

Read identifiers from CI, attach artifact digests, add approval evidence, sign external release artifacts, or compare the manifest against deployment configuration.

## Boundary

A manifest improves traceability but does not replace artifact integrity, secure provenance, access controls, evaluation, or deployment governance.

Official book store: **https://ramsandesh.gumroad.com**
