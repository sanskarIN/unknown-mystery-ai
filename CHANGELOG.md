# Changelog

> 🛒 **Official Gumroad store:** **https://ramsandesh.gumroad.com**

All notable changes to the open-source companion repository are documented here.

## [Unreleased]

Future 1.x work should remain backward-compatible with the documented stable public API unless a security or material correctness issue requires otherwise.

### Added

- Stable `v1.0.0` wheel, source distribution, and `SHA256SUMS.txt` GitHub release assets built from the immutable stable tag
- Release-asset provenance workflow that rebuilds only from `v1.0.0`
- Full-SHA GitHub Action pin validation
- Public-repository commercial-publication boundary validation
- Canonical Gumroad/repository/contact link validation for key project files
- Built distribution content validation
- PEP 561 `py.typed` marker and distribution packaging support
- `python -m umai` module entry point
- Explicit source-distribution manifest
- Branch protection, commit/tag signing, repository settings, installation, Actions security, dependency review, typing, release asset, testing, privacy, security, supply-chain, accessibility, and maintenance guides
- Documentation and question issue templates
- Repository text-normalization rules through `.gitattributes`

### Changed

- Upgraded `actions/checkout` to v7.0.1, `actions/setup-python` to v7.0.0, and `actions/upload-artifact` to v7.0.1
- Pinned external workflow Actions to verified full commit SHAs
- Expanded Quality and Release Candidate workflows with supply-chain, commercial-publication boundary, canonical-link, API, distribution, test, example, build, and checksum checks
- Expanded README navigation, release asset guidance, security documentation, and publication boundary information
- Focused Dependabot on GitHub Actions because the stable companion has no third-party runtime dependencies

## [1.0.0] - 2026-08-17

### Stable milestone

- Declared the documented `umai.__all__` surface stable for the 1.x line
- Added `api/public_api_1_0.json` as the stable compatibility snapshot
- Published 1.x stability guarantees and versioned example contracts
- Added the stable 1.0 maintainer verification checklist
- Updated package metadata to Production/Stable
- Updated citation metadata to 1.0.0
- Published comprehensive 1.0 release notes and README

### Included capability areas

- Reproducibility and fingerprints
- Classification and retrieval evaluation
- RAG and transparent agent teaching patterns
- Versioned prompts and regression fixtures
- Experiment, artifact, release, and governance evidence
- Local serving, monitoring, deployment placement, and configuration patterns
- Privacy redaction, validation, budgets, caching, retry, fallback, and rate limiting
- Structured JSON/text reporting and dependency-free CLI
- Cross-platform examples, CI, quality gates, builds, checksums, and release evidence

## [0.6.0] - 2026-08-17

### Added

- Formal public API compatibility and deprecation policy
- `DeprecatedFeature` and actionable deprecation warning helper
- Deterministic structured JSON and key/value reporting helpers
- Structured `EvidenceBundle` for release evidence
- Dependency-free `umai-companion` CLI and JSON output
- Public API 0.6 snapshot and compatibility checker
- Release-candidate checklist and manual release-candidate workflow
- Expanded API and examples documentation

## [0.5.0] - 2026-08-17

### Added

- Public API compatibility smoke test
- Cross-platform example smoke workflow
- Internal Markdown link validation script and workflow
- Package metadata/version consistency validation
- SHA-256 release artifact manifest generator
- Comprehensive quality workflow with build evidence upload
- Maintainer quality checklist and checksum documentation

## [0.4.0] - 2026-08-17

### Added

- Retrieval ranking metrics: precision@k, recall@k, reciprocal rank
- Transparent prompt/output regression fixtures
- Release metric comparison helpers
- Explicit fallback chains for recoverable failures
- Examples and unit tests for each evaluation/reliability utility

## [0.3.0] - 2026-08-17

### Added

- Local inference request/response serving contracts
- Non-root container example and container safety guide
- Explicit release-gate decisions
- Deterministic synthetic monitoring series
- Edge/cloud placement constraint comparison
- Feature-flag configuration helpers
- Deployment-focused examples and tests

## [0.2.0] - 2026-08-17

### Added

- Deterministic text normalization and chunking
- Versioned prompt templates
- Lightweight numeric drift indicators
- Caller-supplied token cost estimation
- Common email/phone redaction and pseudonymous IDs
- Bounded in-memory LRU cache
- Structured record validation
- Experiment evidence and comparison records
- Artifact registry and explicit approval flow
- Bounded retry helper
- Fixed-window rate limiter
- Runnable examples for every new utility
- Focused unit tests for new utilities and boundary cases
- Architecture, development, release, troubleshooting, FAQ, API, examples, tests, and chapter companion documentation
- CODEOWNERS, Dependabot, EditorConfig, Makefile, release-check workflow, and GitHub funding link
- Expanded README navigation and highlighted Gumroad publication links

## [0.1.0] - 2026-08-17

### Added

- Companion repository README and project metadata
- Apache-2.0 source license boundary and book rights notice
- Reproducibility and stable fingerprint helpers
- Dependency-free classification evaluation helpers
- Minimal lexical retrieval/RAG baseline
- Transparent tool registry and deterministic routing baseline
- Release manifest utility
- Initial runnable examples and unit tests
- CI workflow
- Learning path and project documentation
- Model card, dataset card, and responsible-AI templates
- Community, security, support, and contribution files
- Highlighted Gumroad store badge and links

## Official book

### https://ramsandesh.gumroad.com
