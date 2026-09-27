---
repo: "PhenoApps"
aliases: ["phenotype-apps", "PhenotypeApps"]
status: "active"
last_verified: "2026-09-27"
owner: "kooshapari"
build_deploy_status: "sunset-shelf"
---

# CVP — PhenoApps (phenotype-apps)

## Identity

PhenoApps (GitHub name; registry and every absorption note still say
`phenotype-apps`) is the **canonical application-collection parent** under
ADR-023: the repo that owns every BLOCK-A application as an `apps/<name>`
child with explicit child-level boundaries and lift provenance — source lift,
build verification, and an audit artifact for each absorbed app. The thing it
does that no other fleet repo does is **hold absorbed apps without ever
absorbing spines**: runtimes, governance, and libraries stay in their own
repos; this one is only applications. As of the 2026-09 sunset pivot its
default branch (`apps-extract`) presents as a **"Sunset shelf: retired,
paused, and archived app repos"** while `main` retains the large legacy Go
monorepo — the identity is the _parent_, the shelf is the current face of it.

## Closest Viable Product

The PhenoApps CVP is **a verifier who can**:

1. Open the default branch and reach `archive/` (today: `FocalPoint`,
   `PhenoInfra`) — retired content is present, labeled, and bounded.
2. Trace any absorbed app cited by the registry (for example
   `apps/tracely/`, lifted 2026-07-17 with cargo-check verification and audit
   artifact `audits/absorption-justifications/Tracely-2026-07-17.md`) back to
   its source repo and prove the lift happened (target state — blocked by the
   verification gate above until child paths are located).
3. Read the parent policy (`projects/phenotype-apps.json`
   `absorption_note` + ADR-023) and see it enforced: children under
   `apps/<name>`, no unrelated spines.
4. Recover from the documented local preservation point
   (`recovery/phenotype-apps-local-20260726`, sha
   `5a0672024b798f852b6a36eaa83820c424d0b5aa`) if the remote drifts.

## In CVP (must ship in this slice)

- **`apps/<name>` children with provenance** for absorbed BLOCK-A apps —
  required scope from live disposition rows: `tracely`, `conft`, `apisync`,
  `subject`, `helios-app`. **Excluded from required scope** (disposition/
  card evidence): `datakit` [voided — canonical target
  `phenotype-python-sdk/packages/data-kit`], `planify` [rejected — extract-
  only recommendation, ARCHIVE_ONLY], `melosviz` [card: independent
  application boundary; `apps/melosviz` rows are historical evidence only],
  `testing-kit` [card: retired into
  `phenotype-python-sdk/packages/testing-kit`].
- **`apps/<name>` tree location proven** — the verification gate below:
  child paths after the 2026-09-16 pivot must be located before this CVP
  counts as met.

  > **Verification gate (UNRESOLVED)**: the `apps/<name>` tree location after
  > the 2026-09-16 pivot is unproven (commit `355016f8` `files[]` truncated by
  > the API; `main` has no `apps/` directory) — see Open Questions. Verifier
  > journey steps 2-3 and the children bullet above cannot be checked on the
  > remote until child paths are located. This CVP stays UNRESOLVED until then.

- **`archive/` shelf** on the default branch for retired/paused/archived
  content (`FocalPoint`, `PhenoInfra`).
- **ADR-023 application-collection policy** stated and enforced in the card:
  boundaries explicit per child; no absorption of unrelated runtime,
  governance, or library spines.
- **Preservation chain**: `local_preservation_ref`/`sha` + audit artifact
  `registry/audit-absorption-justification/gap-cohort-20260726.json`.
- **Registry triad**: this CVP + intent + boundary (this repo previously had
  none).

## Post-CVP (defer until CVP is live)

- **`planify-customisations/`**: the registry's recommendation to extract
  only the Phenotype layers out of the Planify `upstream/` fork.
- **Sunset-shelf completion**: finish moving retired apps onto the shelf and
  record each move with provenance, like the July lifts.

## Anti-CVPs

| Looks like PhenoApps CVP                              | Actually lives in                         | Why                                                                    |
| ----------------------------------------------------- | ----------------------------------------- | ---------------------------------------------------------------------- |
| Absorbing a runtime/governance/library spine          | each spine's own repo                     | Explicit registry rule in `projects/phenotype-apps.json`: never.       |
| Planify `upstream/` Plane fork                        | `upstream/` subtree (AGPL, DO NOT MODIFY) | Only Phenotype-specific layers may ever be extracted.                  |
| The `_retire/phenotype-apps` 1.7GB shell (row id=901) | `_retire/phenotype-apps/`                 | A _different_ artifact that was TOO_INCOMPLETE_RETIRE'd 2026-07-18.    |
| Archived source repos' products                       | their own archived/deleted repos          | The parent stores the _lifted content_, not the repo lifecycle.        |
| FocalPoint / PhenoInfra products                      | `archive/` (content only)                 | Those repos are archived; the shelf keeps history, not a live product. |

## Registry reality (as of 2026-09-27)

- **Renamed**: `gh api repos/KooshaPari/phenotype-apps` resolves to
  `full_name: KooshaPari/PhenoApps`, `name: PhenoApps`, `archived: false`,
  `pushed_at: 2026-09-18`, default branch `apps-extract`. Registry `gh_url`
  and dozens of `target: phenotype-apps (apps/...)` notes still use the old
  name (rename redirects keep old links working; the strings are stale).
- **Default branch root is `archive/` only** (1 dir, 0 files at root);
  `main` holds a 126-entry legacy Go monorepo (`go.mod`, `cmd/`, `server/`,
  `services/`, `slm/`, …) with **no `apps/` directory**.
- **`apps/` last touched 2026-09-16** in commit `355016f8` ("chore: archive
  FocalPoint … 4118 files on main") — the same commit that touched
  `apps/tracely` and `apps/conft`. GitHub truncates that commit's `files[]`
  at 300 entries, so the exact disposition of each `apps/<name>` child is
  **not yet proven** from the API.
- **Disposition**: `projects/phenotype-apps.json` =
  `KEEP_CANONICAL_PARENT`, `canonical_routing: true`, ADR-023 rationale —
  coexisting with the "Sunset shelf" description.

## Open Questions

- **Verification gate — where are the `apps/<name>` children after the
  2026-09-16 pivot?** Deleted, moved under `archive/`, or relocated to
  standalone repos? Answer with a tree-level diff of `355016f8` (commit
  `files[]` is truncated) before the next boundary review. Until then the CVP
  above is UNRESOLVED (see the gate in "In CVP").
- **Sunset shelf vs canonical parent**: does "Sunset shelf" describe a
  temporary face of the canonical parent, or a role change? If role change,
  `KEEP_CANONICAL_PARENT` needs a disposition update; if temporary, the
  GitHub description should say so.
- **Rename propagation**: update `gh_url`, card `name`, and (optionally) the
  `target: phenotype-apps` strings fleet-wide to `PhenoApps`, or leave them
  riding the redirect forever?
- **`main` vs `apps-extract`**: which branch is authoritative for the
  legacy monorepo content (default branch is `apps-extract`, but `main`
  holds the bulk)?

## Change Log

| Date       | Change                                                                                              | Worklog                 |
| ---------- | --------------------------------------------------------------------------------------------------- | ----------------------- |
| 2026-09-27 | Initial CVP + first intent/boundary pair for this repo (WBS A3.3); rename + sunset-pivot recorded   | PHENOREG-FORWARD-WBS A3 |
| 2026-09-27 | Review fixes: exclusions split from required children; verification gate (CVP UNRESOLVED); typo fix | PR #585 review round    |
