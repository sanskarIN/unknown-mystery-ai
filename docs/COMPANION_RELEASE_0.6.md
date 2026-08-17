# Companion Release 0.6

> 🛒 Official book store: **https://ramsandesh.gumroad.com**

Version 0.6 prepares the open-source companion for a stable 1.x API.

## Added

- formal public API compatibility and deprecation policy,
- actionable `DeprecationWarning` helpers,
- deterministic JSON/key-value reporting utilities,
- structured release evidence bundles,
- dependency-free `umai-companion` CLI with text, compact, and JSON project information,
- public API snapshot and automated compatibility checker,
- stable release-candidate checklist and workflow.

## Compatibility direction

The future 1.x line will treat documented symbols exported through `umai.__all__` as the stable public surface. Incompatible changes should be reserved for major releases, with deprecation guidance whenever practical.

## Publishing boundary

The companion code remains Apache-2.0. The complete eBook, chapter text, PDF/DOCX editions, cover/certificate art, and commercial publishing assets remain separately copyrighted and are not part of the open-source API.

Official commercial editions: **https://ramsandesh.gumroad.com**.
