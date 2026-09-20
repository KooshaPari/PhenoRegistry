---
repo: "BytePort"
aliases: ["byteport"]
role: product
status: active
last_verified: 2026-09-20
bound_prompts: 39
bound_plans: 0
bound_responses: 0
device: macbook
---

# Intent — byteport

## Intent Statement

BytePort exists to be the **local-first, open-source desktop deployment
application** for the Phenotype ecosystem. A user installs one signed
artifact, gets a native UI that talks to a local Go backend, and can
deploy, monitor, and update containerized workloads on their own
machine without depending on a cloud account or a separate web server.

The repo's core commitments:

1. **Desktop-first surface.** The user reaches for BytePort on their
   own machine, not in a browser tab. The Tauri 2 binary is the canonical
   entry point; the SvelteKit UI exists only inside the desktop shell.
2. **Local data sovereignty.** Deployment state, container logs, and
   credentials live in the desktop app's local data dir. No cloud
   roundtrip required for the CVP. Cloud sync is post-CVP.
3. **Lean transport.** The pure-Rust S3 presigner
   (`crates/byteport-transport/`) ships no AWS SDK and stays small
   enough that other Phenotype tools can adopt it without dragging in
   tokio / aws-sdk-s3 / tracing.
4. **Hardened desktop shell.** `tauri.conf.json` enforces CSP, COOP /
   COEP / CORP, HSTS, X-Frame-Options, X-Content-Type-Options,
   Referrer-Policy, and Permissions-Policy. The asset protocol scope
   is `$APPDATA` and `$APPLOCALDATA` only — never `["**"]`.
5. **Phenotype ecosystem citizenship.** Multi-cloud transport lives in
   `pheno-transport`. MCP server lives in `PhenoMCPServers`. Native
   sandboxing lives in `nanovms`. Agent-specific desktop shells live
   in each agent's own repo. BytePort stays out of all of those.

The thing BytePort *is not*: a generic web deploy UI (Coolify), a
proprietary SaaS (Server Compass), an agent runtime, or a CI server.
Those identities live elsewhere.

## Bound Prompts

| Date | Source | File | Tag |
| ---- | ------ | ---- | --- |
| 2025-10-09 | claude-code | `docs/curated-prompts/claude-code/2025-10/69393c8600a9c906.md` | implementation |
| 2025-10-09 | claude-code | `docs/curated-prompts/claude-code/2025-10/882a654e0c2390e2.md` | narrative |
| 2025-10-09 | claude-code | `docs/curated-prompts/claude-code/2025-10/38803cb91db53f6a.md` | implementation |
| 2025-10-09 | claude-code | `docs/curated-prompts/claude-code/2025-10/9715363cc2ce9d36.md` | narrative |
| 2025-10-09 | claude-code | `docs/curated-prompts/claude-code/2025-10/6cc7655a5a292196.md` | implementation |
| 2025-10-09 | claude-code | `docs/curated-prompts/claude-code/2025-10/807f8f31411abd72.md` | narrative |
| 2025-10-09 | claude-code | `docs/curated-prompts/claude-code/2025-10/d5b0fbc70b7e3ee0.md` | implementation |
| 2025-10-09 | claude-code | `docs/curated-prompts/claude-code/2025-10/bad281df980a82a6.md` | narrative |
| 2025-10-09 | claude-code | `docs/curated-prompts/claude-code/2025-10/872289259b291f04.md` | bugfix |
| 2025-10-09 | claude-code | `docs/curated-prompts/claude-code/2025-10/211c7e67edec7d20.md` | implementation |
| 2025-10-09 | claude-code | `docs/curated-prompts/claude-code/2025-10/1145080efcc84af6.md` | narrative |
| 2025-10-09 | claude-code | `docs/curated-prompts/claude-code/2025-10/4a5e07fc40be76da.md` | narrative |
| 2025-10-10 | claude-code | `docs/curated-prompts/claude-code/2025-10/3c5469fb32889c5f.md` | narrative |
| 2025-10-10 | claude-code | `docs/curated-prompts/claude-code/2025-10/2151e5e7a675edd8.md` | narrative |
| 2025-10-10 | claude-code | `docs/curated-prompts/claude-code/2025-10/378490a489ee87eb.md` | implementation |
| 2025-10-10 | claude-code | `docs/curated-prompts/claude-code/2025-10/a9ee012216b4915c.md` | implementation |
| 2025-10-10 | claude-code | `docs/curated-prompts/claude-code/2025-10/7c019cf89ace4dd1.md` | narrative |
| 2025-10-11 | claude-code | `docs/curated-prompts/claude-code/2025-10/742247306f81da3b.md` | implementation |
| 2025-10-11 | claude-code | `docs/curated-prompts/claude-code/2025-10/b3d29bb5628828b0.md` | narrative |
| 2025-10-11 | claude-code | `docs/curated-prompts/claude-code/2025-10/0b2b34d797a43546.md` | narrative |
| 2025-10-08 | codex | `docs/curated-prompts/codex/2025-10/2e5bb0b6e0e4db1e.md` | implementation |
| 2025-10-08 | codex | `docs/curated-prompts/codex/2025-10/001866478e2e5b4c.md` | narrative |
| 2025-10-08 | codex | `docs/curated-prompts/codex/2025-10/eb9467d118cbdb85.md` | narrative |
| 2025-10-08 | codex | `docs/curated-prompts/codex/2025-10/9fe7f330a734004e.md` | policy-setting |
| 2025-10-08 | codex | `docs/curated-prompts/codex/2025-10/fb143a58ad9a843c.md` | repo-defining |
| 2025-10-08 | codex | `docs/curated-prompts/codex/2025-10/9743ff7835d466fe.md` | repo-defining |
| 2025-10-09 | codex | `docs/curated-prompts/codex/2025-10/12b1a4e94e6c5811.md` | bugfix |
| 2025-10-09 | codex | `docs/curated-prompts/codex/2025-10/904a3fc698cfcfca.md` | bugfix |
| 2025-10-09 | codex | `docs/curated-prompts/codex/2025-10/538a6d25ef14a93c.md` | implementation |
| 2025-10-09 | codex | `docs/curated-prompts/codex/2025-10/346a5aa4612a5609.md` | narrative |
| 2025-10-10 | codex | `docs/curated-prompts/codex/2025-10/8e651db4df95f230.md` | bugfix |
| 2025-10-10 | codex | `docs/curated-prompts/codex/2025-10/c78691cde6d00b2c.md` | narrative |
| 2025-10-10 | codex | `docs/curated-prompts/codex/2025-10/c2ffb59df07cfa54.md` | narrative |
| 2025-10-10 | codex | `docs/curated-prompts/codex/2025-10/5dc37fa674744aa3.md` | implementation |
| 2025-10-19 | codex | `docs/curated-prompts/codex/2025-10/f3c84ccbfe85f491.md` | narrative |
| 2025-10-19 | codex | `docs/curated-prompts/codex/2025-10/62e78d48bdd9c8bd.md` | narrative |
| 2026-04-30 | codex | `docs/curated-prompts/codex/2026-04/8f2a35f28477fe4e.md` | implementation |
| ? | ? | `c352cb811a77d357.md` (not rendered) | ? |
| ? | ? | `d58af7fd4a88eb2c.md` (not rendered) | ? |

## Bound Plans

| Date | Source | File | Status |
| ---- | ------ | ---- | ------ |

## Bound Responses (specs, ideas, plans from agents)

| Date | Source | File | Kind |
| ---- | ------ | ---- | ---- |

## Boundary

See: [`docs/boundary/BytePort.md`](../boundary/BytePort.md)

## CVP

See: [`docs/cvp/BytePort.md`](../cvp/BytePort.md)

## Ecosystem Role

BytePort is the canonical desktop deployment application in the
Phenotype ecosystem. It owns the local-machine deploy / monitor / update
surface for containerized workloads and ships the reusable pure-Rust
S3 presigner that other Phenotype tools depend on. It deliberately
stays out of multi-cloud transport, MCP server hosting, native
sandboxing, and per-agent desktop shells — each of those identities
lives in its own repo.

See [`docs/ECOSYSTEM_MAP_REALIGNMENT.md`](../ECOSYSTEM_MAP_REALIGNMENT.md)
for the broader ecosystem context.

## Open Questions

- **Mobile target scope**: is mobile in scope for a future CVP, or is
  desktop the only target forever? Mobile changes the transport story
  (no local Podman daemon on iOS).
- **`byteport-dag` necessity**: the DAG foundation crate is referenced
  from `byteport-cli` but not from the desktop binary. Confirm it
  belongs in the CVP or move it post-CVP.
- **`backend/bytebridge/` removal**: legacy Go module, no callers. Remove
  in a follow-up cleanup PR.

## Change Log

| Date | Change | Worklog |
| ---- | ------ | ------- |
| 2026-06-17 | Initial binding (L7-001 sweep) | `worklogs/L7-001-intent-boundary-curation-2026-06-17.json` |
| 2026-09-20 | Filled intent statement and added CVP cross-link | this commit |
