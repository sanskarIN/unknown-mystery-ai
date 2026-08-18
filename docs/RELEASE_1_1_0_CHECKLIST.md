# v1.1.0 Project Expansion Release Checklist

> 🛒 Official publication: **https://ramsandesh.gumroad.com**

## Version and compatibility

- [x] `pyproject.toml` version is `1.1.0`.
- [x] `umai.__version__` is `1.1.0`.
- [x] `api/public_api_1_0.json` records `1.1.0` with the same stable 1.x symbol set.
- [x] `CITATION.cff` records `1.1.0`.
- [x] README version badge is `1.1.0`.
- [x] `CHANGELOG.md` contains a `1.1.0` section.
- [x] Coordinated metadata promotion completed without changing the stable public symbol set.

## Project suite

- [x] 25 expected project entry points are tracked.
- [x] Every project default run emits valid JSON.
- [x] Five integrated capstones are included.
- [x] Five capstone subset snapshot fixtures are included.
- [x] Focused unit tests cover the five capstones.
- [x] `projects/catalog.json` is the canonical machine-readable project catalog.
- [x] `scripts/check_project_catalog.py` validates project/catalog parity.
- [x] `scripts/check_projects.py` validates exact runnable inventory.
- [x] `scripts/check_project_snapshots.py` validates stable capstone fixture subsets.

## Complete documentation

- [x] `docs/README.md` provides a canonical documentation index.
- [x] End-to-end `USER_GUIDE.md` is available.
- [x] `DEVELOPER_GUIDE.md` documents the full developer validation workflow.
- [x] `PROJECT_AUTHORING_GUIDE.md` defines project contribution/output contracts.
- [x] `PORTFOLIO_GUIDE.md` documents reproducible project evidence.
- [x] `COMPATIBILITY_MATRIX.md` records supported Python/platform validation.
- [x] `KNOWN_LIMITATIONS.md` makes educational/non-production boundaries explicit.
- [x] `RELEASE_RUNBOOK.md` documents exact release preparation and recovery procedures.
- [x] Root README links to the complete documentation hub.

## Repository integrity

- [x] `scripts/check_repository_completeness.py` validates required top-level paths, documentation, workflows, project catalog count, and canonical durable links.
- [x] Quality workflow runs the repository-completeness validator before deeper checks.
- [x] `make repository-check` is available for local verification.
- [x] Repository-local Markdown link checking remains enabled.
- [x] Public/commercial publication boundary checking remains enabled.
- [x] Durable X/Twitter-link rejection remains enabled outside documented policy exceptions.
- [x] External GitHub Actions remain pinned to full commit SHAs.

## Cross-platform quality

- [x] Dedicated Project Matrix covers Linux, Windows, and macOS.
- [x] Multiple supported Python versions are included in the Project Matrix.
- [x] CI covers the declared supported Python range.
- [x] Quality runs repository, package, API, tests, examples, projects, snapshots, build, and distribution checks.
- [x] Workflow concurrency/timeouts limit stale queue pressure.

## Final release verification

The boxes below must correspond to the **exact final intended release commit**, not an older candidate.

- [ ] Repository completeness check passes.
- [ ] Full Quality workflow passes.
- [ ] CI workflow passes.
- [ ] Project Matrix workflow passes.
- [ ] Documentation Links / Release Check pass when triggered.
- [ ] Create immutable `v1.1.0` from the verified commit.
- [ ] Publish GitHub release using `docs/COMPANION_RELEASE_1.1.0.md`.
- [ ] Build wheel/source/checksum assets from the immutable tag.
- [ ] Verify commercial eBook/publication files are not attached to the public software release.
- [ ] Update `docs/RELEASE_STATUS.md` and `ROADMAP.md` to mark 1.1.0 stable.
- [ ] Close the 1.1.0 release-tracking issue after verification and asset review.

## Administrative settings

Repository/account settings remain tracked separately because they are not ordinary Git commits, including `main` protection, prospective signing, repository homepage/topics, and secret-scanning/push-protection options.

## Official publication

### **https://ramsandesh.gumroad.com**
