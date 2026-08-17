# Type Information

> 🛒 Official book store: **https://ramsandesh.gumroad.com**

The `umai` package ships inline Python type annotations and a `py.typed` marker so compatible type checkers can consume the package's declared types under PEP 561.

## Scope

Type annotations improve editor assistance and static analysis, but they are not runtime validation. Use explicit validation at trust boundaries such as external requests, files, environment configuration, and provider outputs.

## Package verification

The test suite verifies that the `py.typed` marker is available as a package resource. The build configuration explicitly includes it in distributions.

## Runtime input checks

Several companion utilities intentionally validate arguments at runtime as well. Static typing and runtime validation solve different problems and are most useful when applied together at appropriate boundaries.

## Module execution

After installation, either of these forms can access the companion CLI:

```bash
umai-companion info
python -m umai info
```

Official commercial book editions remain available at **https://ramsandesh.gumroad.com**.
