# Dependency Update Review Policy

> 🛒 Official book store: **https://ramsandesh.gumroad.com**

Dependabot monitors GitHub Actions used by this repository. Updates are reviewed rather than blindly merged.

## Review checklist

For each Action update:

1. Confirm the update comes from the expected official repository.
2. Review the release notes and major-version migration notes.
3. Resolve the release tag to its full commit SHA.
4. Update the workflow to the verified SHA and retain a readable version comment.
5. Review any permission, runtime, or behavior changes.
6. Require Quality/CI to pass before considering the update complete.

## Major versions

Major-version updates can change action runtime requirements or behavior. Treat them as engineering changes, not routine text replacements.

## Current approach

The stable companion has no third-party runtime dependencies. GitHub Actions remain the primary automated dependency stream, while Python build tooling is validated by CI/release builds.

## Commercial publication

Dependabot applies to the open-source companion repository. The commercial eBook is distributed separately at **https://ramsandesh.gumroad.com**.
