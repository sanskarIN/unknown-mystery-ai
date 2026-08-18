# Developer Guide

> 🛒 Official book store: **https://ramsandesh.gumroad.com**

This document is the maintainer-oriented guide for making safe, backward-compatible changes to the `unknown-mystery-ai` companion repository.

## Development principles

The repository favors:

- small, reviewable changes,
- dependency-light implementations,
- deterministic behavior where practical,
- explicit validation and failure messages,
- stable 1.x API compatibility,
- local/synthetic examples by default,
- reproducible release evidence,
- clear security/privacy/publication boundaries.

## Local setup

```bash
git clone https://github.com/sanskarIN/unknown-mystery-ai.git
cd unknown-mystery-ai
python -m venv .venv
python -m pip install -e .
```

Use the platform-specific activation steps in [`INSTALLATION.md`](INSTALLATION.md).

Maintainer Git identity:

```bash
git config user.name "Sanskar"
git config user.email "sanskarin@outlook.in"
```

## Repository layers

### `src/umai/`

Stable dependency-light package code. Public exports are controlled by `umai.__all__` and validated against the committed API snapshot.

### `examples/`

Small focused teaching examples. They should remain non-interactive and reproducible.

### `projects/`

Larger runnable educational projects. Default runs must emit valid JSON. See [`PROJECT_AUTHORING_GUIDE.md`](PROJECT_AUTHORING_GUIDE.md).

### `tests/`

Standard-library unit tests and integration invariants.

### `scripts/`

Repository-quality, release, catalog, packaging, checksum, and boundary validators.

### `.github/workflows/`

Cross-platform and release automation. Third-party actions are pinned to full commit SHAs.

## Change categories

### Bug fix

A bug fix should add or improve a regression test where practical. Do not change public behavior unrelated to the bug.

### New public helper

Before adding a new exported symbol, decide whether it truly belongs in the stable public API. Once exported in the 1.x line, removing or incompatibly changing it requires stronger versioning discipline.

### Internal helper

Prefer internal helpers when reuse is implementation-specific and users do not need a stable contract.

### New project

Follow the project authoring contract, update `projects/catalog.json`, and keep default execution credential-free.

### Documentation-only change

Documentation changes must pass repository-local Markdown link validation and must preserve canonical long-lived links.

## Stable API checks

Run:

```bash
python scripts/check_public_api.py --require-version-match
```

If the stable public symbol set intentionally changes, update the committed API snapshot in the same reviewed change and follow semantic-versioning guidance in [`API_COMPATIBILITY.md`](API_COMPATIBILITY.md).

## Core validation

Before proposing a change, run:

```bash
python scripts/check_package_metadata.py
python scripts/check_release_documentation.py
python scripts/check_workflow_pins.py
python scripts/check_public_repository_boundary.py
python scripts/check_project_links.py
python scripts/check_unstable_social_links.py
python scripts/check_markdown_links.py
python scripts/check_public_api.py --require-version-match
python scripts/check_project_catalog.py
python scripts/check_projects.py
python scripts/check_project_snapshots.py
python -m unittest discover -s tests -v
```

For a 1.1.0 release candidate also run:

```bash
python scripts/check_release_candidate.py
```

## Build validation

```bash
python -m pip install build
python -m build
python scripts/check_distribution_contents.py
python scripts/create_checksum_manifest.py dist/* > dist/SHA256SUMS.txt
```

Do not commit generated `dist/` artifacts to `main`; immutable release artifacts belong on the GitHub release generated from the release tag.

## Makefile shortcuts

On compatible systems:

```bash
make install
make test
make examples
make project-catalog
make projects
make project-snapshots
make release-check
make build
```

## Error-handling expectations

Library functions should fail explicitly when inputs violate a documented contract. Prefer clear `ValueError`, `TypeError`, or purpose-specific result objects over silent coercion when silent coercion would hide a meaningful mistake.

Scripts should:

- return exit code `0` on success,
- return non-zero on validation failure,
- print actionable failure descriptions,
- avoid modifying source files unless modification is their documented purpose.

## Determinism

Tests, examples, project snapshots, and release metadata should avoid accidental nondeterminism. If randomness is part of a demonstration, seed it explicitly or constrain validation to deterministic subsets.

## Cross-platform behavior

Do not assume POSIX-only paths inside Python. Prefer `pathlib.Path`. Shell-specific commands belong in documentation or workflows that explicitly declare the shell. The Project Matrix validates the project suite on Linux, Windows, and macOS.

## Security and privacy review

For changes involving data, tools, serving, observability, or automation, review:

- [`../SECURITY.md`](../SECURITY.md)
- [`SECURITY_MODEL.md`](SECURITY_MODEL.md)
- [`PRIVACY_MODEL.md`](PRIVACY_MODEL.md)
- [`RESPONSIBLE_AI_CHECKLIST.md`](RESPONSIBLE_AI_CHECKLIST.md)

Never add secrets or real private user data to test fixtures.

## Workflow security

External GitHub Actions must remain pinned to full commit SHAs. Keep workflow permissions minimal. Do not introduce broad write permissions unless the workflow's exact release function requires them.

## Documentation expectations

Every user-visible feature should have an discoverable documentation path from [`docs/README.md`](README.md) or the repository root README. New concepts should document:

- purpose,
- command/API usage,
- expected output,
- error behavior,
- compatibility expectations,
- limitations,
- security/privacy notes when relevant.

## Release discipline

Do not tag a release merely because the source appears correct. Follow [`RELEASE_RUNBOOK.md`](RELEASE_RUNBOOK.md), verify the intended immutable commit, and publish only the software companion artifacts appropriate for the Apache-2.0 repository.

## Commercial publication boundary

Paid book manuscripts, PDF/DOCX editions, cover artwork, certificates, and commercial publication packages must remain outside the public software repository and public GitHub software releases.

### 🛒 **https://ramsandesh.gumroad.com**
