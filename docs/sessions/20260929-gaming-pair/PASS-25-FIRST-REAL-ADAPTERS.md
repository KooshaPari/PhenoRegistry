# Pass 25 — first real integration adapters

Date 2026-09-30. Exactly Dino + Civis.

## Dino

Implementation candidate PR491 advanced from abstract GenerationStore into two actual runtime adapters:
- PackUnitSpawner.ApplyLookupGeneration
- WaveInjector.ApplyLookupGeneration

Both return structured GenerationConsumerResult and explicitly scope ACK to future lookup behavior. PackUnitSpawner excludes existing spawned entities; WaveInjector excludes already-active waves whose definitions are materialized. This prevents a pointer rebind from overclaiming live-world reconciliation.

Experiment head99cd591e6f0c90ea61786de637f2ef82603faa1b includes a direct test invoking both actual adapters. Dedicated workflow is forced to rerun; no result admitted yet.

BuildMenuInjector/AerialSpawnSystem remain intentionally unwired because their one-shot/materialized semantics require reconcile/restart policy.

## Civis

Expanded spec candidate d990d704e4850ef2760fcf3faa12af512586944a is now exactly qualified by run36711269740:11 prototype/guard greens vs9 unchanged production reds, artifact11094234183 sha256 bba6a17e1f4c41774d79d93ffde1fc6d914a578c81686f7a2f1dd2bbcc2e3426.

Implementation candidate PR1569 promotes the qualified semantic manifest into production-shaped semantic_state_manifest.rs with isolated tests, but does not wire CivSaveBundle. Dedicated experiment run36712033274 remains queued; no integration-candidate green yet.

No third product.
