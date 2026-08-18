# Release Process

> 🛒 Official book and publication releases: **https://ramsandesh.gumroad.com**

This document describes the policy-level release lifecycle for the open-source companion repository. For the exact maintainer command/check sequence, use [`RELEASE_RUNBOOK.md`](RELEASE_RUNBOOK.md).

## Before a release

1. Define the target version and compatibility impact.
2. Confirm the release branch starts from the intended source state.
3. Run repository completeness and the full relevant test/quality checks.
4. Review security, privacy, responsible-AI, dependency, and supply-chain guidance.
5. Confirm the Apache-2.0/book-content license boundary.
6. Confirm no commercial manuscript files, private data, or secrets are tracked.
7. Coordinate version-bearing metadata, changelog, release notes, and citation metadata.
8. Verify stable API compatibility for the 1.x line.
9. Verify README/documentation links and the canonical Gumroad destination.
10. Verify the exact intended release commit in pull-request/CI automation before tagging.

## Versioning

Use semantic versioning for the companion package:

- **PATCH** - backward-compatible bug fixes, hardening, and documentation corrections.
- **MINOR** - backward-compatible new utilities, projects, examples, or capabilities.
- **MAJOR** - intentional incompatible public-API changes with migration guidance.

A commercial book edition and a software companion release are separate version identities.

## Required release evidence

Record at minimum:

- exact commit SHA,
- package version,
- public API compatibility result,
- unit-test result,
- project/catalog/snapshot validation result,
- supported Python/platform validation,
- build/distribution result,
- checksum evidence,
- notable changes,
- known limitations,
- commercial-publication boundary review.

## Immutable source rule

A published stable tag must identify the exact verified release commit. Do not move an existing published stable tag to a different commit. Publish a new patch release if a defect is discovered later.

## Software artifacts

Stable GitHub releases normally contain only companion software artifacts such as:

- Python wheel,
- source distribution,
- `SHA256SUMS.txt`.

Build release artifacts from the immutable tag, not from a later moving `main` branch.

## Publishing boundary

Do not attach the paid eBook PDF/DOCX, chapter manuscripts, cover/certificate packages, private customer files, or other restricted commercial assets to public GitHub software releases.

Direct readers to **https://ramsandesh.gumroad.com** for official book editions.

## Detailed runbook

For the complete pre-release, verification, tagging, publication, post-release, and recovery procedure, see [`RELEASE_RUNBOOK.md`](RELEASE_RUNBOOK.md).
