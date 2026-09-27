---
repo: "AuthKit"
role: canonical-auth-boundary
status: active
last_boundary_review: 2026-09-27
review_cadence: 30d
in_scope:
  - "enforce_pkce_state_session tower middleware (FR-AUTHV-018, PKCE state<->session invariant)"
  - "SessionStore hexagonal port + in-memory implementation"
  - "pinned Rust toolchain + hardening scaffolding (deny.toml, gitleaks.toml, mutants.toml, fuzz/, CI)"
  - "AUT-SOTA expansion series (001..007) when scheduled"
out_of_scope:
  - "WorkOS console / IdP tenant administration (external SaaS)"
  - "per-service authorization policy (each service owns its own)"
  - "TypeScript auth UI surfaces (libs/auth-ts + AuthKit/typescript)"
  - "Authvault session/middleware logic (archived-superseded; GAP-009/010 pending migration)"
---

# Boundary — AuthKit

## In Scope

- **PKCE state ↔ session enforcement**: `enforce_pkce_state_session` tower layer — the one fleet-wide auth invariant; 11 unit tests covering state binding.
- **`SessionStore` hexagonal port** with an in-memory implementation; Redis/KMS-backed stores are post-CVP.
- **Hardening scaffolding**: pinned toolchain, cargo-deny, gitleaks, cargo-mutants, fuzz targets, CI config.
- **Boundary docs**: in-repo `docs/` + `specs/`, cross-linked to this registry triad (`docs/intent/AuthKit.md`, `docs/boundary/AuthKit.md`, `docs/cvp/AuthKit.md`).

## Out of Scope

| Not here                               | Lives in                                               | Reason                                                                 |
| -------------------------------------- | ------------------------------------------------------ | ---------------------------------------------------------------------- |
| WorkOS console / tenant administration | WorkOS (external SaaS)                                 | AuthKit is a runtime boundary, not an IdP product.                     |
| IdP identity stores / user directory   | the IdP (federation)                                   | AuthKit validates sessions/tokens; it does not store identities.       |
| Per-service authorization rules        | each service                                           | AuthKit authenticates; services authorize.                             |
| Web-app auth UI helpers                | `libs/auth-ts` + `AuthKit/typescript/packages/auth-ts` | Separate TypeScript surface; Rust crate is the boundary.               |
| Authvault session/middleware logic     | Authvault (status `archived-superseded`)               | Predecessor is read-only history; GAP-009/010 are pending _migration_. |
| OIDC discovery / JWKS plumbing         | post-CVP (AUT-SOTA-002)                                | Not in the current PKCE + store slice.                                 |

## Boundary Crossings

| Crossing                                | Direction               | Surface             | Status                      |
| --------------------------------------- | ----------------------- | ------------------- | --------------------------- |
| `enforce_pkce_state_session` middleware | AuthKit → PhenoServices | tower Layer/Service | green                       |
| `SessionStore` port                     | PhenoServices → AuthKit | Rust trait          | green (in-memory impl)      |
| Authvault GAP-009/010 migration         | Authvault → AuthKit     | code migration      | amber (pending)             |
| OIDC/JWKS config ingestion              | IdP → AuthKit           | HTTP (post-CVP)     | red (not yet implemented)   |
| TS surface (`auth-ts`) parity           | AuthKit ↔ libs/auth-ts | package dependency  | amber (two candidate homes) |

## Last Boundary Review

**Date:** 2026-09-27
**Reviewer:** jcode agent (PHENOREG-FORWARD-WBS A3.1 / C3.3)
**Worklog / finding:** initial boundary authored from `projects/AuthKit.json`, the local mirror tree (Rust workspace, last commit 2026-08-24), disposition rows (`AFFIRM`, `q20260718` live), and ECOSYSTEM_MAP notes.
**Decisions:**

- GitHub `KooshaPari/AuthKit` 404 recorded as amber/reconcile item, not resolved unilaterally.
- Authvault stays out of scope as `archived-superseded`; GAP-009/010 tracked as a pending crossing.

**Next review:** 2026-10-27
