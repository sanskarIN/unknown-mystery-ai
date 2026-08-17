# Stable Release Candidate Checklist

> 🛒 Official book store: **https://ramsandesh.gumroad.com**

Use this checklist before promoting a companion release candidate toward 1.0.

## API stability

- [ ] Every public symbol is exported through `umai.__all__`.
- [ ] Every public symbol is described in `docs/API_REFERENCE.md`.
- [ ] The compatibility and deprecation policy is current.
- [ ] Public API snapshot checks pass.
- [ ] Any deprecation includes a replacement/removal plan when applicable.

## Tests and examples

- [ ] Unit tests pass on supported Python versions.
- [ ] Numbered examples pass on Linux, Windows, and macOS smoke workflows.
- [ ] Examples rely on synthetic/local data unless a source is explicitly authorized.
- [ ] Failure and boundary behavior is covered for new utilities.

## Packaging

- [ ] Package version matches `umai.__version__`.
- [ ] Wheel and source distribution build successfully.
- [ ] Package metadata validation passes.
- [ ] SHA-256 checksums are generated for build artifacts.

## Documentation and community

- [ ] Internal Markdown links pass validation.
- [ ] README, API reference, changelog, roadmap, and release notes are current.
- [ ] Security, support, contribution, and license-boundary documentation remains accurate.

## Publication boundary

- [ ] No paid eBook PDF/DOCX is tracked in the public repository.
- [ ] No restricted cover/certificate/commercial artwork is accidentally relicensed.
- [ ] Official commercial publication links point to **https://ramsandesh.gumroad.com**.

## Final evidence

Record the source commit, workflow results, package version, build checksums, known limitations, and release notes before tagging the stable release.
