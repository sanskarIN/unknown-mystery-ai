# Recommended GitHub Repository Settings

> 🛒 Official book store: **https://ramsandesh.gumroad.com**

Some important repository controls live in GitHub settings rather than Git-tracked files. The following configuration is recommended for the public companion repository.

## About section

- Description: keep the current official companion description.
- Website/Homepage: **https://ramsandesh.gumroad.com**
- Suggested topics: `artificial-intelligence`, `machine-learning`, `deep-learning`, `generative-ai`, `llm`, `rag`, `ai-agents`, `mlops`, `responsible-ai`, `ai-evaluation`, `python`, `ai-education`.

## Features

- Keep **Issues** enabled for bugs, questions, and documentation reports.
- Keep **Pull Requests** enabled for community contributions.
- Enable **Discussions** only if there is a plan to moderate community questions separately from actionable issues.
- Disable unused features such as Wiki/Projects if they become empty duplicates of tracked documentation/roadmaps.

## Security

- Enable branch/ruleset protection for `main` as documented in [`BRANCH_PROTECTION.md`](BRANCH_PROTECTION.md).
- Keep Dependabot alerts/security updates enabled where available.
- Review secret scanning and push protection options available to the repository/account.
- Consider requiring signed commits for future release work after a signing setup is established.

## Releases

Keep `v1.0.0` immutable in meaning. GitHub software release assets should contain only the Apache-2.0 companion package and checksums, never the commercial manuscript.

## Funding / commercial publication

`.github/FUNDING.yml` points to the official Gumroad store. The public repository should continue directing readers to:

### **https://ramsandesh.gumroad.com**
