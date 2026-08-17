# v1.0.1 Maintenance Release Checklist

> 🛒 Official publication: **https://ramsandesh.gumroad.com**

This checklist records the verified backward-compatible 1.0.1 hardening release.

## Version and API

- [x] `pyproject.toml` version is `1.0.1`.
- [x] `umai.__version__` is `1.0.1`.
- [x] `api/public_api_1_0.json` records `1.0.1` and the public symbol set remains compatible with 1.0.0.
- [x] Citation metadata records `1.0.1`.

## Packaging

- [x] `py.typed` is present in the wheel.
- [x] Required README/LICENSE/NOTICE/CITATION/package metadata are present in the source distribution.
- [x] `python -m umai version` works.
- [x] `umai-companion version` works.
- [x] Wheel and source distributions build successfully.
- [x] SHA-256 checksums are generated.

## Repository hardening

- [x] External GitHub Actions are pinned to full reviewed commit SHAs.
- [x] Public repository manuscript-boundary validation passes.
- [x] Canonical Gumroad/repository/contact link validation passes.
- [x] Internal Markdown link validation passes.
- [x] Unit tests pass.
- [x] Numbered examples pass.
- [x] Cross-platform example smoke workflow remains configured.

## Release

- [x] Quality workflow passes on the exact release commit.
- [x] Create immutable `v1.0.1` from the verified commit.
- [x] Create GitHub release using `docs/COMPANION_RELEASE_1.0.1.md`.
- [x] Build release assets from the immutable `v1.0.1` tag.
- [x] Attach wheel, source distribution, and `SHA256SUMS.txt`.
- [x] Verify no paid manuscript or commercial publication asset is attached.

## Manual GitHub settings

The following remain administrative/account settings rather than normal Git commits. They are intentionally not marked complete because the available repository connector cannot change these account-level settings:

- [ ] Protect `main` using the recommendations in `docs/BRANCH_PROTECTION.md`.
- [ ] Configure prospective commit/tag signing as described in `docs/SIGNING.md` if desired.
- [ ] Set the repository homepage/topics using `docs/REPOSITORY_SETTINGS.md`.

## Commercial publication

Official book editions and commercial publishing materials remain at:

### **https://ramsandesh.gumroad.com**
