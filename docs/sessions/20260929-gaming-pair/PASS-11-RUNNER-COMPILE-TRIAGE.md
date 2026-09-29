# Pass 11 — recovery runner compile triage

Date 2026-09-29. Exactly Dino + Civis.

## Dino

Candidate `f174c2b254eb6ff3859cb81ee46eb25f3eb804c3`, Recovery Oracles run `36623835039`, failed before assertions.

The isolated SDK-only project successfully removed the earlier monolithic test-suite failures, but compilation then exposed a harness identity issue: `RecoveryGenerationOracleTests` uses internal `IPackReloadService`; SDK grants `InternalsVisibleTo("DINOForge.Tests")`, while the isolated project had a different default assembly name.

Classification: harness compile failure, zero behavioral credit.

Repair: isolated project now retains its own project path but sets `AssemblyName=DINOForge.Tests` and `RootNamespace=DINOForge.Tests`, preserving the existing SDK friend-assembly contract without changing production visibility.

## Civis

Candidate `7c359586b69ef23de507bd0168f64ff8256af2db`, Recovery Oracles run `36623832348`, failed in compile step before execution.

Exact blocker: final loaded-mod assertion still used `m.manifest.id`; current ModManifest identity is `m.manifest.meta.id`. Earlier correction had fixed the fixture precondition but missed the final assertion.

Classification: harness compile failure, zero behavioral credit.

Repair: both loaded-mod identity checks now use `manifest.meta.id`.

## Control-loop rule retained

Neither red is a product failure. Both are useful harness evidence because the jobs are candidate-bound and fail-closed, but no semantic assertion executed. The next run is the first one eligible to produce behavioral red/green for these oracles.
