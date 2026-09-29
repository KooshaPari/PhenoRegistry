---
repo: "PhenoApps"
aliases: ["phenotype-apps", "PhenotypeApps"]
role: application-parent
status: active
last_verified: 2026-09-27
bound_prompts: 0
bound_plans: 0
bound_responses: 0
device: windows # authored on the Windows registry workstation (workstation fact recorded here as provenance for the non-macbook value); device vocabulary: root STATUS.md:5 (Author device), gate docs/monorepo-state/STATUS.md:251 (macbook|heavy-runner), ADR-023 policy STATUS.md:290,395
---

# Intent — PhenoApps

## Intent Statement

Act as the **canonical application-collection parent** (application-collection policy per `projects/phenotype-apps.json` `absorption_note`; the card’s `rationale` cites “ADR-023”, which does not resolve to an application-collection ADR in this repo — pointer gap recorded): every
BLOCK-A application lives at `apps/<name>` behind an explicit child boundary,
arriving only through a verifiable lift — source lift, build verification,
and a named audit artifact — and the parent **never absorbs runtime,
governance, or library spines** (those stay in their own canonical repos).
The parent's second duty was retirement custody: at the recorded 2026-09
pivot the default branch (`apps-extract`) was the fleet's sunset shelf where
retired, paused, and archived apps were kept labeled and bounded (`archive/`),
while `main` held the legacy monorepo content. That branch was deleted
2026-09-27; the current shelf location is unresolved. If you swap
PhenoApps out, the fleet loses the one place where absorbed apps and retired
apps are provably accounted for instead of silently scattered.

## Bound Prompts

| Date | Source | File | Tag |
| ---- | ------ | ---- | --- |

_No bindings captured yet — this repo was unindexed until this triad was
authored (WBS A3.3, 2026-09-27)._

## Bound Plans

| Date | Source | File | Status |
| ---- | ------ | ---- | ------ |

## Bound Responses (specs, ideas, plans from agents)

| Date | Source | File | Kind |
| ---- | ------ | ---- | ---- |

## Boundary

See: [`docs/boundary/PhenoApps.md`](../boundary/PhenoApps.md)

## Ecosystem Role

Canonical application-collection parent: `projects/phenotype-apps.json`
disposition `KEEP_CANONICAL_PARENT`, `canonical_routing: true`, card
`rationale` ("large footprint requires boundary audits and child-level
provenance, not repository deletion or broad workspace flattening" — phrased
there as “ADR-023”; pointer gap in Open Questions).
GitHub: `KooshaPari/PhenoApps` (renamed from `phenotype-apps`), default
branch `apps-extract` (recorded pre-deletion — branch deleted 2026-09-27,
current default unverified), not archived, last push 2026-09-18. 14
occurrences of `phenotype-apps (apps/<name>/)` across 9 disposition-index
rows — 9 as `target:` fields, 5 as `absorbed_into:` (`:2354` conft,
`:2588`/`:4730` apisync, `:5229` subject, `:5257` melosviz) — (tracely ×2 on
**two** rows id=59 `:1068` + id=918 `:6032`; conft ×2 the only one-row pair;
apisync ×4 across **two** rows — `repo-Apisync-batch4` + `repo-Apisync`;
subject ×2 and melosviz ×2 one of each kind; testing-kit; tracera —
template `[/]`: 6 of the 14 omit the trailing slash (apisync `:4730`/`:4741`,
subject `:5229`/`:5240`, melosviz `:5257`/`:5268`); plus exactly 196 rows
targeting bare `phenotype-apps`).

## Open Questions

- Where did the `apps/<name>` children go after the 2026-09-16 pivot commit
  `355016f8`? **Evidence captured 2026-09-27, source since deleted**: the
  pre-deletion tree diff shows `apps/` deleted from that tree (root reduced
  to `archive/`) with children recorded on `absorb-sessionledger` +
  `absorb-researchledger` — those branches (plus `main-focalpoint-archive`,
  `apps-extract`) were then deleted and both commits return HTTP 422, so the
  open sequence is: recover the branches, then decide restore-vs-scope
  (see [`docs/cvp/PhenoApps.md`](../cvp/PhenoApps.md)).
- Where is the application-collection ADR-023 the card cites? (`docs/adr/`
  has ADR-004..007; `ADR-ECO-023` = SDK consolidation; `docs/monorepo-state/AGENTS.md:119` ADR-023
  = agent-effort governance, source not present.)
- Does the "Sunset shelf" GitHub description change the
  `KEEP_CANONICAL_PARENT` disposition, or is it a temporary face of the same
  canonical parent?
- Propagate the `phenotype-apps` → `PhenoApps` rename into `gh_url` and
  target strings, or keep riding the redirect?

## Change Log

| Date       | Change                                                                                                                                                                                                                                                     | Worklog                   |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| 2026-09-27 | Initial binding — first intent doc for this repo (authored triad, WBS A3.3)                                                                                                                                                                                | `docs/cvp/PhenoApps.md`   |
| 2026-09-27 | Kilo round 2: ADR-023 re-attributed to the card (+ pointer-gap OQ), children question answered, row count corrected, `device: windows` annotated                                                                                                           | PR #585 review round      |
| 2026-09-27 | Kilo round 3: gate evidence re-labeled pre-deletion (holder branches deleted 22:04Z; commits 422), row-coverage arithmetic fixed (apisync spans two rows; 196 exact), ADR-023 cite path qualified, `device:` comment cites the define-the-vocabulary lines | PR #584/#585 review round |
| 2026-09-27 | Kilo round 4: shelf statement past-tense + current location unresolved; arithmetic split into 9 `target` + 5 `absorbed_into` fields with tracely on two rows (id=59/918), conft named the only one-row pair                                                | PR #584 review round      |
| 2026-09-27 | Kilo round 5: slash-template note added to the Ecosystem Role paragraph (5 of the 14 — apisync `:4730`, subject `:5229`/`:5240`, melosviz `:5257`/`:5268`)                                                                                                 | PR #584 review round      |
| 2026-09-29 | Kilo round 7: slash-template count 5 → 6 (`:4741` added; 8 slash / 6 no-slash verified by script)                                                                                                                                                          | PR #584 review round      |
