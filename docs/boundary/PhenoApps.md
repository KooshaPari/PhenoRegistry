---
repo: "PhenoApps"
aliases: ["phenotype-apps", "PhenotypeApps"]
role: application-parent
status: active
last_boundary_review: 2026-09-27
review_cadence: 30d
in_scope:
  - "apps/<name> BLOCK-A application children with lift provenance (tracely, conft, apisync, melosviz, subject, testing-kit, helios-app, ...)"
  - "archive/ retirement shelf on the default branch (FocalPoint, PhenoInfra)"
  - "ADR-023 application-collection policy enforcement (child boundaries, no spine absorption)"
  - "preservation chain (recovery/phenotype-apps-local-20260726 + gap-cohort audit artifact)"
out_of_scope:
  - "runtime / governance / library spines — each in its own canonical repo"
  - "Planify upstream/ AGPL subtree (verbatim fork, DO NOT MODIFY)"
  - "_retire/phenotype-apps 1.7GB iOS+Web shell artifact (disposition row id=901)"
  - "archived source repos' lifecycle (archive/delete happens at the source repo)"
---

# Boundary — PhenoApps

## In Scope

- **Application children**: BLOCK-A apps under `apps/<name>`, each with an
  explicit boundary and lift provenance (source lift + build verification +
  named audit artifact, e.g. `audits/absorption-justifications/Tracely-2026-07-17.md`).
- **Retirement shelf**: `archive/` on the default branch (`apps-extract`)
  holding retired/paused/archived content, labeled and bounded.
- **Collection policy**: ADR-023 as stated in `projects/phenotype-apps.json`
  (`absorption_note`): keep application boundaries explicit under
  `apps/<name>`; do not absorb unrelated runtime, governance, or library
  spines.
- **Preservation**: local recovery ref
  (`recovery/phenotype-apps-local-20260726`, sha
  `5a0672024b798f852b6a36eaa83820c424d0b5aa`) + audit artifact
  `registry/audit-absorption-justification/gap-cohort-20260726.json`.

## Out of Scope

| Not here                                 | Lives in                            | Reason                                                                       |
| ---------------------------------------- | ----------------------------------- | ---------------------------------------------------------------------------- |
| Runtime / governance / library spines    | each spine's own canonical repo     | Explicit registry rule: the parent never absorbs non-application content.    |
| Planify `upstream/` (Plane fork, AGPL)   | `upstream/` subtree (DO NOT MODIFY) | Verbatim vendor subtree; only Phenotype layers may be extracted (post-CVP).  |
| The 1.7GB iOS+Web shell (row id=901)     | `_retire/phenotype-apps/`           | Separate artifact, TOO_INCOMPLETE_RETIRE 2026-07-18; not part of the parent. |
| Source repos' archive/delete lifecycle   | the source repos themselves         | The parent stores lifted content, never the repo lifecycle.                  |
| FocalPoint / PhenoInfra as live products | `archive/` (content only)           | Those repos are archived; the shelf keeps history, not a product.            |

## Boundary Crossings

| Crossing                                                                                | Direction                             | Surface                   | Status                                                                |
| --------------------------------------------------------------------------------------- | ------------------------------------- | ------------------------- | --------------------------------------------------------------------- |
| Absorbed app lift (tracely, conft, apisync, melosviz, subject, testing-kit, helios-app) | source repo → PhenoApps `apps/<name>` | git lift + build verify   | green (registry-cited July lifts)                                     |
| FocalPoint / PhenoInfra retirement move                                                 | source repo → `archive/`              | git archive move          | green (PR #169, 2026-09-17)                                           |
| `apps/<name>` children reachable at default-branch root                                 | PhenoApps → verifiers                 | git tree                  | amber (root now `archive/` only; post-2026-09-16 location unverified) |
| Planify upstream sync                                                                   | upstream Plane → `upstream/`          | vendored subtree          | amber (read-only; do not modify)                                      |
| Services consuming absorbed apps                                                        | PhenoServices → PhenoApps             | package / repo dependency | amber (depends on children location question)                         |

## Last Boundary Review

**Date:** 2026-09-27
**Reviewer:** jcode agent (PHENOREG-FORWARD-WBS A3.3)
**Worklog / finding:** initial boundary authored from
`projects/phenotype-apps.json`, GitHub tree probes (both branches), and
disposition-index absorption rows.
**Decisions:**

- First boundary doc for this repo; `apps/<name>` post-pivot location
  recorded as amber, not guessed.

**Next review:** 2026-10-27
