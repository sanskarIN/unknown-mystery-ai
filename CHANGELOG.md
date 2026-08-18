# Changelog

> 🛒 **Official Gumroad store:** **https://ramsandesh.gumroad.com**

All notable changes to the open-source companion repository are documented here.

## [Unreleased]

Future 1.x work should remain backward-compatible with the documented stable public API unless a security or material correctness issue requires otherwise.

## [1.1.0] - 2026-08-18

### Added

- Twenty-five complete runnable companion projects under `projects/`:
  - Evaluation Report Studio
  - Experiment Leaderboard
  - RAG Knowledge Explorer
  - Retrieval Ranking Benchmark
  - Text Chunking Lab
  - Prompt Template Studio
  - Prompt Regression Lab
  - Agent Router Sandbox
  - Local Serving Contract
  - Resilient Request Pipeline
  - Artifact Registry Workflow
  - Release Manifest Builder
  - Evidence Bundle Builder
  - Release Comparison Dashboard
  - Release Gate Simulator
  - Feature Flag Rollout Lab
  - Edge Cloud Planner
  - Model Monitoring Lab
  - Privacy Audit Workbench
  - Cost Budget Planner
  - AI Release Readiness Console
  - RAG Evaluation Capstone
  - MLOps Release Pipeline
  - Responsible AI Review Board
  - Production Resilience Lab
- `projects/catalog.json` as a machine-readable 25-project inventory with categories, levels, entry points, and snapshot declarations
- `scripts/check_project_catalog.py` and project-catalog unit tests
- `scripts/check_projects.py` inventory validation for every runnable project
- `scripts/check_project_snapshots.py` stable-subset JSON snapshot validation for integrated capstones
- `expected.json` fixtures for the five integrated capstones
- Focused unit tests for all five integrated capstones
- `.github/workflows/projects.yml` cross-platform project verification on Linux, Windows, and macOS
- `make project-catalog`, `make projects`, `make project-snapshots`, and `make release-check` convenience targets
- Expanded project index, staged learning-order documentation, catalog contract, and testing strategy
- Durable social-link policy and automated rejection of change-prone X/Twitter URLs in long-lived repository files
- 1.1.0 release notes, compatibility rationale, metadata policy, release-candidate verifier, and release checklist

### Changed

- CI, Quality, Project Matrix, Documentation Links, Example Smoke Tests, and Release Check workflows now cancel superseded runs with workflow/ref-or-PR concurrency groups
- High-frequency workflow jobs now have explicit timeout limits to prevent indefinitely hanging jobs
- Quality workflow now validates project catalog integrity, all 25 companion projects, capstone snapshot fixtures, and 1.1.0 release-candidate invariants
- Project Matrix now validates the machine-readable project catalog before project smoke/snapshot checks
- Project smoke inventory expanded from twenty to twenty-five runnable projects
- README repository map, navigation, badges, and quality-gate documentation now include the capstone and cross-platform project suite
- `docs/PROJECTS.md` now documents implemented capstones, snapshot contracts, and project verification flow
- Long-lived project documentation prefers stable GitHub, repository, Gumroad, and email destinations over X/Twitter profile URLs
- Package, citation, README, changelog, and stable 1.x API-snapshot metadata promoted to 1.1.0 without changing the documented public symbol set

## [1.0.1] - 2026-08-17

### Added

- Stable software release asset workflow that rebuilds from immutable tags rather than post-release `main`
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
- Preserved the documented 1.0 public API without incompatible changes

## [1.0.0] - 2026-08-17

### Stable milestone

- Declared the documented `umai.__all__` surface stable for the 1.x line
- Added `api/public_api_1_0.json` as the stable compatibility snapshot
- Published 1.x stability guarantees and versioned example contracts
- Added the stable 1.0 maintainer release checklist
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
