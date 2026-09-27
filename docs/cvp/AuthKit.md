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

AuthKit is the **canonical authentication runtime boundary**
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
3. Run the crate's unit suite — 11 tests covering PKCE state binding —
   from the local mirror (the card's `ci_state` reads `newly-created; CI not
yet configured (SOTA-001 unit)`, and the GitHub 404 makes remote CI status
   unverifiable).
4. Build from a pinned toolchain with the repo's hardening scaffolding
   present in the mirror: `rust-toolchain.toml`, `deny.toml`, `gitleaks.toml`,
   `mutants.toml`, `fuzz/`, `.circleci` CI config, `Justfile`/`Makefile`
   drivers — files present, CI execution unconfirmed (`ci_state` caveat above).

That slice already exists in the local mirror; the CVP question is whether it
stays reachable and CI-backed (see registry reality below).

## In CVP (must ship in this slice)

- **`enforce_pkce_state_session` tower middleware** — the one non-negotiable
  security invariant; 11 unit tests as reported by the card (no run artifact —
  CI unconfigured; the verifier journey above hedges the same claim).
- **`SessionStore` hexagonal port** with an in-memory implementation; other
  implementations (Redis, KMS-backed) are post-CVP.
- **Hardening scaffolding**: pinned Rust toolchain, cargo-deny, gitleaks,
  cargo-mutants config, fuzz targets, CI config files (present in the mirror;
  card `ci_state` says not yet configured — CI execution unconfirmed).
- **Boundary documentation**: `docs/` + `specs/` in-repo, cross-linked to
  `docs/boundary/AuthKit.md` and `docs/intent/AuthKit.md` in the registry.
- **Registry triad**: this CVP + intent + boundary, kept checked against the
  actual tree (not the stale card description).

## Post-CVP (defer until CVP is live)

- **AUT-SOTA series**: key rotation, OIDC discovery, WebAuthn, TOTP,
  KMS-backed secrets, DPoP, rate limiting — the documented expansion (an
  aggregate seven-item list in `projects/AuthKit.json:26`; no per-item
  AUT-SOTA records exist, so numeric ids are positional, not stable keys).
- **Per-adapter expansion**: one layer per adapter/framework beyond the base
  tower layer.
- **Authvault gap follow-through**: per the definition table
  (`archives/zz-archive-phenotype-registry/patches/authkit-absorption.patch:1817-1820`),
  GAP-007 (RS256/ES256 alg-confusion defense → FR-AUTHV-017) and GAP-010
  (Tracera/AgilePlus middleware adapter) are **SHIPPED**; **GAP-009 —
  rate-limiting on failed auth attempts — is still PLANNED** on Authvault main.
  The card's `absorption_note` previously mislabeled GAP-009 as the
  alg-confusion work; card corrected in this review round — do not migrate
  shipped work; the open item is rate limiting only.
- **TypeScript surface reconciliation**: `AuthKit/typescript/packages/auth-ts`
  (ECOSYSTEM_MAP absorption note) vs `libs/auth-ts` — one home, not two
  (`libs/auth-ts` is recorded GitHub-404 in
  `.kilo/audits/org-absorption-2026-06-18.md:121,265`; establish the target
  exists before picking it as the home).

## Anti-CVPs

| Looks like AuthKit CVP                 | Actually lives in                          | Why                                                                                  |
| -------------------------------------- | ------------------------------------------ | ------------------------------------------------------------------------------------ |
| Authvault session/middleware logic     | Authvault (read-only history)              | Archived predecessor; GAP-009 (rate limiting) is the open gap — GAP-007/010 shipped. |
| WorkOS console / tenant administration | WorkOS (external SaaS)                     | AuthKit is a runtime boundary, not an IdP product.                                   |
| Web-app auth UI helpers                | `libs/auth-ts` + `AuthKit/typescript/...`  | Separate TypeScript surface; the Rust crate is the boundary.                         |
| Per-service authorization rules        | each service                               | AuthKit authenticates; services authorize.                                           |
| OIDC discovery / JWKS plumbing         | post-CVP (AUT-SOTA series: OIDC discovery) | Not in the current slice; the slice is PKCE + store only.                            |

## Registry reality (as of 2026-09-27)

- **GitHub `KooshaPari/AuthKit` returns 404** — checked via `gh api
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
  (canonical WorkOS-themed)" (`disposition-index.json:1382` — note this
  `default: standalone` entry is fleet-wide boilerplate with an AuthKit gloss;
  the identical string appears at `:441`, `:1336`, `:1803`, `:3226`). The same
  row block (`:1381`) also records `resolved 2026-07-17: AuthKit source
absorbed into Authvault per SupSUPERSEDE-2026-06-20. Source repo archived.` —
  the inverse of this CVP's "supersedes Authvault" framing. Both records stand;
  the direction conflict is tracked in Open Questions.
- **Same-name repo collision (not a stale card)**: `projects/AuthKit-2026-06-25.json`
  describes a 25,149 KB **Go** repo created 2025-04-18 with 8 branches (audit:
  "Go | 91%", 7 remote branches); `projects/AuthKit.json` describes a 17 KB
  **Rust** crate created 2026-06-24 with 1 branch (`disposition-index.json:1380-1385`
  = 2 branches / 17 KB). A 25 MB Go repo and a 17 KB Rust crate cannot be the
  same repository — both cards carry `gh_url: .../KooshaPari/AuthKit`, so this
  is a same-path collision between two repos, not one card going stale.

## Open Questions

- **Where did the GitHub repo go?** Deleted vs made private vs renamed — this
  is the single blocking discrepancy between "canonical" (registry) and
  "unreachable" (GitHub). If deletion was intentional, the disposition rows
  need a tombstone note; if not, restore or re-point `gh_url`.
- **GAP-009 rate-limiting gap** (GAP-007 RS256/ES256 and GAP-010 middleware
  adapter are shipped; the card's GAP-009 mislabel was corrected this round —
  source: `authkit-absorption.patch:1817-1820`): schedule or explicitly defer
  at the next boundary review.
- **TypeScript ownership**: `AuthKit/typescript/packages/auth-ts` vs
  `libs/auth-ts` — establish that `libs/auth-ts` exists first (recorded
  GitHub-404: `.kilo/audits/org-absorption-2026-06-18.md:121,265`), then pick
  one canonical home and update ECOSYSTEM_MAP.
- **Card collision (do not merge)**: the two cards describe two different
  repos sharing one `gh_url` — 25,149 KB Go repo created 2025-04-18 (8
  branches) vs 17 KB Rust crate created 2026-06-24 (1 branch). Reconcile the
  collision: which repo is canonical, what happened to the other, and why both
  cards carry `KooshaPari/AuthKit`. Merging the cards as previously phrased
  would collapse the Go repo's record into the Rust crate's. Repeated at
  `docs/intent/AuthKit.md:99`.
- **CI state discrepancy**: the local mirror contains `.circleci/`,
  `gitleaks.toml`, `mutants.toml` etc. while the card's `ci_state` reads
  `newly-created; CI not yet configured (SOTA-001 unit)` — reconcile the card
  with the tree (or vice versa) at the next boundary review.

## Change Log

| Date       | Change                                                                                                                                                                                                                                                        | Worklog                 |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| 2026-09-27 | Initial CVP (WBS A3.1). GitHub 404 + local-mirror status recorded; triad authored same day                                                                                                                                                                    | PHENOREG-FORWARD-WBS A3 |
| 2026-09-27 | Review fixes: authentication-only boundary wording (services own authz), CI claim corrected to card `ci_state`                                                                                                                                                | PR #585 review round    |
| 2026-09-27 | Kilo round 2: GAP-009 corrected (card + triad; GAP-007/010 shipped), collision diagnosis replaces stale-card/merge, USER-DECISION boilerplate + absorbed-into-Authvault counter-record recorded, AUT-SOTA positional ids qualified, `ci_state` quoted in full | PR #585 review round    |
