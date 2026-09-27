---
repo: "AuthKit"
aliases: ["authkit"]
role: canonical-auth-boundary
status: active
last_verified: 2026-09-27
bound_prompts: 139
bound_plans: 0
bound_responses: 0
device: macbook
---

# Intent — AuthKit

## Intent Statement

Own the fleet's authentication and authorization runtime boundary as a single Rust crate: enforce the PKCE state ↔ session invariant at the middleware for every PhenoService (`enforce_pkce_state_session`, FR-AUTHV-018, 11 unit tests), store sessions behind the hexagonal `SessionStore` port, and grow through the documented AUT-SOTA series (key rotation, OIDC discovery, WebAuthn, TOTP, KMS-backed secrets, DPoP, rate limiting). AuthKit supersedes Authvault (card status `archived-superseded`) and is designated the standalone canonical WorkOS-themed auth hub by USER-DECISION 2026-07-19. Services authenticate through AuthKit; each service keeps its own authorization policy.

## Bound Prompts

| Date       | Source      | File                                                           | Tag            |
| ---------- | ----------- | -------------------------------------------------------------- | -------------- |
| 2025-10-01 | claude-code | `docs/curated-prompts/claude-code/2025-10/894b24f2bea65f3e.md` | narrative      |
| 2025-10-01 | claude-code | `docs/curated-prompts/claude-code/2025-10/e9726f1c0df7f095.md` | implementation |
| 2025-10-01 | claude-code | `docs/curated-prompts/claude-code/2025-10/448084cd097e7342.md` | implementation |
| 2025-10-01 | claude-code | `docs/curated-prompts/claude-code/2025-10/0c7ebe530800f50c.md` | narrative      |
| 2025-10-01 | claude-code | `docs/curated-prompts/claude-code/2025-10/7cdd13381c0bcacf.md` | policy-setting |
| 2025-10-01 | claude-code | `docs/curated-prompts/claude-code/2025-10/9214b97510091686.md` | narrative      |
| 2025-10-01 | claude-code | `docs/curated-prompts/claude-code/2025-10/9286f0ba2c272476.md` | implementation |
| 2025-10-01 | claude-code | `docs/curated-prompts/claude-code/2025-10/b872eacee8f15b95.md` | implementation |
| 2025-10-01 | claude-code | `docs/curated-prompts/claude-code/2025-10/1a149c1c72598fb8.md` | bugfix         |
| 2025-10-01 | claude-code | `docs/curated-prompts/claude-code/2025-10/3a5754bad44733c1.md` | bugfix         |
| 2025-10-01 | claude-code | `docs/curated-prompts/claude-code/2025-10/a7180b6c68138c61.md` | narrative      |
| 2025-10-01 | claude-code | `docs/curated-prompts/claude-code/2025-10/e9a5c26a111df6aa.md` | narrative      |
| 2025-10-01 | claude-code | `docs/curated-prompts/claude-code/2025-10/28c6d69e96cb8f4b.md` | bugfix         |
| 2025-10-01 | claude-code | `docs/curated-prompts/claude-code/2025-10/d14ebea73377a31a.md` | bugfix         |
| 2025-10-01 | claude-code | `docs/curated-prompts/claude-code/2025-10/1ad09eaca9f19a12.md` | bugfix         |
| 2025-10-01 | claude-code | `docs/curated-prompts/claude-code/2025-10/f78da52a3188e6ce.md` | narrative      |
| 2025-10-01 | claude-code | `docs/curated-prompts/claude-code/2025-10/c320cb026289e4a7.md` | narrative      |
| 2025-10-01 | claude-code | `docs/curated-prompts/claude-code/2025-10/f5704e07f6eeed85.md` | narrative      |
| 2025-10-02 | claude-code | `docs/curated-prompts/claude-code/2025-10/d39e336111706610.md` | narrative      |
| 2025-10-03 | claude-code | `docs/curated-prompts/claude-code/2025-10/47ac92cfee1b3558.md` | implementation |
| 2025-10-03 | claude-code | `docs/curated-prompts/claude-code/2025-10/8fc8a0149f4371da.md` | implementation |
| 2025-10-06 | claude-code | `docs/curated-prompts/claude-code/2025-10/a7478103c0c313d5.md` | narrative      |
| 2025-10-06 | claude-code | `docs/curated-prompts/claude-code/2025-10/697b0b7486d242fd.md` | bugfix         |
| 2025-10-06 | claude-code | `docs/curated-prompts/claude-code/2025-10/0ad731722985e215.md` | narrative      |
| 2025-10-06 | claude-code | `docs/curated-prompts/claude-code/2025-10/7501aa9d479dfd07.md` | bugfix         |
| 2025-10-06 | claude-code | `docs/curated-prompts/claude-code/2025-10/d07ebfe481a5cd54.md` | narrative      |
| 2025-10-07 | claude-code | `docs/curated-prompts/claude-code/2025-10/469375fe2058de62.md` | narrative      |
| 2025-10-07 | claude-code | `docs/curated-prompts/claude-code/2025-10/28b5664a49da3644.md` | bugfix         |
| 2025-10-07 | claude-code | `docs/curated-prompts/claude-code/2025-10/ea999b5445c5112a.md` | implementation |
| 2025-10-07 | claude-code | `docs/curated-prompts/claude-code/2025-10/eb61b705bb154a7a.md` | bugfix         |
| 2025-10-07 | claude-code | `docs/curated-prompts/claude-code/2025-10/04669092de3f36c7.md` | narrative      |
| 2025-10-07 | claude-code | `docs/curated-prompts/claude-code/2025-10/c500ccaa4613888c.md` | narrative      |
| 2025-10-07 | claude-code | `docs/curated-prompts/claude-code/2025-10/31900834eb6a5961.md` | implementation |
| 2025-10-09 | claude-code | `docs/curated-prompts/claude-code/2025-10/ab78db304e0a7a9d.md` | implementation |
| 2025-10-10 | claude-code | `docs/curated-prompts/claude-code/2025-10/29763cbd49a2ef90.md` | narrative      |
| 2025-10-17 | claude-code | `docs/curated-prompts/claude-code/2025-10/1645f72334f260a1.md` | bugfix         |
| 2025-10-17 | claude-code | `docs/curated-prompts/claude-code/2025-10/4247c17b71f8efbf.md` | policy-setting |
| 2025-10-17 | claude-code | `docs/curated-prompts/claude-code/2025-10/29947ed723aadfac.md` | policy-setting |
| 2025-10-17 | claude-code | `docs/curated-prompts/claude-code/2025-10/e871a5f2a952bb4b.md` | narrative      |
| 2025-10-25 | claude-code | `docs/curated-prompts/claude-code/2025-10/782fca907816adef.md` | bugfix         |
| 2025-11-08 | claude-code | `docs/curated-prompts/claude-code/2025-11/a013f4002c8df1bd.md` | implementation |
| 2025-11-25 | claude-code | `docs/curated-prompts/claude-code/2025-11/85658572d8b56c65.md` | implementation |
| 2025-11-25 | claude-code | `docs/curated-prompts/claude-code/2025-11/6c230b3c7fab7b76.md` | implementation |
| 2025-11-27 | claude-code | `docs/curated-prompts/claude-code/2025-11/1f2801d8fc8a35da.md` | bugfix         |
| 2025-11-27 | claude-code | `docs/curated-prompts/claude-code/2025-11/3de0fa77d8ebf9d6.md` | bugfix         |
| 2025-11-27 | claude-code | `docs/curated-prompts/claude-code/2025-11/6a44b2b8361b1e63.md` | bugfix         |
| 2026-02-01 | claude-code | `docs/curated-prompts/claude-code/2026-02/d6c8617c88a6adb8.md` | narrative      |
| 2025-09-08 | codex       | `docs/curated-prompts/codex/2025-09/a625d0defbb45a98.md`       | policy-setting |
| 2025-09-08 | codex       | `docs/curated-prompts/codex/2025-09/c4ab866ad18bc2f5.md`       | policy-setting |
| 2025-09-08 | codex       | `docs/curated-prompts/codex/2025-09/f301cb1433c2a415.md`       | repo-defining  |

_…and 89 more. See `_bindings.json` for full list._

## Bound Plans

| Date | Source | File | Status |
| ---- | ------ | ---- | ------ |

## Bound Responses (specs, ideas, plans from agents)

| Date | Source | File | Kind |
| ---- | ------ | ---- | ---- |

## Boundary

See: [`docs/boundary/AuthKit.md`](../boundary/AuthKit.md)

## Ecosystem Role

Canonical auth-runtime boundary: `projects/AuthKit.json` disposition `AFFIRM` with `canonical_routing: true`; `q20260718-AuthKit` row `fsm: live` ("canonical hub kept alive"). Supersedes Authvault; superseded_by: none. Neighbor surfaces: `libs/auth-ts` and the absorbed `phenotype-auth-ts` (ECOSYSTEM_MAP note 2026-06-18). `ECOSYSTEM_MAP.md` currently lists AuthKit under **SDK** while also naming it in the superseded/archived row — contradiction tracked for the A4.4 consistency pass.

## Open Questions

- **GitHub reachability**: `KooshaPari/AuthKit` returns 404 (verified 2026-09-27 via `gh api` + `git ls-remote` with a full-repo-scope token) while the registry marks the repo canonical and a local mirror (last commit 2026-08-24, `chore: add genuine files + scorecard CI`) survives. Deleted, made private, or renamed — reconcile before the next boundary review.
- **GAP-009 / GAP-010 migration** from Authvault (RS256/ES256 alg-confusion defense + middleware adapter docs) — schedule or explicitly defer.
- **TypeScript surface ownership**: `AuthKit/typescript/packages/auth-ts` (ECOSYSTEM absorption note) vs `libs/auth-ts` — pick one canonical home.
- **Card discrepancy**: `projects/AuthKit-2026-06-25.json` describes a "Go SDK + server / Large Go+proto codebase" while the actual tree is a Rust workspace — correct or merge the cards.

## Change Log

| Date       | Change                                                                                              | Worklog                                                    |
| ---------- | --------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| 2026-06-17 | Initial binding (L7-001 sweep)                                                                      | `worklogs/L7-001-intent-boundary-curation-2026-06-17.json` |
| 2026-09-27 | Intent statement, ecosystem role, and open questions filled (authored triad: `docs/cvp/AuthKit.md`) | PHENOREG-FORWARD-WBS A3.1 / C3.3                           |
