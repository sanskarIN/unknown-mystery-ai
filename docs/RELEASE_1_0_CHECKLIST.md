# Stable 1.0 Maintainer Checklist

> 🛒 Official publication: **https://ramsandesh.gumroad.com**

## Public API

- [ ] `api/public_api_1_0.json` matches `umai.__all__`.
- [ ] API reference documents every exported symbol/group.
- [ ] API compatibility and stability policies are published.
- [ ] CLI entry point and documented commands work.

## Validation

- [ ] Unit tests pass.
- [ ] Public API test passes.
- [ ] Example smoke matrix passes.
- [ ] Internal Markdown links pass.
- [ ] Package metadata/version check passes.
- [ ] Wheel and source distribution build.
- [ ] SHA-256 checksums are generated.

## Repository governance

- [ ] LICENSE, NOTICE, CONTRIBUTING, SECURITY, SUPPORT, CODEOWNERS, and community templates are present.
- [ ] Dependabot and CI workflows are enabled.
- [ ] Changelog, roadmap, citation metadata, and release notes are current.

## Publication boundary

- [ ] No paid manuscript PDF/DOCX is in the public repository.
- [ ] No commercial cover/certificate assets are mistakenly Apache-2.0 licensed.
- [ ] Gumroad is highlighted as the official commercial publication destination: **https://ramsandesh.gumroad.com**.

## Tagging

- [ ] Record the final source commit.
- [ ] Confirm latest relevant workflows pass.
- [ ] Create the `v1.0.0` tag from the verified commit.
- [ ] Publish release notes that restate the code/book licensing boundary.
