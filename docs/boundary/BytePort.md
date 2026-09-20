---
repo: "BytePort"
role: product
status: active
last_boundary_review: 2026-09-20
review_cadence: 30d
in_scope:
  - Tauri 2.x desktop application (Rust + SvelteKit frontend)
  - Pure-Rust S3 presigner crate (`crates/byteport-transport/`)
  - Go 1.25 backend (`backend/byteport/`) — healthz + presign endpoints on port 8081
  - Astro docs frontend (marketing site)
  - Tightly-scoped asset protocol (Tauri-side, only APPDATA scopes)
out_of_scope:
  - Multi-cloud transport abstraction (lives in `pheno-transport`)
  - MCP server (lives in `PhenoMCPServers`)
  - Native sandboxing (lives in `nanovms`)
  - Per-agent desktop shells (lives in `thegent/desktop` etc.)
  - Cloud-hosted multi-tenant BytePort (post-CVP)
  - Mobile deployment targets (post-CVP)
---

# Boundary — BytePort

> Boundary file for BytePort. Updated 2026-09-20 with intent + CVP
> alignment. The pre-existing 2026-06-23 audit data (47/60 scorecard,
> BP-001 dead-code removal) is preserved below for review traceability.
>
> BytePort is correctly listed in [`ECOSYSTEM_MAP.md`](../../ECOSYSTEM_MAP.md)
> as active — under **product / app** (row 49) and **compute / infra
> subtree** (row 58). The earlier 2026-06-17 sweep output that listed
> it as superseded/archived was reclassified to active in
> [`ADR-ECO-022`](../../docs/adrs/ADR-ECO-022-compute-infra-subtree-registry-correction.md)
> on 2026-06-23; that reclassification is now reflected in the map.

## In Scope (2026-09-20 CVP-aligned)

1. **`frontend/web/src-tauri/`** — Tauri 2.x desktop binary (Rust)
   with a typed `IpcEnvelope<T>` JSON-RPC contract. Hardened
   `tauri.conf.json` (CSP, COOP/COEP/CORP, HSTS, X-Frame-Options,
   X-Content-Type-Options, Referrer-Policy, Permissions-Policy).
   Asset protocol scope is `["$APPDATA/uploads", "$APPDATA/cache",
   "$APPLOCALDATA/uploads", "$APPLOCALDATA/cache"]` only (not `["**"]`).
2. **`frontend/web/`** — SvelteKit 5 / Svelte 5 frontend. Renders inside
   the Tauri shell only; not served as a standalone web app.
3. **`crates/byteport-transport/`** — pure-Rust S3 presigner (no AWS
   SDK). Exposes a `Transport` trait and `S3UploadTransport` impl that
   the Tauri app uses directly. Small enough to be a reusable Phenotype
   dependency.
4. **`backend/byteport/`** — Go 1.25 HTTP backend with healthz + presign
   endpoints on port 8081. The CI matrix exercises Linux + macOS + Windows.
   This is the canonical Go module; `backend/bytebridge/` is unused.
5. **Astro docs** — marketing site at `apps/` (or similar root-level
   subdir).
6. **`tauri.conf.json`** — strict CSP, COOP/COEP/CORP, HSTS, X-Frame-
   Options, X-Content-Type-Options, Referrer-Policy, Permissions-
   Policy.

## Out of Scope

| Not here | Lives in | Reason |
| -------- | -------- | ------ |
| MCP server | `PhenoMCPServers` | MCP is a separate runtime |
| Native sandboxing | `nanovms` | Process isolation is a nanovms concern |
| thegent desktop shell | `thegent/desktop` | Each agent gets its own shell |
| Multi-cloud transport | `pheno-transport` | SOTA transport is in the SDK |
| Cloud-hosted multi-tenant BytePort | post-CVP | CVP is single-user local; cloud needs auth/billing |
| Mobile (iOS / Android) | post-CVP | No local Podman daemon on mobile; transport story changes |
| Fleet orchestration | post-CVP | CVP is one user, one machine |

## Boundary Crossings

| Crossing | Direction | Surface | Status |
| -------- | --------- | ------- | ------ |
| Tauri IPC → backend | this→other | JSON-RPC over HTTP (port 8081) | green |
| Tauri → S3 presigner | internal | `byteport_transport::S3UploadTransport` | green |
| Backend → S3 | this→cloud | AWS SDK / pure HTTP | green |
| Frontend → backend | this→other | fetch | green |
| Desktop → local FS | this→system | Tauri asset protocol (scoped) | green |
| Desktop → Podman / Docker | this→system | CLI invocation via Go backend | green |

## 71-Pillar Scorecard (2026-06-23, preserved)

**Score: 47/60 (78.3%)** — strong after BP-001 (removed -445 LOC of
dead code; hardened `tauri.conf.json`).

## Last Review

**Date:** 2026-06-23 (audit); 2026-09-20 (CVP alignment).
**Reviewer:** forge session (Phase 1 of `plans/2026-06-22-compute-infra-dag-v1.md`),
then this CVP/intent/boundary pass.
**Worklog / finding:** `phenotype-infra/worklog/2026-06-23-71-pillar-scorecard.md`
**Decisions:**
- BP-001 (dead code removal + tauri.conf.json hardening) MERGED (commit `ceb703df`)
  - Deleted: `src/ipc.rs`, `src/network.rs`, `src/adapters/`, `src/ports/`
  - Pruned: `aws-sdk-s3`, `tokio`, `tracing`, `async-trait`, `thiserror`,
    `url`, `tauri-plugin-os`, `mockall`
  - Hardened: `tauri.conf.json` identifier + CSP + scope + headers
- Open: BP-070 (keep or delete `vendor/aws-runtime`?)

**Next review:** 2026-10-20 (30d cadence from CVP alignment).
