# Execution receipt 20 — KCode effect primitive qualified; Helios helper reachability kept honest

Date: 2026-09-30. Program remains OPEN.

## KCode #20
Exact candidate `bac23f8885bb4a5f17bad926ca1451581b1a8b51` is green on Effect Recovery Hook run 36738409142, daemon-identity regression 36738409456 and linked-issue governance 36738409163. This qualifies the optional Write effect hook, committed-effect/failed-confirmation -> UNCERTAIN behavior and pure Write attempt-B reconciliation primitive.

K-F008 is **not closed**: no intended production durable-effort adapter currently loads an uncertain receipt and invokes the reconciler before redispatch. Registry trace is therefore QUALIFIED_CANDIDATE_PRIMITIVE / REACHABILITY_OPEN. CURRENT-STATE binds the exact evidence.

## HeliosLite #333
Previous exact head `b455e1fc...` had a green focused Effect Recovery Hook but branch-wide platform failures because the new ReconcileDecision/reconcile_write_postcondition helper was unmounted and dead-code is denied. This is treated as reachability evidence. Commit `b6880fbc95089c1f2476d3372e6fb52cd602b786` makes the reconciliation helper test-only; all fresh checks are queued.

Stable ToolCallId propagation remains in #333. Adapter injection/reconciliation remain intentionally unmounted, so H-F008 stays blocking regardless of focused unit success.

## Shared recovery model
Separate-process replacement oracle remains green on both spec branches. The model is qualified; actual durable-workflow reachability is the remaining closure boundary.

No merge or completion verdict.