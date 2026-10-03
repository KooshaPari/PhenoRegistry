# Pass 27 — CI mounted-surface correction

Date 2026-09-30. Exactly Dino + Civis.

## Dino PR491

Run36714888435 failed before assertions with CS0234: DINOForge.Runtime.Generation absent. Root cause is not missing source: GenerationStore.cs exists on the experiment branch. Runtime csproj sets GameInstalled=false in CI, removes **all** Runtime .cs files, then re-includes a pure-C# allowlist. GenerationStore was not in that allowlist, so the built Runtime DLL could not expose the namespace.

Classification: CI mounted-surface/build-graph failure, zero semantic credit.

Experiment branch now includes Generation/GenerationStore.cs in the CI-safe Runtime allowlist (8b3df5642f380447777dc60009d4fb8e0fadb8de). The direct actual-consumer test was removed from the CI pure-core project because PackUnitSpawner/WaveInjector themselves are game/runtime consumers excluded from GameInstalled=false; their adapters remain source integration candidates requiring game-installed or separately extracted pure adapter seams. Pure GenerationStore candidate tests remain.

This is an important distinction: source exists != mounted in a candidate build.

## Civis PR1569

Semantic adapter candidate is queued in run36714954137. It now tests compatibility-first ordering before CivSaveBundle integration. No result inferred while queued.

No third product.
