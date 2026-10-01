---
repo: "PhenoApps"
aliases: ["phenotype-apps", "PhenotypeApps"]
role: application-parent
status: active
last_boundary_review: 2026-10-01
review_cadence: 30d
in_scope:
  - "apps/<name> BLOCK-A application children with lift provenance — required per disposition rows: conft (repo-Conft live), apisync (batch4 live + ABSORB), tracera (id=922: disposition TOO_LARGE_RETIRE + fsm live — both fields stated), tracely (id=59/918 deleted — target-of-record), subject (FINAL-subject-app archived 2026-07-18). Excluded: helios-app (no apps/* row; heliosApp id=904 TOO_INCOMPLETE -> _retire/ + boundary/heliosApp.md TOO_LARGE_RETIRE do-not-absorb), datakit voided, planify rejected, melosviz (card: independent; FINAL-Melosviz fsm archived, target phenotype-apps (apps/melosviz)), phenoData (row exists: repo-phenoData fsm live, target pheno (crates/pheno-data-*), cited artifact phenoData-2026-07-17.md absent — no apps/phenoData-targeted row)"
  - "archive/ retirement shelf (pivot-tree contents: FocalPoint only; PhenoInfra has no disposition row; live gh api probe 2026-09-27 reports archived: true (no in-repo record otherwise); shelf branches main-focalpoint-archive + apps-extract deleted 2026-09-27 — current home unresolved, see cvp gate)"
  - "application-collection policy enforcement per card absorption_note (child boundaries, no spine absorption)"
  - "preservation chain (recovery/phenotype-apps-local-20260726 + gap-cohort audit artifact)"
out_of_scope:
  - "runtime / governance / library spines — each in its own canonical repo"
  - "Planify upstream/ AGPL subtree (verbatim fork, DO NOT MODIFY)"
  - "row id=901 = superseded classification of this same repo (KooshaPari/phenotype-apps, 1.7GB; disposition B:WORKING / fsm archived; note: TOO_INCOMPLETE_RETIRE 2026-07-17, resolved 2026-07-18) — evidence for the sunset-shelf question, out of in-scope contract"
  - "archived source repos' lifecycle (archive/delete happens at the source repo)"
  # testing-kit (row id=912 target `apps/testing-kit/`): not classified in or out — unresolved row/card conflict; see `## Unresolved scope (non-gating)` below
---

# Boundary — PhenoApps

## In Scope

- **Application children**: BLOCK-A apps under `apps/<name>`, each with an
  explicit boundary and lift provenance — source lift + build verification +
  a named audit artifact **where one exists** (directory fact:
  `audits/absorption-justifications/` holds 92 `.md` manifests; claim: of the
  artifacts these rows cite, `Tracely-2026-07-17.md` and required-child
  `Tracera-2026-06-25.md` are present, while `conft`
  (`disposition-index.json:2356`) and `apisync` (`:2590`) reference
  `Conft-2026-07-17.md` / `Apisync-2026-07-17.md`, which are **absent**,
  `phenoData`'s row cites `phenoData-2026-07-17.md` (`:2822`) — also
  **absent** — and `subject` (`:5228-5241`) cites no artifact at all: recorded
  as registry data gaps, not silently claimed). `phenoData` is **excluded**
  with row evidence: `repo-phenoData` (`:2830-2833`, `fsm: live` `:2827`,
  `target: pheno (crates/pheno-data-*)`, `absorbed_at: 2026-07-18` `:2817`, row also `absorbed_on: 2026-07-17` `:2819`) — the
  source content's canonical home is the `pheno` crates; the mirror
  (`docs/absorption/phenoData/ACTIVE_SOURCE_REVALIDATION_20260807.md:12,23-25`,
  identical blob SHAs at the cited preservation sha) is revalidation
  evidence. No row targets `apps/phenoData` (earlier "no disposition row"
  wording corrected this round).
- **Retirement shelf**: `archive/` holding retired/paused/archived content,
  labeled and bounded — pivot-tree contents `FocalPoint` only; shelf branches
  `main-focalpoint-archive` + `apps-extract` deleted 2026-09-27, current home
  unresolved (see cvp gate).
- **Collection policy**: as stated in `projects/phenotype-apps.json`
  (`absorption_note`): keep application boundaries explicit under
  `apps/<name>`; do not absorb unrelated runtime, governance, or library
  spines. (The card’s `rationale` labels this “ADR-023”, but the ADR-023
  **source file** (`docs/adr/2026-06-15/ADR-023-agent-effort-governance.md`)
  is absent — `docs/adr/` holds ADR-004..007 only; the label maps to
  agent-effort governance via `docs/monorepo-state/AGENTS.md:119` (and `:169` = the app-level triage / app-substrate section under that ADR), while
  `docs/adrs/ADR-ECO-023-sdk-consolidation.md` is SDK consolidation — pointer
  gap tracked as an Open Question in `docs/cvp/PhenoApps.md`.)
- **Preservation**: local recovery ref
  (`recovery/phenotype-apps-local-20260726`, sha
  `5a0672024b798f852b6a36eaa83820c424d0b5aa`) + audit artifact
  `registry/audit-absorption-justification/gap-cohort-20260726.json`.

## Unresolved scope (non-gating)

- **`testing-kit`** — neither in scope nor out of scope until the row/card
  conflict is reconciled (row id=912 `TOO_LARGE_RETIRE` / `fsm: live` with
  `target: phenotype-apps (apps/testing-kit/)` vs card retirement into
  `phenotype-python-sdk/packages/testing-kit`); tracked as an Open Question
  in `docs/cvp/PhenoApps.md`. Non-gating for the boundary contract.

## Out of Scope

| Not here                                                                                 | Lives in                            | Reason                                                                                                                                                                                             |
| ---------------------------------------------------------------------------------------- | ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Runtime / governance / library spines                                                    | each spine's own canonical repo     | Explicit registry rule: the parent never absorbs non-application content.                                                                                                                          |
| Planify `upstream/` (Plane fork, AGPL)                                                   | `upstream/` subtree (DO NOT MODIFY) | Verbatim vendor subtree; only Phenotype layers may be extracted (post-CVP).                                                                                                                        |
| Superseded classification of this repo (row id=901)                                      | `_retire/phenotype-apps/` shelf     | Same repo `KooshaPari/phenotype-apps`: `B:WORKING`/`fsm: archived`, note `TOO_INCOMPLETE_RETIRE 2026-07-17`, resolved 2026-07-18 — evidence for the sunset-shelf question, not a foreign artifact. |
| Source repos' archive/delete lifecycle                                                   | the source repos themselves         | The parent stores lifted content, never the repo lifecycle.                                                                                                                                        |
| FocalPoint as a live product (PhenoInfra dropped: no disposition row, own archived repo) | `archive/` (content only)           | FocalPoint archived; the shelf keeps history, not a product.                                                                                                                                       |

## Boundary Crossings

| Crossing                                                                                                                                                                       | Direction                             | Surface                   | Status                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------- | ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Absorbed app lift (conft, apisync, tracera live rows; tracely, subject target-of-record; phenoData excluded with row evidence; excluded cohorts per card/disposition evidence) | source repo → PhenoApps `apps/<name>` | git lift + build verify   | amber (registry-cited July lifts; tree location answered but restore decision pending — see cvp gate)                                                                                                                |
| FocalPoint / PhenoInfra retirement move                                                                                                                                        | source repo → `archive/`              | git archive move          | amber (PR #169 2026-09-17 cited, but no in-repo artifact corroborates it — only `disposition-index.json:1013` source-repo archive + `audits/absorption-justifications/FocalPoint-2026-07-17.md` for the July action) |
| `apps/<name>` children reachable at default-branch root                                                                                                                        | PhenoApps → verifiers                 | git tree                  | amber (root now `archive/` only; post-2026-09-16 location unverified)                                                                                                                                                |
| Planify upstream sync                                                                                                                                                          | upstream Plane → `upstream/`          | vendored subtree          | amber (read-only; do not modify)                                                                                                                                                                                     |
| Services consuming absorbed apps                                                                                                                                               | PhenoServices → PhenoApps             | package / repo dependency | amber (depends on children location question)                                                                                                                                                                        |

## Last Boundary Review

**Date:** 2026-09-27
**Reviewer:** jcode agent (PHENOREG-FORWARD-WBS A3.3)
**Worklog / finding:** initial boundary authored from
`projects/phenotype-apps.json`, GitHub tree probes (both branches), and
disposition-index absorption rows.
**Decisions:**

- First boundary doc for this repo; `apps/<name>` post-pivot location
  recorded as amber, not guessed.
- Tree-level diff of `355016f8` (2026-09-27 kilo round): `apps/` was deleted
  from that branch’s root (reduced to `archive/FocalPoint`); children verified
  intact on `absorb-sessionledger` + `absorb-researchledger`. Gate stays open
  pending the restore-vs-scope USER-DECISION; both crossing rows above
  downgraded from green to amber (unproven move / missing corroboration).
- Row id=901 re-classified as this repo’s superseded classification (same
  `gh_url`), not a separate artifact; `helios-app` removed from required scope
  (no `apps/*` row; `do-not-absorb` record) and `tracera` added (live row).
- Post-capture update (2026-09-27 22:04Z): the `absorb-sessionledger`,
  `absorb-researchledger`, `main-focalpoint-archive`, and `apps-extract`
  branches were deleted after the tree evidence above was recorded, and both
  pivot commits return HTTP 422 — the evidence stands as a pre-deletion
  capture; the gate remains open with branch restoration as blocker (1).

**Date:** 2026-10-01
**Reviewer:** jcode agent (PHENOREG-FORWARD-WBS, PR #598 `8e64c8e6`)
**Worklog / finding:** kilo round-12 thread `PRRT_kwDOR5eICc6oFRcM` (post-merge on
PR #586): the `testing-kit` clause was dropped from `in_scope[0]` without any
record in this file's review metadata, so a future reviewer cannot tell the
removal from an accidental drop.
**Decisions:**

- `testing-kit` (row id=912 target `apps/testing-kit/`) removed from
  `in_scope[0]` membership **deliberately**: a YAML sequence item asserts
  in-scope no matter how its scalar ends, contradicting the prose's "neither
  in scope nor out of scope until the row/card conflict is reconciled" hold.
  The no-verdict pointer now lives only in the `#`-comment beside the lists
  and the `## Unresolved scope (non-gating)` section.
- Validator checked: `tools/check-ecosystem.ts` (1,223 lines) contains no
  `testing-kit` and no `in_scope` reference — no tooling requires the
  membership entry, so removal changes prose contract only.
- Mirrors the per-round `## Change Log` pattern in `docs/cvp/PhenoApps.md:246`.

**Next review:** 2026-10-31
