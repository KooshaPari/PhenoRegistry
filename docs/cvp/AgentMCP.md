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
Python client surface that let Phenotype agents discover and
call MCP servers. Its identity today survives as the **hexagonal
`agentmcp-hex` package inside `phenotype-python-sdk`**: extracted from
`McpKit/python/agentmcp/` v0.x.x → 0.3.0 with the hexagonal DDD structure
preserved, shipped as a P1 patch per the McpKit absorption audit
(`phenotype-python-sdk#21`, merged 2026-06-19), while the higher-level MCP
_patterns_ were routed to Agentora per the ADR-017/019 retirement wave
(`docs/specs/pheno-specs/adrs/017-mcp-polyrepo-boundaries.md` +
`019-mcp-runtime-implementation-deps.md`, both dated 2026-06-17; absorption-
audit merge / `relocated_date` 2026-06-18 per `disposition-index.json:899` —
not the ADR-017/019 rows in `docs/monorepo-state/AGENTS.md`, which map
different `settly-*`/`pheno-vessel-*` deprecations). What you would lose without this identity: the extracted
`agentmcp-hex` package and its provenance chain — the package triad scopes it
as the hex-grid testing harness (see Open Questions for the scope
contradiction).

## Closest Viable Product

The AgentMCP CVP is **a Python consumer that can**:

1. `import` the `agentmcp-hex` package from an installed
   `phenotype-python-sdk`.
2. Run the deterministic hex-grid testing harness and its 16-task fleet
   (the package triad's declared scope).
3. Rely on the P1 patch lineage (bugfixes landed with the extraction, not a
   verbatim copy).
4. Trace the provenance back through the registry notes to the original
   0.3.0 source (`registry/disposition-index.json` extraction row +
   `docs/intent/agentmcp-hex.md` / `docs/boundary/agentmcp-hex.md`).

That slice shipped on 2026-06-19 — this CVP documents the shipped state and
the retirement of the standalone repo.

## In CVP (must ship in this slice)

- **`agentmcp-hex` package** in `phenotype-python-sdk/packages/agentmcp-hex/`
  with the hexagonal DDD structure intact (disposition note: "hexagonal DDD
  pattern preserved"; package triad scope: hex-grid test harness — see Open
  Questions).
- **P1 patch behavior** from the McpKit absorption audit carried into the
  package.
- **Provenance chain**: disposition-index extraction row (source
  `McpKit/python/agentmcp/`, target package, PR reference) + the
  `agentmcp-hex` intent/boundary triad in the registry.
- **Pattern hand-off disposition recorded**: the conflicting registry records
  over where MCP patterns live are enumerated and flagged (see Open
  Questions); the hand-off itself remains unresolved — Agentora is 404
  (crossing red).

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

| Looks like AgentMCP CVP      | Actually lives in                                                                                                                                                                          | Why                                                                                                                |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| McpKit Python framework      | retired (vendored `docs/specs/pheno-specs/adrs/017`+`019`)                                                                                                                                 | Superseded 2026-06-17; do not add new dependents.                                                                  |
| PhenoMCP Rust/Go MCP library | retired (same vendored ADR-017/019 wave)                                                                                                                                                   | Superseded alongside McpKit in the same wave.                                                                      |
| `cheap-llm-mcp` runtime CLI  | retired (same vendored ADR-017/019 wave)                                                                                                                                                   | Runtime CLI strand of the retirement; absorbed where needed.                                                       |
| MCP _server_ hosting         | `PhenoMCPServers` — disposition contested (`disposition-index.json:3014` DECLARE_SPINE "not absorbable" vs `:3440-3451` ABSORB into `phenotype-tooling/crates/phench-mcp/`; card `queued`) | AgentMCP was the client side; servers are a separate runtime — but the owner row is contested, see Open Questions. |
| MCP orchestration patterns   | `Agentora` (registry target, currently 404)                                                                                                                                                | Patterns were routed out of AgentMCP during the absorption.                                                        |
| Go/TypeScript MCP SDKs       | scaffold placeholders (`NO_MERIT`)                                                                                                                                                         | Never implemented; reviving them would contradict ECOSYSTEM_MAP.                                                   |

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

- **Package scope contradiction**: the package triad
  (`docs/intent/agentmcp-hex.md`, `docs/boundary/agentmcp-hex.md`) scopes
  `agentmcp-hex` as a hex-grid testing harness — deterministic decimal math,
  16-task fleet, CI integration — while the disposition extraction row frames the same
  lift as an MCP client extraction with "hexagonal DDD pattern preserved."
  Whether any MCP client ports survived inside the package is not resolvable
  from registry records; check the `phenotype-python-sdk` source before
  claiming MCP client capability anywhere.
- **Tombstone or re-point**: should the AgentMCP disposition rows be given an
  explicit tombstone? **No usable model exists.** The nearest candidate,
  `repo-mcpkit-superseded` (`disposition-index.json:1299-1310`), records a
  verified-404 tombstone **only in its note** (`:1306-1310`, "Tombstone
  closed 2026-06-23 (verified via gh api 404 + git clone --bare Repository not
  found)") while its machine fields read `disposition: NEVER_EXISTED` /
  `final_classification: J:NEVER_EXISTED` / `fsm: never_existed`
  (`:1302-1304`) — a note-only artifact directly contradicted by its own
  machine fields, same phantom class as `repo-phenotype-config` (`:3577-3582`)
  and `repo-kvirtualdesktop-core` (`:3561-3566`, both `J:NEVER_EXISTED`
  despite historical refs). AgentMCP needs a predecessor → absorbed → now-404
  row model that none of these express; adopting one is a maintainer decision
  (disposition-index is frozen) — not a citation to an existing row. Now that
  neither AgentMCP nor Agentora is on GitHub, an explicit tombstone or
  `gh_url` re-point remains the open choice.
- **Where do the MCP patterns live?** Both registry rows carry disposition
  `TOO_LARGE_RETIRE`; the real divergence is `fsm: live` vs `archived` and
  `target: KooshaPari/Agentora` vs `target: pheno (crates/agentora)` —
  `queue-repo-agentora` at `disposition-index.json:14153-14161` vs
  `repo-Agentora` at `:3486-3502` (both rows; "canonical" appears only inside
  the queue-row note, not as a competing disposition). A third record is in tension:
  `projects/Agentora.json:19-21` = `KEEP_STANDALONE_PENDING_BOUNDARY_REVIEW`
  ("Historic ABSORB -> pheno (crates/agentora) claims are not supported by
  source-level migration proof") — the best current evidence for where MCP
  patterns should live. Resolve all three in a registry pass.
- **Does `agentmcp-hex` get its own CVP?** If the SDK's MCP slice is a live
  product, promote its triad to first-class.

## Change Log

| Date       | Change                                                                                                                                                                                                                                            | Worklog                   |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| 2026-09-27 | Initial CVP (WBS A3.2). Documents shipped `agentmcp-hex` slice + standalone-repo retirement                                                                                                                                                       | PHENOREG-FORWARD-WBS A3   |
| 2026-09-27 | Review fixes: port-name claims removed (package records scope a hex-grid harness); scope contradiction added as Open Question                                                                                                                     | PR #585 review round      |
| 2026-09-27 | Kilo round 2: vendored ADR-017/019 paths + date split, tombstone precedent → `repo-mcpkit-superseded`, Agentora divergence stated precisely (+ card `:19-21`), PhenoMCPServers contested-owner note                                               | PR #585 review round      |
| 2026-09-27 | Kilo round 3: tombstone OQ reframed (no usable model — note vs machine fields contradiction), both Agentora row ranges cited, SPINE citation split (note prose vs DSPI-13 fields; card `:7`/`:11`/`:14`), pattern-hand-off wording matches record | PR #584/#585 review round |
