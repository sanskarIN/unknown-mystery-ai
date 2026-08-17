# Release Process

> 🛒 Official book and publication releases: **https://ramsandesh.gumroad.com**

This document covers only the open-source companion repository.

## Before a release

1. Run the complete test suite.
2. Run the release-check workflow.
3. Review security and privacy guidance.
4. Confirm the Apache-2.0/book-content license boundary.
5. Confirm no commercial manuscript files or secrets are tracked.
6. Update `CHANGELOG.md` and package version.
7. Verify README links, especially the official Gumroad store.

## Versioning

Use semantic versioning for the companion package:

- PATCH: compatible fixes and documentation improvements.
- MINOR: compatible new utilities and examples.
- MAJOR: intentional incompatible API changes.

## Release evidence

Record:

- commit SHA,
- package version,
- test result,
- supported Python versions,
- notable changes,
- known limitations.

## Publishing boundary

Do not attach the paid eBook PDF/DOCX or restricted commercial assets to public GitHub releases. Direct readers to **https://ramsandesh.gumroad.com** for official book editions.
