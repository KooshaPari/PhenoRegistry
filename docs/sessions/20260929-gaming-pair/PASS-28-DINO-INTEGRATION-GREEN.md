# Pass 28 — Dino integration core green; materialized consumers fail closed

Date 2026-09-30. Exactly Dino + Civis.

## Dino PR491

GenerationStore implementation candidate is now candidate-bound green:
- candidate e267db309f4ca0cbc3bdef41d93741afa60a48d9
- run36715187076
-4/4 integration-candidate tests passed
- artifact11096300343
- sha256 b43844c7314a57c7bb76b9ec99c047450b0ad6f63d93c4bf50b4be7c38ff2c6f
- raw TRX + receipt present.

Warnings DF0099 remain in GenerationStore dictionary construction and are quality debt, not test failure.

Materialized real consumers are now explicitly fail-closed on the experiment branch:
- BuildMenuInjector.AssessGeneration -> RESTART_REQUIRED because live menu state is cached/materialized and no reversible delta is proven.
- AerialSpawnSystem.AssessBuildingGeneration -> RESTART_REQUIRED because existing system instances have a one-shot building sweep.

This is intentionally conservative: observing desired G2 cannot manufacture a live-materialization green.

## Civis PR1569

Semantic Save Manifest Experiment run36714954137 remains queued. Candidate includes compatibility-first SemanticSaveAdapter; CivSaveBundle default path remains untouched. No execution credit yet.

No third product, no merge authorization.
