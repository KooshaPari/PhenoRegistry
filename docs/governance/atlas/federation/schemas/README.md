# Illustrative federation profiles

These additive schemas demonstrate a stricter structure than v1.2's free-text federation policy. They intentionally require synthetic examples and null runtime/authorization results. They are not production identity/permission schemas and cannot authorize activation. The legacy applet schema remains unchanged for old records.

`manifest.schema.json` describes explicit capability offers, semantic-contract references, base/optional requirements, host slots and state ownership. `composition-plan.schema.json` binds a scoped perspective to locked artifacts, providers and mounts. The two examples reverse host perspective without changing the data owner for either capability.

`check_plans.py` checks only selected schema and referential constraints: duplicate IDs, lock consistency, typed offer references, same-scope bindings, authority references, host-slot support and acyclic initial startup/mount graphs. It does not parse upstream semantic-version ranges, verify signatures, issue/revoke grants, check actual OS identities, execute programs, measure performance, prove native UI quality or enforce runtime access. Grant IDs are unresolved illustrative references, not evidence of consent. A forged but structurally consistent example can pass.

Real runtimes need authenticated platform-specific artifacts, conformance proofs and provider-side enforcement. Adopt existing suitable IDL/resolver/extension facilities before promoting or expanding these illustrative profiles into production code.

From `docs/`, run `python federation/check_plans.py` for the examples and `python -m unittest discover -s tests -p 'test_federation_contract.py' -v` for reference checks. Product acceptance is in `federation/ACCEPTANCE.md` and is unexecuted.
