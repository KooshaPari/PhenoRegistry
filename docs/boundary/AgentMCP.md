---
repo: "AgentMCP"
role: absorbed-mcp-client-hub
status: active
last_boundary_review: 2026-09-27
review_cadence: 30d
in_scope:
  - "agentmcp-hex package (hex-grid test harness scope per package triad; hexagonal DDD structure preserved per disposition note) in phenotype-python-sdk"
  - "P1 patch behavior from the McpKit absorption audit"
  - "provenance chain (disposition-index extraction row + this triad)"
out_of_scope:
  - "MCP server hosting (PhenoMCPServers)"
  - "MCP orchestration patterns (routed to Agentora — currently 404)"
  - "retired McpKit / PhenoMCP / cheap-llm-mcp (ADR-017/019)"
  - "TypeScript / Go MCP clients (NO_MERIT scaffold placeholders)"
---

# Boundary — AgentMCP

## In Scope

- **`agentmcp-hex` package** (`phenotype-python-sdk/packages/agentmcp-hex/`) with the hexagonal DDD structure intact (disposition note: "hexagonal DDD pattern preserved"). Package triad scope: hex-grid test harness — deterministic decimal math, 16-task fleet, CI integration (`docs/intent/agentmcp-hex.md`, `docs/boundary/agentmcp-hex.md`).
- **P1 patch lineage** carried into the package (bugfixes landed with the extraction, not a verbatim copy).
- **Provenance chain**: disposition-index extraction row (source `McpKit/python/agentmcp/`, PR `phenotype-python-sdk#21` merged 2026-06-19) + `docs/intent/agentmcp-hex.md` / `docs/boundary/agentmcp-hex.md` + this triad.
- **Pattern hand-off documented**: which MCP patterns went to Agentora (routed target currently 404) and which stayed in the package.

## Out of Scope

| Not here                                           | Lives in                                           | Reason                                                                                                |
| -------------------------------------------------- | -------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| MCP server hosting                                 | `PhenoMCPServers`                                  | AgentMCP was the client side; servers are a separate runtime.                                         |
| MCP orchestration patterns                         | `Agentora` (registry target; 404 as of 2026-09-27) | Patterns were routed out during the ADR-017/019 absorption.                                           |
| McpKit framework                                   | retired (ADR-017/019)                              | Superseded 2026-06-17; no new dependents.                                                             |
| PhenoMCP Rust/Go library                           | retired (ADR-017/019)                              | Superseded in the same wave.                                                                          |
| `cheap-llm-mcp` runtime CLI                        | retired (ADR-017/019)                              | Runtime strand of the retirement.                                                                     |
| Go/TypeScript MCP SDKs                             | scaffold placeholders (`NO_MERIT`)                 | Never implemented; reviving contradicts ECOSYSTEM_MAP.                                                |
| MCP client port claims (agent / directory / tools) | unresolved (needs `phenotype-python-sdk` source)   | Package records define the hex-grid harness scope only; see Open Questions in `docs/cvp/AgentMCP.md`. |

## Boundary Crossings

| Crossing                           | Direction                        | Surface                        | Status                            |
| ---------------------------------- | -------------------------------- | ------------------------------ | --------------------------------- |
| `agentmcp-hex` package consumption | phenotype-python-sdk → consumers | Python import                  | green (shipped, PR #21)           |
| McpKit → agentmcp-hex extraction   | McpKit → agentmcp-hex            | code lift (P1 patch)           | green (merged 2026-06-19)         |
| MCP pattern hand-off               | AgentMCP → Agentora              | documentation/pattern transfer | red (Agentora 404)                |
| Standalone repo disposition        | AgentMCP → registry rows         | tombstone notes                | amber (no explicit tombstone yet) |

## Last Boundary Review

**Date:** 2026-09-27
**Reviewer:** jcode agent (PHENOREG-FORWARD-WBS A3.2 / C3.3)
**Worklog / finding:** boundary authored from `registry/disposition-index.json` extraction row, ECOSYSTEM_MAP retirement note, ADR-017/019 references, and live GitHub probes (AgentMCP + Agentora both 404).
**Decisions:**

- Standalone repository recorded as retired; capability lives in `agentmcp-hex` (own triad exists).
- Port-name claims removed from this triad (2026-09-27 review round): package records scope a hex-grid testing harness; whether MCP client ports survived is an Open Question, not an in-scope fact.
- Agentora pattern target recorded as red/unreachable pending disposition reconciliation.

**Next review:** 2026-10-27
