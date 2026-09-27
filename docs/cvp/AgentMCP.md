---
repo: "AgentMCP"
aliases: ["agentmcp"]
status: "shipped"
last_verified: "2026-09-27"
owner: "kooshapari"
build_deploy_status: "absorbed"
---

# CVP — AgentMCP

## Identity

AgentMCP was the fleet's **MCP (Model Context Protocol) client hub** — the
agent ↔ MCP-directory ↔ tools surface that let Phenotype agents discover and
call MCP servers. Its identity today survives as the **hexagonal
`agentmcp-hex` package inside `phenotype-python-sdk`**: extracted from
`McpKit/python/agentmcp/` v0.x.x → 0.3.0 with the hexagonal DDD structure
preserved, shipped as a P1 patch per the McpKit absorption audit
(`phenotype-python-sdk#21`, merged 2026-06-19), while the higher-level MCP
_patterns_ were routed to Agentora per the ADR-017/019 retirement wave
(2026-06-17/18). What you would lose without this identity: the Python SDK's
MCP client slice — an agent with no protocol-facing directory/tools ports.

## Closest Viable Product

The AgentMCP CVP is **a Python consumer that can**:

1. `import` the `agentmcp-hex` package from an installed
   `phenotype-python-sdk`.
2. Wire an agent to an MCP server through the preserved hexagonal ports
   (agent, directory, tools) — the same ports that existed in
   `McpKit/python/agentmcp/`.
3. Rely on the P1 patch lineage (bugfixes landed with the extraction, not a
   verbatim copy).
4. Trace the provenance back through the registry notes to the original
   0.3.0 source (`registry/disposition-index.json` extraction row +
   `docs/intent/agentmcp-hex.md` / `docs/boundary/agentmcp-hex.md`).

That slice shipped on 2026-06-19 — this CVP documents the shipped state and
the retirement of the standalone repo.

## In CVP (must ship in this slice)

- **`agentmcp-hex` package** in `phenotype-python-sdk/packages/agentmcp-hex/`
  with the hexagonal DDD structure intact (ports not flattened).
- **P1 patch behavior** from the McpKit absorption audit carried into the
  package.
- **Provenance chain**: disposition-index extraction row (source
  `McpKit/python/agentmcp/`, target package, PR reference) + the
  `agentmcp-hex` intent/boundary triad in the registry.
- **Pattern hand-off documented**: which MCP patterns went to Agentora and
  which stayed in the package (see Open Questions — Agentora is currently
  unreachable).

## Post-CVP (defer until CVP is live)

- **Agentora pattern integration**: richer MCP orchestration patterns were
  routed to Agentora (registry note `target: Agentora`); resuming that
  integration requires Agentora to be reachable again.
- **TypeScript / Go MCP clients**: explicitly `NO_MERIT` scaffold
  placeholders per ECOSYSTEM_MAP (never implemented; do not revive).
- **A dedicated `agentmcp-hex` CVP**: the package has its own
  intent/boundary docs (`docs/intent/agentmcp-hex.md`,
  `docs/boundary/agentmcp-hex.md`) and may deserve a first-class CVP if the
  SDK's MCP slice grows.

## Anti-CVPs

| Looks like AgentMCP CVP      | Actually lives in                           | Why                                                              |
| ---------------------------- | ------------------------------------------- | ---------------------------------------------------------------- |
| McpKit Python framework      | retired (ADR-017/019)                       | Superseded 2026-06-17; do not add new dependents.                |
| PhenoMCP Rust/Go MCP library | retired (ADR-017/019)                       | Superseded alongside McpKit in the same wave.                    |
| `cheap-llm-mcp` runtime CLI  | retired (ADR-017/019)                       | Runtime CLI strand of the retirement; absorbed where needed.     |
| MCP _server_ hosting         | `PhenoMCPServers`                           | AgentMCP was the client side; servers are a separate runtime.    |
| MCP orchestration patterns   | `Agentora` (registry target, currently 404) | Patterns were routed out of AgentMCP during the absorption.      |
| Go/TypeScript MCP SDKs       | scaffold placeholders (`NO_MERIT`)          | Never implemented; reviving them would contradict ECOSYSTEM_MAP. |

## Registry reality (as of 2026-09-27)

- **No standalone repository**: `KooshaPari/AgentMCP` returns 404, no match
  in `gh repo list` (53 visible repos), no `projects/AgentMCP.json` card —
  unlike peers, AgentMCP has no card at all.
- **Disposition evidence is note-only**: the extraction row in
  `registry/disposition-index.json` (`python/agentmcp` →
  `phenotype-python-sdk/packages/agentmcp-hex`, PR `phenotype-python-sdk#21`
  merged 2026-06-19) and the ECOSYSTEM_MAP retirement note ("AgentMCP
  patterns → Agentora") are the system of record.
- **The pattern target is also unreachable**: `KooshaPari/Agentora` returns
  404 as of 2026-09-27, so the pattern lineage currently points at a repo
  that no longer exists on GitHub.

## Open Questions

- **Tombstone or re-point**: should the AgentMCP disposition rows be given an
  explicit tombstone (as with `repo-phenotype-config` / `repo-kvirtualdesktop-core`)
  now that neither AgentMCP nor Agentora is on GitHub?
- **Where do the MCP patterns live?** Agentora was the routed target
  (`queue-repo-agentora` row says canonical, `repo-Agentora` row says
  `TOO_LARGE_RETIRE` with target `pheno (crates/agentora)` — contradictory
  even before the 404). Resolve the contradiction in a registry pass.
- **Does `agentmcp-hex` get its own CVP?** If the SDK's MCP slice is a live
  product, promote its triad to first-class.

## Change Log

| Date       | Change                                                                                      | Worklog                 |
| ---------- | ------------------------------------------------------------------------------------------- | ----------------------- |
| 2026-09-27 | Initial CVP (WBS A3.2). Documents shipped `agentmcp-hex` slice + standalone-repo retirement | PHENOREG-FORWARD-WBS A3 |
