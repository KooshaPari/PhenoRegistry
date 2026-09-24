# Historical write payload — unverified

Recovered from 4b2411cd-830d-4727-9b70-b86073e37e5a message 35. Do not adopt its recommendations without the v0.2 audit.

# GitOps + Update Automation — Architecture Assessment for the 'this' ecosystem

**Scope:** A multi-repo GitHub org deploying onto a **single** WSL2/podman node.
**Date:** 2026-09-11
**Sections:** (A) GitOps controllers, (B) GitHub native deploy primitives, (C) dependency/update automation, then a recommended architecture.

---

## TL;DR / Verdict

- **GitOps controller:** NOT justified for one node. Both Argo CD and Flux assume a Kubernetes cluster as their substrate. On a single WSL2/podman node they add a deploy-time control plane (CRDs, controllers, app-server/applicationset, source-controller) whose cost buys pull-model reconciliation you do not need for one host. **Use a plain CI → deploy workflow (GitHub Actions) instead.**
- **GitHub native gating:** Owned and standardized. Use **Environments** (`dev`, `staging`, `prod`) with **deployment protection rules** — required reviewers, wait timers, deployment-branch restrictions. This is the "approval-then-run" primitive.
- **Update bot:** **Renovate** is the better fit for a Rust+Python+JS multi-repo org, especially self-hosted (global config-as-code, aggregation/grouping, monorepo/workspace support). Dependabot remains the low-effort default and the carrier of native security **alerts**; the two are complementary, not strictly alternative.

---

## (A) GitOps controllers: Argo CD vs Flux

### 1. What each actually is

Both are **Kubernetes-native controllers**. They are not standalone tools that "point at podman" — they reconcile *in-cluster* state to the desired state declared in Git.

**Argo CD**
- App-centric: an `Application` CR defines a source repo/path and a destination cluster + namespace. The **API server** serves the Web UI/CLI/gRPC, and the **controller** reconciles applications. An **ApplicationSet** template generates many Applications.
- Components: `argocd-server`, `argocd-repo-server`, `argocd-application-controller`, Redis, Dex (SSO). Multi-component footprint.
- Source: https://argo-cd.readthedocs.io/en/stable/operator-manual/architecture/

**Flux (v2)**
- Controller-based: `source-controller` (fetch git/OCI/helm), `kustomize-controller`, `helm-controller`, `notification-controller`, `image-reflector-controller`, `image-automation-controller`.
- Reconciliation is driven by `Kustomization`/`HelmRelease` CRs that reference `GitRepository`/`HelmRepository` sources.
- Generally considered **lighter** than Argo CD (no app server, no UI, no Redis/Dex by default), and better at Helm/Kustomize primitives.
- Source: https://fluxcd.io/

### 2. Footprint on a single WSL2/podman node

- Neither runs "on podman" natively. To use either you must stand up a **Kubernetes cluster on the node** (k3s/k0s/kind/minikube in WSL2). Podman does not provide an orchestration/`Pod` abstraction that these controllers drive; they need a Kube API server.
- So the realistic comparison is "GitOps controller **plus a k8s cluster** on the node" vs "plain container deploy on the node (podman systemd units / rootless containers / compose)".

| | Argo CD | Flux v2 |
|---|---|---|
| Model | App-centric (`Application`) | Controller/Kustomize/Helm-centric |
| K8s requirement | Full K8s cluster | Full K8s cluster |
| Components on node | server, controller, repo-server, Redis, Dex | source, kustomize, helm, notification, image automation |
| UI | Rich built-in Web UI | No UI (Flux UI on top of GitOps Toolkit) |
| Non-K8s (plain container) targets | No — K8s only | No — K8s only |
| Drift detection / self-heal | Yes (in-cluster) | Yes (in-cluster) |
| Relative weight | Heavier | Lighter |
| Release-tag image automation | No (external) | Yes (`image-automation-controller`) |

### 3. GitOps vs plain CI → deploy — worth it for one node?

**What GitOps genuinely buys (the pull model):**
- Git is the single source of truth for *desired* state.
- Drift detection + self-healing: a controller continuously reconciles toward Git even when something diverges on the host.
- Unattended/someone-deletes-a-container recovery.
- Audit + rollback by reverting a commit.

**Why that does not earn its keep on one node:**
- You are not running a pod workload that can be endlessly reconciled; you are running a fixed set of containers/services on one host.
- Cost: a full k8s cluster (k3s) **plus** a GitOps controller **plus** network pull cadence, for what a controlled, single-shot deploy does deterministically.
- Realistic single-node failures (disk, node down, bad deploy) are not "recovered automatically by Git reconciliation" — you need re-provisioning / backups, which GitOps controllers do not provide on a bare node.
- The pull model's biggest advantage (many clusters / many envs reconciled without CI in the critical path) does not apply to a 1-node fleet.

**Verdict:** For one node, GitOps is **not justified**. A deterministic CI → deploy workflow gives you: build, test, tag, push image, run deployment — all gateable by GitHub's native environments and protection rules (Section B). Introduce a GitOps controller only if/when the node becomes a real cluster or the fleet grows beyond a handful of hosts. If that day comes, **Flux** is the lighter, fits-helm/kustomize choice for a small footprint.

---

## (B) GitHub native primitives

### 1. Environments

An **environment** is a named target for a deployment (e.g. `dev`, `staging`, `prod`). A GitHub Actions job can declare `environment: <name>`, which:
- creates/selects that environment,
- exposes environment-scoped **secrets** and variables,
- and, crucially, **must satisfy every deployment protection rule configured on the environment before the job runs** (or before it accesses the environment's secrets).

> Docs: *"A job that references an environment must follow any protection rules for the environment before running or accessing the environment's secrets."*

This is the core hook for **approval-then-run**.

### 2. Deployment protection rules (the gating primitives)

Per-environment rules you can toggle:

- **Required reviewers** — named users or **teams** whose *approval* of the pending deployment is required before the job proceeds.
- **Wait timer** — a configurable pause (e.g. 5/10/30 min) after the workflow is triggered, before the environment job may run.
- **Deployment branches** — an allowlist (or, via a saved expressions patterns like `release/*`, `main`) restricting which branches may deploy to that environment.
- **Required status checks** — CI checks that must pass first (use existing branch-protection status checks, or custom checks with a required environment).

These are configured in the repo **Settings → Environments → *environment* → Protection rules**. Docs:
- https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments

### 3. Deployments REST API

Lifecycle endpoints (all under `/repos/{owner}/{repo}/deployments`):

| Operation | Endpoint |
|---|---|
| Create deployment | `POST /repos/{owner}/{repo}/deployments` |
| List deployments | `GET /repos/{owner}/{repo}/deployments` |
| Create/update deployment **status** | `POST /repos/{owner}/{repo}/deployments/{deployment_id}/statuses` |
| List statuses | `GET /repos/{owner}/{repo}/deployments/{deployment_id}/statuses` |
| Get pending deployments | `GET /repos/{owner}/{repo}/deployments/{ref}/pending_deployments` |
| Review a pending deployment (approve/reject) | `POST /repos/{owner}/{repo}/deployments/{deployment_id}/reviews` |
| Get deployment reviews | `GET /repos/{owner}/{repo}/deployments/{deployment_id}/reviews` |

Statuses: `pending`, `success`, `error`, `failure`, `in_progress`, `inactive`, `queued`. The environment protection rules are enforced when a deployment has status pending — this is what blocks until reviewers approve.

### 4. Deployment reviews & approval-then-run flow

The mechanism (why `environment:` alone gives you approval gating):

1. CI job declares `environment: prod`.
2. The environment has **required reviewers** + optional **wait timer** + **deployment-branch** restriction.
3. On push/PR, GitHub creates a deployment with status `pending` (blocked by the protection rules).
4. The job **pauses / waits in the pending state** until the protection rules are satisfied.
5. A required reviewer opens the Environments panel in the repo UI and presses **Review deployments → Approve** (or Reject). For teams, any member of an approved team counts.
6. On approval, the deployment transitions to `in_progress` and the job's deploy step runs. Now you can also read `github.event.deployment` / the `deployment` context within the job.

This gives you a fully-native **manual approval gate** with an audit trail (who approved/at what commit) without any third-party approval bot. It composes with:
- concurrency control (`concurrency:` group with `cancel-in-progress`),
- required status checks,
- the wait timer for a "staged rollout" delay.

Docs for the review UI & behavior: Section Viewing deployment activity + Environments management.

### 5. Deployment branches (restriction)

The **Deployment branches** rule allows either "All branches" or "Selected branches" — you configure branch patterns (e.g. `main`, `release/*`). Any deployment whose ref is not allowed is skipped/failed for that environment. Combined with required reviewers this is your standard "only main / release/* can ship to prod, and only with human sign-off."

### 6. Feature-plan caveat

Environments and protection rules require a plan that includes them:
- Free plan: environments only for **public** repositories; protection rules ignored on private repos.
- Environment secrets, required reviewers, wait timer require **Pro/Team** (or Enterprise on GHES/GHEC).

Version banner on the docs page currently reads "Free, Pro, & Team" — but the gating (protection rules, required reviewers, wait timer, deployment-branch) specifically needs the paid plan. Confirm billing for private repos before standardizing.

---

## (C) Dependency / update automation: Renovate vs Dependabot

### 1. Ecosystem / monorepo coverage

| | Renovate | Dependabot |
|---|---|---|
| **Rust (cargo/workspaces, crates.io)** | Excellent — native `cargo` manager; aware of workspace members, publishes grouped crate bumps | Supported (`package-ecosystem: cargo`), per-directory, simpler, less clever with large workspaces |
| **Python (pip / poetry / pyproject.toml / pip-tools / uv)** | Excellent — many managers (`pip_requirements`, `poetry`, `pep621`, `pyproject`, `pip-compile`, `uv`), supports locked + dynamic | Supported (`pip`, `poetry`), decent but narrower manager surface |
| **JS (npm / pnpm / yarn)** | Excellent — npm/pnpm/yarn; monorepo/workspace aware; lockfile handling | Supported (`npm`, `yarn`, `pnpm` — pnpm support has lagged) |
| Monorepo / workspace | First-class; can bump across many packages in one PR | Per-package-ecosystem and per-directory (with grouping now); coarser |

Renovate's manager breadth + workspace awareness makes it the stronger choice for a **Rust+Python+JS** mix.

### 2. Aggregation / reducing PR noise

- **Renovate:** `groupName` (and `group:` presets like `group:all`, `group:docker`, `group:typeMajorInOnePr`) let you **open one PR** for many dependencies — dramatically less noise across multi-repos. Package rules can split by major/minor, language, or update type.
  - Source: https://docs.renovatebot.com/configuration-options/ (`groupName`).
- **Dependabot:** natively opens one PR per dependency update (well-known noise problem). Grouping is now supported via `groups:` in `dependabot.yml`, but it is newer/coarser than Renovate's rules engine.

### 3. Scheduling, automerge, security

- **Renovate:** `schedule` (e.g. weekday/weekend windows), hourly PR limits, automerge on check-success, `updateNotScheduled`. Very configurable. **Security:** does discovery/vulnerability matching via its own advisories but does **not** natively consume GitHub Dependency Graph alerts the way Dependabot does; for vuln alerts you keep GitHub Dependabot alerts on.
- **Dependabot:** built-in **security updates + Dependabot alerts** off the GitHub security graph — this is its killer native feature; version updates scheduled via `schedule` in the yml; automerge via GitHub "enable auto-merge" + required status checks; known for less scheduling granularity than Renovate.

### 4. Configuration & multi-repo org management

- **Renovate** = **config-as-code** (`renovate.json` per repo, plus global config for GitHub-hosted customization). Can run as the **SaaS GitHub App** (gitHub-hosted) *or* **self-hosted** with a single global config that centralizes repos: patterns, groups, presets, scheduling apply org-wide. Best for orgs with many repos wanting consistency.
- **Dependabot** = **`dependabot.yml` per repo**, managed repo-by-repo; no org-wide config file (there's no central settings file for Dependabot update config — you mirror yml). Built into GitHub (no extra service).

### 5. Verdict for a Rust+Python+JS multi-repo org

- **Primary update bot: Renovate.** Best manager breadth (cargo/poetry/pip-tools/uv/npm/pnpm/yarn), monorepo/workspace awareness, aggregation to cut PR noise, config-as-code that standardizes an org, optional self-hosting for a single global rule set.
- **Keep Dependabot for security alerts** (Dependabot Alerts + security updates are first-class GitHub features that Renovate does not replace). You can disable Dependabot *version* updates if you use Renovate for version bumps, and rely on Dependabot purely for vulnerability detection/alerts.

---

## Recommended Architecture

### Layer 1 — Deploy engine (NOT GitOps)

- **Use a plain GitHub Actions → deploy workflow. Skip ArgoCD/Flux.**
- Rationale: single node; GitOps adds a k8s+controller control plane that buys pull-model reconciliation you do not need. Deterministic CI → deploy is simpler, cheaper, fully auditable.
- Deploy path: CI builds/test → tags/pushes OCI image (to GHCR or container registry) → deploy job SSHs into / invokes podman on the WSL2 node (`podman pull` + `podman generate systemd` unit or compose stack + `systemctl restart`). Container runs via **podman systemd** for restart-on-boot (the self-healing you actually want on a node).

### Layer 2 — GitHub native gating (standardize on this)

Standardize these across all deployable repos:

1. **Environments:** `dev`, `staging`, `prod`.
2. **Protection rules per non-default env:**
   - `prod`: **required reviewers** (a team), **deployment branches** limited to `main`/`release/*`, optional **wait timer** (e.g. 5 min), required status checks (tests + build) green.
   - `staging`: required status checks only (fast), or optional reviewers.
   - `dev`: no blockers (trunk).
3. **Approval-then-run** is automatic via the `environment:` job keyword + required reviewers (Section B.4). No external approval bot needed.
4. **Concurrency guard:** `concurrency:` group per environment with `cancel-in-progress: false` so deploys serialize/queue.
5. **Deployments/REST** used for provenance: the Actions deploy step creates/updates deployment statuses so history + "In progress / Review required" state is visible in the repo's **Environments** tab.
6. **Audit:** every push to a deployable branch, every approval, and every deploy-to-env is a recorded event (who/when/which SHA).

### Layer 3 — Update automation (standardize on Renovate + Dependabot alerts)

- **Renovate** as the version-update engine, run as a **GitHub App**, with **global config-as-code** applied org-wide:
  - presets: `config:recommended`, `group:all`-style grouping to cut PR noise,
  - per-ecosystem managers: `cargo` (workspace), `poetry`/`pyproject`/`uv`, then `npm`/`pnpm` for JS,
  - `schedule` windowed (e.g. weekday morning) as appropriate to the team,
  - each update PR runs the gate pipeline; automerge allowed only when required checks pass and only on non-prod paths.
- **Dependabot** kept **ON** for **Alerts + security updates** (native vuln coverage from GitHub's security graph) and (optionally) for lockfile security patches; **disable** Dependabot version-update schedule if Renovate takes that role, to avoid duplicate PRs.

### Acceptance criteria to confirm before adopting

- GitHub plan includes **Environments + protection rules** on private repos (Pro/Team set shown; confirm billing for your org).
- Team members are used as **required reviewers** (Teams scale better than individuals; any member of the team can approve).
- `git` (not just the default branch) is the single source of truth for *code*; deployment *desired state* for the node is captured as declarative podman/systemd or compose definitions in a `deploy/` directory of each repo (or one ops repo) — giving you a lightweight form of "GitOps the source of truth without the k8s controller."

---

## Sources

- Argo CD architecture: https://argo-cd.readthedocs.io/en/stable/operator-manual/architecture/
- Flux: https://fluxcd.io/
- GitHub Environments / protection rules: https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments
- GitHub config-and-manage deployments hub: https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments
- Dependabot options: https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuration-options-for-the-dependabot.yml-file
- Renovate configuration options (grouping etc.): https://docs.renovatebot.com/configuration-options/