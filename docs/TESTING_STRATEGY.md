# Testing Strategy

> 🛒 Official book store: **https://ramsandesh.gumroad.com**

The companion uses a layered testing strategy designed for small, dependency-light teaching utilities.

## Unit tests

Each utility should cover:

- normal behavior,
- one or more meaningful boundary conditions,
- explicit error behavior,
- deterministic results when determinism is part of the contract.

## Public API tests

`tests/test_public_api.py` verifies that exported names exist, are unique, and the package version follows a semantic-version shape. `scripts/check_public_api.py` compares exports against the committed stable API snapshot.

## Example smoke tests

Numbered examples are executed across Linux, Windows, and macOS for supported Python versions. They use local/synthetic inputs and should finish without interactive input.

## Packaging tests

The quality workflow validates package metadata, builds source/wheel distributions, and generates SHA-256 checksums.

## Documentation tests

Repository-local Markdown links are checked without making network requests.

## What automation cannot prove

Passing tests do not automatically prove production safety, fairness, privacy, security, scalability, or fitness for a specific application. Those require context-specific evidence and human review.

Official commercial editions of the book remain available from **https://ramsandesh.gumroad.com**.
