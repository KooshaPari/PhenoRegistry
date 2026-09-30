# Pass 26 — integration candidates advance one layer

Date 2026-09-30. Exactly Dino + Civis.

## Dino PR491

First candidate run36712259808 failed before assertions with NETSDK1022 because GenerationStoreIntegrationCandidateTests.cs was both implicitly included by SDK default compile items and explicitly included in the isolated csproj. Artifact11094861002 sha256929726748a53dcb70b98470b0d90eb319a2a368d09f4ada866d348d74420ac2b contained receipt only. Classification: harness compile failure, zero behavioral credit.

Redundant Compile item removed at5a212d91420aa8a8bcd91da580e35adeb3be8b4e. Fresh Generation Store Experiment run36714888435 is in progress.

Candidate also now contains actual PackUnitSpawner/WaveInjector generation adapters from prior head; their ACK scope remains future lookups only.

## Civis PR1569

Because current production load imports mod guest memory before any mod compatibility resolution, direct CivSaveBundle wiring would preserve the reproduced orphan-mod semantic failure. The candidate therefore advances through a staged `SemanticSaveAdapter` instead:
- write/read required semantic-state.json;
- fail closed on missing/unsupported semantic component;
- validate guest-memory IDs against an already-resolved active mod set;
- only then apply semantic state.

Files: semantic_save_adapter.rs + tests, mounted at head46e9df293ee05334305b122ec6fb245bfb999fef. Dedicated workflow expanded to run all semantic candidate/adapter tests. CivSaveBundle remains untouched until compatibility-first ordering qualifies.

No third product, no merge authorization.
