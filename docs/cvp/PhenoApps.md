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
`phenotype-apps`) is the **canonical application-collection parent** under the
card's application-collection policy (`projects/phenotype-apps.json`
`absorption_note`: children under `apps/<name>`, no spine absorption — the
same file's `rationale` cites “ADR-023”, but no application-collection ADR-023
resolves in this repo; see Open Questions): the repo that owns every BLOCK-A
application as an `apps/<name>`
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
   `absorption_note` — the in-repo source of the application-collection rule)
   and see it enforced: children under `apps/<name>`, no unrelated spines.
4. Recover from the documented local preservation point
   (`recovery/phenotype-apps-local-20260726`, sha
   `5a0672024b798f852b6a36eaa83820c424d0b5aa`) if the remote drifts.

## In CVP (must ship in this slice)

- **`apps/<name>` children with provenance** for absorbed BLOCK-A apps —
  required scope from disposition rows, each with its row state: `conft`
  (`repo-Conft`, `fsm: live`), `apisync` (`repo-Apisync-batch4` `fsm: live`;
  `repo-Apisync` ABSORB absorbed), `tracera` (row id=922, `fsm: live`,
  `target: phenotype-apps (apps/tracera/)` — newly accounted this round), plus
  target-of-record `tracely` (rows id=59/id=918, `fsm: deleted`) and `subject`
  (`FINAL-subject-app`, `fsm: archived`, resolved 2026-07-18). **Excluded from
  required scope** (disposition/card evidence): `helios-app` [no `apps/*`
  disposition row exists anywhere; `heliosApp` row id=904 is `TOO_INCOMPLETE`
  → `_retire/heliosApp/`, and `docs/boundary/heliosApp.md:7,14` records
  `TOO_LARGE_RETIRE` — “do not absorb”], `datakit` [voided — canonical target
  `phenotype-python-sdk/packages/data-kit`], `planify` [rejected — extract-
  only recommendation, ARCHIVE_ONLY], `melosviz` [card: independent
  application boundary; `FINAL-Melosviz` archived 2026-07-18 = historical
  evidence only], `testing-kit` [row id=912 `TOO_LARGE_RETIRE`; card: retired
  into `phenotype-python-sdk/packages/testing-kit`]. A sixth child,
  `phenoData`, is evidenced by mirror revalidation
  (`docs/absorption/phenoData/ACTIVE_SOURCE_REVALIDATION_20260807.md:12,23-25`
  — identical blob SHAs at the preservation sha) but has no disposition row —
  data gap recorded at the boundary (see `docs/boundary/PhenoApps.md`).
- **`apps/<name>` tree location proven** — the verification gate below:
  child paths after the 2026-09-16 pivot must be located before this CVP
  counts as met.

  > **Verification gate (UNRESOLVED — evidence complete, decision pending):**
  > the tree-level diff of `355016f8` (Git Trees API, 2026-09-27) answers
  > “deleted or moved”: parent `be419459` root held the full monorepo incl.
  > `apps/` (16,868 files: `.github, apisync, conft, helios-app, ios, tracely,
web`); the pivot commit’s root holds exactly one entry — `archive/`
  > (containing only `FocalPoint`). All of `apps/` was **deleted from that
  > tree**, not relocated under `archive/` (subtree-sha match: none). The
  > children survive intact on branches `absorb-sessionledger` and
  > `absorb-researchledger` (verified via `contents/apps?ref=…`) and in
  > history (`be419459`); neither `apps-extract` (default) nor `main` has an
  > `apps/` directory. Remaining blocker = maintainer USER-DECISION: restore
  > `apps/` on the default branch from `absorb-*`, or scope children to those
  > branches. Verifier journey steps 2-3 stay uncheckable on the default
  > branches until then.

- **`archive/` shelf** on the default branch for retired/paused/archived
  content (`FocalPoint`, `PhenoInfra`).
- **Application-collection policy stated and enforced in the card**:
  boundaries explicit per child; no absorption of unrelated runtime,
  governance, or library spines (`projects/phenotype-apps.json`
  `absorption_note`; its `rationale` says “ADR-023” but that pointer does not
  resolve to an application-collection ADR in this repo — see Open Questions).
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

| Looks like PhenoApps CVP                                                                     | Actually lives in                         | Why                                                                                                                                                                                                                                    |
| -------------------------------------------------------------------------------------------- | ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Absorbing a runtime/governance/library spine                                                 | each spine's own repo                     | Explicit registry rule in `projects/phenotype-apps.json`: never.                                                                                                                                                                       |
| Planify `upstream/` Plane fork                                                               | `upstream/` subtree (AGPL, DO NOT MODIFY) | Only Phenotype-specific layers may ever be extracted.                                                                                                                                                                                  |
| Superseded classification of this very repo (row id=901, `KooshaPari/phenotype-apps`, 1.7GB) | `_retire/phenotype-apps/` shelf           | Same repository, not a foreign artifact: `disposition: B:WORKING` / `fsm: archived`, note carries `[TOO_INCOMPLETE_RETIRE 2026-07-17 per ADR-007 §3]`, `resolved_at: 2026-07-18` — direct evidence for the sunset-shelf Open Question. |
| Archived source repos' products                                                              | their own archived/deleted repos          | The parent stores the _lifted content_, not the repo lifecycle.                                                                                                                                                                        |
| FocalPoint / PhenoInfra products                                                             | `archive/` (content only)                 | Those repos are archived; the shelf keeps history, not a live product.                                                                                                                                                                 |

## Registry reality (as of 2026-09-27)

- **Renamed**: `gh api repos/KooshaPari/phenotype-apps` resolves to
  `full_name: KooshaPari/PhenoApps`, `name: PhenoApps`, `archived: false`,
  `pushed_at: 2026-09-18`, default branch `apps-extract`. Registry `gh_url`
  and the `target: phenotype-apps (apps/...)` strings (14 occurrences across 9
  rows: tracely ×2, conft ×2, apisync ×4, subject ×2, melosviz ×2, testing-kit,
  tracera; a further ~196 rows target bare `phenotype-apps`) still use the old
  name (rename redirects keep old links working; the strings are stale).
- **Default branch root is `archive/` only** (1 dir, 0 files at root);
  `main` holds a 126-entry legacy Go monorepo (`go.mod`, `cmd/`, `server/`,
  `services/`, `slm/`, …) with **no `apps/` directory**.
- **`apps/` removed from the tree at the 2026-09-16 pivot** (commit
  `355016f8`, branch `main-focalpoint-archive`): a Git Trees diff against its
  parent `be419459` shows the root reduced to `archive/` (FocalPoint only) —
  all 16,868 `apps/` files deleted from that tree, with no subtree-sha copy
  under `archive/`. Children verified present on `absorb-sessionledger` and
  `absorb-researchledger`; absent from `apps-extract` and `main`. (The old
  “`files[]` truncated at 300 entries” limitation does not apply to the Trees
  API and is superseded by this diff.)
- **Disposition**: `projects/phenotype-apps.json` =
  `KEEP_CANONICAL_PARENT`, `canonical_routing: true`, card `rationale`
  (labeled “ADR-023” there — pointer gap recorded) —
  coexisting with the "Sunset shelf" description.

## Open Questions

- **Verification gate — ANSWERED (2026-09-27); decision pending**: the tree
  diff of `355016f8` shows `apps/<name>` was deleted from that branch’s tree
  (not moved under `archive/`); children survive on `absorb-sessionledger` +
  `absorb-researchledger` (and history `be419459`). Open decision: restore
  `apps/` on the default branch or scope children to the `absorb-*` branches
  (maintainer USER-DECISION; gate in “In CVP” stays UNRESOLVED until then).
- **Where is the application-collection ADR-023?** The card’s `rationale`
  cites “ADR-023 application-collection policy”, but `docs/adr/` holds only
  ADR-004..007, `docs/adrs/ADR-ECO-023-sdk-consolidation.md` is an SDK-
  consolidation decision, and `docs/monorepo-state/AGENTS.md:119` maps ADR-023
  to agent-effort governance (source path `docs/adr/2026-06-15/ADR-023-agent-
effort-governance.md`, not present here). The policy text itself lives in
  `projects/phenotype-apps.json:26-27`. Add the missing ADR pointer or stop
  citing ADR-023 for app-collection policy (six citations across this triad
  were re-attributed to the card in this review round).
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

| Date       | Change                                                                                                                                                                                                                                                                             | Worklog                 |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| 2026-09-27 | Initial CVP + first intent/boundary pair for this repo (WBS A3.3); rename + sunset-pivot recorded                                                                                                                                                                                  | PHENOREG-FORWARD-WBS A3 |
| 2026-09-27 | Review fixes: exclusions split from required children; verification gate (CVP UNRESOLVED); typo fix                                                                                                                                                                                | PR #585 review round    |
| 2026-09-27 | Kilo round 2: gate evidence completed (tree diff — `apps/` deleted, restore source = `absorb-*` branches), required/excluded children re-derived from row states (+tracera, −helios-app, phenoData gap), row-901 same-repo correction, ADR-023 citations re-attributed to the card | PR #585 review round    |
