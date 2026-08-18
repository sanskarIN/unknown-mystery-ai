## Summary

<!-- What changed, why is it needed, and which compatibility or project contract does it affect? -->

## Validation

- [ ] `python scripts/check_repository_completeness.py` passes locally
- [ ] `python scripts/check_public_api.py --require-version-match` passes when package/API files changed
- [ ] `python scripts/check_project_catalog.py` passes when project/catalog files changed
- [ ] `python scripts/check_projects.py` passes when project/package behavior changed
- [ ] `python scripts/check_project_snapshots.py` passes for capstone/output-contract changes
- [ ] `python -m unittest discover -s tests -v` passes locally
- [ ] New or fixed behavior has regression tests where practical
- [ ] Documentation was updated for user-visible behavior or contracts
- [ ] No secrets, credentials, private data, or confidential logs are included
- [ ] No paid book manuscript content or commercial publication assets are included
- [ ] Long-lived files do not add change-prone X/Twitter profile URLs outside the documented policy

## Compatibility

- [ ] Stable 1.x public APIs remain backward-compatible, or the compatibility impact is explicitly documented
- [ ] No mandatory runtime dependency was added without a documented reason and review
- [ ] Cross-platform behavior was considered for paths, commands, and output

## Limitations / follow-up

<!-- What remains uncertain, needs production-specific review, or is intentionally out of scope? -->

---

🛒 **Official book store:** https://ramsandesh.gumroad.com
