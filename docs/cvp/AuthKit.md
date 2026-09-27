---
repo: "AuthKit"
aliases: ["authkit"]
status: "active"
last_verified: "2026-09-27"
owner: "kooshapari"
build_deploy_status: "mirror-only"
---

# CVP — AuthKit

## Identity

AuthKit is the **canonical authentication and authorization runtime boundary**
of the Phenotype fleet: a Rust crate (hexagonal `SessionStore` port + tower
PKCE middleware) that supersedes Authvault and is designated the standalone,
WorkOS-themed auth hub by USER-DECISION 2026-07-19. The thing it does that
nothing else in the fleet does is **own the PKCE state ↔ session invariant at
the middleware** — every service mounts the same enforcement instead of
reimplementing session hygiene. Swap it out and you lose the single enforced
boundary: auth stops being a fleet property and becomes per-service drift.

## Closest Viable Product

The AuthKit CVP is **a PhenoService that can**:

1. Depend on the `authkit` crate and mount `enforce_pkce_state_session` as a
   tower layer on its authentication routes (FR-AUTHV-018, landed in commit
   `064b310`).
2. Store and retrieve sessions exclusively through the `SessionStore` port
   (in-memory implementation for now).
3. Run the crate's unit suite — 11 tests covering PKCE state binding — green
   on every push.
4. Build from a pinned toolchain with the repo's hardening scaffolding
   present: `rust-toolchain.toml`, `deny.toml`, `gitleaks.toml`, `mutants.toml`,
   `fuzz/`, `.circleci` CI, `Justfile`/`Makefile` drivers.

That slice already exists in the local mirror; the CVP question is whether it
stays reachable and CI-backed (see registry reality below).

## In CVP (must ship in this slice)

- **`enforce_pkce_state_session` tower middleware** — the one non-negotiable
  security invariant;11 unit tests.
- **`SessionStore` hexagonal port** with an in-memory implementation; other
  implementations (Redis, KMS-backed) are post-CVP.
- **Hardening scaffolding**: pinned Rust toolchain, cargo-deny, gitleaks,
  cargo-mutants config, fuzz targets, CI config.
- **Boundary documentation**: `docs/` + `specs/` in-repo, cross-linked to
  `docs/boundary/AuthKit.md` and `docs/intent/AuthKit.md` in the registry.
- **Registry triad**: this CVP + intent + boundary, kept verified against the
  actual tree (not the stale card description).

## Post-CVP (defer until CVP is live)

- **AUT-SOTA-001..007**: key rotation, OIDC discovery, WebAuthn, TOTP,
  KMS-backed secrets, DPoP, rate limiting — the documented expansion series.
- **Per-adapter expansion**: one layer per adapter/framework beyond the base
  tower layer.
- **GAP-009 / GAP-010 migration**: RS256/ES256 alg-confusion defense and
  middleware adapter docs currently live on Authvault main (per
  `projects/AuthKit.json`); migrate them into AuthKit when Authvault is fully
  retired.
- **TypeScript surface reconciliation**: `AuthKit/typescript/packages/auth-ts`
  (ECOSYSTEM_MAP absorption note) vs `libs/auth-ts` — one home, not two.

## Anti-CVPs

| Looks like AuthKit CVP                 | Actually lives in                         | Why                                                                      |
| -------------------------------------- | ----------------------------------------- | ------------------------------------------------------------------------ |
| Authvault session/middleware logic     | Authvault (read-only history)             | Archived predecessor; GAP-009/010 are pending _migration_, not new work. |
| WorkOS console / tenant administration | WorkOS (external SaaS)                    | AuthKit is a runtime boundary, not an IdP product.                       |
| Web-app auth UI helpers                | `libs/auth-ts` + `AuthKit/typescript/...` | Separate TypeScript surface; the Rust crate is the boundary.             |
| Per-service authorization rules        | each service                              | AuthKit authenticates; services authorize.                               |
| OIDC discovery / JWKS plumbing         | post-CVP (AUT-SOTA-002)                   | Not in the current slice; the slice is PKCE + store only.                |

## Registry reality (as of 2026-09-27)

- **GitHub `KooshaPari/AuthKit` returns 404** — verified via `gh api
repos/KooshaPari/AuthKit` and `git ls-remote` (both not-found) with a
  full-`repo`-scope owner token. The repo is deleted, private-beyond-token, or
  renamed.
- **Local mirror survives**: `C:\Users\koosh\AuthKit` (partial clone,
  `blob:none`) with last commit `1bb9c46` (2026-08-24, "chore: add genuine
  files + scorecard CI"); tree = Rust workspace (`Cargo.toml`,
  `rust-toolchain.toml`, `src/`, `tests/`, `fuzz/`).
- **Registry says canonical**: `projects/AuthKit.json` disposition `AFFIRM`
  with `canonical_routing: true`; `q20260718-AuthKit` row `fsm: live`
  ("canonical hub kept alive"); USER-DECISION 2026-07-19 "standalone
  (canonical WorkOS-themed)".
- **Stale card**: `projects/AuthKit-2026-06-25.json` describes a "Go SDK +
  server / Large Go+proto codebase" — the actual tree is Rust-first; the Go
  description predates or misstates the crate.

## Open Questions

- **Where did the GitHub repo go?** Deleted vs made private vs renamed — this
  is the single blocking discrepancy between "canonical" (registry) and
  "unreachable" (GitHub). If deletion was intentional, the disposition rows
  need a tombstone note; if not, restore or re-point `gh_url`.
- **GAP-009/010 migration** from Authvault: schedule or explicitly defer at
  the next boundary review.
- **TypeScript ownership**: `AuthKit/typescript/packages/auth-ts` vs
  `libs/auth-ts` — pick one canonical home and update ECOSYSTEM_MAP.
- **Card consolidation**: merge or correct the Rust/Go discrepancy between
  `projects/AuthKit.json` and `projects/AuthKit-2026-06-25.json`.

## Change Log

| Date       | Change                                                                                     | Worklog                 |
| ---------- | ------------------------------------------------------------------------------------------ | ----------------------- |
| 2026-09-27 | Initial CVP (WBS A3.1). GitHub 404 + local-mirror status recorded; triad authored same day | PHENOREG-FORWARD-WBS A3 |
