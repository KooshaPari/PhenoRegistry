# Pass 3 — effective generation and authoritative state

Date 2026-09-29. Program remains exactly Dino + Civis.

## Dino

Product pass3 commit: `fd07ea26ecfb1f520415333164f690939cf3a527`.

The raw Registry is intentionally multi-source: each ID owns a priority-sorted list and All/Get project the top entry. Therefore the transaction boundary should be the **effective generation**, not "only one registration may exist."

New source risks:
- reload reuses the same RegistryManager; Registry<T> exposes no inspected remove-by-pack/generation primitive;
- IPackReloadService.ReloadPack calls LoadPack against that state;
- removed IDs from a newer pack generation can therefore remain candidates unless cleanup exists elsewhere;
- RegistryImportService's patched-YAML cache has SetPatchedYaml but source search found no clear/reset API; when a later load has no patches, ApplyPatchPhase returns without rebuilding the cache, creating a concrete stale-patch hypothesis.

The next native fixture is versioned pack replacement: v1 IDs x,y + patch; v2 changes x/removes y/removes patch. Repeated reload must converge rather than accumulate.

## Civis

Product pass3 commit: `c600ef2f9373438f8bef056a138ee0198e02175a`.

The state denominator is now demonstrably broader than WorldState. Simulation owns ECS, RNG, economy/market, policy, voxel, mod host, queues and extensive social/runtime state. WorldState itself contains six serde-skipped subsystem fields.

Critical oracle defect: WorldState PartialEq compares only tick, population, energy budget, rng seed and aggregate resources. A whole-state equality assertion is therefore not an exhaustive persistence oracle. Selected-field tests may still be valid for their named subjects.

Another apparent defect was falsified: `crates/engine/src/save.rs` looks internally inconsistent, but lib.rs does not mount/export that module. It is orphan/dead source under the inspected active crate graph. Its tests/capabilities must not qualify CivSaveBundle.

The v5 integrity manifest is valuable byte-integrity evidence for files that exist, but cannot prove that every authoritative live field was serialized. State completeness must be established before artifact integrity can close persistence.

## Next control-loop step

Generate semantic state inventories from actual fields/mutation sites, map to active persistence/restore symbols, then create omission/stale-generation fixtures. No count target and no product-completion credit from this pass.
