# UMAI Companion 1.1.0

> 🛒 Official publication: **https://ramsandesh.gumroad.com**

Version **1.1.0** expands the open-source companion with a portfolio-oriented project layer, five integrated capstones, a complete documentation system, and stronger repository-integrity validation while preserving the documented stable 1.x `umai` public API.

## Highlights

- 25 complete runnable companion projects under `projects/`.
- Five integrated capstones that combine multiple stable utilities into end-to-end teaching workflows.
- Machine-readable project catalog with schema/inventory validation.
- Stable-subset JSON snapshot fixtures for the integrated capstones.
- Cross-platform project verification on Linux, Windows, and macOS.
- Focused project tests integrated into the standard unit-test suite.
- Canonical documentation hub plus complete user, developer, project-authoring, portfolio, compatibility, limitations, testing, and release-runbook guidance.
- Repository-completeness validation integrated into the Quality workflow.
- Durable social-link policy that avoids embedding change-prone X/Twitter profile URLs in long-lived repository assets.
- Public/commercial publication boundary checks that keep paid book assets outside the Apache-2.0 software release.

## Integrated capstones

1. **AI Release Readiness Console** — validation, privacy-aware identifiers, evaluation, gates, and evidence.
2. **RAG Evaluation Capstone** — retrieval, relevance judgments, ranking metrics, and output regression.
3. **MLOps Release Pipeline** — artifact approval, baseline comparison, gates, release manifest, and evidence bundle.
4. **Responsible AI Review Board** — intended-use documentation, human oversight, privacy-aware display, and governance gates.
5. **Production Resilience Lab** — fallback, cache, serving identity, placement constraints, and explicit cost assumptions.

## Documentation

Version 1.1.0 adds a canonical [`docs/README.md`](README.md) index and dedicated guides for:

- end-to-end repository use,
- developer contribution and validation,
- project authoring contracts,
- portfolio evidence,
- Python/platform/API compatibility,
- known limitations and non-goals,
- exact maintainer release procedures.

The root README points to this documentation hub so major user and maintainer workflows are discoverable from the repository front page.

## Repository integrity and verification

The repository now includes a structural completeness gate in addition to package and project tests:

```bash
python scripts/check_repository_completeness.py
python scripts/check_project_catalog.py
python -m unittest discover -s tests -v
python scripts/check_projects.py
python scripts/check_project_snapshots.py
python scripts/check_public_api.py --require-version-match
python scripts/check_release_candidate.py
```

The completeness gate checks required top-level repository assets, durable documentation, required workflows, project catalog count, documentation discoverability, and canonical long-lived links.

A dedicated Project Matrix repeats project/catalog/snapshot checks across Linux, Windows, and macOS using multiple supported Python versions. The Quality workflow additionally verifies metadata, release documentation, full-SHA workflow pins, public/commercial boundaries, durable links, stable API identity, examples, package builds, distribution contents, and SHA-256 evidence.

## Compatibility

The stable public `umai` symbol set is unchanged from 1.0.x. Version 1.1.0 adds projects, fixtures, tests, workflows, validation scripts, and documentation without removing or incompatibly changing documented 1.x APIs.

The stable package continues to target Python 3.10+ and does not add a mandatory third-party runtime dependency.

## Limitations

The companion remains an educational engineering baseline. Passing repository automation does not certify a system as production-safe, secure, private, fair, scalable, legally compliant, or fit for a particular high-stakes use. These boundaries are documented in `docs/KNOWN_LIMITATIONS.md` and the security/privacy guidance.

## Release verification rule

The `v1.1.0` stable tag must be created from the **exact intended release commit only after the required repository, Quality, CI, Project Matrix, and release/documentation checks have succeeded**. Built software assets should come from the immutable tag.

## Public/commercial boundary

The Apache-2.0 GitHub repository contains companion software and eligible educational resources only.

The complete eBook, chapter text, PDF/DOCX editions, cover artwork, certificate artwork, and other commercial publication assets remain **© 2026 Ram Sandesh. All Rights Reserved.** They must not be attached to the public Apache-2.0 software release.

## Official publication

### **https://ramsandesh.gumroad.com**
