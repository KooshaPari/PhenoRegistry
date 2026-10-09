# Pass 29 — relation audit, v2 machine traces, VS-02 fixtures

Date 2026-09-30.

## Retroactive cross-repo relation audit

The new authority rule was applied beyond the PhenoLab correction.

### Portage ↔ Harbor
Receipt `9a3d47c1344eba56aa02d4444872d087544fec14`.

Typed as historical fork/upstream lineage + implementation reuse/dependency + interoperability/extension candidate. “Delegate to Harbor” means reuse existing implementation where it satisfies Portage semantics; it is not product-governance subordination. Portage may still become plugin/library/gateway/minimal fork or disappear.

### PhenoMLX ↔ hwLedger / OmniRoute
Receipt `9667529805f9fcc31e07a9ecb093da0c3ba35ea0`.

Current registry evidence **does** explicitly make hwLedger canonical home for hardware/fleet ledger/capacity-planner UX and explicitly excludes LLM route/proxy plane. Therefore hwLedger may provide hardware observations without owning PhenoMLX profile qualification.

OmniRoute is different: its current boundary file is scaffold/unknown, while the detailed router/data-plane split is only a PROPOSED ADR awaiting sponsor. Prior wording that OmniRoute definitely consumes PhenoMLX qualification truth was too strong. Relation is downgraded to optional/unresolved integration until direct/accepted evidence exists.

This is exactly the kind of overreach the relation-authority rule is intended to prevent.

## V2 machine traces

Portage `8ccae60bb1fc1b4aa901ca651effa8cdb120878e`.
PhenoMLX `8711efad9c050839abcd02904596bb8ec869b468`.
PhenoLab `e1cfd84214612628af2b7eb57ed8f9929c5ebcd3`.

All v2 obligations now map to slice, blocking status, oracle and acceptable evidence class. PhenoLab trace uses corrected standalone R&D semantics.

## VS-02 schema fixtures

Portage `40932f1e3b05074fd1becb1dcd684f6bf4888a25`.
PhenoMLX `ad9d532412a33c3cd4d4638485b5f29f4786d2ae`.
PhenoLab `863dc6a13ebd4c1406fd4831997009985b99ec52`.

These are permitted schema/read-only fixtures and cannot be used to claim native VS-02 completion.

## Next

Highest-value remaining spec work:
1. direct current cross-repo API/schema inspection where actual repos are available, without inferring ownership;
2. statistical/causal methodology pass for PhenoLab;
3. engine version/license/project-health matrix for PhenoMLX;
4. Portage package/install + semantic fork-delta closure;
5. build source-ledger resolved-row metrics (coverage only, not product completion);
6. await VS-01 native evidence.
