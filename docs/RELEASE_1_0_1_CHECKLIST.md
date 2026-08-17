# v1.0.1 Maintenance Release Checklist

> 🛒 Official publication: **https://ramsandesh.gumroad.com**

This checklist verifies the backward-compatible 1.0.1 hardening release.

## Version and API

- [ ] `pyproject.toml` version is `1.0.1`.
- [ ] `umai.__version__` is `1.0.1`.
- [ ] `api/public_api_1_0.json` records `1.0.1` and the public symbol set remains compatible with 1.0.0.
- [ ] Citation metadata records `1.0.1`.

## Packaging

- [ ] `py.typed` is present in the wheel.
- [ ] Required README/LICENSE/NOTICE/CITATION/package metadata are present in the source distribution.
- [ ] `python -m umai version` works.
- [ ] `umai-companion version` works.
- [ ] Wheel and source distributions build successfully.
- [ ] SHA-256 checksums are generated.

## Repository hardening

- [ ] External GitHub Actions are pinned to full reviewed commit SHAs.
- [ ] Public repository manuscript-boundary validation passes.
- [ ] Canonical Gumroad/repository/contact link validation passes.
- [ ] Internal Markdown link validation passes.
- [ ] Unit tests pass.
- [ ] Numbered examples pass.
- [ ] Cross-platform example smoke workflow remains configured.

## Release

- [ ] Quality workflow passes on the exact release commit.
- [ ] Create immutable `v1.0.1` from the verified commit.
- [ ] Create GitHub release using `docs/COMPANION_RELEASE_1.0.1.md`.
- [ ] Build release assets from the immutable `v1.0.1` tag.
- [ ] Attach wheel, source distribution, and `SHA256SUMS.txt`.
- [ ] Verify no paid manuscript or commercial publication asset is attached.

## Manual GitHub settings

The following remain administrative/account settings rather than normal Git commits:

- [ ] Protect `main` using the recommendations in `docs/BRANCH_PROTECTION.md`.
- [ ] Configure prospective commit/tag signing as described in `docs/SIGNING.md` if desired.
- [ ] Set the repository homepage/topics using `docs/REPOSITORY_SETTINGS.md`.

## Commercial publication

Official book editions and commercial publishing materials remain at:

### **https://ramsandesh.gumroad.com**
