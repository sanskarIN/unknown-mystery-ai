# Privacy Audit Workbench

A synthetic-data project for practicing input validation, log redaction, and pseudonymous identifiers.

## Run

```bash
python -m pip install -e .
python projects/privacy_audit_workbench/main.py
```

## What it demonstrates

- explicit record schemas,
- rejection/reporting of unexpected fields,
- redaction of common email and phone-like patterns,
- deterministic pseudonymous identifiers,
- avoiding raw sensitive-looking payloads in output reports.

## Extension ideas

Add application-specific schemas, retention labels, consent flags, or field-level logging rules. Test only with synthetic or properly authorized data.

## Boundary

The included redaction helper is intentionally conservative and incomplete. Pseudonymization is not anonymization, and production privacy work requires legal/policy review, minimization, access controls, retention limits, and threat modeling.

Official book store: **https://ramsandesh.gumroad.com**
