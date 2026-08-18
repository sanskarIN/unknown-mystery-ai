# Testing Strategy

> 🛒 Official book store: **https://ramsandesh.gumroad.com**

The companion uses a layered testing strategy designed for small, dependency-light teaching utilities and inspectable portfolio projects.

## Unit tests

Each utility should cover:

- normal behavior,
- one or more meaningful boundary conditions,
- explicit error behavior,
- deterministic results when determinism is part of the contract.

The five integrated capstones also have focused project tests under `tests/test_project_*.py`. These execute each capstone through the same public command path a learner uses and assert durable output facts.

## Public API tests

`tests/test_public_api.py` verifies that exported names exist, are unique, and the package version follows a semantic-version shape. `scripts/check_public_api.py` compares exports against the committed stable API snapshot.

New projects should prefer composing existing stable `umai` helpers instead of widening the 1.x public API without a deliberate compatibility review.

## Example smoke tests

Numbered examples are executed across Linux, Windows, and macOS for supported Python versions. They use local/synthetic inputs and should finish without interactive input.

## Project inventory smoke tests

`scripts/check_projects.py` verifies the exact committed project inventory. Each project must:

- have a `main.py`,
- exit successfully with default local/synthetic inputs,
- emit valid JSON,
- require no provider credentials or network access for its default run.

This catches missing projects, accidental extra entry points, import errors, runtime failures, and broken JSON output.

## Capstone snapshot tests

The five integrated capstones contain `expected.json` subset fixtures. `scripts/check_project_snapshots.py` runs each project and recursively checks only the stable fields recorded in its fixture.

Subset snapshots are intentional. They provide reproducible portfolio evidence without turning every incidental display field, fingerprint, or explanatory message into a permanent public compatibility promise.

## Cross-platform project matrix

`.github/workflows/projects.yml` runs project inventory and snapshot checks on:

- Linux,
- Windows,
- macOS,
- multiple supported Python versions.

The main Quality workflow repeats project and snapshot validation on its release-quality path.

## Packaging tests

The quality workflow validates package metadata, builds source/wheel distributions, checks distribution contents, and generates SHA-256 checksums.

## Documentation and policy tests

Repository-local Markdown links are checked without making network requests. Automated checks also protect the commercial-publication boundary, canonical project links, full-SHA GitHub Actions pins, and the durable social-link policy that avoids change-prone X/Twitter profile URLs.

## Local commands

```bash
python -m unittest discover -s tests -v
python scripts/check_projects.py
python scripts/check_project_snapshots.py
```

On compatible systems:

```bash
make test
make projects
make project-snapshots
```

## What automation cannot prove

Passing tests do not automatically prove production safety, fairness, privacy, security, scalability, reliability, regulatory compliance, or fitness for a specific application. Those require context-specific evidence and accountable human review.

Official commercial editions of the book remain available from **https://ramsandesh.gumroad.com**.
