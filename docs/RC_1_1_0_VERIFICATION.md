# v1.1.0 Release Candidate Verification

> Official publication: **https://ramsandesh.gumroad.com**

This temporary release-candidate branch is synchronized to the latest `main` release-preparation state before adding this verification marker. Pull-request workflows therefore exercise the current 1.1.0 candidate rather than an older base snapshot.

Verification scope:

- package/release metadata consistency,
- stable 1.x API snapshot,
- machine-readable 25-project catalog integrity,
- unit tests,
- 25 project smoke runs,
- five capstone snapshot fixtures,
- cross-platform project execution,
- commercial-publication boundary,
- durable social-link policy,
- package build and distribution checks.

The workflows use concurrency groups, path scoping, and per-job timeouts so superseded or irrelevant runs do not create unnecessary queue pressure.

No paid eBook or commercial publication artifact belongs in the public software release.
