---
repo: "PhenoApps"
aliases: ["phenotype-apps", "PhenotypeApps"]
role: application-parent
status: active
last_boundary_review: 2026-09-27
review_cadence: 30d
in_scope:
  - "apps/<name> BLOCK-A application children with lift provenance — required per disposition rows: conft (repo-Conft live), apisync (batch4 live + ABSORB), tracera (id=922 live), tracely (id=59/918 deleted — target-of-record), subject (FINAL-subject-app archived 2026-07-18); phenoData evidenced by mirror revalidation but has no row (data gap). Excluded: helios-app (no apps/* row; heliosApp id=904 TOO_INCOMPLETE -> _retire/ + boundary/heliosApp.md TOO_LARGE_RETIRE do-not-absorb), datakit voided, planify rejected, melosviz independent, testing-kit (id=912 TOO_LARGE_RETIRE -> python-sdk)"
  - "archive/ retirement shelf on the default branch (FocalPoint, PhenoInfra)"
  - "application-collection policy enforcement per card absorption_note (child boundaries, no spine absorption)"
  - "preservation chain (recovery/phenotype-apps-local-20260726 + gap-cohort audit artifact)"
out_of_scope:
  - "runtime / governance / library spines — each in its own canonical repo"
  - "Planify upstream/ AGPL subtree (verbatim fork, DO NOT MODIFY)"
  - "row id=901 = superseded classification of this same repo (KooshaPari/phenotype-apps, 1.7GB; disposition B:WORKING / fsm archived; note: TOO_INCOMPLETE_RETIRE 2026-07-17, resolved 2026-07-18) — evidence for the sunset-shelf question, out of in-scope contract"
  - "archived source repos' lifecycle (archive/delete happens at the source repo)"
---

# Boundary — PhenoApps

## In Scope

- **Application children**: BLOCK-A apps under `apps/<name>`, each with an
  explicit boundary and lift provenance — source lift + build verification +
  a named audit artifact **where one exists** (`Tracely-2026-07-17.md` is the
  only file actually present in `audits/absorption-justifications/`; the rows
  for `conft` (`disposition-index.json:2356`) and `apisync` (`:2590`) reference
  `Conft-2026-07-17.md` / `Apisync-2026-07-17.md`, which are **absent**, and
  `subject` (`:5228-5241`) cites no artifact at all — recorded as registry data
  gaps, not silently claimed). A sixth child, `phenoData`, is evidenced by
  `docs/absorption/phenoData/ACTIVE_SOURCE_REVALIDATION_20260807.md:12,23-25`
  (mirror with identical blob SHAs at the cited preservation sha) but has no
  disposition row — in neither the required nor the excluded list until a row
  exists.
- **Retirement shelf**: `archive/` on the default branch (`apps-extract`)
  holding retired/paused/archived content, labeled and bounded.
- **Collection policy**: as stated in `projects/phenotype-apps.json`
  (`absorption_note`): keep application boundaries explicit under
  `apps/<name>`; do not absorb unrelated runtime, governance, or library
  spines. (The card’s `rationale` labels this “ADR-023”, but no
  application-collection ADR-023 resolves in this repo — pointer gap tracked
  as an Open Question in `docs/cvp/PhenoApps.md`.)
- **Preservation**: local recovery ref
  (`recovery/phenotype-apps-local-20260726`, sha
  `5a0672024b798f852b6a36eaa83820c424d0b5aa`) + audit artifact
  `registry/audit-absorption-justification/gap-cohort-20260726.json`.

## Out of Scope

| Not here                                            | Lives in                            | Reason                                                                                                                                                                                             |
| --------------------------------------------------- | ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Runtime / governance / library spines               | each spine's own canonical repo     | Explicit registry rule: the parent never absorbs non-application content.                                                                                                                          |
| Planify `upstream/` (Plane fork, AGPL)              | `upstream/` subtree (DO NOT MODIFY) | Verbatim vendor subtree; only Phenotype layers may be extracted (post-CVP).                                                                                                                        |
| Superseded classification of this repo (row id=901) | `_retire/phenotype-apps/` shelf     | Same repo `KooshaPari/phenotype-apps`: `B:WORKING`/`fsm: archived`, note `TOO_INCOMPLETE_RETIRE 2026-07-17`, resolved 2026-07-18 — evidence for the sunset-shelf question, not a foreign artifact. |
| Source repos' archive/delete lifecycle              | the source repos themselves         | The parent stores lifted content, never the repo lifecycle.                                                                                                                                        |
| FocalPoint / PhenoInfra as live products            | `archive/` (content only)           | Those repos are archived; the shelf keeps history, not a product.                                                                                                                                  |

## Boundary Crossings

| Crossing                                                                                                                                                      | Direction                             | Surface                   | Status                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- | ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Absorbed app lift (conft, apisync, tracera live rows; tracely, subject target-of-record; phenoData evidenced; excluded cohorts per card/disposition evidence) | source repo → PhenoApps `apps/<name>` | git lift + build verify   | amber (registry-cited July lifts; tree location answered but restore decision pending — see cvp gate)                                                                                                                |
| FocalPoint / PhenoInfra retirement move                                                                                                                       | source repo → `archive/`              | git archive move          | amber (PR #169 2026-09-17 cited, but no in-repo artifact corroborates it — only `disposition-index.json:1013` source-repo archive + `audits/absorption-justifications/FocalPoint-2026-07-17.md` for the July action) |
| `apps/<name>` children reachable at default-branch root                                                                                                       | PhenoApps → verifiers                 | git tree                  | amber (root now `archive/` only; post-2026-09-16 location unverified)                                                                                                                                                |
| Planify upstream sync                                                                                                                                         | upstream Plane → `upstream/`          | vendored subtree          | amber (read-only; do not modify)                                                                                                                                                                                     |
| Services consuming absorbed apps                                                                                                                              | PhenoServices → PhenoApps             | package / repo dependency | amber (depends on children location question)                                                                                                                                                                        |

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

**Next review:** 2026-10-27
