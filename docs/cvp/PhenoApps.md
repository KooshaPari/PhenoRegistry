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
repos; this one is only applications. At the 2026-09 sunset pivot its
default branch (`apps-extract`) presented as a **"Sunset shelf: retired,
paused, and archived app repos"** while `main` retained the large legacy Go
monorepo — the identity is the _parent_, and at that recorded moment the shelf
was the face of it. That branch has since been deleted (2026-09-27); the current
shelf location is unresolved (gate below).

## Closest Viable Product

The PhenoApps CVP is **a verifier who can**:

1. Open the shelf and reach `archive/` — retired content present, labeled,
   and bounded. **Shelf state captured 2026-09-27 (Git Trees diff of the
   pivot):** `archive/` held **`FocalPoint` only**; `PhenoInfra` has no
   disposition row anywhere in `registry/disposition-index.json` and lives in
   its own archived repo. The shelf branch itself was then deleted (enumeration
   of 37 branches as of 22:04Z holds no archive holder; `main-focalpoint-archive`
   and `apps-extract` both gone), so verifier step 1 now begins with locating
   the shelf's current home (blocked — gate below).
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
  `repo-Apisync` ABSORB absorbed), `tracera` (row id=922,
  `disposition: TOO_LARGE_RETIRE` (`:6076`) + `fsm: live` (`:6077`), note
  `[FIXED 2026-07-19: done->live, canonical disposition]` (`:6081`),
  `target: phenotype-apps (apps/tracera/)` (`:6084`) — newly accounted this
  round), plus
  target-of-record `tracely` (rows id=59/id=918, `fsm: deleted`) and `subject`
  (`FINAL-subject-app`, `fsm: archived`, resolved 2026-07-18). **Excluded from
  required scope** (disposition/card evidence): `helios-app` [no `apps/*`
  disposition row exists anywhere; `heliosApp` row id=904 is `TOO_INCOMPLETE`
  → `_retire/heliosApp/`, and `docs/boundary/heliosApp.md:7,14` records
  `TOO_LARGE_RETIRE` — “do not absorb”], `datakit` [voided — canonical target
  `phenotype-python-sdk/packages/data-kit`], `planify` [rejected — extract-
  only recommendation, ARCHIVE_ONLY], `melosviz` [card: independent
  application boundary; `FINAL-Melosviz` archived 2026-07-18 = historical
  evidence only]. `phenoData` is **excluded with
  row evidence**: `repo-phenoData` (`disposition-index.json:2830-2833`,
  `fsm: live` `:2827`) targets `pheno (crates/pheno-data-*)` with
  `absorbed_at: 2026-07-18` (`:2817`; the row also carries
  `absorbed_on: 2026-07-17` `:2819` — two fields, both dates as recorded), and its row cites
  `audits/absorption-justifications/phenoData-2026-07-17.md` (`:2822` —
  **absent on disk**: registry data gap) — the source content's canonical home
  is the `pheno` crates; the mirror revalidation
  (`docs/absorption/phenoData/ACTIVE_SOURCE_REVALIDATION_20260807.md:12,23-25`)
  is mirror evidence, not an unclassified child. What does not exist is a row
  targeting `apps/phenoData` (earlier "no disposition row" wording corrected
  this round — see Open Questions).
- **UNRESOLVED scope — not excluded**: `testing-kit` [row id=912
  `TOO_LARGE_RETIRE`, `fsm: live`, target
  `phenotype-apps (apps/testing-kit/)` (row note: content absorbed into its
  apps submodule); card: retired into
  `phenotype-python-sdk/packages/testing-kit` — row and card conflict, live
  registry target vs retired card]. Not in either the required-scope or the
  excluded list until reconciled (Open Questions below).
- **`apps/<name>` tree location proven** — the verification gate below:
  child paths after the 2026-09-16 pivot must be located before this CVP
  counts as met.

  > **Verification gate (UNRESOLVED — source branches deleted, decision
  > pending):** tree-level diff captured 2026-09-27 (Git Trees API, before
  > deletion): parent `be419459` **root** held the full monorepo incl.
  > `apps/`; the recorded **`apps/` children list** (previously conflated
  > with the root in this sentence) = `.github, apisync, conft, helios-app,
ios, tracely, web` (16,868 files) — caveat: that recorded enumeration
  > omits required-scope children `tracera` and `subject` (phenoData is
  > excluded per row evidence above, not required scope; all three landed
  > later or elsewhere in the tree; not re-verifiable post-deletion). The
  > pivot commit’s root holds exactly one entry — `archive/`
  > (containing only `FocalPoint`). All of `apps/` was **deleted from that
  > tree**, not relocated under `archive/` (subtree-sha match: none).
  > Recorded children then verified on `absorb-sessionledger` +
  > `absorb-researchledger` (via `contents/apps?ref=…`) and in history
  > (`be419459`); neither `apps-extract` (default) nor `main` held an
  > `apps/` directory. **Update 2026-09-27 22:04Z:** those holder branches
  > (`absorb-sessionledger`, `absorb-researchledger`,
  > `main-focalpoint-archive`, `apps-extract`) have been **deleted**, and
  > both pivot commits now return HTTP 422 on the commits API (unreachable) —
  > the tree evidence above was captured pre-deletion and is no longer
  > re-runnable from live refs. Two blockers now stand: (1) locate or
  > recreate the restore source (re-derive from a clone that still has
  > `absorb-*`, or restore the branches), and (2) maintainer USER-DECISION —
  > restore `apps/` on the default branch or scope children to the recovered
  > branches. Verifier steps 2-3 stay uncheckable until both clear.

- **`archive/` shelf** for retired/paused/archived content — pivot-tree
  contents: `FocalPoint` only; current home unresolved (shelf branches
  deleted 2026-09-27 — gate below). `PhenoInfra` dropped from this claim: no
  disposition row exists for it, and a live
  `gh api repos/KooshaPari/PhenoInfra` probe (2026-09-27) reports
  `archived: true` — no in-repo record of the archive otherwise.
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
| FocalPoint products                                                                          | `archive/` (content only)                 | FocalPoint is archived and was shelf-held at the pivot (tree evidence); PhenoInfra dropped from this claim — no disposition row, its own archived repo.                                                                                |

## Registry reality (as of 2026-09-27)

- **Renamed**: `gh api repos/KooshaPari/phenotype-apps` resolves to
  `full_name: KooshaPari/PhenoApps`, `name: PhenoApps`, `archived: false`,
  `pushed_at: 2026-09-18`, default branch `apps-extract` (recorded before that
  branch's deletion on 2026-09-27 — current default branch unverified).
  Registry `gh_url`
  and the `phenotype-apps (apps/<name>/)` strings (14 occurrences across 9
  rows: 9 are `target:` fields, 5 are `absorbed_into:` (`:2354` conft,
  `:2588`/`:4730` apisync, `:5229` subject, `:5257` melosviz) — tracely ×2 on
  **two** rows (id=59 `:1068`, id=918 `:6032`), conft ×2 the only pair on one
  row, apisync ×4 across **two** rows
  — `repo-Apisync-batch4` and `repo-Apisync`, two fields each — subject
  ×2 and melosviz ×2 one field of each kind, testing-kit, tracera (template `[/]`: 5 of the 14 — apisync `:4730`,
  subject `:5229`/`:5240`, melosviz `:5257`/`:5268` — omit the trailing
  slash); exactly 196 further rows target bare
  `phenotype-apps`) still use the old
  name (rename redirects keep old links working; the strings are stale).
- **Default branch root was `archive/` only** (1 dir, 0 files at root;
  recorded pre-deletion — `apps-extract` deleted 2026-09-27, current default
  branch unverified);
  `main` holds a 126-entry legacy Go monorepo (`go.mod`, `cmd/`, `server/`,
  `services/`, `slm/`, …) with **no `apps/` directory**.
- **`apps/` removed from the tree at the 2026-09-16 pivot** (commit
  `355016f8`, branch `main-focalpoint-archive`): a Git Trees diff against its
  parent `be419459` shows the root reduced to `archive/` (FocalPoint only) —
  all 16,868 `apps/` files deleted from that tree, with no subtree-sha copy
  under `archive/`. Children verified present on `absorb-sessionledger` and
  `absorb-researchledger`; absent from `apps-extract` and `main`. _(All four
  branches named here were deleted 2026-09-27 after this capture; both commits
  now return HTTP 422 on the commits API — evidence stands as a pre-deletion
  capture, not re-runnable from live refs.)_ (The old
  “`files[]` truncated at 300 entries” limitation does not apply to the Trees
  API and is superseded by this diff.)
- **Disposition**: `projects/phenotype-apps.json` =
  `KEEP_CANONICAL_PARENT`, `canonical_routing: true`, card `rationale`
  (labeled “ADR-023” there — pointer gap recorded) —
  coexisting with the "Sunset shelf" description.

## Open Questions

- **Verification gate — evidence captured, source branches deleted; decision
  pending**: the pre-deletion tree diff of `355016f8` shows `apps/<name>`
  deleted from that branch’s tree (not moved under `archive/`) with children
  recorded on `absorb-sessionledger` + `absorb-researchledger` (and history
  `be419459`); those branches — plus `main-focalpoint-archive`,
  `apps-extract` — were deleted 2026-09-27 after the capture, and the pivot
  commits return HTTP 422 (unreachable). Open decisions: (1) locate or
  recreate the child-bearing branches (re-derive from a clone that still has
  them), then (2) restore `apps/` on the default branch or scope children to
  the recovered branches (maintainer USER-DECISION). Gate in “In CVP” stays
  UNRESOLVED until both clear.
- **`testing-kit` scope unresolved**: row id=912 says `TOO_LARGE_RETIRE` /
  `fsm: live` with `target: phenotype-apps (apps/testing-kit/)` while the
  card records retirement into `phenotype-python-sdk/packages/testing-kit`.
  Until row and card are reconciled, `testing-kit` is neither confirmed
  required-scope nor confirmed excluded (maintainer call).
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
  holds the bulk)? (`apps-extract` deleted 2026-09-27 — the question now
  includes where the default branch went.)
- **Catalog status vs card/GitHub (generator authority)**:
  `catalog/registry.yaml` `phenotype-apps.status` stays `archived` because
  `scripts/sync_catalog.py` regenerates it from frozen row id=901
  (`fsm: archived`, `frozen: true`) — a hand flip to `active` (earlier in
  this PR) is reverted on the next sync. The card (`KEEP_CANONICAL_PARENT`,
  `status: active`) and GitHub (`archived: false`) disagree with the frozen
  index; resolving needs the unfreeze decision. README + this CVP describe
  card/GitHub reality; the catalog reflects the frozen index.

## Change Log

| Date       | Change                                                                                                                                                                                                                                                                                                                                                                                                    | Worklog                   |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| 2026-09-27 | Initial CVP + first intent/boundary pair for this repo (WBS A3.3); rename + sunset-pivot recorded                                                                                                                                                                                                                                                                                                         | PHENOREG-FORWARD-WBS A3   |
| 2026-09-27 | Review fixes: exclusions split from required children; verification gate (CVP UNRESOLVED); typo fix                                                                                                                                                                                                                                                                                                       | PR #585 review round      |
| 2026-09-27 | Kilo round 2: gate evidence completed (tree diff — `apps/` deleted, restore source = `absorb-*` branches), required/excluded children re-derived from row states (+tracera, −helios-app, phenoData gap), row-901 same-repo correction, ADR-023 citations re-attributed to the card                                                                                                                        | PR #585 review round      |
| 2026-09-27 | Kilo round 3: shelf claim narrowed (FocalPoint only; PhenoInfra no row), gate evidence re-labeled pre-deletion (holder branches deleted 22:04Z, commits 422), phenoData given row evidence + moved to excluded, apisync two-row arithmetic + 196 exact, catalog-status divergence OQ (sync_catalog.py reverts hand flips)                                                                                 | PR #584/#585 review round |
| 2026-09-27 | Kilo/CR round 4: shelf statement past-tense + unresolved (CR), testing-kit marked scope UNRESOLVED pending row/card reconciliation (CR), `absorbed_at` cite `:2817` + `absorbed_on` cross-note, PhenoInfra archived claim → dated live probe, 14-string arithmetic split (9 `target` + 5 `absorbed_into`; tracely rows id=59/918), caveat drops phenoData from required scope, REGISTRY 82-vs-86 restated | PR #584 review round      |
