# Contributing

> 🛒 **Official Gumroad store:** **https://ramsandesh.gumroad.com**

Thank you for helping improve the open-source companion repository for **_The Unknown Mystery of the AI_** by Ram Sandesh.

## Good contributions

- bug fixes,
- unit tests,
- clearer examples,
- documentation corrections,
- accessibility improvements,
- reproducibility utilities,
- small portfolio project starters,
- safe and transparent AI engineering patterns.

## Keep commercial book content out of the repository

Do not submit the complete paid manuscript, chapter dumps, commercial PDF/DOCX files, cover source artwork, or other All-Rights-Reserved publishing assets.

## Development setup

```bash
git clone https://github.com/sanskarIN/unknown-mystery-ai.git
cd unknown-mystery-ai
python -m venv .venv
pip install -e .
python -m unittest discover -s tests -v
```

## Commit identity for local Git

The project maintainer uses:

```bash
git config user.name "Sanskar"
git config user.email "sanskarin@outlook.in"
```

Contributors should use their own valid Git identity unless they are the maintainer.

## Commit style

Prefer small, focused commits such as:

- `feat: add evaluation helper`
- `test: cover retrieval ranking`
- `docs: explain release manifests`
- `fix: reject duplicate document ids`
- `chore: update CI matrix`

## Pull requests

A pull request should explain:

1. what changed,
2. why it changed,
3. how it was tested,
4. any limitations or follow-up work.

## Licensing

Source-code contributions are expected to be compatible with the repository's Apache License 2.0. See `NOTICE` and `docs/LICENSE_SCOPE.md`.

## Book and official releases

### https://ramsandesh.gumroad.com
