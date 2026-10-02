# Pass 3 — lineage closure receipts

Date 2026-09-29. Product source snapshots remain unchanged.

## Portage / Helios

Portage has **two non-equivalent HeliosBench lineages** that must not be conflated.

1. Historical `heliosBench` repository: Registry's 2026-09-01 audit classifies it as a Python measurement runtime, absorbed history-preservingly into `phenotype-tooling/crates/heliosbench/` via source split `5f85de67` and target commit `172ab8fd`. That audit explicitly rejects Portage as its canonical target because Portage is the Harbor environment substrate.
2. Current Portage `helios_bench`: `TASK_helios_stage1.md` defines an 8-task Python code-generation dataset/promotion target intended to run through Harbor, result JSON, Langfuse and bun-viewer.
3. Frozen Portage tree separately contains a dangling gitlink `benchmarks/heliosbench` → commit `c758019115876ed0d99019060adfd08b17a912c5`, with no current `.gitmodules` URL. Its repository identity is still unresolved.

Alias collision is now resolved enough to prevent importing the old measurement-runtime product contract into Portage. Gitlink provenance and the historical Stage-1 runtime result remain open.

Portage spec receipt: `6d1e348982e187206931e7fbbe974f55ab6be1b6`.

## PhenoMLX temp lineage

Accessible archived `KooshaPari/PhenoMLX-temp` (ID 1372886076) main head is `70529a879715a8078e26eb564f8fc312e1923f57`. That exact commit/tree/parent exists in current `KooshaPari/PhenoMLX`; its handoff patch says the temp remote was used after the original was accidentally deleted pending restore.

Current PhenoMLX compares **89 commits ahead, 0 behind** from that exact base, with merge-base equal to the temp head. Thus accessible temp **main** contains no post-head commit missing from current main history.

Do not overclaim all-ref completeness: preservation records separately mention older zz-archive tmp/temp supersets with non-main refs and a missing-ref/all-ref comparison gate.

Formal-looking temp/current `PRD.md` and `FUNCTIONAL_REQUIREMENTS.md` are exact blobs describing phenotype-shared infrastructure, not PhenoMLX. They are explicit contamination evidence and are not accepted PhenoMLX obligations.

PhenoMLX spec receipt: `da35b7e6489a0d83eebe45049359391cfb85170e`.

## PhenoLab / PhenoLM source chain

Direct original user-intent evidence is now recovered from Registry's exported 2026-05-24 ChatGPT RLVR-AF conversation. The user explicitly targets optimization of the **owned harness-model combination**, including prompts, tools, skills, guardrails/hooks, harness code and optional LoRA/model-level changes, and later generalizes to multi-model role/organization optimization. This replaces reliance on memory summaries for that core mature horizon.

The same exported transcript contains extensive assistant-proposed architecture/research. Those remain assistant suggestions unless separately accepted.

Current `specs.lock` identifies lower-case `KooshaPari/pheno-specs`, path `agileplus-specs`, commit `13fcdc554c73abc765a34592a244abcf16eddf43`, tag `v0.1.0-spec-baseline`. PhenoLab history contains the commit that split specs into that submodule. Current PhenoLM migration docs supersede it as the primary living source but explicitly forbid deleting/detaching it before import verification.

Registry also contains a capitalized ecosystem `PhenoSpecs` absorption into `docs/specs/pheno-specs/`. Equivalence with the lower-case PhenoLab submodule is **not established** and must not be assumed.

PhenoLab spec receipt: `6a0e08da5339942bc4550403eef02fe1a364d063`.

## Remaining archaeology blockers

- Portage: locate gitlink commit `c758019...`; recover exact Harbor fork merge-base/delta and authoritative current packaging.
- PhenoMLX: inspect non-main archived tmp/temp refs only to the extent needed to falsify missing unique history; classify contaminated formal docs and current source ownership.
- PhenoLab: recover lower-case `pheno-specs` pinned content or an authenticated mirror of that exact commit; reconcile its accepted content against current PhenoLM docs.

No product is complete; no fourth product program, merge, release, archive restore or production mutation was performed.
