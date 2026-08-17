# The Unknown Mystery of the AI — Companion Repository

<p align="center">
  <strong>Learn • Build • Deploy • Audit • Master AI</strong>
</p>

<p align="center">
  <a href="https://ramsandesh.gumroad.com"><img src="assets/gumroad-store-badge.svg" alt="Get The Unknown Mystery of the AI on Gumroad" width="420"></a>
</p>

<p align="center">
  <a href="https://github.com/sanskarIN/unknown-mystery-ai/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/sanskarIN/unknown-mystery-ai/actions/workflows/ci.yml/badge.svg"></a>
  <a href="https://github.com/sanskarIN/unknown-mystery-ai/actions/workflows/quality.yml"><img alt="Quality" src="https://github.com/sanskarIN/unknown-mystery-ai/actions/workflows/quality.yml/badge.svg"></a>
  <img alt="Version 1.0.1" src="https://img.shields.io/badge/version-1.0.1-brightgreen">
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/license-Apache--2.0-blue"></a>
  <a href="https://ramsandesh.gumroad.com"><img alt="Gumroad" src="https://img.shields.io/badge/Gumroad-Official%20Store-ff90e8"></a>
</p>

> ## 🛒 Official store: **https://ramsandesh.gumroad.com**

This is the official open-source companion repository for **_The Unknown Mystery of the AI_** by **Ram Sandesh**. Version **1.0.1** is a backward-compatible stable maintenance release with dependency-light code examples, evaluation helpers, reproducibility utilities, RAG/agent patterns, deployment primitives, release evidence, operational safeguards, packaging checks, supply-chain hardening, tests, and engineering documentation that complement the 120-chapter AI mastery journey.

The repository is intentionally **inspectable, testable, local/synthetic by default, and safe for learning**. Small teaching utilities are not presented as automatic substitutes for production security, privacy, scalability, governance, or reliability engineering.

## Stable 1.x areas

- AI/ML evaluation and reproducibility
- Text normalization and deterministic chunking
- Versioned prompts and output regression fixtures
- Retrieval-Augmented Generation (RAG) baselines and ranking metrics
- Transparent agent/tool orchestration
- Experiment comparison, artifact registries, and release evidence
- Release gates, release comparisons, and stable API snapshots
- Local serving contracts, container guidance, monitoring data, placement, and feature flags
- Privacy redaction, structured validation, cost budgeting, caching, retries, fallback, and rate limiting
- CLI-friendly JSON/text reporting and `python -m umai` execution
- PEP 561 inline typing support
- Responsible AI, privacy, security, reproducibility, supply-chain, accessibility, and governance guidance

## Quick start

```bash
git clone https://github.com/sanskarIN/unknown-mystery-ai.git
cd unknown-mystery-ai
python -m venv .venv
```

Activate the environment and install:

```bash
python -m pip install -e .
python -m unittest discover -s tests -v
```

Use the companion CLI:

```bash
umai-companion version
umai-companion info
umai-companion info --json
umai-companion store
```

The module form is also supported:

```bash
python -m umai info
```

Or use the Makefile on compatible systems:

```bash
make install
make test
make examples
```

For stable release installation options, see [`docs/INSTALLATION.md`](docs/INSTALLATION.md).

## Runnable examples

The numbered example suite covers reproducibility, evaluation, RAG, agents, release identity, observability, text chunking, prompt versioning, drift, budgeting, privacy, caches, validation, experiments, artifact approvals, retries, rate limiting, serving contracts, release gates, synthetic monitoring, edge/cloud placement, feature flags, ranking metrics, regression tests, release comparisons, fallback chains, deprecations, and structured release evidence.

See **[`examples/README.md`](examples/README.md)**.

## Repository map

```text
unknown-mystery-ai/
├── api/                       # Committed public API compatibility snapshots
├── assets/                    # Gumroad badge and repository visual assets
├── docs/                      # Architecture, API, learning, governance, release docs
├── examples/                  # Small runnable teaching examples
├── scripts/                   # Quality and release-evidence scripts
├── src/umai/                  # Stable dependency-light typed companion package
├── tests/                     # Standard-library unit tests
├── .github/                   # CI, quality, funding, Dependabot, templates
├── Dockerfile                 # Non-root companion container example
├── MANIFEST.in                # Source distribution manifest
├── LICENSE                    # Apache License 2.0 for source code
├── NOTICE                     # Book/content rights notice
├── Makefile                   # Common local development commands
└── README.md
```

## Documentation

Recommended starting points:

- [`docs/BOOK_COMPANION.md`](docs/BOOK_COMPANION.md) — how this repository complements the book
- [`docs/CHAPTER_COMPANION_INDEX.md`](docs/CHAPTER_COMPANION_INDEX.md) — 120-chapter block mapping
- [`docs/API_REFERENCE.md`](docs/API_REFERENCE.md) — public utility reference
- [`docs/API_COMPATIBILITY.md`](docs/API_COMPATIBILITY.md) — semantic-versioning and deprecation policy
- [`docs/STABILITY.md`](docs/STABILITY.md) — 1.x stability guarantees
- [`docs/CLI.md`](docs/CLI.md) — command-line usage
- [`docs/INSTALLATION.md`](docs/INSTALLATION.md) — clone and stable-release installation
- [`docs/TYPING.md`](docs/TYPING.md) — inline typing and PEP 561 support
- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) — design principles and trust boundaries
- [`docs/DEVELOPMENT.md`](docs/DEVELOPMENT.md) — local development workflow
- [`docs/TESTING_STRATEGY.md`](docs/TESTING_STRATEGY.md) — automated validation layers
- [`docs/SECURITY_MODEL.md`](docs/SECURITY_MODEL.md) — trust boundaries and safe defaults
- [`docs/PRIVACY_MODEL.md`](docs/PRIVACY_MODEL.md) — privacy and telemetry model
- [`docs/SUPPLY_CHAIN.md`](docs/SUPPLY_CHAIN.md) — software supply-chain controls
- [`docs/GITHUB_ACTIONS_SECURITY.md`](docs/GITHUB_ACTIONS_SECURITY.md) — full-SHA Action pinning policy
- [`docs/DEPENDENCIES.md`](docs/DEPENDENCIES.md) — minimal dependency policy
- [`docs/DEPENDABOT.md`](docs/DEPENDABOT.md) — dependency-update review policy
- [`docs/ACCESSIBILITY.md`](docs/ACCESSIBILITY.md) — accessible documentation/output guidance
- [`docs/EXAMPLE_CONTRACTS.md`](docs/EXAMPLE_CONTRACTS.md) — numbered example compatibility rules
- [`docs/BRANCH_PROTECTION.md`](docs/BRANCH_PROTECTION.md) — recommended `main` protection settings
- [`docs/SIGNING.md`](docs/SIGNING.md) — prospective commit/tag signing guidance
- [`docs/REPOSITORY_SETTINGS.md`](docs/REPOSITORY_SETTINGS.md) — recommended GitHub settings and topics
- [`docs/RELEASE_ASSETS.md`](docs/RELEASE_ASSETS.md) — wheel/source/checksum release provenance
- [`docs/RELEASE_STATUS.md`](docs/RELEASE_STATUS.md) — stable release identity
- [`docs/MAINTENANCE.md`](docs/MAINTENANCE.md) — post-1.0 maintenance policy
- [`docs/RELEASE_1_0_CHECKLIST.md`](docs/RELEASE_1_0_CHECKLIST.md) — original stable 1.0 verification
- [`docs/RELEASE_1_0_1_CHECKLIST.md`](docs/RELEASE_1_0_1_CHECKLIST.md) — 1.0.1 maintenance release verification
- [`docs/COMPANION_RELEASE_1.0.md`](docs/COMPANION_RELEASE_1.0.md) — 1.0.0 release notes
- [`docs/COMPANION_RELEASE_1.0.1.md`](docs/COMPANION_RELEASE_1.0.1.md) — 1.0.1 hardening release notes
- [`docs/GUMROAD.md`](docs/GUMROAD.md) — official commercial publication destination

## Quality gates

The repository includes automated checks for:

- supported Python tests,
- cross-platform numbered example smoke runs,
- package metadata/version consistency,
- release notes/changelog/version consistency,
- PEP 561 typing marker packaging,
- full-commit-SHA GitHub Action pins,
- public-repository commercial manuscript boundaries,
- canonical Gumroad/repository/contact links in key files,
- internal Markdown links,
- public API snapshot consistency,
- wheel/source distribution contents,
- SHA-256 build manifests,
- release-candidate build evidence.

## Stable GitHub release

The stable GitHub software release contains the companion wheel, source distribution, and `SHA256SUMS.txt`, built from the immutable version tag. These are software companion artifacts only; the paid eBook and commercial artwork remain outside the public GitHub release.

Current stable release page: **https://github.com/sanskarIN/unknown-mystery-ai/releases/tag/v1.0.1**

Historical v1.0.0 release: **https://github.com/sanskarIN/unknown-mystery-ai/releases/tag/v1.0.0**

## Book vs. code licensing

The **source code** in this repository is licensed under the **Apache License 2.0** unless a file says otherwise.

The complete eBook, chapter text, PDF/DOCX editions, cover artwork, certificate artwork, book-specific illustrations, and commercial publication assets are **© 2026 Ram Sandesh. All Rights Reserved.** They are not distributed under Apache-2.0 and are intentionally not included in this public repository.

See [`NOTICE`](NOTICE) and [`docs/LICENSE_SCOPE.md`](docs/LICENSE_SCOPE.md).

## Official book store

### 🛒 **https://ramsandesh.gumroad.com**

The Gumroad store is the primary place for official book releases, updated commercial editions, and related publishing materials.

## Author and project links

- Author: **Ram Sandesh**
- GitHub: **https://github.com/sanskarIN**
- Repository: **https://github.com/sanskarIN/unknown-mystery-ai**
- Gumroad: **https://ramsandesh.gumroad.com**
- Contact: **sanskarin@outlook.in**

## Contributing

Contributions are welcome for original code examples, documentation corrections, tests, accessibility improvements, reproducibility tooling, and safe educational resources. Read [`CONTRIBUTING.md`](CONTRIBUTING.md) first.

Maintainer Git identity for repository work:

```bash
git config user.name "Sanskar"
git config user.email "sanskarin@outlook.in"
```

## Security and privacy

Do not publish secrets, credentials, private datasets, personal information, or sensitive user payloads in issues, examples, tests, or pull requests. See [`SECURITY.md`](SECURITY.md).

---

<p align="center">
  <strong>Support the complete AI learning journey:</strong><br>
  <a href="https://ramsandesh.gumroad.com"><strong>🛒 https://ramsandesh.gumroad.com</strong></a>
</p>
