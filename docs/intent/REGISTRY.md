# Bound Repos

This index is the master list of repositories carrying L7-001 sweep bindings — row-vs-sweep deltas are open (see the Open reconciliation note below: 86 rows = 82 case-folded unique repos with same-repo alias pairs ruled case-by-case (2 ruled, candidates unruled — no settled count; see note); 12 rows match no `docs/intent/` file and 3 more only under a name variant); doc-only CVP triads are indexed by `docs/cvp/README.md` instead.

> **L7-001 sweep — 2026-06-17:** 45,091 curated records (merged-unique corpus figure — phrasing corrected 2026-09-29, see Open reconciliation note below) bound to 82 repos across Mac + Windows prompt histories from four of the corpus's seven partitions (claude-code, codex, cursor-agent, forge; partition layout and sources list: `docs/registries.md:65`, `docs/registries.md:83` — the droid, aider, and other partitions hold zero kept records per the table reconciliation below). The Curation sources table below itemizes kept records per contributing source: its four rows sum to 45,427 raw (41,585 Mac + 3,842 Win) and dedup by exactly 336 (−322 Mac, −13 Win, −1 cross-OS) onto merged_unique 45,091 — so droid/aider/other contributed no kept records (any nonzero kept set would require a fifth row for the sums to reach the total). The previous placeholders in this file have been replaced with the actual bindings from the sweep.
>
> **CVP triad registration — 2026-09-27:** the `AuthKit` / `AgentMCP` /
> `PhenoApps` CVP doc triads (`docs/cvp/` + `docs/intent/` + `docs/boundary/`,
> PR #585) are authored curation, separate from this sweep table. Only
> `PhenoApps` lacks a table row; `AuthKit` (`:47`, 139 intents) and `AgentMCP`
> (`:105`, 2 intents) are sweep-derived rows with real bindings — the zero-
> binding property applies to the `PhenoApps` CVP docs only.
>
> **Open reconciliation (both deltas):** (1) **82 vs 86 rows** — L7-001 above
> binds 82 repos (2026-06-17); the heading reads 86 rows. Case-folding gives
> 82 unique + 4 case-variant pairs — `FocalPoint`/`focalpoint` (`:45`/`:69`), `agileplus`/
> `AgilePlus` (`:51`/`:55`), `byteport`/`BytePort` (`:56`/`:63`), `Phenotype-Terrain`/
> `phenotype-terrain` (`:81`/`:84`) — but same-repo pairs beyond case folding sit in
> the table too. Ruled: `phenoErrors` (`:87`) = `phenotype-errors` (`:74`) (alias note
> `projects/pheno-errors.json:22`), and `HeliosCLI` (`:62`) = `helios-cli` (`:65`)
> (disposition `registry/disposition-index.json:1175`; dated live probe 2026-10-01:
> `gh api repos/KooshaPari/helios-cli --jq .name` → `HeliosCLI`). Unruled candidates: `WSM` (`:120`) ~ `WorldSphereMod` (`:86`, only the
> latter has an intent doc), and `BytePort-Worktree` (`:114`) ~ `BytePort` (`:56`/`:63`).
> No settled unique count is claimed: case-folding gives 82 and each ruled pair
> lowers it; the delta stays open until every candidate is ruled and the table is
> diffed against the sweep's input repo list (or a re-run of L7-001). (2) **45,091 vs 24,213
> records** — L7-001's 45,091 is the merged-unique corpus figure (`:133`,
> 41,263 Mac + 3,829 Win before one cross-OS dedup — 41,263 + 3,829 − 1 = 45,091), while the 86 rows below sum to 24,213 (24,135
> intents + 28 plans + 50 responses) at time of writing: different bases
> (corpus-unique vs per-repo attribution), and whether every corpus record is
> attributable to one of these rows is the open question. Both numbers stand
> as recorded until reconciled.

## Canonical bound repos (86)

| Repo                    | Intents | Plans | Responses | First seen | Last seen |
| ----------------------- | ------- | ----- | --------- | ---------- | --------- |
| phenotype-registry      | 18119   | 9     | 8         | 2025-08    | 2026-06   |
| phenoVibeproxy          | 1389    | 2     | 0         | 2025-08    | 2026-06   |
| Dino                    | 1228    | 0     | 17        | 2025-08    | 2026-06   |
| thegent                 | 747     | 1     | 0         | 2025-08    | 2026-06   |
| cliproxyapi-plusplus    | 401     | 3     | 0         | 2025-08    | 2026-06   |
| phenotype-journeys      | 368     | 0     | 0         | 2025-08    | 2026-06   |
| DINOForge-UnityDoorstop | 362     | 0     | 0         | 2025-08    | 2026-06   |
| FocalPoint              | 170     | 0     | 1         | 2025-08    | 2026-06   |
| vibeproxy               | 151     | 0     | 0         | 2025-08    | 2026-06   |
| AuthKit                 | 139     | 0     | 0         | 2025-08    | 2026-06   |
| bifrost                 | 134     | 0     | 0         | 2025-08    | 2026-06   |
| phenoRouterMonitor      | 108     | 0     | 0         | 2025-08    | 2026-06   |
| pheno-contracts         | 77      | 1     | 0         | 2025-08    | 2026-06   |
| agileplus               | 64      | 1     | 10        | 2025-08    | 2026-06   |
| phenoResearch           | 52      | 0     | 0         | 2025-08    | 2026-06   |
| pheno                   | 47      | 0     | 0         | 2025-08    | 2026-06   |
| helios-router           | 45      | 0     | 0         | 2025-08    | 2026-06   |
| AgilePlus               | 39      | 1     | 3         | 2025-08    | 2026-06   |
| byteport                | 39      | 0     | 0         | 2025-08    | 2026-06   |
| phenotype-tooling       | 37      | 1     | 4         | 2025-08    | 2026-06   |
| phenotype-omlx          | 31      | 0     | 0         | 2025-08    | 2026-06   |
| ResilienceKit           | 30      | 1     | 0         | 2025-08    | 2026-06   |
| phenotype-org-audits    | 30      | 0     | 0         | 2025-08    | 2026-06   |
| OmniRoute               | 26      | 2     | 0         | 2025-08    | 2026-06   |
| HeliosCLI               | 18      | 2     | 0         | 2025-08    | 2026-06   |
| BytePort                | 16      | 0     | 0         | 2025-08    | 2026-06   |
| PhenoDevOps             | 12      | 0     | 0         | 2025-08    | 2026-06   |
| helios-cli              | 12      | 0     | 0         | 2025-08    | 2026-06   |
| phenotype-dep-guard     | 11      | 0     | 0         | 2025-08    | 2026-06   |
| phenotype-infra         | 11      | 2     | 0         | 2025-08    | 2026-06   |
| PhenoProc               | 10      | 0     | 0         | 2025-08    | 2026-06   |
| focalpoint              | 10      | 0     | 0         | 2025-08    | 2026-06   |
| heliosApp               | 10      | 0     | 0         | 2025-08    | 2026-06   |
| helioscope              | 10      | 0     | 0         | 2025-08    | 2026-06   |
| Civis                   | 9       | 0     | 3         | 2025-08    | 2026-06   |
| pheno-otel              | 9       | 0     | 0         | 2025-08    | 2026-06   |
| phenotype-errors        | 9       | 0     | 0         | 2025-08    | 2026-06   |
| ObservabilityKit        | 8       | 0     | 0         | 2025-08    | 2026-06   |
| NetScript               | 7       | 0     | 0         | 2025-08    | 2026-06   |
| KaskMan                 | 7       | 0     | 0         | 2025-08    | 2026-06   |
| HeliosLab               | 7       | 0     | 0         | 2025-08    | 2026-06   |
| HexaKit                 | 7       | 0     | 0         | 2025-08    | 2026-06   |
| KodeVibe                | 7       | 0     | 0         | 2025-08    | 2026-06   |
| Phenotype-Terrain       | 6       | 0     | 0         | 2025-08    | 2026-06   |
| phenotype-org           | 6       | 0     | 0         | 2025-08    | 2026-06   |
| Authvault               | 6       | 0     | 0         | 2025-08    | 2026-06   |
| phenotype-terrain       | 5       | 0     | 0         | 2025-08    | 2026-06   |
| PhenoProject            | 5       | 0     | 0         | 2025-08    | 2026-06   |
| WorldSphereMod          | 6       | 2     | 4         | 2025-08    | 2026-06   |
| phenoErrors             | 1       | 0     | 0         | 2025-08    | 2026-06   |
| Conft                   | 4       | 0     | 0         | 2025-08    | 2026-06   |
| Eventra                 | 4       | 0     | 0         | 2025-08    | 2026-06   |
| Apisync                 | 4       | 0     | 0         | 2025-08    | 2026-06   |
| KlipDot                 | 3       | 0     | 0         | 2025-08    | 2026-06   |
| Tokn                    | 3       | 0     | 0         | 2025-08    | 2026-06   |
| Tracera                 | 3       | 0     | 0         | 2025-08    | 2026-06   |
| KWatch                  | 3       | 0     | 0         | 2025-08    | 2026-06   |
| phenoWater              | 3       | 0     | 0         | 2025-08    | 2026-06   |
| Agentora                | 3       | 0     | 0         | 2025-08    | 2026-06   |
| phenotype-bus           | 3       | 0     | 0         | 2025-08    | 2026-06   |
| Benchora                | 3       | 0     | 0         | 2025-08    | 2026-06   |
| Eidolon                 | 3       | 0     | 0         | 2025-08    | 2026-06   |
| pheno-vessel            | 2       | 0     | 0         | 2025-08    | 2026-06   |
| pheno-types             | 2       | 0     | 0         | 2025-08    | 2026-06   |
| PhenoPlugins            | 2       | 0     | 0         | 2025-08    | 2026-06   |
| phenotype-python-sdk    | 2       | 0     | 0         | 2025-08    | 2026-06   |
| KDesktopVirt            | 2       | 0     | 0         | 2025-08    | 2026-06   |
| AgentMCP                | 2       | 0     | 0         | 2025-08    | 2026-06   |
| PhenoKits               | 2       | 0     | 0         | 2025-08    | 2026-06   |
| Portage                 | 2       | 0     | 0         | 2025-08    | 2026-06   |
| PolicyStack             | 2       | 0     | 0         | 2025-08    | 2026-06   |
| phenodocs               | 2       | 0     | 0         | 2025-08    | 2026-06   |
| PhenoSpec               | 2       | 0     | 0         | 2025-08    | 2026-06   |
| FenotypeIO              | 2       | 0     | 0         | 2025-08    | 2026-06   |
| PhenoHandbook           | 2       | 0     | 0         | 2025-08    | 2026-06   |
| AppGen                  | 1       | 0     | 0         | 2025-08    | 2026-06   |
| BytePort-Worktree       | 1       | 0     | 0         | 2025-08    | 2026-06   |
| CoreSDK                 | 1       | 0     | 0         | 2025-08    | 2026-06   |
| planify                 | 1       | 0     | 0         | 2025-08    | 2026-06   |
| nora                    | 1       | 0     | 0         | 2025-08    | 2026-06   |
| nugget                  | 1       | 0     | 0         | 2025-08    | 2026-06   |
| quartz                  | 1       | 0     | 0         | 2025-08    | 2026-06   |
| WSM                     | 1       | 0     | 0         | 2025-08    | 2026-06   |
| thegent-landing         | 2       | 0     | 0         | 2025-08    | 2026-06   |
| cheaptalk               | 1       | 0     | 0         | 2025-08    | 2026-06   |
| sharecli                | 1       | 0     | 0         | 2025-08    | 2026-06   |

## Curation sources

| Source           | Records kept (Mac) | Records kept (Win) | Drop reasons                            |
| ---------------- | -----------------: | -----------------: | --------------------------------------- |
| claude-code      |             27,809 |              3,252 | slash-command-only, single-word-confirm |
| codex            |             13,757 |                578 | single-word-confirm, slash-command-only |
| cursor-agent     |                  7 |                 12 | single-word-confirm                     |
| forge            |                 12 |                  0 | —                                       |
| **TOTAL unique** |         **41,263** |          **3,829** | **merged_unique=45,091**                |

## Pending binding (scraped but not yet bound)

Records that don't have a project context, or whose project context is to a directory we don't recognise as a repo, end up in `docs/curated-prompts/_orphan/`. The biggest orphan category is `/Users/&lt;REDACTED&gt;/CodeProjects/Phenotype/repos` (~10k records) which maps to the **phenotype-registry** meta-repo (already bound, see row 1).

Weekly re-render (per ADR-024) will keep this file in sync.

## Repos explicitly out of scope

| Repo            | Reason                                                |
| --------------- | ----------------------------------------------------- |
| netweave-final2 | temp dir, scratch work, no upstream                   |
| archived-repos  | archive root, individual archived repos still tracked |
| examples        | not a real repo                                       |
| tests           | not a real repo                                       |

---

_Generated 2026-06-17 22:30 PDT by `scripts/render-per-repo.py` from `_bindings.json` (Mac+Win merged)._
_Worklog: `worklogs/L7-001-intent-boundary-curation-2026-06-17.json`_
_Refresh: `bash scripts/run-all.sh` then `bash scripts/run-windows.sh --incremental` then `python3 scripts/render-per-repo.py --out . --force`_
