# Pass 8 — candidate-bound recovery runners

Date 2026-09-29. Exactly Dino + Civis.

## Dino

- recovery oracle head: `6f494343934bb37d8ff9211ab2792cac9624210e`
- workflow: `.github/workflows/recovery-oracles.yml`
- workflow run: `36622441461`
- job: `recovery-generation-oracles`
- runner: `windows-latest`
- targeted tests: `FullyQualifiedName~RecoveryGenerationOracleTests`
- raw artifact contract: candidate receipt + TRX under `recovery-artifacts`
- fail-closed: yes; the earlier temporary `continue-on-error` design was removed before this run.
- real-game workflow on the same candidate: skipped; contributes zero runtime qualification.

The test set now includes same-pack replacement/removal convergence, repeated identical reload convergence, and stale patched-YAML invalidation using the repository's existing PatchSet syntax.

## Civis

- recovery oracle head: `432aa1059672c0caf4d0d3a9cfec1f5efddadb78`
- workflow: `.github/workflows/recovery-oracles.yml`
- workflow run: `36622448639`
- job: `semantic-persistence-oracles`
- runner: `ubuntu-24.04`
- targeted tests: `cargo test -p civ-engine recovery_oracle_`
- raw artifact contract: candidate receipt + captured cargo log
- fail-closed: yes.
- fixture corrections were made before this run: ResearchCache.queued uses VecDeque push_back and LoadedMod identity is manifest.meta.id.

Targeted semantics: economy policy continuity; research-cache continuity; orphan guest-memory versus active loaded-mod identity.

## Evidence policy

Workflow existence is not a pass. Queued/in-progress is UNKNOWN. A compile failure is evidence about the oracle patch/candidate, not automatically evidence that the product behavior fails. A test assertion failure after successful compilation is stronger behavioral evidence but remains bound to the exact synthetic fixture/entry path. No result from these jobs qualifies the licensed Dino host or Civis user journey beyond the exercised subject.
