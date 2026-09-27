---
repo: "AgentMCP"
aliases: ["agentmcp"]
role: absorbed-mcp-client-hub
status: active
last_verified: 2026-09-27
bound_prompts: 21
bound_plans: 0
bound_responses: 0
device: macbook
---

# Intent — AgentMCP

## Intent Statement

Preserve the fleet's MCP client capability as the hexagonal `agentmcp-hex` package inside `phenotype-python-sdk` — agent, MCP-directory, and tool ports intact (DDD preserved from `McpKit/python/agentmcp/` v0.x.x → 0.3.0, shipped as a P1 patch per the McpKit absorption audit, `phenotype-python-sdk#21` merged 2026-06-19) — while the higher-level MCP _patterns_ were routed to Agentora during the ADR-017/019 retirement wave (2026-06-17/18). The standalone AgentMCP repository is retired; what the fleet must not lose is the Python SDK's MCP client slice: an agent with protocol-facing directory/tools ports.

## Bound Prompts

| Date | Source      | File                                                           | Tag            |
| ---- | ----------- | -------------------------------------------------------------- | -------------- |
| ?    | claude-code | `docs/curated-prompts/claude-code/unknown/9c7fd03d8b6603bf.md` | policy-setting |
| ?    | claude-code | `docs/curated-prompts/claude-code/unknown/b2af4e0a2f2a5885.md` | policy-setting |
| ?    | claude-code | `docs/curated-prompts/claude-code/unknown/84463a2ed65973d6.md` | bugfix         |
| ?    | claude-code | `docs/curated-prompts/claude-code/unknown/2fa5fd35fac94b68.md` | implementation |
| ?    | claude-code | `docs/curated-prompts/claude-code/unknown/a24db2bf85373a23.md` | narrative      |
| ?    | claude-code | `docs/curated-prompts/claude-code/unknown/f9f90d8d94147882.md` | narrative      |
| ?    | claude-code | `docs/curated-prompts/claude-code/unknown/c25e17842827ad52.md` | implementation |
| ?    | claude-code | `docs/curated-prompts/claude-code/unknown/a8e183dcd8ba605c.md` | implementation |
| ?    | claude-code | `docs/curated-prompts/claude-code/unknown/240aa085be832a14.md` | implementation |
| ?    | claude-code | `docs/curated-prompts/claude-code/unknown/8a7415d679c51227.md` | narrative      |
| ?    | claude-code | `docs/curated-prompts/claude-code/unknown/512522d9e7745c14.md` | bugfix         |
| ?    | claude-code | `docs/curated-prompts/claude-code/unknown/19c46ccb769bbfaa.md` | implementation |
| ?    | claude-code | `docs/curated-prompts/claude-code/unknown/ca584a85e4049e2f.md` | bugfix         |
| ?    | claude-code | `docs/curated-prompts/claude-code/unknown/6d69cf05325bc58e.md` | bugfix         |
| ?    | claude-code | `docs/curated-prompts/claude-code/unknown/c0bf11cdffc7e5c9.md` | bugfix         |
| ?    | claude-code | `docs/curated-prompts/claude-code/unknown/57e657eaf6d2f7b1.md` | policy-setting |
| ?    | claude-code | `docs/curated-prompts/claude-code/unknown/19923724c837aee5.md` | policy-setting |
| ?    | claude-code | `docs/curated-prompts/claude-code/unknown/b0dcde9249e072a6.md` | repo-defining  |
| ?    | claude-code | `docs/curated-prompts/claude-code/unknown/d1b1506a6f097f26.md` | repo-defining  |
| ?    | claude-code | `docs/curated-prompts/claude-code/unknown/6e8958f1831db38e.md` | narrative      |
| ?    | claude-code | `docs/curated-prompts/claude-code/unknown/ed442018cd0bcabb.md` | implementation |

## Bound Plans

| Date | Source | File | Status |
| ---- | ------ | ---- | ------ |

## Bound Responses (specs, ideas, plans from agents)

| Date | Source | File | Kind |
| ---- | ------ | ---- | ---- |

## Boundary

See: [`docs/boundary/AgentMCP.md`](../boundary/AgentMCP.md)

## Ecosystem Role

Legacy MCP client hub, retired 2026-06-17/18 per ADR-017/019: Py package lives on as `phenotype-python-sdk/packages/agentmcp-hex` (extraction row in `registry/disposition-index.json`, PR `phenotype-python-sdk#21`); MCP patterns routed to Agentora (ECOSYSTEM_MAP note; also listed in the superseded cohort). No standalone repository exists: `KooshaPari/AgentMCP` returns 404 and there is no `projects/AgentMCP.json` card — the disposition notes plus `docs/intent/agentmcp-hex.md` / `docs/boundary/agentmcp-hex.md` are the system of record.

## Open Questions

- **Pattern target unreachable**: Agentora (`KooshaPari/Agentora`) also returns 404 as of 2026-09-27, and the disposition rows contradict each other (`queue-repo-agentora` says canonical; `repo-Agentora` says `TOO_LARGE_RETIRE` targeting `pheno (crates/agentora)`). Resolve before the next boundary review.
- **Tombstone or re-point**: should the AgentMCP disposition rows get an explicit tombstone (as `repo-phenotype-config` did) now that neither AgentMCP nor Agentora is on GitHub?
- **Does `agentmcp-hex` get its own first-class CVP?** It already has its own intent/boundary triad.

## Change Log

| Date       | Change                                                                                               | Worklog                                                    |
| ---------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| 2026-06-17 | Initial binding (L7-001 sweep)                                                                       | `worklogs/L7-001-intent-boundary-curation-2026-06-17.json` |
| 2026-09-27 | Intent statement, ecosystem role, and open questions filled (authored triad: `docs/cvp/AgentMCP.md`) | PHENOREG-FORWARD-WBS A3.2 / C3.3                           |
