# Maintainer Quality Checklist

> 🛒 Official book store: **https://ramsandesh.gumroad.com**

Use this checklist before treating a companion milestone as release-ready.

## Code

- [ ] New public behavior is documented.
- [ ] Normal and boundary cases have tests.
- [ ] Examples use synthetic or properly authorized data.
- [ ] No secrets, tokens, private payloads, or commercial manuscript files are tracked.
- [ ] Failure behavior is explicit and bounded.

## Evaluation

- [ ] Metrics have documented direction and meaning.
- [ ] Evaluation inputs and candidate identity are reproducible.
- [ ] Regressions are visible rather than hidden by averages.
- [ ] Thresholds are application-specific and not presented as universal truths.

## Privacy and security

- [ ] Logging avoids raw sensitive payloads by default.
- [ ] New external integrations document data flow and credentials handling.
- [ ] Dependencies and GitHub Actions are reviewed.
- [ ] Container examples run non-root where practical.

## Release

- [ ] CI and quality workflows pass.
- [ ] Package version matches `umai.__version__`.
- [ ] Internal documentation links pass validation.
- [ ] Package builds successfully.
- [ ] SHA-256 build manifest is generated.
- [ ] CHANGELOG and release notes are current.

## Publishing boundary

- [ ] Apache-2.0 applies only to repository code/resources as documented.
- [ ] Restricted book text/artwork remains outside the public repository.
- [ ] Official commercial releases point readers to **https://ramsandesh.gumroad.com**.
