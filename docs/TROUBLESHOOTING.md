# Troubleshooting

> 🛒 Official publication: **https://ramsandesh.gumroad.com**

## `ModuleNotFoundError: umai`

Install the project from the repository root:

```bash
python -m pip install -e .
```

## Tests cannot discover modules

Confirm the editable install completed and run:

```bash
python -m unittest discover -s tests -v
```

## Different results between runs

Use the reproducibility helpers and record the seed, inputs, configuration, Python version, and release identity. Some external numerical libraries and hardware can still introduce variation; document it rather than hiding it.

## RAG demo returns weak matches

The included retriever is intentionally simple and lexical. It is a teaching baseline, not a semantic embedding system. Add clearer document text or compare it with a properly evaluated semantic retriever in your own authorized project.

## CI passes locally but fails on GitHub

Check the supported Python matrix, path assumptions, case-sensitive filenames, and whether an untracked local file is being relied upon.

## Never commit secrets

If a credential is accidentally committed, revoke/rotate it immediately and follow the repository security policy. Removing it from a later commit alone does not invalidate an exposed credential.
