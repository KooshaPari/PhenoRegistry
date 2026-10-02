# Execution receipt 13 — contract diagnostics qualified; macOS policy primitive qualified

Date: 2026-09-30. Program remains OPEN.

## External-effect contract
Both spec PRs now have successful External Effect Recovery Contract workflows: HeliosLite run 36706606329 and KCode run 36706612269. This qualifies the standalone state-machine diagnostic with real subprocess death, fsync'd receipts/effect log, idempotent/queryable recovery and non-queryable UNCERTAIN behavior. It does **not** close H-F008/K-F008 because product-integrated attempt-A/attempt-B reconciliation is still absent.

Registry trace rows were promoted from CONTRACT_DIAGNOSTIC_QUEUED to CONTRACT_DIAGNOSTIC_QUALIFIED.

## HeliosLite #333
Platform Tests failed on macOS and Windows because `with_effect_recovery` was dead code under the repository's deny-warnings policy. This is not dismissed as unrelated: it proves the hook was not mounted by production code. The builder is now test-only in commit `249d4788374ad845e52833031daa7651a862db4c`, preserving the primitive experiment without falsely claiming reachability. Focused Effect Recovery Hook CI remains to qualify.

## KCode macOS trust policy
Candidate #22 `a9daae12bb102047b3bbb708e516a841af686036` passed macOS Trust Policy run 36712215260. Frozen startup-time xattr stripping/ad-hoc re-signing is fork-specific; current upstream handles quarantine in installation and lacks the inspected startup mutation routine. Candidate #22 makes repair explicit opt-in and normal startup non-mutating.

This qualifies compile/policy behavior only. Signed-release/local-build before/after digest, codesign identity/designated requirement, xattrs, read-only executable, missing tooling and repeated-launch experiments remain open. K-F009 records the provenance conflict and CURRENT-STATE binds the exact candidate/run.

## Other queues
KCode #20 product effect hook remains queued. KCode #22 daemon-identity regression and governance checks remain queued. Queued is not green.

No architecture freeze, merge or completion verdict follows.