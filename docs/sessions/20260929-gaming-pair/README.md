# Gaming pair — mature-first recovery, first execution cycle

Program ID: `gaming-pair-20260929`. Date: **2026-09-29**. Status: **INCOMPLETE / NOT ACCEPTED / NOT A PRODUCT QUALIFICATION**.

## Scope lock and ownership

Exactly two product programs: **KooshaPari/Dino (DINOForge)** and **KooshaPari/Civis**. Other gaming/graphics names are inventory and lineage leads only. This registry directory indexes evidence/research and does not start a third product. No absorption, archive, deletion, merge, stable release or dependency upgrade is authorized by these documents.

| Subject | Frozen source commit | Source tree | Specification/research branch |
|---|---|---|---|
| Dino | `17119051e782b32615413049c1c3cd207f0b540e` | `d158e1904a128f3e80f26606e639a8011cadf7a1` | `spec/mature-recovery-20260929` |
| Civis | `b3cd62a7394878cc64d024fbfcfd398b8bb88bf1` | `184f53f90e983ef5d9da5fc5f926bdd564ad0819` | `spec/mature-recovery-20260929` |
| PhenoRegistry | `85d7cd00cf59c379c05b740e8130a85b0d5bd31b` | `e1fdef39df291c5aab7532cda0e8ca43d50d7dbf` | `research/gaming-pair-20260929` |
| Civis dependency: vendor/phenodocs | `35e0e90a19dfd93ce4e1a81210ade92088b2bbbc` | Not inspected | Gitlink identity only, no product program |

GitHub repository IDs: Dino `1177712269`, Civis `1164684442`, PhenoRegistry `1201113097`. The phenodocs pin is the exact submodule object returned from Civis at its source snapshot; dependency contents were not reviewed. Dino's exact-path `.gitmodules` read returned 404, which does not prove absence of dependencies. Its native/vendor/package pins remain to be enumerated.

**Implementation candidates: none submitted by this program.** Specification branch changes are documents/experimental policy design, never silently substituted for an executed product candidate. Existing source and historical work are preserved.

## Index

- [Alias, lineage and authority map](ALIAS-LINEAGE.md)
- [Dino: internal archaeology and research pass 1](Dino/PASS-01-ARCHAEOLOGY-SOTA.md)
- [Civis: internal archaeology and research pass 1](Civis/PASS-01-ARCHAEOLOGY-SOTA.md)
- [MACE/autograder, evidence and lifetimes doctrine](MACE-AUTOGRADER-DOCTRINE.md)

Detailed canonical recovery drafts and source-family ledgers belong in each product at `docs/product-recovery/2026-09-29/`. Registry summaries do not override them. Follow draft PR references in the program receipt/PR descriptions. An AgilePlus registration was not created or verified; this durable program ID is not an invented AgilePlus issue ID.

## Current decisive findings

**Dino:** the runtime's ModPlatform constructs ContentLoader with `schemaValidator:null`. The loader documents that null skips schema validation. Compatibility and dependency checks still exist. A compiler/schema-test green cannot establish live runtime schema enforcement. Another ingress guard could change the end-to-end conclusion and remains to be checked.

**Civis:** the initial deterministic-replay hypothesis was falsified by the May 29 charter correction and Accepted May 30 ADR. Global bit-identical replay is not required; v1 is single-player and excludes multiplayer/co-op/spectator. Faithful actual-state restoration remains important. Save metadata absence selects legacy loading; current-format corruption vs legitimate legacy classification and atomic save replacement require experiments.

**Registry:** Civis's July archive/read-only boundary conflicts with live active GitHub state and its active project card. Preserve the old record as history, do not treat it as current retirement authority. Both intent files contain literal placeholders despite prompt-binding counts. One rendered Dino prompt link returned 404. Counts are not recovered intent.

## Progress accounting

No overall completion percentage is assigned. Source-family inventories exist, but file-level/history/conversation denominators remain OPEN. Native product tests/builds/renderer/game journeys were **NOT RUN**: this environment has neither cargo nor dotnet; attempted network clones failed DNS; licensed DINO host and Civis runtime sessions were not available. Authorized connector reads did work.

Keep independent coordinates: specification coverage; demonstrated implementation; current candidate-bound evidence; stage journey closure; quality qualifications; uncertainty; transition debt; external user validation. Do not average a critical failure away. Scope additions and engineering gains must be recorded as separate deltas.

The strict completion gates are unpassed. In particular, full source resolution, authority/supersession recovery, full SOTA coverage, accepted semantic obligations, architecture experiments, complete implementation mapping and an independent/fresh incompleteness attack are outstanding. Nothing here authorizes beginning repository #3.
