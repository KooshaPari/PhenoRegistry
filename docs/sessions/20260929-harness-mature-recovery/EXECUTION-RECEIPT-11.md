# Execution receipt 11 — product-integrated effect hooks implemented as separate candidates

Date: 2026-09-30. Program remains OPEN.

## Separate implementation candidates
HeliosLite draft #333, head `d18b37b45e06919baaf97b2de3e978588d578e01`, branches from the previously oracle-qualified candidate. ToolExecutor now has an optional EffectRecoveryAdapter; only Write is protected in the first experiment. A common execute_effect wrapper records intent, dispatch, success confirmation and UNCERTAIN on post-effect confirmation failure. Focused tests prove ordering and prove the side effect can be committed while durable confirmation fails. Targeted CI is queued.

KCode draft #20, current head `0f1a2f5a7d80328661ff4438549d55cd60bfc488`, branches from the daemon-identity-qualified candidate. Registry owns an optional EffectRecoveryAdapter; only resolved `write` is protected initially. Real WriteTool tests use isolated filesystem state and prove normal transition ordering plus committed-file/failed-confirmation -> UNCERTAIN. Adapter context is now preserved through Registry clones and WeakRegistry upgrade so nested/batch registry use cannot silently drop the safety boundary. Targeted CI is queued.

## Scope control
Neither candidate implements replacement-worker reconciliation yet. Neither changes ordinary sessions when no adapter is supplied. Neither claims exactly-once. Neither expands protection beyond Write until tool classes/reconcilers are explicitly designed and tested.

## Contract diagnostics
Standalone External Effect Recovery Contract jobs on both spec PRs remain runner-queued. Those jobs validate the state-machine contract with subprocess death/fsync'd files; #333/#20 validate the product execution seams. Neither substitutes for the later full attempt-A/attempt-B restart fixture.

## Existence pressure
KCode's ForgeCode provider remains adapter-shaped and current upstream supports external-provider composition, strengthening CONTRIBUTE UPSTREAM / EXTERNAL RUNTIME ADAPTER as its default disposition pending golden semantic fidelity tests.

No merge or completion gate is awarded.