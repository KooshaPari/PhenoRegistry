---
repo: "BytePort"
aliases: ["byteport"]
status: "active"
last_verified: "2026-09-20"
owner: "kooshapari"
build_deploy_status: "shipping"
---

# CVP — BytePort

## Identity

BytePort is the **only open-source desktop deployment application in the
Phenotype ecosystem**. A multi-language (Rust core + SvelteKit frontend + Go
backend) cross-platform solution, packaged as a Tauri 2 desktop binary,
that turns a local machine into a deployment target for containerized
workloads.

The thing BytePort does that no other open-source project in the ecosystem
does is **own the desktop deployment surface end-to-end** for Phenotype
users — a single downloadable artifact bundles the local Go backend, the
asset transport, and the native UI. Closest neighbors: Server Compass
(proprietary, $29) and Coolify (web-based, requires a separate server).
BytePort's identity is *"open-source, local-first, embedded in the
Phenotype toolchain"* — those three together is what the user loses if
you swap it out.

## Closest Viable Product

The BytePort CVP is **a single user on macOS / Linux / Windows who can**:

1. Download and install BytePort from a signed release artifact.
2. Launch the desktop app and connect to the local Go backend (auto-started
   by the Tauri shell on port 8081).
3. Deploy a containerized workload from a local image or compose file to
   the local Podman / Docker daemon through the Go backend.
4. See container health, logs, and metrics in real time in the desktop UI.
5. Persist deployments across app restarts (SQLite-backed state in the
   desktop app's local data dir).
6. Ship a typed pure-Rust S3 presigner (`byteport-transport`) as a
   reusable crate that other Phenotype tools can depend on without taking
   on AWS SDK dependency weight.

Everything else (multi-cloud transport, MCP server integration, fleet
orchestration, native sandboxing via nanovms, thegent-specific desktop
shells) is post-CVP — see `docs/boundary/BytePort.md` for the explicit
delegations.

## In CVP (must ship in this slice)

- **Tauri 2 desktop binary** (`frontend/web/src-tauri/`). Rust core with a
  hardened `tauri.conf.json` (CSP, COOP/COEP/CORP, HSTS, X-Frame-Options,
  X-Content-Type-Options, Referrer-Policy, Permissions-Policy) and an
  asset protocol scope narrowed to `$APPDATA/uploads`, `$APPDATA/cache`,
  `$APPLOCALDATA/uploads`, `$APPLOCALDATA/cache` (never `["**"]`).
- **SvelteKit 5 / Svelte 5 frontend** (`frontend/web/`) talking to the
  Rust shell via a typed `IpcEnvelope<T>` JSON-RPC contract. No untyped
  strings across the bridge.
- **Go 1.25 backend** (`backend/byteport/`). Container orchestration via
  the Podman / Docker CLI. SQLite for persistence. Healthz + presign
  endpoints exposed for the desktop shell.
- **Pure-Rust S3 presigner crate** (`crates/byteport-transport/`). `Transport`
  trait + `S3UploadTransport` impl. No `aws-sdk-s3` dependency — keeps the
  crate lean enough that downstream Phenotype tools can adopt it.
- **Astro docs site** (marketing, current release notes, screenshots).
- **Signed releases** for macOS / Linux / Windows. CI matrix exercises all
  three platforms on every push to `main`.
- **`Cargo.toml` workspace** (resolver 3) excluding the desktop binary
  crate so plain `cargo build` does not produce a white-window binary —
  the Tauri CLI must drive the desktop build to embed frontend assets.

## Post-CVP (defer until CVP is live)

These are explicitly out of the CVP slice:

- **Multi-cloud transport abstraction** beyond S3 (lives in
  `pheno-transport`).
- **MCP server** for remote BytePort control (lives in
  `PhenoMCPServers`).
- **Native sandboxing** (lives in `nanovms`).
- **Per-agent desktop shells** for thegent / other Phenotype agents
  (each agent gets its own desktop shell under its own repo).
- **Multi-node / fleet orchestration** beyond a single user's machine.
- **Cloud-hosted multi-tenant BytePort** (the CVP is desktop + local).
- **Mobile (iOS / Android)** deployment targets (CVP is desktop only).

## Anti-CVPs

Things that look like they belong in the BytePort CVP but don't, and
where they actually live:

| Looks like BytePort CVP | Actually lives in | Why |
| ----------------------- | ------------------ | --- |
| Multi-cloud S3-compatible transport | `pheno-transport` | BytePort only ships S3 presign; multi-cloud is a shared SDK concern. |
| Remote MCP control of BytePort | `PhenoMCPServers` | MCP is a separate runtime; BytePort is local-first. |
| Cross-platform process isolation | `nanovms` | Native sandboxing is a kernel-level concern outside BytePort's scope. |
| Agent-specific desktop shells | `thegent/desktop` (per agent) | Each agent gets its own native shell; BytePort is the **deploy** app, not an agent shell. |
| Cloud-hosted multi-user BytePort | post-CVP | CVP is single-user local; cloud hosting needs auth/billing first. |
| Generic web-based deploy UI | `Coolify` (external) | BytePort's identity is desktop, not web — a web UI defeats the local-first point. |

## Build-deploy status

As of 2026-09-20:

- **Desktop binary**: builds and runs on macOS / Linux / Windows. CI matrix
  green on all three. Release artifacts (DMG / AppImage / MSI) signed and
  published.
- **Backend (Go 1.25)**: `backend/byteport/` is the canonical module and
  is what the desktop app talks to on port 8081. The legacy
  `backend/bytebridge/` module is unused and should be removed in a
  follow-up cleanup.
- **Rust crates**: `byteport-transport`, `byteport-cli`, `byteport-dag`,
  `byteport-otel` all build and pass `cargo test` on the workspace.
- **Frontend**: SvelteKit 5 app builds via `cargo tauri build`. Bare
  `cargo build -p app` is documented as broken (white-window binary)
  in the repo README and is excluded from the workspace.
- **Astro docs site**: builds and deploys.
- **71-pillar scorecard**: 47/60 (78.3%) as of 2026-06-23. The score
  stayed flat through the BP-001 dead-code removal and
  `tauri.conf.json` hardening.

The CVP "ship" state was reached when the signed release artifacts
landed on the GitHub Releases page and CI was green across the matrix.
That state is live now.

## Long-term paths (executed 2026-09-20)

To not block on the slow CI loop, the following foundational work was
done in parallel during the same build-deploy window:

1. **CVP doc** at `docs/cvp/BytePort.md` (this file).
2. **Intent fill-in** at `docs/intent/BytePort.md` — replaces the
   placeholder with the actual BytePort intent statement.
3. **Boundary fill-in** at `docs/boundary/BytePort.md` — replaces the
   placeholder with the actual in-scope / out-of-scope and
   boundary-crossings table.
4. **71-pillar scorecard refresh** tracked for the next boundary review
   cycle (2026-07-23 review window).

These moves do not require BytePort CI to land and shrink the critical
path for any future rationalization work.

## Open Questions

- **`backend/bytebridge/` removal**: is now unused. Confirm with the
  owner and remove in a follow-up cleanup PR. No callers exist.
- **`byteport-dag` scope**: the DAG foundation crate is referenced from
  `byteport-cli` but not from the desktop binary. Does the CVP actually
  need DAG execution, or is it speculative? Decide before the next
  release.
- **Mobile**: is mobile in scope for a future CVP (post-CVP), or is
  desktop the only target forever? Mobile changes the transport story
  (no local Podman daemon on iOS).
- **Update channel**: signed releases only, or also auto-update via
  Tauri updater? CVP ships signed releases only; auto-update is
  post-CVP.

## Change Log

| Date | Change | Worklog |
| ---- | ------ | ------- |
| 2026-09-20 | Initial CVP, status = active (shipping) | this file |
