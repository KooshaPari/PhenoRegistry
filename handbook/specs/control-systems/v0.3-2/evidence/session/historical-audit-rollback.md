# Historical write payload — unverified

Recovered from 3cf77748-c6c1-44d0-9ddf-36e26df2b28d message 110. Do not adopt its recommendations without the v0.2 audit.

# Audit — Rollback & Branching Patterns (Subagent C)

Date: 2026-09-11
Repo: Tracera (`C:\Users\koosh\Tracera`, remote `KooshaPari/Tracera`, default branch `main`)
Scope: deploy/release workflows + eviction/rollback tooling + manual-vs-auto prod release flow.

## 0. Workflow inventory (Tracera `.github/workflows/`)

| File | Purpose | Triggers |
|------|---------|----------|
| `deploy-render.yml` | Backend → Render (REST API deploy) | push main + `ci/infisical-deploys` (path-filtered), wf_dispatch `force_deploy` |
| `deploy-vercel.yml` | Frontend → Vercel (prod + PR preview) | push main, PR main, wf_dispatch |
| `deploy-cloudflare.yml` | Edge → Cloudflare Workers | push main + `ci/infisical-deploys` (path-filtered), wf_dispatch (production/staging) |
| `deploy-full-stack.yml` | Orchestrator: test → backend+frontend+edge → summary | push main (path-filtered `crates/**`,`frontend/**`,Dockerfile,render.yaml,wrangler.toml,vercel.json), wf_dispatch (environment + skip_tests) |
| `deploy-pages.yml` | GitHub Pages docs | — |
| `build-push-image.yml` | Docker image build/push | — |
| `release.yml` | Rust release build+test → GitHub Release | tag `v*`, wf_dispatch |
| `release-desktop.yml` | Cross-platform Electrobun desktop installers + GitHub Release | tag `v*`, wf_dispatch |
| `release-crates.yml` | `cargo publish` `tracera-server` + `tracertm-mcp` | tag `v*` (publish), PR (preflight) |
| `release-dist.yml` | Server+CLI binary archives (4 targets) → release assets | tag `v*` |
| `release-macos.yml` | Reusable `kooshapari/phenotype-fleet-ops` macOS sign/notarize | tag `v*.*.*`, wf_dispatch |
| `release-desktop-sign.yml` | (manual desktop signing) | wf_dispatch |

## 1. Existing rollback strategy — NONE for deploys

- **No automated rollback code anywhere in Tracera.** No `rollback`/`revert`/`git revert` step, no `previous release` tracking, no canary ramp, no redeploy-of-previous-commit job in the workflows. Every deploy is **forward-only, fire-and-forget**:
  - `deploy-render.yml:91-111` — triggers Render via `curl -X POST https://api.render.com/v1/services/$SERVICE_ID/deploys`; captures `DEPLOY_ID` but never stores a "last-good" image/tag to roll back to. `deploy-render.yml:113+` waits on deploy status, `deploy-render.yml:138` health-checks `/healthz`, both `continue-on-error` / non-fatal.
  - Backend/frontend/edge recovery relies on Render/Vercel/Cloudflare **native dashboard rollback** — not wired into any workflow.
- The only matches for the term `rollback`/`revert` in the repo are unrelated to deployment:
  - `frontend/.../CacheManager.ts` — cache/stale-data invalidation ("rollback"-style cache revert).
  - `crates/tracera-server/src/queue/claim.rs:52`, `lifecycle.rs` — DB transaction `tx.rollback()`.
  - `chocolatey/tools/uninstall.ps1` + `docs/specs/013-desktop-hardening.md` — installer uninstall restores prior state.
  - `CHANGELOG.md:33` — `revert to tower_governor` (#888), a source revert, not a deploy rollback.
- **Desktop** releases are immutable GitHub Release artifacts + an update feed ("latest-version wins"). Rollback = cutting a new release of a prior tag; no downgrade/auto-rollback guard in `release-desktop.yml`.

## 2. How release CI differs from normal CI

- **Normal CI (`ci.yml`)** — validates, never deploys. Triggers: push to `main|master|develop|release/**`, PRs, `merge_group`, wf_dispatch (runner choice). `ci.yml:43` `detect-changes` gates per-language jobs (rust/python/go/typescript). Blacksmith → GitHub-hosted fallback runners, `concurrency: cancel-in-progress: true`. Output = pass/fail only.
- **Release CI (`release*.yml`)** — tag-gated (`v*`), also honors `workflow_dispatch`. Escalates permissions: `contents: write`, `id-token: write`, `attestations: write` (vs `contents: read` for deploy/normal). Difference highlights:
  - `release.yml` — `--release` build/test, then GitHub Release with auto-generated notes.
  - `release-desktop.yml` — matrix installers (macOS arm64 / Windows x64 / Linux x64) + `actions/attest-build-provenance@v2` provenance, attached to the tag's Release.
  - `release-crates.yml` — version-match guard (`CRATE_VERSION == TAG_VERSION`) before `cargo publish` (line 54-57); PR preflight vs tag publish split by `if: github.event_name == 'push'`.
  - `release-dist.yml`, `release-macos.yml` — multi-target binaries / signed+notarized macOS via reusable fleet-ops (self-hosted runners, zero billed minutes).
- Net: normal CI = branch/PR-quality gate; release CI = immutable artifact production triggered by semantic version tags, with provenance/signing and no rollback lane.

## 3. Current manual-vs-auto prod release flow

- **Prod backend/edge = fully AUTOMATIC on push to `main`.** `deploy-render.yml:3`, `deploy-cloudflare.yml:3` path-filtered push; `deploy-full-stack.yml:16` pushes all three after test pass. A merge to main auto-deploys production to Render + Cloudflare Workers (+ Vercel frontend) with **no required human approval**.
  - Environment protection reality (via `gh api`): `render-production` = 0 protection rules; `cloudflare-production` = 0; `vercel-production` = 1 rule of type `branch_policy` (only allows deploys from a protected branch — **not** an approval-reviewer gate). So the "required reviewers" the `deploy-vercel.yml:17-19` comment asks the operator to configure are **not configured**.
- **Manual levers (workflow_dispatch)** exist but are optional/alternative: `deploy-render` `force_deploy`, `deploy-cloudflare`/`deploy-full-stack` environment choice (production/staging) + `skip_tests`. These are not mandatory gates.
- **Releases are MANUAL by tag:** an engineer pushes a `v*` tag; that triggers all `release*.yml` to publish installers, crates.io releases, and GitHub Release. No CI human-approval step; the git tag IS the authorization.
- **No `trio` (three manual approvals) pattern exists** anywhere in Tracera (searched `trio`, `manual-approval`, `approval`, `required reviewers` — only the unused comment in `deploy-vercel.yml`).

## 4. Adjacent rollback/canary tooling (eligible template)

- **`phenotype-tooling/.github/workflows/canary-rollout.yml` + `phenotype-tooling/deploy/health-gate.yml`** is the only real rollout/rollback machinery on this machine. `health-gate.yml:1-13` documents: canary lane → Prometheus SLO checks (PHENOTYPE-1/2/3) → promote to 100%; `rollback_on_failure: true` auto-rollback + WP-19 incident page; `canary-rollout.yml` supports `start_pct`, `ramp_steps`, `rollback_on_alert`. Consumed by `pt deploy`. This is the natural reference implementation if Tracera gains a gated/canary release path — **but it is NOT wired into Tracera today**.

## 5. Key gaps / recommendations (for the trio/manual-approval feature)

1. **Rollback is entirely manual (provider dashboards).** No last-known-good tag/pin is persisted; consider recording stable `DEPLOY_ID`/tag and adding a `workflow_dispatch` "redeploy previous tag" lane.
2. **`main` push auto-promotes to prod with no approval.** To add a manual (trio) gate, convert deploy jobs to `workflow_run`/`workflow_dispatch` or add **required-reviewer protection rules** on `render-production`/`vercel-production`/`cloudflare-production` environments (currently absent).
3. **Adopt `canary-rollout.yml`-style gates** for the edge/backend if staged rollout is required (exists in `phenotype-tooling`, unused here).
4. Release vs normal CI are cleanly separated by tags; a trio-approval wrap on tag cut would be the least-invasive manual gate.