# External-effect recovery finding — pass 1

Date: 2026-09-30. Applies to both primary products without merging them.

Targeted source searches for explicit idempotency/effect receipts/uncertain-effect/deduplication terminology did not surface a first-class product abstraction in either frozen primary source. Search absence is not proof of behavioral absence; it establishes that the mature-contract requirement is not yet traceable by obvious named implementation.

## Required semantic states
For a side effect outside the runtime's own transactional store, record at minimum:
- effect_id and owning durable effort/attempt;
- operation/target and authorization basis;
- INTENT_RECORDED before dispatch;
- DISPATCHED with provider/tool request identity where available;
- CONFIRMED_SUCCESS with provider receipt or observed postcondition;
- CONFIRMED_FAILURE;
- UNCERTAIN when crash/timeout/disconnect leaves outcome unknowable;
- RECONCILED before any retry of an uncertain effect.

Do not promise exactly-once external effects unless the downstream system supplies the necessary idempotency/transaction semantics. The safe product obligation is no blind retry of UNCERTAIN effects and explicit reconciliation.

## First vertical-slice experiment
Use a deterministic local side-effect fixture with an idempotency key and durable receipt log. Kill attempt A at three boundaries: before dispatch, after downstream effect before local acknowledgement, and after acknowledgement before terminal product state. Start attempt B under the same DurableEffortRef. Expected outcomes: retry known-not-dispatched; reconcile uncertain post-dispatch state before retry; never duplicate a confirmed effect; preserve attempt lineage and exact evidence.

Repeat with a downstream fixture that does **not** support idempotency. The product must expose UNCERTAIN/manual-or-policy reconciliation rather than manufacturing a green.

## Architecture consequence
This durable effect ledger belongs with durable development effort/orchestration, not solely in a disposable worker session. HeliosLite/KCode need adapters/hooks sufficient to emit and consume effect identities, but should not each grow a separate canonical effort engine unless a thin adapter is experimentally inadequate.

Current state: DESIGN_REQUIRED / IMPLEMENTATION_MAPPING_OPEN / NATIVE_EXPERIMENT_NOT_RUN.