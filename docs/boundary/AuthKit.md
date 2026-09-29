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
  - "AUT-SOTA expansion series when scheduled (aggregate list in projects/AuthKit.json:26; no per-item records — numeric ids positional)"
out_of_scope:
  - "WorkOS console / IdP tenant administration (external SaaS)"
  - "per-service authorization policy (each service owns its own)"
  - "TypeScript auth UI surfaces (libs/auth-ts + AuthKit/typescript)"
  - "Authvault session/middleware logic (archived-superseded; GAP-009 rate-limiting is the open gap — GAP-007/010 shipped)"
---

# Boundary — AuthKit

## In Scope

- **PKCE state ↔ session enforcement**: `enforce_pkce_state_session` tower layer — the one fleet-wide auth invariant; 11 unit tests covering state binding as reported by the card (no run artifact: the absorption-patch enumeration lists 10 unique names — `expired_state_is_rejected` appears twice — and `projects/AuthKit.json:34` says CI is not configured; the CVP hedges the same claim).
- **`SessionStore` hexagonal port** with an in-memory implementation; Redis/KMS-backed stores are post-CVP.
- **Hardening scaffolding**: pinned toolchain, cargo-deny, gitleaks, cargo-mutants, fuzz targets, CI config.
- **Boundary docs**: in-repo `docs/` + `specs/`, cross-linked to this registry triad (`docs/intent/AuthKit.md`, `docs/boundary/AuthKit.md`, `docs/cvp/AuthKit.md`).

## Out of Scope

| Not here                               | Lives in                                               | Reason                                                                                        |
| -------------------------------------- | ------------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| WorkOS console / tenant administration | WorkOS (external SaaS)                                 | AuthKit is a runtime boundary, not an IdP product.                                            |
| IdP identity stores / user directory   | the IdP (federation)                                   | AuthKit validates sessions/tokens; it does not store identities.                              |
| Per-service authorization rules        | each service                                           | AuthKit authenticates; services authorize.                                                    |
| Web-app auth UI helpers                | `libs/auth-ts` + `AuthKit/typescript/packages/auth-ts` | Separate TypeScript surface; Rust crate is the boundary.                                      |
| Authvault session/middleware logic     | Authvault (status `archived-superseded`)               | Predecessor is read-only history; GAP-009 (rate limiting) remains open — GAP-007/010 shipped. |
| OIDC discovery / JWKS plumbing         | post-CVP (AUT-SOTA series: OIDC discovery)             | Not in the current PKCE + store slice.                                                        |

## Boundary Crossings

| Crossing                                | Direction               | Surface             | Status                                                                                                                                                                         |
| --------------------------------------- | ----------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `enforce_pkce_state_session` middleware | AuthKit → PhenoServices | tower Layer/Service | amber (unverified local mirror — no run artifact: CI unconfigured, GitHub 404; card `ci_state` = `newly-created; CI not yet configured (SOTA-001 unit)`)                       |
| `SessionStore` port                     | PhenoServices → AuthKit | Rust trait          | amber (unverified local mirror — no run artifact: CI unconfigured, GitHub 404)                                                                                                 |
| Authvault GAP-009 rate-limiting gap     | Authvault → AuthKit     | code migration      | amber — **RISK-ACCEPTED 2026-09-27** (owner: Authvault main; re-review 2026-10-27; interim: no brute-force protection on verifier/state/bearer endpoints; GAP-007/010 shipped) |
| OIDC/JWKS config ingestion              | IdP → AuthKit           | HTTP (post-CVP)     | red (not yet implemented)                                                                                                                                                      |
| TS surface (`auth-ts`) parity           | AuthKit ↔ libs/auth-ts | package dependency  | amber (`libs/auth-ts` recorded 404 — establish target exists first)                                                                                                            |

## Last Boundary Review

**Date:** 2026-09-27
**Reviewer:** jcode agent (PHENOREG-FORWARD-WBS A3.1 / C3.3)
**Worklog / finding:** initial boundary authored from `projects/AuthKit.json`, the local mirror tree (Rust workspace, last commit 2026-08-24), disposition rows (`AFFIRM`, `q20260718` live), and ECOSYSTEM_MAP notes.
**Decisions:**

- GitHub `KooshaPari/AuthKit` 404 recorded as amber/reconcile item, not resolved unilaterally.
- Authvault stays out of scope as `archived-superseded`; GAP-009 (rate limiting) is the single pending crossing — GAP-007 (RS256/ES256 → FR-AUTHV-017) and GAP-010 shipped; the card's GAP-009 mislabel was corrected in the 2026-09-27 kilo review round (source: `authkit-absorption.patch:1817-1820`).

**Next review:** 2026-10-27
