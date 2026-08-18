# UMAI Companion 1.1.0

> 🛒 Official publication: **https://ramsandesh.gumroad.com**

Version **1.1.0** expands the open-source companion with a portfolio-oriented project layer while preserving the documented stable 1.x `umai` public API.

## Highlights

- 25 complete runnable companion projects under `projects/`.
- Five integrated capstones that combine multiple stable utilities into end-to-end teaching workflows.
- Stable-subset JSON snapshot fixtures for the integrated capstones.
- Cross-platform project verification on Linux, Windows, and macOS.
- Focused project tests integrated into the standard unit-test suite.
- Expanded project, testing, roadmap, and repository documentation.
- Durable social-link policy that avoids embedding change-prone X/Twitter profile URLs in long-lived repository assets.

## Integrated capstones

1. **AI Release Readiness Console** — validation, privacy-aware identifiers, evaluation, gates, and evidence.
2. **RAG Evaluation Capstone** — retrieval, relevance judgments, ranking metrics, and output regression.
3. **MLOps Release Pipeline** — artifact approval, baseline comparison, gates, release manifest, and evidence bundle.
4. **Responsible AI Review Board** — intended-use documentation, human oversight, privacy-aware display, and governance gates.
5. **Production Resilience Lab** — fallback, cache, serving identity, placement constraints, and explicit cost assumptions.

## Verification

The repository now provides three project validation layers:

```bash
python -m unittest discover -s tests -v
python scripts/check_projects.py
python scripts/check_project_snapshots.py
```

A dedicated GitHub Actions Project Matrix repeats project and snapshot checks across Linux, Windows, and macOS using multiple supported Python versions.

## Compatibility

The stable public `umai` symbol set is unchanged from 1.0.x. Version 1.1.0 adds projects, fixtures, tests, workflows, and documentation without removing or incompatibly changing documented 1.x APIs.

## Public/commercial boundary

The Apache-2.0 GitHub repository contains companion software and eligible educational resources only.

The complete eBook, chapter text, PDF/DOCX editions, cover artwork, certificate artwork, and other commercial publication assets remain **© 2026 Ram Sandesh. All Rights Reserved.**

## Official publication

### **https://ramsandesh.gumroad.com**
