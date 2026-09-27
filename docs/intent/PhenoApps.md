---
repo: "PhenoApps"
aliases: ["phenotype-apps", "PhenotypeApps"]
role: application-parent
status: active
last_verified: 2026-09-27
bound_prompts: 0
bound_plans: 0
bound_responses: 0
device: windows
---

# Intent — PhenoApps

## Intent Statement

Act as the **canonical application-collection parent** (ADR-023): every
BLOCK-A application lives at `apps/<name>` behind an explicit child boundary,
arriving only through a verifiable lift — source lift, build verification,
and a named audit artifact — and the parent **never absorbs runtime,
governance, or library spines** (those stay in their own canonical repos).
The parent's second duty is retirement custody: the default branch
(`apps-extract`) is the fleet's sunset shelf where retired, paused, and
archived apps are kept labeled and bounded (`archive/`), while `main` retains
the legacy monorepo content until it is explicitly sorted. If you swap
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
disposition `KEEP_CANONICAL_PARENT`, `canonical_routing: true`, ADR-023
rationale ("large footprint requires boundary audits and child-level
provenance, not repository deletion or broad workspace flattening").
GitHub: `KooshaPari/PhenoApps` (renamed from `phenotype-apps`), default
branch `apps-extract`, not archived, last push 2026-09-18. Dozens of
disposition-index absorption rows target `phenotype-apps (apps/<name>/)`.

## Open Questions

- Where did the `apps/<name>` children go after the 2026-09-16 pivot commit
  `355016f8` (see [`docs/cvp/PhenoApps.md`](../cvp/PhenoApps.md))?
- Does the "Sunset shelf" GitHub description change the
  `KEEP_CANONICAL_PARENT` disposition, or is it a temporary face of the same
  canonical parent?
- Propagate the `phenotype-apps` → `PhenoApps` rename into `gh_url` and
  target strings, or keep riding the redirect?

## Change Log

| Date       | Change                                                                      | Worklog                 |
| ---------- | --------------------------------------------------------------------------- | ----------------------- |
| 2026-09-27 | Initial binding — first intent doc for this repo (authored triad, WBS A3.3) | `docs/cvp/PhenoApps.md` |
