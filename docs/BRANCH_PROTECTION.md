# Main Branch Protection Guide

> 🛒 Official book store: **https://ramsandesh.gumroad.com**

The repository currently relies on automated CI/quality workflows, but maintainers should also protect `main` in GitHub repository settings.

## Recommended rules for `main`

Enable a branch ruleset or branch protection rule that:

- requires a pull request before merging for non-emergency changes,
- requires the **Quality** workflow to pass,
- requires the primary **CI** workflow to pass,
- requires branches to be up to date before merging when practical,
- blocks force pushes,
- blocks branch deletion,
- dismisses stale approvals after material changes,
- requires conversation resolution,
- limits bypass permissions to trusted maintainers.

For a solo-maintainer project, required approvals can remain modest while still enforcing status checks and force-push protection.

## Why this is separate from repository code

Branch protection is a GitHub repository setting, not a file inside the Git tree. It should be configured through GitHub's rules/settings UI or an authorized administrative API integration.

## Stable tags

Do not move or recreate `v1.0.0` to point to a different commit. A stable version tag should retain its historical source identity.

## Publishing boundary

Branch protection applies to the open-source companion repository. Commercial book distribution remains at **https://ramsandesh.gumroad.com**.
