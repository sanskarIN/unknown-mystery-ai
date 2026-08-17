# The Unknown Mystery of the AI — Companion Repository

<p align="center">
  <strong>Learn • Build • Deploy • Audit • Master AI</strong>
</p>

<p align="center">
  <a href="https://ramsandesh.gumroad.com"><img src="assets/gumroad-store-badge.svg" alt="Get The Unknown Mystery of the AI on Gumroad" width="360"></a>
</p>

> **Official store:** **https://ramsandesh.gumroad.com**

This is the official open-source companion repository for **_The Unknown Mystery of the AI_** by **Ram Sandesh**. It provides selected code examples, reproducibility utilities, exercises, project starters, evaluation helpers, and practical learning resources that complement the 120-chapter AI mastery series.

## What this repository covers

- Artificial intelligence foundations
- Machine learning and evaluation
- Deep learning concepts
- Generative AI and LLM application patterns
- Retrieval-Augmented Generation (RAG)
- Agent-style orchestration patterns
- MLOps, release manifests, reproducibility, and observability
- Responsible AI, safety, privacy, and governance concepts
- Portfolio projects and interview preparation

## Quick start

```bash
git clone https://github.com/sanskarIN/unknown-mystery-ai.git
cd unknown-mystery-ai
python -m venv .venv
```

Activate the virtual environment, then install the project in editable mode:

```bash
pip install -e .
python -m unittest discover -s tests -v
```

Run the examples:

```bash
python examples/01_reproducible_experiment.py
python examples/02_evaluation_demo.py
python examples/03_rag_demo.py
python examples/04_agent_demo.py
python examples/05_release_manifest.py
```

## Repository map

```text
unknown-mystery-ai/
├── assets/                    # Store badge and visual repository assets
├── docs/                      # Companion documentation and learning roadmaps
├── examples/                  # Small, readable runnable examples
├── src/umai/                  # Reusable companion utilities
├── tests/                     # Standard-library unit tests
├── .github/                   # CI, issue templates, and PR template
├── LICENSE                    # Apache License 2.0 for source code
├── NOTICE                     # Book/content rights notice
└── README.md
```

## Book vs. code licensing

The **source code** in this repository is licensed under the **Apache License 2.0** unless a file says otherwise.

The complete eBook, chapter text, PDF/DOCX editions, cover artwork, certificate artwork, book-specific illustrations, and commercial publication assets are **© 2026 Ram Sandesh. All Rights Reserved.** They are not distributed under the Apache License 2.0 and are intentionally not included here.

See [`NOTICE`](NOTICE) and [`docs/LICENSE_SCOPE.md`](docs/LICENSE_SCOPE.md) for details.

## Official book store

### 🛒 Get the book and official releases

**https://ramsandesh.gumroad.com**

The Gumroad store is the primary place for book releases, updated editions, and related publishing materials.

## Author and project links

- Author: **Ram Sandesh**
- GitHub: **https://github.com/sanskarIN**
- Repository: **https://github.com/sanskarIN/unknown-mystery-ai**
- Gumroad: **https://ramsandesh.gumroad.com**
- Contact: **sanskarin@outlook.in**

## Contributing

Contributions are welcome for code examples, documentation corrections, tests, accessibility improvements, learning resources, and reproducibility tooling. Read [`CONTRIBUTING.md`](CONTRIBUTING.md) before opening a pull request.

## Security

Please do not publish secrets, private data, credentials, or sensitive user information in issues or pull requests. See [`SECURITY.md`](SECURITY.md).

---

<p align="center">
  <strong>Support the complete AI learning journey:</strong><br>
  <a href="https://ramsandesh.gumroad.com"><strong>https://ramsandesh.gumroad.com</strong></a>
</p>
