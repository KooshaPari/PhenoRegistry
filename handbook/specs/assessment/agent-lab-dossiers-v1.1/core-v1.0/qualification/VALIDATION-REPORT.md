# Release validation — v1.0

**Status:** PASS for the checks listed below. This is a local qualification report, not a product/portfolio certification or an independent attestation.

**Recorded at:** 2026-09-11T07:20:26.393200+00:00. Execution timestamps are UTC; the handoff's prepared date uses America/Los_Angeles. The actual tested environment is preserved in [validation.json](validation.json).

| Check | Observed result |
|---|---|
| Reference-kernel unit tests | **68 passed**, process exit 0. |
| JSON Schemas | **25** documents accepted by the installed Draft 2020-12 validator. |
| Record cross-check | **1166** schema-conformant records/criterion entries, including both custom-kernel and separate jsonschema validation. |
| Candidate catalog structure | **18 domains / 108 pillars / 1,080 entries**, zero exact duplicate predicates; semantic overlap remains for adjudication. |
| Work dependencies | **36 proposed tasks**; references resolved and graph acyclic. |
| Source references | Every candidate related-reading ID resolves in the source register. |
| Python source | Parsed successfully without executing untrusted product code. |
| Internal Markdown targets | 95 targets resolved during the content check; final release checked again after report creation. |
| Synthetic before/after | Actual no-op restoration was rejected; corrected restoration and corruption detection passed the qualified toy checks. |

The unit tests cover digest tampering, wrong subject/epoch/catalog/assignment, stale and future evidence, missing or failed qualification, zero assertions, conflicting result leaves, supersession/cycles, duplicate/invalid weights, critical gates, unresolved applicability, missing versus hidden records, error/failure separation, unsafe paths, symlinks, invalid JSON, schema vocabulary, placeholders, no-overwrite initialization, bounded inspection and delivery-state consistency. See [unit-tests.log](unit-tests.log) for named outcomes.

## Reproduce the core checks

From a clean extraction:

```sh
python tools/pep.py check-package
python tools/pep.py self-test
python tools/pep.py summarize examples/executed-toy-loop/before
python tools/pep.py summarize examples/executed-toy-loop/after
python tools/demo_loop.py --out .local-runs/fresh-toy
```

The `jsonschema` package was used only for an additional release-time cross-check; it is not a runtime dependency. Its observed installed version is in validation.json. The runtime validator intentionally implements only the bundled schema subset.

## Meaning and limits

These checks establish observed behavior of this small reference kernel and trusted synthetic fixture in the recorded Linux/Python environment. They do not establish correctness of all catalog predicates, agent-generated product behavior, authenticated identity, actual permission enforcement, adversarial isolation, live registry delivery, cross-platform support, regulatory compliance or economic convergence.

The evidence path can be forged by an actor who controls every record and verifier. Passing structural validation is not authentication or product acceptance. Other operating systems/interpreter versions were not executed here. No user's repository or device was changed or graded in this release qualification.

Archive CRC, exact extraction, clean-extraction self-test and integrity negative-control results are recorded in [archive-verification.json](archive-verification.json). The final archive is verified after these receipts are included; the ZIP hash is distributed separately to avoid self-referential hashing.
