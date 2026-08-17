# The Unknown Mystery of the AI — Companion Repository

<p align="center">
  <strong>Learn • Build • Deploy • Audit • Master AI</strong>
</p>

<p align="center">
  <a href="https://ramsandesh.gumroad.com"><img src="assets/gumroad-store-badge.svg" alt="Get The Unknown Mystery of the AI on Gumroad" width="420"></a>
</p>

<p align="center">
  <a href="https://github.com/sanskarIN/unknown-mystery-ai/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/sanskarIN/unknown-mystery-ai/actions/workflows/ci.yml/badge.svg"></a>
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/license-Apache--2.0-blue"></a>
  <a href="https://ramsandesh.gumroad.com"><img alt="Gumroad" src="https://img.shields.io/badge/Gumroad-Official%20Store-ff90e8"></a>
</p>

> ## 🛒 Official store: **https://ramsandesh.gumroad.com**

This is the official open-source companion repository for **_The Unknown Mystery of the AI_** by **Ram Sandesh**. It contains selected code examples, reproducibility utilities, evaluation helpers, RAG and agent teaching patterns, operational helpers, governance examples, tests, and practical documentation for the 120-chapter AI mastery journey.

The repository is intentionally **dependency-light, inspectable, testable, and safe for learning**. It does not pretend that a small teaching implementation is automatically production-ready.

## What this repository covers

- AI/ML evaluation and reproducibility
- Text normalization and deterministic chunking
- Generative AI prompt identity and versioning
- Retrieval-Augmented Generation (RAG) baselines
- Transparent agent/tool orchestration
- Experiment comparison and artifact governance
- Release manifests and reproducible deployment evidence
- Drift indicators and privacy-aware observability
- Cost budgeting, bounded caching, retries, and rate limiting
- Input validation and common identifier redaction
- Responsible AI, privacy, security, and governance checklists
- Portfolio projects, learning roadmaps, and interview preparation

## Quick start

```bash
git clone https://github.com/sanskarIN/unknown-mystery-ai.git
cd unknown-mystery-ai
python -m venv .venv
```

Activate the environment and install the package:

```bash
python -m pip install -e .
python -m unittest discover -s tests -v
```

Or use the Makefile on compatible systems:

```bash
make install
make test
```

## Runnable examples

The repository includes focused examples for reproducibility, evaluation, RAG, agent routing, release manifests, observability, text chunking, prompt versioning, drift, budgeting, privacy redaction, bounded caching, validation gates, experiment comparison, artifact approval, retry limits, and request rate limiting.

See **[`examples/README.md`](examples/README.md)** for the full runnable index.

## Repository map

```text
unknown-mystery-ai/
├── assets/                    # Gumroad badge and repository visual assets
├── docs/                      # Architecture, learning, governance, API and release docs
├── examples/                  # Small, readable runnable examples
├── src/umai/                  # Reusable dependency-light companion utilities
├── tests/                     # Standard-library unit tests
├── .github/                   # CI, release checks, funding, Dependabot, templates
├── LICENSE                    # Apache License 2.0 for source code
├── NOTICE                     # Book/content rights notice
├── Makefile                   # Common local development commands
└── README.md
```

## Documentation

Start with:

- [`docs/BOOK_COMPANION.md`](docs/BOOK_COMPANION.md) — how the repository complements the book
- [`docs/CHAPTER_COMPANION_INDEX.md`](docs/CHAPTER_COMPANION_INDEX.md) — 120-chapter block mapping
- [`docs/API_REFERENCE.md`](docs/API_REFERENCE.md) — compact API guide
- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) — design and trust boundaries
- [`docs/DEVELOPMENT.md`](docs/DEVELOPMENT.md) — local setup and maintainer workflow
- [`docs/LEARNING_PATH.md`](docs/LEARNING_PATH.md) — companion study path
- [`docs/PROJECTS.md`](docs/PROJECTS.md) — portfolio-ready project ideas
- [`docs/REPRODUCIBILITY.md`](docs/REPRODUCIBILITY.md) — reproducibility checklist
- [`docs/OBSERVABILITY.md`](docs/OBSERVABILITY.md) — privacy-aware telemetry guidance
- [`docs/RESPONSIBLE_AI_CHECKLIST.md`](docs/RESPONSIBLE_AI_CHECKLIST.md) — responsible AI review
- [`docs/RELEASE_PROCESS.md`](docs/RELEASE_PROCESS.md) — companion release procedure
- [`docs/TROUBLESHOOTING.md`](docs/TROUBLESHOOTING.md) — common setup and CI issues
- [`docs/FAQ.md`](docs/FAQ.md) — scope and licensing questions
- [`docs/GUMROAD.md`](docs/GUMROAD.md) — official publication store

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

Do not publish secrets, credentials, private datasets, personal information, or sensitive user payloads in issues, examples, tests, or pull requests. See [`SECURITY.md`](SECURITY.md) and the privacy-aware observability guidance.

---

<p align="center">
  <strong>Support the complete AI learning journey:</strong><br>
  <a href="https://ramsandesh.gumroad.com"><strong>🛒 https://ramsandesh.gumroad.com</strong></a>
</p>
