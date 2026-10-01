---
repo: "AgentMCP"
aliases: ["agentmcp"]
role: extracted-python-package
status: active
last_verified: 2026-09-27
bound_prompts: 21
bound_plans: 0
bound_responses: 0
device: macbook
---

# Intent — AgentMCP

## Intent Statement

Preserve the fleet's extracted MCP-side package as the hexagonal `agentmcp-hex` package inside `phenotype-python-sdk` — scoped by the package triad as the deterministic hex-grid testing harness (exact-decimal math, 16-task fleet, CI integration), extracted with "hexagonal DDD pattern preserved" from `McpKit/python/agentmcp/` v0.x.x → 0.3.0 as a P1 patch per the McpKit absorption audit (disposition row id=54, `phenotype-python-sdk#21` merged 2026-06-19) — while the higher-level MCP _patterns_ were routed to Agentora during the ADR-017/019 retirement wave (vendored `docs/specs/pheno-specs/adrs/017-mcp-polyrepo-boundaries.md` + `019-mcp-runtime-implementation-deps.md`, both 2026-06-17; absorption-audit merge / `relocated_date` 2026-06-18 per `disposition-index.json:899`). The standalone AgentMCP repository is retired; what the fleet must not lose is the extracted package and its provenance chain. Whether MCP client ports (the pre-extraction surface) survived inside the package is an open question: the package records define the harness scope only.

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

Legacy MCP-side package, retired in the vendored-ADR-017/019 wave (dates: ADRs 2026-06-17, absorption-audit merge 2026-06-18): Py package lives on as `phenotype-python-sdk/packages/agentmcp-hex` (extraction row in `registry/disposition-index.json`, PR `phenotype-python-sdk#21`); MCP patterns routed to Agentora (`ECOSYSTEM_MAP.md:393`, Cluster L legacy paragraph — note AgentMCP has **no** entry in the §1 role tables nor in the Retirements/Merges cohort; the earlier "also listed in the superseded cohort" claim in this file was unsupported and is removed). No standalone repository exists: `KooshaPari/AgentMCP` returns 404 and there is no `projects/AgentMCP.json` card — the system of record is the disposition extraction row + the `ECOSYSTEM_MAP.md:393` note; the `agentmcp-hex` package triad (`docs/intent/agentmcp-hex.md`, `docs/boundary/agentmcp-hex.md`) scopes the package as a hex-grid harness and does **not** evidence MCP client capability (see Open Questions below).

## Open Questions

- **Package scope contradiction**: `docs/intent/agentmcp-hex.md` and `docs/boundary/agentmcp-hex.md` (the package triad) scope `agentmcp-hex` as a hex-grid testing harness, while the disposition extraction row frames the lift as an MCP client extraction with "hexagonal DDD pattern preserved." Port-level claims (agent / directory / tools) are not evidenced by package records — verify against the `phenotype-python-sdk` source before asserting MCP client capability.
- **Pattern target unreachable**: Agentora (`KooshaPari/Agentora`) also returns 404 as of 2026-09-27, and the disposition rows diverge on `fsm` (`live` vs `archived`) and `target` (`KooshaPari/Agentora` vs `pheno (crates/agentora)`) while both carry `disposition: TOO_LARGE_RETIRE` — `queue-repo-agentora` at `disposition-index.json:14153-14161` vs `repo-Agentora` at `:3486-3502` ("canonical" appears only in the queue-row note) — plus `projects/Agentora.json:19-21` = `KEEP_STANDALONE_PENDING_BOUNDARY_REVIEW`. Resolve before the next boundary review.
- **Tombstone or re-point**: should the AgentMCP disposition rows get an explicit tombstone? No usable model exists — the nearest candidate `repo-mcpkit-superseded` (`:1299-1310`) carries a verified-404 tombstone only in its note while its machine fields are `NEVER_EXISTED` (`:1302-1304`), and the `repo-phenotype-config` / `repo-kvirtualdesktop-core` rows are `J:NEVER_EXISTED` phantoms (`:3577-3582` / `:3561-3566`), not precedents for "existed, absorbed, now 404". Adopting a predecessor → absorbed → now-404 row model is a maintainer decision (disposition-index is frozen) — see `docs/cvp/AgentMCP.md` for the full comparison.
- **Does `agentmcp-hex` get its own first-class CVP?** It already has its own intent/boundary triad.

## Change Log

| Date       | Change                                                                                                                                                                                                                          | Worklog                                                    |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| 2026-06-17 | Initial binding (L7-001 sweep)                                                                                                                                                                                                  | `worklogs/L7-001-intent-boundary-curation-2026-06-17.json` |
| 2026-09-27 | Intent statement, ecosystem role, and open questions filled (authored triad: `docs/cvp/AgentMCP.md`)                                                                                                                            | PHENOREG-FORWARD-WBS A3.2 / C3.3                           |
| 2026-09-27 | Kilo round 3: both Agentora row ranges cited, tombstone OQ reframed (no usable model; note vs machine fields), hand-off wording matches record                                                                                  | PR #584/#585 review round                                  |
| 2026-09-27 | Kilo round 2: frontmatter role → `extracted-python-package` (no capability claim), unsupported cohort citation removed, system-of-record claim aligned with Open Questions, Agentora divergence + tombstone precedent corrected | PR #585 review round                                       |
