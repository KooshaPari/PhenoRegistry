# Verification matrix template

| ID | Repository/layer | Claim or requirement | Evidence source | Test/build command | Expected observable | Current result | Confidence | Blocking contradiction |
|---|---|---|---|---|---|---|---|---|
| V-000 | ecosystem | All scoped repositories acquired with all advertised refs | acquisition logs + refs | `git fsck --full` per mirror | no missing reachable objects | pending semantic review | low | authenticated/private refs may be absent |

## Required matrix dimensions

- supported OS and architecture;
- language/runtime/toolchain versions;
- clean checkout versus incremental build;
- unit, integration, end-to-end, compatibility, migration, rollback, security, and performance tests;
- online/offline and degraded dependency behavior;
- CLI/API/schema compatibility across repository version combinations;
- generated-file reproducibility;
- package/release artifact equivalence to source.

A green command is not proof of requirement satisfaction unless the expected observable is explicit and the test fails when the behavior is broken.
