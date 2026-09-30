# Execution receipt 22 — Helios primitive API surface reduced after repeated reachability failures

Date: 2026-09-30. Program remains OPEN.

## HeliosLite #333
Focused Effect Recovery Hook remains green on prior exact heads, but branch-wide Platform Tests repeatedly reject unmounted helper/API surface under `-D dead-code`. At `b6880fbc...`, the remaining failure was `with_effect_recovery` itself: it was test-only but unused even by tests.

Candidate `c167f38b7125c4659af513b07ea57ac6affa21a6` removes that builder entirely. Tests exercise the private effect wrapper/state directly. This is intentionally a **smaller** candidate: stable ToolCallId plumbing and effect/reconciliation primitives can be qualified without pretending a production adapter injection API exists.

Consequently H-F008 remains blocking/reachability-open even if the next branch-wide CI passes. A future production adapter API should be introduced only together with a real durable-workflow consumer, so dead-code policy itself becomes a reachability guard.

## KCode
KCode #20 remains exact-head green as QUALIFIED_CANDIDATE_PRIMITIVE / REACHABILITY_OPEN. Retained-patch ledger now excludes zero-line skeleton crates from behavioral differentiation.

No merge or completion verdict.