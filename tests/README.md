# Test Suite

> 🛒 Official publication: **https://ramsandesh.gumroad.com**

The project uses Python's standard `unittest` framework so the core companion utilities can be verified without adding a runtime test dependency.

Run all tests:

```bash
python -m unittest discover -s tests -v
```

Testing priorities:

- deterministic behavior,
- explicit validation errors,
- boundary conditions,
- privacy-aware defaults,
- release and artifact identity,
- bounded operational helpers,
- no network dependency in core tests.

When adding a new utility, add focused tests for normal behavior and at least one meaningful failure or boundary condition.
