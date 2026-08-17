# Companion Release 1.0.1

> 🛒 Official book store: **https://ramsandesh.gumroad.com**

Version **1.0.1** is a backward-compatible maintenance and hardening release of the open-source companion for **_The Unknown Mystery of the AI_** by **Ram Sandesh**.

## Highlights

- Ships a PEP 561 `py.typed` marker so compatible type checkers can consume inline annotations.
- Supports both `umai-companion ...` and `python -m umai ...` command forms.
- Defines source-distribution contents and validates wheel/source package contents in CI.
- Pins external GitHub Actions to verified full commit SHAs while tracking official updates through Dependabot.
- Adds automated guards against accidentally committing paid manuscript formats or commercial package names to the public repository.
- Validates canonical Gumroad, repository, and maintainer contact links in key files.
- Expands installation, testing, security, privacy, accessibility, dependency, supply-chain, branch-protection, signing, repository-setting, and maintenance documentation.
- Keeps stable GitHub release assets separate from commercial book artifacts.

## Compatibility

The documented public `umai` API remains unchanged from 1.0.0. This release preserves the 1.x compatibility guarantees and focuses on packaging, quality, security, documentation, and repository maintenance.

## GitHub Actions hardening

External Actions used by repository workflows are pinned to full commit SHAs. Current reviewed releases include:

- `actions/checkout` v7.0.1
- `actions/setup-python` v7.0.0
- `actions/upload-artifact` v7.0.1

The Quality workflow validates that external `uses:` references remain full-SHA pinned.

## Public/commercial boundary

The Apache-2.0 GitHub release contains only companion software and eligible repository resources.

The complete eBook, chapter text, PDF/DOCX editions, cover artwork, certificates, and other commercial publishing assets remain **© 2026 Ram Sandesh. All Rights Reserved.** They are intentionally excluded from the public software distribution.

## Official publication

### **https://ramsandesh.gumroad.com**

Use the official Gumroad store for commercial book editions and publication materials.
