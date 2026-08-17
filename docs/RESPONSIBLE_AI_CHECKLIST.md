# Responsible AI Review Checklist

> 🛒 **Official Gumroad store:** **https://ramsandesh.gumroad.com**

Use this checklist before treating an AI demo as a production-ready system.

## Purpose and impact

- [ ] The intended task and users are documented.
- [ ] Unsupported or inappropriate uses are documented.
- [ ] Human oversight is defined where the system can materially affect people.

## Data

- [ ] Data sources and authorization are documented.
- [ ] Sensitive data is minimized.
- [ ] Leakage and contamination checks are recorded.
- [ ] Important slices or subgroups are evaluated when relevant.

## Evaluation

- [ ] Metrics match the real task.
- [ ] A baseline or comparison is included.
- [ ] Failure cases are reviewed, not only aggregate scores.
- [ ] Release criteria are defined before deployment.

## Privacy and security

- [ ] Secrets and credentials are kept out of logs and repositories.
- [ ] Input and output trust boundaries are documented.
- [ ] Least-privilege access is used.
- [ ] Data retention and deletion behavior are understood.

## Reliability

- [ ] Timeouts, fallbacks, and rollback paths are defined.
- [ ] Resource limits are set where needed.
- [ ] Monitoring includes release identity.
- [ ] Incident ownership is clear.

## Transparency

- [ ] Limitations are communicated.
- [ ] Model/data/release versions are traceable.
- [ ] Generated output is not presented as guaranteed truth.
- [ ] Changes that may alter behavior trigger re-evaluation.

## Complete responsible-AI coverage

### https://ramsandesh.gumroad.com
