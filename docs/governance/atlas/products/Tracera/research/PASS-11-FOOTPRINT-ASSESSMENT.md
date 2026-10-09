# Pass 11 — Dependency Footprint + Real Assessment Correction

**Date:** 2026-09-30  
**Status:** partial; implementation changed, native Rust execution still unverified in current tool environment.

## EXP-11

Synthetic reference experiment executed locally:
- 6/6 semantic dependency-footprint checks passed;
- 4/4 omitted-dependency mutants exposed the broken "absence = independence" shortcut.

Promoted invariant:
**missing/inferred absence cannot prove independence.**

Inference may conservatively add dependencies/rechecks. Removing a dependency from a criterion footprint requires stronger deterministic/accepted irrelevance evidence or scoped compatibility proof.

## Current Rust source finding

Inspection of `product/assessment.rs` confirmed:
- `assess_product` filtered a capability map by product but then passed the entire observation slice into each capability assessment;
- product baseline and observation_count were derived from the entire input slice;
- product identity was being used as a capability grouping key despite `Observation.capability_id` existing;
- explicit fresh `Unknown` and `Stale` outcomes were not exhaustively handled before the final Satisfied fallthrough;
- freshness read `Utc::now()` internally;
- test helper `ts(_secs)` ignored its argument and returned `Utc::now()`, masking intended timestamp fixtures.

## Implementation ledger

Commit `751d4f1b5d6a76dbf0a4fb7396da90f5f4939cca`:
- added explicit-time capability assessment;
- prevented explicit Unknown/Stale from falling through to Satisfied;
- scoped product aggregation to requested product;
- grouped by explicit capability_id;
- scoped baseline/count to product observations.

Commit `19b774e68ded90e97eda4df764fb96137907ed43`:
- added adversarial controls for explicit Unknown/Stale;
- frozen evaluation time;
- two-product same-capability isolation;
- product-level evidence not being silently recast as capability evidence.

These commits are intentionally separate to preserve implementation vs oracle evolution in the Git ledger.

## Verification limitation

The current execution environment does not have Cargo installed and no checked-out Tracera source tree is mounted. Therefore the Rust tests are **not claimed passing** here.

The PR remains draft and mergeable from GitHub metadata. Native CI/local execution is still required before these commits become verified product evidence.

## AgilePlus parallel finding

Current `main` is `e367f89e37314529afd125ae369fc64692c6fdfd`; the mature-contract branch is `b1e1172938904bc962cb20929f537a6f1e299999`.

Current main contains substantial newer methodology/harmonization material (framework analysis, unified artifact/lifecycle/traceability/layer ADRs, worktree isolation, claim/lease implementations, agent-lab assignment/epoch/grader schemas) that is not safely assumed present on the stale spec branch.

Do not continue AgilePlus semantic closure from the stale branch until ancestry/integration is reconciled without destroying history.

## Next

Tracera:
1. native Rust execution of new adversarial controls;
2. suspect/invalidation propagation;
3. VS-01 repository/identity contract;
4. persistence parity.

AgilePlus:
1. branch ancestry/reconciliation decision preserving commits;
2. source-ledger refresh from current main;
3. reconcile existing harmonization/agent-lab systems with mature-first doctrine rather than re-inventing them.
