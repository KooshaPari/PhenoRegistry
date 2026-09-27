---
repo: "AgentMCP"
role: extracted-python-package
status: active
last_boundary_review: 2026-09-27
review_cadence: 30d
in_scope:
  - "agentmcp-hex package (hex-grid test harness scope per package triad; hexagonal DDD structure preserved per disposition note) in phenotype-python-sdk"
  - "P1 patch behavior from the McpKit absorption audit"
  - "provenance chain (disposition-index extraction row + this triad)"
out_of_scope:
  - "MCP server hosting (PhenoMCPServers — owner row contested: disposition-index.json:3014 is note prose 'DECLARE_SPINE/not absorbable' while the DSPI-13 row's machine fields at :3000-3023 are disposition B:WORKING / final_classification A:SPINE; vs :3440-3451 ABSORB into phenotype-tooling/crates/phench-mcp/)"
  - "MCP orchestration patterns (routed to Agentora — currently 404)"
  - "retired McpKit / PhenoMCP / cheap-llm-mcp (vendored docs/specs/pheno-specs/adrs/017-mcp-polyrepo-boundaries.md + 019-mcp-runtime-implementation-deps.md)"
  - "TypeScript / Go MCP clients (NO_MERIT scaffold placeholders)"
---

# Boundary — AgentMCP

## In Scope

- **`agentmcp-hex` package** (`phenotype-python-sdk/packages/agentmcp-hex/`) with the hexagonal DDD structure intact (disposition note: "hexagonal DDD pattern preserved"). Package triad scope: hex-grid test harness — deterministic decimal math, 16-task fleet, CI integration (`docs/intent/agentmcp-hex.md`, `docs/boundary/agentmcp-hex.md`).
- **P1 patch lineage** carried into the package (bugfixes landed with the extraction, not a verbatim copy).
- **Provenance chain**: disposition-index extraction row (source `McpKit/python/agentmcp/`, PR `phenotype-python-sdk#21` merged 2026-06-19) + `docs/intent/agentmcp-hex.md` / `docs/boundary/agentmcp-hex.md` + this triad.
- **Pattern hand-off disposition recorded**: the conflicting registry records over where MCP patterns live are enumerated in `docs/cvp/AgentMCP.md` Open Questions; the hand-off itself is unresolved (Agentora 404 — crossing below).

## Out of Scope

| Not here                                           | Lives in                                                                                                                                                                                                                                                                                                                                                                       | Reason                                                                                                             |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| MCP server hosting                                 | `PhenoMCPServers` — owner row contested (`disposition-index.json:3014` note prose `DECLARE_SPINE "not absorbable"` vs DSPI-13 machine fields `:3000-3023` `B:WORKING`/`A:SPINE`; vs `:3440-3451` ABSORB into `phenotype-tooling/crates/phench-mcp/`; card fields: `projects/PhenoMCPServers.json:7` status `queued`, `:11` disposition `ABSORB`, `:14` proposed_target `self`) | AgentMCP was the client side; servers are a separate runtime — routing stays provisional until the rows reconcile. |
| MCP orchestration patterns                         | `Agentora` (registry target; 404 as of 2026-09-27)                                                                                                                                                                                                                                                                                                                             | Patterns were routed out during the vendored ADR-017/019 wave.                                                     |
| McpKit framework                                   | retired (vendored `docs/specs/pheno-specs/adrs/017`+`019`)                                                                                                                                                                                                                                                                                                                     | Superseded 2026-06-17; no new dependents.                                                                          |
| PhenoMCP Rust/Go library                           | retired (same vendored ADR-017/019 wave)                                                                                                                                                                                                                                                                                                                                       | Superseded in the same wave.                                                                                       |
| `cheap-llm-mcp` runtime CLI                        | retired (same vendored ADR-017/019 wave)                                                                                                                                                                                                                                                                                                                                       | Runtime strand of the retirement.                                                                                  |
| Go/TypeScript MCP SDKs                             | scaffold placeholders (`NO_MERIT`)                                                                                                                                                                                                                                                                                                                                             | Never implemented; reviving contradicts ECOSYSTEM_MAP.                                                             |
| MCP client port claims (agent / directory / tools) | unresolved (needs `phenotype-python-sdk` source)                                                                                                                                                                                                                                                                                                                               | Package records define the hex-grid harness scope only; see Open Questions in `docs/cvp/AgentMCP.md`.              |

## Boundary Crossings

| Crossing                           | Direction                        | Surface                        | Status                                                                                                                                                                                     |
| ---------------------------------- | -------------------------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `agentmcp-hex` package consumption | phenotype-python-sdk → consumers | Python import                  | green (shipped, PR #21)                                                                                                                                                                    |
| McpKit → agentmcp-hex extraction   | McpKit → agentmcp-hex            | code lift (P1 patch)           | green (merged 2026-06-19)                                                                                                                                                                  |
| MCP pattern hand-off               | AgentMCP → Agentora              | documentation/pattern transfer | red (Agentora 404)                                                                                                                                                                         |
| Standalone repo disposition        | AgentMCP → registry rows         | tombstone notes                | amber (no usable tombstone model: nearest candidate `repo-mcpkit-superseded` carries its verified-404 tombstone only in the note, machine fields `NEVER_EXISTED` — see cvp Open Questions) |

## Last Boundary Review

**Date:** 2026-09-27
**Reviewer:** jcode agent (PHENOREG-FORWARD-WBS A3.2 / C3.3)
**Worklog / finding:** boundary authored from `registry/disposition-index.json` extraction row, ECOSYSTEM_MAP retirement note, vendored `docs/specs/pheno-specs/adrs/017`/`019` references, and live GitHub probes (AgentMCP + Agentora both 404).
**Decisions:**

- Standalone repository recorded as retired; capability lives in `agentmcp-hex` (own triad exists).
- Port-name claims removed from this triad (2026-09-27 review round): package records scope a hex-grid testing harness; whether MCP client ports survived is an Open Question, not an in-scope fact.
- Agentora pattern target recorded as red/unreachable pending disposition reconciliation.
- Frontmatter role set to `extracted-python-package` (kilo round 2, 2026-09-27). It replaces an earlier `absorbed-mcp-client-hub` value that only ever existed in this PR's uncommitted intermediate state (committed base at `976f30c` had `role: unknown`) — recorded here so a future reader does not hunt for a revert on `main`; the capability such a role name would assert is marked unresolved above.

**Next review:** 2026-10-27
