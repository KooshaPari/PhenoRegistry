# Execution receipt 14 — contract green, product-hook reachability and attempt-B API

Date: 2026-09-30. Program remains OPEN.

## Qualified contract layer
External Effect Recovery Contract is green on both spec branches. This qualifies the standalone crash-state machine, not product integration.

## HeliosLite #333
Initial Platform Tests failure was caused by repository deny-dead-code policy: the production builder `with_effect_recovery` was unmounted. This is meaningful reachability evidence, not an unrelated CI nuisance. Commit `249d4788...` makes the builder test-only so the primitive can be tested without claiming a mounted product path. New Platform Tests are in progress; focused hook CI remains queued.

Design review found another blocker before reachability: candidate effect identity used durable effort + conversation + file path. Repeated legitimate writes to the same path could alias. The mature contract now requires a runtime-generated call/effect identity in ToolCallContext; path-only identity is explicitly test scaffolding.

## KCode #20
Effect hook CI remains queued. Attempt-B contract is now pinned: replacement loads the durable effect record and reconciles before any fresh dispatch. Write reconciliation compares the persisted expected postcondition/content hash to the actual file. Match => RECONCILED_SUCCESS/no write; provable absence => RETRY_ALLOWED; conflicting/unknowable => STILL_UNCERTAIN. Missing transcript ToolResult is never retry authorization.

## KCode #22
macOS policy primitive remains native-green. K-F009 and CURRENT-STATE bind the exact candidate/run while signed-release provenance experiments remain open.

## Next implementation threshold
Do not mount Helios effect recovery until stable per-call identity is propagated. Do not claim either H-F008/K-F008 closed until a product-integrated attempt-A/attempt-B fixture proves no duplicate effect and fail-closed uncertainty.

No merge or completion verdict.