# Phenotype deployment & runtime control — consolidated report

Version 0.3 · Audited design baseline, not production approval.


---

# Phenotype control systems docset v0.3

This package supersedes the deployment/runtime v0.2 design baseline by reconciling four coupled systems: BytePort/local-cloud lifecycle, Assessment Dossier convergence, Emergent Garden/ResearchLedger continuation, and quota-aware semantic review control.

Start with `STATUS.md` and `docs/25-cross-system-control-plane.md`. Machine truth is in `machine/docset.json`; generated Markdown/HTML are views.

**No operational approval is implied.** Target-environment acceptance tests remain unrun; no personal host, repository, provider billing or deployment was modified by producing this package.


---

# Status — v0.3

**State:** design baseline / integration handoff, not deployment or merge approval.

- Findings: 46
- Proposed functional requirements: 58
- Target-environment acceptance tests: 58, all `not_run`
- Decision records: 18
- Work packages: 21
- Source records: 79

## Highest-priority live blockers

1. Current canonical owner/module for the local-node daemon/provider path is unresolved.
2. Foreground reserve/QoS values for the desktop and laptop have not been measured.
3. Emergent Garden Wave 5 is preserved on a closed-unmerged ResearchLedger PR and must be reconciled into source authority.
4. Review provider quotas/credits are dynamic; live account state and historical backlog size are not yet inventoried.
5. Existing deployment v0.2 operational acceptance tests remain unrun.

Package validation proves internal consistency only.


---

# Changelog

## 0.3.0 — 2026-09-12

- Generalized the v0.2 delivery baseline into four coupled control systems.
- Added local personal-device compute as a capability-qualified BytePort provider design with node-daemon, QoS, immutable pull delivery, stateful lifecycle and safe update contracts.
- Elevated human/agent/automation parity to a global product tenet.
- Reconciled the audit/scorecard question to one Assessment Dossier with inventory and evaluation phases.
- Audited Emergent Garden current state: preserved Wave 5 work on ResearchLedger PR 81 is closed unmerged; downstream registry projection is merged. Added salvage-before-new-wave plan.
- Extended the existing review-control contract into a live quota-aware broker, zero-new-spend policy, normalized finding model and historical merged-PR reconciliation lane.
- Added local-node and review-provider machine schemas/examples.

## 0.2.0

See the prior deployment/runtime baseline retained in repository history/package lineage.


---

# Cross-system control plane

These four workstreams should share primitives without collapsing their domain authorities.

| System | Canonical object | Scheduler/control concern | Evidence concern |
|---|---|---|---|
| BytePort/local cloud | desired deployment + observed target state | placement, lifecycle, resource budget | artifact/target/health/recovery receipt |
| Assessment | Assessment Dossier | applicability and measurement execution | qualified observations/verdicts |
| ResearchLedger corpus | source/claim record + bounded projection | research work packages | provenance, source revision, experiment evidence |
| Review control | normalized review finding + review run | provider quota/risk dispatch | finding adjudication/remediation receipt |

## Shared primitives to reuse

- stable subject/candidate identity;
- immutable or append/supersede evidence;
- plan versus apply separation;
- idempotency and leases;
- capability discovery instead of assumption;
- budgets as explicit policy objects (CPU/VRAM, money/credits, review quota, research scope);
- event streams and receipts;
- exact revision binding;
- unknown/blocked distinct from fail/pass;
- a human/agent/automation-neutral API surface.

The mistake to avoid is a "mega ledger" that owns all four domains. Share schemas and evidence conventions while keeping ResearchLedger, Assessment Dossiers, deployment state and review findings under their real owners.

## Priority order

1. **Authority recovery:** current owners, closed-unmerged research branch, historical BytePort contracts, review backlog identity.
2. **Control contracts:** local-node capabilities/QoS, review provider state, Assessment Dossier staging.
3. **One narrow executable slice each:** one disposable local service; one real assessment dossier; PR-81 salvage; one historical review backlog sample.
4. **Metrics and adaptation:** resource interference, provider yield/quota efficiency, assessment instrument quality, research experiment outcomes.
5. **Only then broaden coverage.**

This ordering intentionally attacks the contradictions first: we should not automate a control plane whose authority is ambiguous, score evidence before applicability is settled, restart research that already exists on an unmerged branch, or spray review calls before quotas are modeled.


---

# Local cloud and qualified personal compute nodes

## Decision brief

Treat a personal desktop, laptop, workstation or future small node as a **qualified local provider target**, not as a generic self-hosted runner and not as a new public cloud. BytePort remains the experience/control plane; a privately connected node daemon exposes capabilities, receives desired state and pulls immutable artifacts. S052, S058.

This deliberately separates three layers:

| Layer | Owns | Must not own |
|---|---|---|
| BytePort control plane | project/repository linkage, environments, desired state, provider selection, lifecycle, evidence, GUI/API/CLI/SDK | hypervisor/runtime internals unique to one node |
| local-fleet provider | node inventory, placement, capability matching, lease/admission, provider-specific plans | a second project registry or GUI truth store |
| node daemon/runtime adapters | artifact pull, local execution, health, resource enforcement, volume/device hooks, safe daemon update | portfolio-wide deployment authority |

Historical BytePort work already described a local `nvms + vLLM` tier and later compute-mesh desired state, but both inspected PRs are closed and unmerged. They are design ancestry, not current implementation authority. S059, S060.

## Why not just install a full private cloud?

The alternatives are useful references but fail as a universal default:

- **Kubernetes/Nomad/OpenNebula-style cluster everywhere**: good for dedicated servers; poor fit for a laptop or gaming/LLM workstation that must remain primarily a human machine.
- **Incus/Proxmox as the product boundary**: useful execution substrates and excellent reference semantics for VM/container/resource limits, but they do not replace BytePort's cross-provider lifecycle. Incus is therefore an adapter candidate, not the canonical API. S076, S077.
- **GitHub self-hosted runner as the abstraction**: handles jobs, not durable databases, volumes, service health, VM lifecycle or provider portability.
- **CI pushes over SSH/root runtime socket**: easy to prototype, but expands credentials and inbound/control authority on personal machines.

The selected shape survives these contradictions: BytePort plans; provider adapters qualify; the daemon executes.

## Node capability record

A node record should include at least:

```text
node_id / owner / trust_state / agent_version
os / arch / virtualization / container / wasm / native adapters
cpu topology + allocatable / memory total+reserve / disks+IO / network
GPU devices / VRAM / passthrough or exclusive-lease capability
battery / power / thermal observability where available
runtime versions and feature flags
volume/back-up capabilities
private connectivity and identity state
current host mode / drain state / workload leases
```

A missing capability is **unknown/unsupported**, never inferred from operating-system family.

## Foreground reservations and modes

The old runner design's process-pause idea is too narrow. Use explicit host modes whose values feed admission and preemption, for example:

| Mode | Typical intent | Background policy |
|---|---|---|
| `interactive` | normal foreground use | preserve CPU/RAM latency reserve; no surprise exclusive devices |
| `creator_audio` | Ableton/low-latency audio | large CPU/RAM reserve, protect real-time scheduling and disk IO, normally no disruptive updates |
| `gaming` | foreground game | reserve GPU/VRAM exclusively and substantial CPU/RAM; preempt eligible GPU workloads |
| `llm_local` | local inference | explicit GPU/VRAM lease; competing GPU deployments blocked or drained |
| `idle` | machine available | highest allocatable background envelope |
| `maintenance` | upgrades/recovery | drain normal workloads; allow lifecycle operations only |

The mode is only one signal. Battery state, thermals, disk pressure and user-defined per-node reserves also gate placement. Laptop defaults should be substantially more conservative than a desktop, but this docset does **not** invent exact percentages before measurement.

## Workload contract

Every workload declares resource requests/limits plus `priority`, `preemptible`, `eviction_grace`, `stateful`, device requirements and recovery expectations. Stateful workloads additionally declare volume identity, backup/restore behavior and RPO/RTO. A containerized Postgres instance is not automatically equivalent to RDS, Supabase or Neon.

## Release and update path

```text
Git commit
  -> deterministic CI + selected review gates
  -> immutable artifact + SBOM/provenance
  -> registry/artifact store
  -> BytePort desired-state authorization
  -> private/outbound node notification or reconciliation
  -> node pulls exact digest
  -> local runtime adapter stages/restarts/health-checks
  -> node reports observed digest + health + resources
  -> controller commits deployment receipt
```

Daemon updates use the same discipline: staged version, compatibility check, health, rollback. A daemon upgrade must not erase desired state or orphan workloads.

## Production versus local placement

Local nodes are first-class **targets**, not automatically production-quality targets. The same workload can be planned against local, PaaS, VPS or hyperscaler providers. The planner returns exact/approximate/unsupported semantics and costs/risks. Promotion can move a workload without pretending every provider offers identical managed behavior.


---

# Human, agent and automation interface tenet

## Global product rule

The user's requirement is stronger than "have an API": **humans, agents and automations are all first-class users**. S052.

The durable rule should be adopted at governance/charter level across products:

> One capability model, one authorization model, one observable state and evidence model; multiple ergonomic clients.

## Surface contract

| Surface | Optimized for | Required properties |
|---|---|---|
| GUI | discovery, comprehension, approvals, visual state | every mutation maps to public typed operations; no hidden state |
| CLI | expert/operator speed | script-safe modes, JSON output, stable exit codes, explicit plans/diffs |
| SDK | composition | typed models, idempotency, retries, pagination, streaming/events |
| agents | reasoning + tools | compact schemas, explainable failures, dry-run, bounded actions, receipts |
| automations | unattended reliability | deterministic identifiers, idempotency keys, event cursors, leases, backoff semantics |

The GUI may aggregate and visualize. It must not possess an unexported deployment capability that agents cannot invoke. Conversely, an agent-only privileged backdoor is not acceptable simply because agents are important.

## Mutation envelope

For meaningful mutations, expose a common lifecycle:

`discover -> plan -> validate -> authorize -> apply -> observe -> reconcile/recover`.

Return machine-readable preconditions, unsupported capabilities, cost/budget impact, exact target and artifact identities, and receipts. Human confirmation can be one authorization policy; automation can use pre-authorized policy scopes. Both operate on the same candidate object.

## Why this matters beyond BytePort

The same rule applies to Tracera evidence, AgilePlus work graphs, review control, assessment dossiers, ResearchLedger and future products. It prevents a recurring failure mode where agent-generated automation becomes a separate unobservable system beside the user-facing application.


---

# Assessment dossier convergence

## Resolution of the "inventory versus scorecard" question

Use **one logical Assessment Dossier with two operational phases**, not two canonical systems. This matches the already-developed Master Assessment Kit contract. S053, S054.

### Phase A — inventory / applicability / evidence map

Populate subject identity, component BOM, beneficiary/scope, claims, observed artifacts, requirements, assumptions, missing obligations, evidence references and applicability. Measurement/verdict/score fields remain `unknown` or null.

The purpose is to answer **what exists, what is claimed, what applies and what can actually be measured?**

### Phase B — evaluation / score / decision

Bind selected criteria to qualified instruments, execute them, record raw observations, verdicts, freshness, reviewer state, findings and decisions. Only now calculate scoped metrics.

The purpose is to answer **what did the qualified evidence establish for this exact scope?**

## Why a single dossier is better

A separate inventory truth store plus scorecard truth store creates subject-identity drift, duplicated evidence, stale applicability and "100%" scores over different denominators. The dossier already separates these concepts internally, so the UI can present two stages without splitting authority.

## How to absorb existing scorecards

Do not throw away the 88-pillar/large rubric work. Convert it into:

- versioned **criterion catalogs**;
- **profiles** that select obligations for product/repository/slice types;
- **measurement bindings** defining the real instrument/fixture/threshold/freshness rule;
- generated human and machine views.

A linter pass, a document's existence, an exercised behavior and proven consumer value remain distinct predicates. Unselected is unassessed, not automatically N/A. A waiver does not become a pass. S053.

## Recommended canonical row lifecycle

```text
criterion instance
  -> applicability: applicable | not_applicable | unresolved
  -> evidence/instrument qualification
  -> execution: not_run | blocked | executed | stale
  -> verdict: pass | fail | unknown | contested | waived
  -> review disposition
  -> finding/decision linkage
  -> generated score/view
```

This directly supports the user's desired workflow: during inventory the score column is effectively empty; later evaluation fills it without copying the row into another authority.


---

# Emergent Garden corpus — actual status and restart packet

## Current status

This work **did not merely fail and disappear**. The exact ResearchLedger PR-81 head contains substantial Wave 5 research and executed package validation. PR 81 reports 70 offline tests rerun after extraction, 32 synthetic admission cases, 74 public uploads reconciled and explicit remaining gaps. S061, S062.

But the integration state is bad:

- ResearchLedger PR **#81 is closed, draft and not merged**. S061.
- The reviewed current `main` snapshot did not expose `docs/corpora/emergent-garden/research/README.md` at that path. S063.
- phenotype-registry PR **#550 did merge** a routing projection pointing at the pinned ResearchLedger evidence head. S064.

So the failure is primarily **source-authority integration**, not absence of research output.

## Do not restart from YouTube

The first action should preserve the exact PR-81 head and published artifact/hash records, compare its tree against current main, and decide whether to rebase/cherry-pick/reconstruct a minimal new PR. Do not redo the crawl just because the original PR is closed.

## Restart sequence

1. Pin `8822aa14baef2a964288076645edcc493c338688` and the publication artifact/hash from PR 81.
2. Diff its corpus paths and supporting scripts against current ResearchLedger main.
3. Classify conflicts as already-landed elsewhere, superseded, still-needed or stale.
4. Rebuild a clean source-authority integration branch from current main containing only still-valid records/tools.
5. Rerun the corpus bundle verifier, all 70 offline tests and synthetic admission cases; record any changed denominator rather than forcing the historical counts.
6. Land or explicitly supersede the source authority.
7. Update/qualify downstream projections such as phenotype-registry routing.
8. Only then continue independent remaining research lanes.

## Remaining lanes are independent

The branch itself says these remain open: full transcripts, exhaustive audience semantic review, broad recursive nested-source closure, complete historical behavior/lineage reconstruction, the persistent one-comment discrepancy and a live coordination/Benchora experiment. S061, S062.

Do not roll these into one giant "finish corpus" percentage. Each receives its own evidence denominator and stop condition.

## Authority

ResearchLedger remains the source/claim authority. Downstream project comments and registry links are bounded projections, not permission to alter product behavior automatically. The corpus can inspire hypotheses; it does not prove that more agents, a particular emergent architecture, or any transferred technique improves a target project until an experiment does so.


---

# Review broker and historical finding reconciliation

## Goal

Extend the existing review/GitOps controller into a **quota-aware semantic-review broker**. Do not create a second review product. S052, S065.

The user's current provider set is already large enough: Kilo, CodeRabbit, CodeAnt, Macroscope while existing credit remains, Codex, plus deterministic and existing GitHub/security tooling. A sixth semantic reviewer is not a default requirement.

## Live provider facts that matter

| Provider | Useful current control | Budget/limit implication |
|---|---|---|
| CodeRabbit | auto-review can be disabled; labels/description/manual `@coderabbitai review`; pause/resume/full review | Free PR bucket documented at 3/hour; OSS may vary 1–8/hour; actual PR evidence hit a reset wait. S067-S069, S078 |
| CodeAnt | CLI can enumerate unresolved provider comments and resolve by thread/comment id | Useful for reconciliation; resolving is an action after adjudication, not the adjudicator. S070 |
| Kilo | GitHub reviewer, free models can be selected | Free models can be upstream-rate-limited/change over time; auto update reviews can waste capacity. S072-S073 |
| Macroscope | usage-priced review with spend caps; initial/free credit may exist | finite-credit specialist lane; `cash_spend_allowed=false`, auto-refill off. S071, S079 |
| Codex | GitHub review included within ChatGPT/Codex plan usage; `@codex review` supported | shared scarce subscription allowance; current remaining quota must be observed rather than treated as free. S074-S075 |

Deterministic tests/security remain outside this table: they are gates, not semantic-review quota competitors.

## Provider adapter state

```text
provider_id
health / auth / repository_eligibility
trigger_mode: automatic | label | comment | cli | unavailable
quota_remaining / reset_at / quota_confidence
credit_remaining / cash_spend_allowed / auto_refill
max_files / max_bytes / supported languages/specialties
supports_incremental / supports_full / supports_resolve
last_success / latency / reliability
unique_valid_yield / duplicate_rate / false_positive_rate
```

Do not encode CodeRabbit as "2/hour" or any other remembered constant. Refresh effective state because plan, OSS classification and fair-use windows differ.

## Risk-tier scheduler

A default policy can be:

- **R0**: deterministic gates only; docs/generated/trivial changes where semantic review is explicitly unnecessary.
- **R1**: one semantic reviewer selected for availability and fit.
- **R2**: primary reviewer plus one orthogonal specialist if risk warrants.
- **R3**: release/security/high-impact change; at least two independent semantic perspectives where capacity permits, plus all mandatory deterministic/security gates.
- **R4**: explicitly budgeted review summit for disputed or unusually high-risk work; never the default.

A provider being unavailable does not make a PR green. The broker either selects an allowed substitute or reports a blocked policy requirement.

## Quota discipline

- Disable/limit automatic per-push review where supported.
- Do not request review while the coding agent is producing rapid intermediate commits.
- Dispatch after a coherent candidate/repair batch.
- Reserve scarce reviews for exact-head final passes and escalations.
- Use bounded retries only for transient provider failures; quota exhaustion waits for reset/fallback instead of hammering the endpoint.
- Never enable paid overage or auto-refill under the current zero-new-spend authority.

## Common finding record

Normalize every provider finding into one record:

```text
finding_id / provider / review_run_id
repo / PR / base_sha / head_sha
path / diff anchor / semantic signature
severity / confidence / category
provider text reference (not copied authority)
status: valid_current | fixed_unresolved | stale_revalidate | duplicate |
        false_positive | accepted_risk | unclear
supersedes / duplicate_of
adjudication evidence
remediation PR/commit/test receipt
thread resolution receipt
```

## Historical reconciliation algorithm

1. Enumerate open PRs, recently merged PRs, then older backlog by risk and unresolved age.
2. Fetch review threads/comments from every installed provider plus human reviews.
3. Normalize and deduplicate findings.
4. Revalidate the code fact against the relevant current revision.
5. **Open PR:** repair valid findings on the current branch when still in scope.
6. **Merged/closed PR:** inspect current default branch. If the defect survives, open a new remediation PR; otherwise record `fixed_unresolved`, `stale`, `duplicate`, `false_positive` or `accepted_risk` with evidence.
7. Resolve old threads only after disposition is grounded.
8. Run exact-head deterministic gates and selected semantic final review.
9. Record review yield and remaining backlog.

ForgeCode PR 277 demonstrates why this matters: earlier audit evidence found unresolved material threads, and the PR is now merged. Current comments also show CodeAnt continuing while Copilot and CodeRabbit hit quota/limit states. S065-S068.

## Metrics

Track unique valid findings per review, duplicates, false positives, remediation rate, median latency, quota consumed per valid finding, cash/credit consumed, unresolved age and provider availability. Add another default reviewer only when these data show marginal value or useful independent availability.


---

# Reference landscape and alternatives

The platform should model **capability classes**, not encode a fashionable provider list as architecture.

## Provider classes

- Hyperscale IaaS/platform: AWS, GCP, Azure and peers — broad primitives and deep operational controls.
- Developer PaaS/edge: Vercel, Render, Railway, Fly.io, Heroku, Netlify, Cloudflare and peers — narrower abstractions with strong deployment DX.
- VPS/commodity cloud: Hetzner, OVHcloud, DigitalOcean, Vultr/Akamai and peers — simple machines/network/storage with operator-owned higher layers.
- Managed data/backend: Supabase, Neon, PlanetScale, Turso/Aiven and peers — database/backend semantics that cannot be reduced to "a container is running".
- Local/private execution substrates: Podman/WSLC/native/NVMS/Incus and potentially dedicated-host platforms — execution implementations beneath the BytePort provider contract.

The important output of planning is therefore not `provider = X`. It is a capability-qualified plan that states which semantics are native, emulated, approximated or unsupported.

## What to borrow from existing private-cloud systems

Incus is a useful reference because its REST API exposes resources, instances and backups and its configuration includes CPU/memory/IO limits. S076-S077. That supports the v0.3 contract design, but does not establish that Incus should be installed on the user's laptop or desktop.

Dedicated-node private clouds can become optional adapters later. The default personal-device path should stay lighter because those hosts retain interactive, creator, gaming and local-inference duties.

## What to borrow from managed PaaS

The target UX is the good part: repository linkage, build/deploy histories, previews, environment promotion, health, rollback, logs, managed secrets and clear state transitions. The local provider should reproduce the **control experience where the underlying capability exists**, not fake managed durability or HA it does not have.


---

# What the full session changes

## Bottom line

The earlier v0.1 design was directionally useful but lacked decisive implementation evidence and part of the product intent. The full stored session now supplies both. **The recovered pilot should be treated as a failed qualification fixture, not a deployment-ready implementation.** Repair it within the existing ecosystem rather than installing it and discovering these defects against a live service.

This is not a blanket judgment on every repository or all work performed in that Forge session. The strongest conclusions concern the exact caller, reusable nightly workflow, branch JSON and Blueprint that the session read back. Later source states and live deployments require separate receipts. [S032; S033]

## 1. The real scope is an API-driven local/managed lifecycle

E001 calls for the dev backend to join the desktop, for an eight-hour OR greater-than-one-new-commit cadence, and for production to require maximal CI strictness plus another trio-style run before final confirmation. E002 asks for managed-service-like ergonomics on the local node. E003 explicitly keeps the application/GUI layer in BytePort and asks for plans at the API/automation layer. E004 names the existing ecosystem and recalls PhenotypeActions as a possible home for GitOps work. E005 preserves the runtime and GitHub plan preference.

Consequences: a second GUI is outside scope; a second managed Render dev service is not the requested default; a generic local process launcher is insufficient; and “project agnostic” cannot mean every repository is a web service. CLI packages, libraries, desktop releases and documentation have different delivery outputs. The portable object is a typed application/environment contract with provider bindings—not a promise of identical implementations everywhere.

The domain/tailnet feedback in E006 further favors private access for internal services. Public reachability is an explicit exception. A polished API should handle lifecycle and evidence without requiring the human to paste tokens into ad hoc commands. These are design requirements, not claims that the current products already provide them.

## 2. The candidate trio is recoverable, but not yet trustworthy authority

The prior CI audit identifies `ci / lint`, `ci / test` and `CI`; a current connected read of Tracera’s CI file independently shows those job-name declarations. Our v0.1 claim that the members were unavailable is therefore superseded. However, the historical protection JSON records `ci/lint` and `ci/test` without spaces. Normalizing those names is not harmless if the enforcing system expects exact check contexts. [E008; E013; S034]

There is a second problem: names are not execution coverage. The fetched final `CI` aggregate lists dependencies including `detect-changes`, `dependency-review` and `trunk-check`, but its result-checking array omits those three. The displayed aggregates reject failure/cancellation but do not themselves require an explicit reason for a skipped dependency. Some skips may be valid path-based exclusions; production requires evidence that they were intentional and sufficient, not a universal skipped-equals-success rule.

Resolve actual check-run/context identifiers and trusted app/workflow provenance against the exact candidate. The list must come from the current policy and observed GitHub results, not merely job names or a JSON file. A stricter production rerun must exercise the candidate and required coverage; renaming a green aggregate is not a rerun.

## 3. GitHub cannot call the stored reusable-workflow path as written

The recovered caller references `.github/workflows/reusable/nightly-dev-deploy.yml@main`. GitHub documents reusable workflow files directly under `.github/workflows`; subdirectories are unsupported. A YAML parser can parse the file while the platform rejects the workflow reference. This is a semantic qualification failure. [E007; E009; S036]

The connected exact-path lookup also returned 404 during this audit. That is a separate observation: it does not prove the historical local file was never written or that no valid renamed replacement exists. Repair must first locate the canonical shared implementation, then version/pin a supported caller path and verify actual resolution.

## 4. The candidate being tested is not bound to the image being deployed

E010 defines `runtime: image` and an image tag ending in `:latest`. E009 checks out the caller’s source, runs configurable build/test commands, then triggers a Render deploy with `commitId`. It does not publish the image produced from that source or select its immutable digest. Render distinguishes Git-backed commit selection from deploying an existing image. [S037; S038]

Even a successful local build would therefore not establish that the runtime uses those tested bytes. The repair is not “add a commit label”: select a source mode, build once, publish an immutable artifact, record source/build provenance, and bind deployment and approval to its digest. Promote that same digest across eligible environments. For Git-backed managed builds, capture and verify the provider’s resulting artifact/revision instead of claiming prebuilt-image semantics.

The Blueprint also declares automatic deployment on the purported manual fallback and includes unsupported-by-this-evidence OIDC comments. Treat those as unverified configuration claims. The visible nightly uses a bearer API key; a comment does not establish an OIDC trust exchange or disable alternate deployment paths.

## 5. Failure handling is not rollback

The complete 205-line nightly implementation polls for live state and performs a health request. Its failure paths exit nonzero. There is no stored previous deploy ID, invocation of a rollback action/API, data compatibility decision, or post-recovery observation in that recovered file. [E009]

A nonzero job conclusion is useful but does not undo a deployment. The Render rollback API is a separate operation referring to a previous deployment, and invoking it does not inherently disable future automatic deploys. App-level recovery additionally depends on schema/data compatibility. [S039]

The design now separates failed promotion, recovery requested, recovery in progress, recovery observed and service still unknown. Restoring executable bytes is not sufficient when a migration has changed the database. A recovery receipt must describe both code/config and data state.

## 6. The trigger silently changes the requested policy

The user requested every eight hours OR **more than one new commit**. The caller has every-eight-hour cron plus every `main` push. The callee only compares the live commit to the checkout SHA. One new commit can therefore trigger deployment; no commit-count threshold is evaluated. The comment stating that every push naturally implements `>1` is false. [E001; E007; E009]

The comparison also presumes that the provider can supply the relevant live source identity. The listing reads only 20 deployments, assumes a response shape and treats no matching live commit as a reason to deploy. Missing/unknown provider state should not become approval. Pagination and recorded response fixtures are required; this audit does not claim a specific alternative JSON shape was proven. [S051]

A typed scheduler and reference truth table now preserve the literal threshold, use a last **observed healthy** candidate as the watermark, reject unknown/divergent ancestry, coalesce offline work and separate eligibility from authorization. Time-based eligibility is not a hard guarantee of execution while a desktop is unavailable.

## 7. Health, secrets and fallback storage need qualification

The caller uses `/health`; the Blueprint configures `/healthz`. Both could exist, but no contract or test proves that. Worse, the nightly exits successfully when it cannot resolve the service URL, skipping health validation. Unknown observation cannot produce a healthy promotion receipt. [E007; E009; E010]

The caller explicitly forwards only `RENDER_API_KEY`, while the callee needs a service ID through an input or secret. A configured environment secret could satisfy that dependency, but its presence was not established. Repository secrets are not automatically forwarded merely because a called workflow names them. Validate the actual secret-delivery contract without displaying values. [S036]

Build/test command strings run in the same job that exports provider credentials. That enlarges the trusted code surface. Separate untrusted or general build execution from the actuator’s credentials, then verify provenance at the boundary. The Blueprint’s static authentication values and in-memory SQLite settings are unsuitable defaults for a durable reusable fallback. Selected evidence redacts those values; their presence does not establish live compromise.

## 8. Stored output completeness needs its own audit

The initial workflow report repeatedly says 24 files while listing 25 rows. It also mixes runner labels and deployment environments in its prose. A later compaction frame calls the pilot production-ready while a readback shows modified/untracked manifests and the defects above. These are specific examples of summary drift—not grounds to assume every report is wrong. [S032; E011; E016]

The report-recovery map distinguishes exact write payloads, partial reads/patches and no direct body recovered. Both final Free/student and Podman/WSL/PaaS follow-up audit bodies remain unfinished or unrecovered in the retained contexts. A descendant’s VSOCK “stable” verdict relies on lack of negative evidence and should not be promoted to compatibility proof. Podman’s documented networking primitives do not establish that the proposed inter-service path uses VSOCK at all. [E014; E015; S041]

## 9. External corrections do not erase the user’s requirements

Render’s free-service budget is not literally a one-service rule; its documented shared hours and storage limits still matter. Correcting that misconception does not change the user’s selected local-dev placement. LocalStack’s March 2026 transition changed image/access distribution; the product did not disappear. A replaceable local API surface can use focused emulators for tests and actual durable services for stateful work, with separate claims and tests. [S040; S043–S047]

## Recommended order

Resolve authority and active revisions; repair the platform-invalid workflow call and exact check coverage; specify one local service profile; prove the event predicate and trusted build/apply boundary; then qualify one private route and real recovery. Add a managed binding only after its source mode, state, identity and recovery behavior are explicit. The goal is one demonstrated end-to-end path, not another completed-looking stack diagram.


---

# Lifecycle and delivery profiles

**Proposed contract.** FR-DEP-025 through FR-DEP-030 expand the original requirements without asserting a working implementation. The reference schedule evaluator tests this policy locally; the target-environment acceptance catalog remains unrun.

## Separate the four identities

A **workload** is the product component and its execution needs. An **environment** is an isolation/policy/data lifecycle such as dev, preview or prod. A **target** is the qualified execution location and runtime. A **candidate** is the immutable set of source/artifact/configuration/policy bindings to be promoted. None of these is simply a Git branch name.

Example: `tracera-server / dev / local-desktop-podman / candidate-42` and `tracera-server / prod-fallback / managed-image-service / candidate-42` share a workload and may share an image digest. They do not share data identity, secret grants, route policy or approval automatically. A second target in the same environment must have an explicit writer/failover policy; it is not automatically active-active.

### Delivery profile matrix

| Profile | Primary output | Applicable gates | What must not be inferred |
|---|---|---|---|
| Resident API/service | Qualified running process/image + endpoint and data bindings | Health, exact artifact observation, access, recovery, resource limits | A successful build means a healthy deployed service |
| Worker/scheduled job | Qualified execution definition + durable completion/checkpoint semantics | Idempotency, retries, cancellation, duplicate delivery, state ownership | HTTP health alone certifies useful work |
| CLI/library/package | Versioned, signed where applicable package and release metadata | Tests, package content, install/use/uninstall, provenance, compatibility | It needs a public server or persistent container |
| Desktop app | Per-platform bundle, distribution/update metadata | Build/signing, install/update/uninstall, smoke tests, UX/AX coverage where applicable | Backend deployment tests certify the desktop release |
| Documentation/static site | Versioned content bundle + publication receipt | Build, links, accessibility, routing/cache consistency | It should share production application secrets |
| Data migration | Versioned migration/restore procedure with state evidence | Forward/backward compatibility, backups, integrity and recovery | Code rollback necessarily reverses data changes |

A repository can publish multiple profiles. A monorepo change may affect several; a pure library may have no deploy profile. Required checks derive from the profile and change scope, not a one-size-fits-all shell command.

## Environment policy

**Dev:** default to the local desktop/qualified preferred-runtime target, as requested. Keep the same CI definitions used for production; a dev profile may use a declared subset or lower isolation requirement when risk permits, but must not silently swallow failures. Failure should preserve the previously observed healthy generation or remain explicitly degraded.

**Preview:** optional, keyed to an immutable candidate or PR revision, with a declared time-to-live and cleanup owner. Use isolated disposable data and credentials. A preview route is private unless an approved profile explicitly makes it public. Closing a PR is a cleanup request, not proof that all resources were deleted.

**Prod:** require the full approved check set, maximal profile strictness, a fresh qualifying rerun as requested, and final authorization bound to the exact plan and candidate. The deployment authority must not be editable by the candidate it judges. A Git tag, green named aggregate or manual dispatch alone is not approval.

**Prod fallback:** a separate, declared recovery destination. Specify whether it is cold standby, warm standby or manually restored. Capture data freshness and expected recovery time. Do not name an in-memory scratch service “fallback” and imply it preserves the primary service’s data.

**Other environments:** add a profile only with an owner, target class, access/data lifecycle, entry/exit gates and retention policy. Do not generate empty stage names for visual symmetry.

## Precise interpretation of “every 8 hours OR >1 commit”

The chosen policy preserves the literal greater-than comparison:

```text
candidate_changed
AND (scheduled_tick_due OR new_eligible_commits > 1 OR authorized_force)
AND identity_and_lineage_known
```

For a first deployment, require a separate explicitly authorized bootstrap. For existing deployments, use the most recent **observed healthy** candidate, not the latest attempted workflow, as the watermark. The candidate key includes artifact, config, target binding and policy; a source SHA alone cannot represent all deployment-relevant changes.

The schedule is a due-work policy. One proposed implementation uses a fixed UTC three-times-daily cadence with a non-top-of-hour offset; another uses elapsed time since the last healthy observation. These are different semantics. The implementation must select and record one rather than quietly mixing them. This package chooses **fixed scheduled ticks for the reference policy**, with offline ticks recorded as pending reconciliation. Exact cron offset is an implementation/configuration choice, not a recovered user requirement.

### Decision table

| State at evaluation | Result | Why |
|---|---|---|
| Same candidate already observed healthy | No-op | No new artifact/config/policy to promote |
| One new commit, ordinary push, no tick due | Defer | `1 > 1` is false |
| Two new eligible commits, push | Eligible for CI/policy evaluation | Threshold met; not yet permission to deploy |
| One new commit, scheduled tick due | Eligible for CI/policy evaluation | Time alternative met |
| Config-only changed candidate, tick due | Eligible for CI/policy evaluation | Candidate changes are wider than source commits |
| Unknown last successful state or unknown ancestry | Block | No safe comparison or implicit bootstrap |
| History diverged/force-pushed | Block and reconcile | Do not infer positive change count from unrelated history |
| First deployment, explicit bootstrap authorization | Eligible after all other qualification gates | Distinct decision, not missing state interpreted as success |
| Authorized force of a changed candidate | Eligible after all other gates | Force bypasses scheduling delay, not CI or authority |
| Force requested without authorization | Block | A client-supplied flag cannot grant authority |
| Target offline and candidate eligible | Queue/coalesce latest desired candidate | Do not claim a deployment or advance watermark |
| Environment lease held elsewhere | Coalesce | One writer owns that environment generation |

“New eligible commits” means a versioned graph/counting rule, for example first-parent commits between observed source revision and candidate source revision on the declared integration branch. A merge/squash can make counts differ from contributor commits. Record that choice. Fail or request reconciliation if the observed revision is not an ancestor; do not silently treat unrelated histories as a large delta.

## Coalescing and concurrency

Maintain one active promotion lease per workload/environment writer domain. A lease holder must use a fencing/generation token so an expired holder cannot write after a new holder takes over. An in-memory mutex is not sufficient across multiple controllers or restarts; an existing durable controller/state owner must provide the lease semantics.

A new candidate arriving during a deployment updates desired state but does not mutate the in-flight candidate. After the current candidate succeeds or fails, reconcile to the latest eligible desired candidate. Never deploy a backlog of 200 obsolete commits merely because the desktop was offline. Never reuse an authorization for a replacement candidate.

Avoid cancelling a process in the middle of an unsafe migration just to prioritize the latest push. Cancellation must enter a declared safe checkpoint or recovery state. The next controller must observe unfinished work rather than assuming a cancelled CI job means the external deployment stopped.

## Artifact and check binding

For an image profile: build source once, capture its build inputs and test results, publish an immutable digest, and promote that digest. For a provider-managed Git build: pin the source and capture the provider build/deployment result and observed revision. A local binary profile records the executable/package digest and launch configuration. Unsupported source-mode conversions return a qualification error.

Checks and approval bind to candidate identity, plan hash, target generation, policy version and relevant check-run evidence. A changed artifact, configuration, policy, secret version or target binding invalidates the approval when it changes the approved risk or semantics. Secret values never belong in candidate documents; use secret version references and server-side grants.

## Post-deployment observation and recovery

Readiness requires a live observation of the intended candidate, a profile-defined health probe, and any essential application/data invariants. Missing URL, unrecognized provider status, unhealthy response, stale observation or mismatched identity means unknown/failure—not success.

On failure, preserve the prior observed healthy candidate reference. Determine whether code/config reversal is safe with current data. Execute the approved recovery plan and observe recovery independently. Only then advance a recovered-state receipt. A failed recovery must remain prominently degraded or unknown, not converted into a successful rollout summary.

## Reference artifacts

`tools/schedule_policy.py` implements the scheduling portion as a pure function. Its inputs represent facts that a real controller must obtain through trusted observations. It performs no GitHub queries, credential retrieval, network requests or deployments. Its passing tests validate predicate behavior and reject malformed inputs; they do not establish that a real provider or host supplies truthful inputs.


---

# API and service-binding contract

**Proposal for the existing controller boundary, not a new service or GUI.** BytePort remains the user-facing application. The contracts below should be implemented or adapted in the canonical existing deployment/runtime modules after current ownership is resolved. [E003; E004; S002–S006]

## A useful local managed-service surface

The user’s request is more than container startup. A caller should be able to describe an application profile, inspect a plan, bind services and secrets, request an authorized promotion, observe the intended and actual generations, recover, and retire ephemeral environments. The API should expose the same lifecycle concepts on local and managed targets while returning explicit unsupported capabilities.

Do not hide provider-specific limitations. A local Postgres instance, a Supabase deployment and a managed Postgres service can share a database binding class without sharing auth, storage, realtime, backup or branching features. “Portable” means a declared compatibility contract and tested migration path, not a common JSON wrapper around incompatible behavior.

## Logical ownership, with physical location unresolved

| Concern | Logical owner | Boundary |
|---|---|---|
| Human UI and application experience | BytePort | Consumes the control API; does not become a second hidden actuator |
| Desired state, plans and deployment receipts | Existing canonical deployment controller | One writer per target/environment, explicit policy and idempotency |
| Workload graph/runtime capability resolution | Existing PhenoCompose/nanovms/runtime modules as currently authoritative | No duplicate graph store or second independent reconciler |
| Host/provider infrastructure state | Existing IaC authority and provider adapters | Exclusive ownership/locking for each resource; no competing state owners |
| CI/release orchestration | Existing shared workflow owner; investigate recalled PhenotypeActions | Reusable producer interfaces, pinned callers, trusted checks |
| Contracts, decisions and shared types | Existing specification/type authorities | Versioned schemas with compatibility rules |
| Research, traces and audit/session evidence | Existing ledger/observability owners | Import references and receipts; do not create another registry |

This table allocates responsibilities, not repositories to rename or merge. Current consumer imports, ADRs and immutable revisions must resolve the physical owner. The presence of a similarly named repo is not enough.

## Proposed operation contract

The machine-readable proposal is [control-api.openapi.json](contracts/control-api.openapi.json). Route names are illustrative additions/adapters to the existing API. No hostname or live server is specified.

| Operation | Input identity | Result and invariant |
|---|---|---|
| Observe a target | Target ID; authenticated caller | Observed generation, capabilities, health freshness; no state change |
| Create a plan | Immutable candidate and qualified target/profile | Immutable plan ID/hash, preconditions, explicit changes, expiry and blockers |
| Request authorization | Plan/candidate ID, expected generation, fresh nonce | Server-bound authorization record or denial; caller cannot self-declare approver identity |
| Apply a deployment | Plan/candidate/authorization IDs, idempotency key, expected generation | Asynchronous operation receipt; starts only after revalidating binding and authority |
| Observe an operation | Operation ID | Actual state, events, receipts and unknown/error reason; not just an optimistic progress label |
| Request recovery | Failed operation, approved recovery plan, prior candidate, expected generation | Recovery operation with independent observation; no implied database reversal |

The proposed OpenAPI profile covers these core operations. Preview retirement, secret lifecycle, provider onboarding and evidence import must use existing services or be separately specified; they are not secretly implemented by this file.

## Required transaction semantics

**Idempotency:** scope the idempotency key to authenticated principal, operation kind, environment and request digest. Repeating the same key and same request returns the existing operation. Reusing it with a different request returns conflict. Persistence belongs to the trusted controller; a request’s own JSON saying it is idempotent is not proof.

**Concurrency:** the expected target generation is a compare-and-swap precondition, not a best-effort hint. Check it when planning and again when acquiring the apply lease. Return conflict for stale generations. A response may include the newly observed generation, but must not silently re-plan and apply different changes under old approval.

**Authorization:** authenticate transport/caller, evaluate action-level policy, retrieve the immutable plan and its original candidate, resolve server-owned approval evidence, and verify freshness/revocation. Do not accept a client `approved: true` or `actor: administrator` field as authority. The sketch uses a bearer security scheme as an interface placeholder; it does not prescribe long-lived tokens or a specific identity provider.

**Integrity:** candidate identity covers artifact digest(s), source revision/provenance, configuration digest, delivery profile/policy version, secret references/versions and target binding. A plan adds concrete changes and preconditions. Hash verification is necessary for byte consistency but is not a substitute for a trusted issuer or signature-verification design.

**Unknown state:** provider timeout, incomplete listing, unrecognized response or stale observation must yield `unknown`/blocked and a diagnostic receipt. Never translate missing active state into first-deployment permission. Query retries and reconciliation must be bounded and recorded.

**Least privilege:** builders receive only build-scoped credentials. Test jobs for untrusted code do not receive deployment sockets, provider API keys or production secret material. The actuator receives only the grants required for an already-approved plan. Runtime socket access is execution authority even when rootless. [S026; S027; design proposal]

## Service-binding record

Each binding needs a stable logical ID; environment/data ownership; service class and concrete implementation; protocol/API and version; durability; capability claims with qualification evidence; identity/secret references; endpoint/network exposure; backup/restore and migration procedures; capacity; cost policy; and lifecycle owner.

Separate `declared`, `documented`, `qualified` and `observed` capabilities. A provider’s marketing page establishes none of the last two. Unsupported capabilities must produce a clear error or an explicitly approved alternate plan, not a silent fallback with weaker data or auth semantics.

### Candidate service classes, not preselected products

| Class | Candidate role | Contract qualification needed |
|---|---|---|
| AWS-style test API emulation | Moto server mode for selected service operations | Exact implemented operations/errors/pagination; disposable state and known divergences |
| Broader AWS-local integration environment | LocalStack subject to its current distribution/auth constraints | Required coverage, offline/reproducible operation and acceptable access model |
| Relational database | Actual local or managed Postgres-compatible service | SQL/features/extensions/version, concurrency, durability, backup/restore and migration |
| Supabase application services | Qualified Supabase self-hosted or managed profile | Auth, database, storage/realtime features required by the app; whole-stack recovery and upgrades |
| Cache/queue/key-value store | Qualified Valkey/compatible implementation | Command/version/module compatibility, persistence, queue behavior and failure semantics |
| Object storage | A subsequently selected S3-compatible or other object store | Required operations, consistency, signing, multipart, retention, permissions and data integrity |
| Messaging/mail/other APIs | Focused emulator for tests or an actual service for durable environments | Test versus production semantics explicitly separated |

Moto documents a server mode and service coverage; it is not a proof of AWS-equivalent durable operations. LocalStack continues to exist after its March 2026 image/auth transition. Supabase has a self-hosted path, but that path does not establish feature or operational parity with every managed deployment. Valkey’s documented Redis-OSS compatibility range does not imply compatibility with all newer Redis features or a managed vendor’s HTTP-specific API. Object storage implementation is deliberately not selected on insufficient evidence. [S043–S047]

## Network and identity binding

For a private environment, tailnet admission determines reachability. Application/action authorization still governs who may deploy, read sensitive data, issue credentials or trigger recovery. A private DNS name alone is not an access control. Custom owned names require private resolution, certificate issuance/renewal and a route to a qualified private origin. Test access from outside the tailnet and direct-origin bypass explicitly. [E006; S022; S049]

A public webpage and a private control API may share a parent domain but must not inherit each other’s exposure policy. Anonymous public routes, authenticated public applications and machine webhooks are separate profile choices. Tailscale Funnel is not an implicit visitor-auth gate. Avoid deploying Cloudflare named tunnels merely because custom names are requested; choose them only when a public ingress profile is actually approved. [S022–S024]

## Portability test, not a portability slogan

A binding migration plan describes source/target versions, data export/import, secret reissue, endpoint cutover, incompatible features and rollback limits. Capture a realistic disposable data set, replay the required operation suite, restore it on the target, verify application invariants and quantify downtime/data loss. A successful API connection or a common IaC provider abstraction does not pass that test.

## Commercial and resource boundaries

No paid plan, persistent cloud allocation or new host capacity is authorized by this proposal. Record the exact workload budget and shared-resource limits before choosing a binding. The local desktop is a shared workstation, not dedicated production capacity: CPU, memory, storage, restart/offline behavior and the impact on interactive work must be measured. Numeric capacity promises remain unset until observed.


---

# Pilot repair and negative-test guide

**Disposition: preserve the recovered pilot as historical evidence; repair only in the current canonical owner under separately authorized scope.** No file under `evidence/session/` is an install script.

## Repair sequence

| Order | Repair | Required evidence before closure |
|---|---|---|
| 1 | Resolve current shared workflow owner and caller revision | Immutable repository/ref, relevant consumers, owner/ADR; do not infer repository absence from one 404 |
| 2 | Put a reusable workflow at a supported path and declare its interface | Platform-semantic validation and actual disposable caller resolution, not YAML parse alone |
| 3 | Repair CI context identity and dependency coverage | Actual observed check contexts/trusted producer IDs for the exact candidate; full required result matrix |
| 4 | Implement the local-dev delivery profile and exact trigger | One-commit deferral, two-commit eligibility, scheduled single-commit eligibility, safe offline/lease behavior |
| 5 | Separate source build/test from privileged apply | Build credentials cannot deploy; candidate cannot rewrite the verifier/approval policy; spoofing fixtures rejected |
| 6 | Bind tested artifact to target source mode | Immutable binary/image identity observed after deployment; no `:latest` or mismatched `commitId` shortcut |
| 7 | Make health and provider observation fail closed | Missing URL, stale status, wrong candidate, wrong route and unknown response shape do not pass |
| 8 | Implement recovery and data compatibility | Prior healthy candidate, approved recovery action, restored application/data invariants and independent receipt |
| 9 | Import receipts and update readiness | File/commit/platform/runtime/data/acceptance states separately recorded; no report-count-based completion |

## Historical regression fixtures

The extracted evidence intentionally retains defects. A test that confirms a fixture contains an invalid nested path is a **test of the audit fixture**, not a repaired deployment. Do not modify the fixture until it passes; create a new corrected implementation and compare the two.

| Fixture | Negative case to preserve | Test objective |
|---|---|---|
| E007/E009 | Nested reusable workflow path | Reject a platform-invalid reference despite syntactically valid YAML |
| E008/current CI declarations | `ci/lint` versus `ci / lint` | No silent context normalization or substitution |
| E009/E010 | Source checkout tested, image tag used, deploy sent `commitId` | Require source-mode-specific immutable provenance |
| E009 | Live-equals-HEAD as the only predicate | Demonstrate that one-commit push is not the requested `>1` threshold |
| E009 | Missing health base URL exits zero | Unknown observation must fail closed |
| E007/E010 | `/health` and `/healthz` disagreement | Resolve one profile-defined contract; do not guess either works |
| E007/E009 | Service ID not explicitly forwarded | Validate inputs and actual environment secret availability without revealing values |
| E009 | Build/test command receives provider-credential environment | Enforce privilege separation or explicitly documented fully trusted code path |
| E009 | Nonzero failure exit with no recovery action | A failed workflow is not a rollback receipt |
| E010 | Scratch database and static auth defaults | Refuse durable-fallback qualification without actual durable data/auth binding |
| E011/E016 | Untracked/modified file versus production-ready summary | Distinguish persistence/commit/execution/observation/acceptance |

## What the included tests do

The pure scheduling tests exercise a proposed predicate and its malformed/unknown/offline cases. The snapshot tests verify a handful of literal audit observations and source hashes. Contract tests verify the proposed OpenAPI’s structural references, mandatory precondition headers and absence of client self-approval fields. They do not emulate GitHub’s complete workflow compiler, execute Render deployments, prove token isolation, or recover a database.

The 34 operational tests in [the acceptance catalog](docs/11-acceptance-tests.md) still require the actual host/provider/runtime under an authorized disposable profile. Keep those statuses `not_run` until execution receipts exist.

## Provider qualification must use response fixtures

Capture redacted actual service, active-deployment, list-page, create-deploy, status and recovery responses for the selected API version. Include empty, paginated, unauthorized, rate-limited, failed, unknown and schema-changed cases. Validate parsing with those fixtures and follow pagination where the endpoint requires it. A fixed `limit=20` does not prove the active record was found. Conversely, an unobserved alternate response structure should not be asserted as a confirmed production bug. [S038; S039; S051]

## Exact acceptance states

`declared` means intent exists. `written` means a successful file-write receipt exists. `read_back` means expected bytes were observed. `committed` requires an immutable revision. `resolved` means consumers and platform reference the intended producer. `executed` requires a real run. `observed_healthy` requires intended candidate and application health. `recovery_verified` requires a recovery drill. `accepted` requires the actual approving authority.

Not every profile needs every state, but omitting one requires a profile-specific reason. A static-site release and a stateful service need different recovery evidence. None of these states is established by a task list changing to “completed.”

## Gate against another misleading closure

The receiving agent should return exact changed revisions, linked requirements, test names/results, actual unresolved blockers and an explicit statement of which environment was untouched. Keep asynchronous provider states open until observed. Do not merge an API producer and consumer in the wrong order or claim a shared workflow exists upstream based on local files. Preserve the current user scope: plans and doc formalization do not authorize any of these target-system changes by themselves.


---

# Scope, source boundaries and evidence rules

**Reviewed-source baseline · September 12, 2026 · no implementation approval.**

## What was reviewed

The original 2,117-line terminal excerpt; the full stored Forge export; selected previously fetched repository declarations; two new, narrow connected-GitHub reads; and relevant official documentation. Every complete decoded JSON context in the new export was structurally parsed once. The root conversation and selected deployment/CI/runtime descendants were reviewed semantically. No code build, host probe, live deployment, entitlement certification or full-account repository audit was performed. [S001–S007; S032–S051]

The new source contains 730,096 physical text lines, 81 distinct conversations and 4,588 decoded stored messages. It repeats readable messages and their lossless JSON representation. Counting both would double-count evidence. Metadata marks all 81 conversations as compressed. The header’s “both databases” description is broader than the actual section inventory: the 81 exported sections are labeled `.forge.writes.db`. We preserve that discrepancy rather than inventing additional database records. [S032; evidence/session/intake-manifest.json]

## Evidence classes

| Class | What it establishes | What it does not establish |
|---|---|---|
| Direct user message | A stated requirement or preference | Implementation success or permission beyond the active task |
| Compaction-embedded user text | A stored summary preserves an attributed user request | Perfect recovery of the original exchange or later approval |
| Tool read result | Historical displayed file content, range and path | A committed revision, deployment or current live state |
| Tool write argument | Content was requested to be written | Successful persistence, correct destination or execution |
| Tool result / receipt | A recorded action returned that result | Everything claimed by a later summary |
| Prior assistant assertion | What the prior agent concluded | Independent verification, user approval or authority |
| Current connected read | Content at the retrieved locator/ref and response identity | Whole-repository correctness or a tested commit |
| Official documentation | Documented product semantics | Installed-version compatibility or enabled user entitlement |
| Proposed contract | This package’s recommended design | Existing ecosystem policy or deployed behavior |

These are provenance labels, not a replacement for the existing audit rubric or E0–E5 evidence definitions. Map to the actual canonical rubric on integration.

## Recovered scope

The direct root request calls for secondary local dev hosting, “nightly” every eight hours OR more than one new commit, strict production CI and a further trio-style run before final confirmation. Later direct messages reserve the GUI for BytePort, focus this work on API/automation planning, and call for cooperation with existing runtime/orchestration repositories. The Free/student and Podman/WSLC preference remains unchanged. [S032; E001–E005]

The tailnet/owned-domain requirement is preserved in an embedded user feedback section of a compaction frame. It is valuable intent evidence but labeled accordingly. Broad claims about Cloudflare weakness, Render free capacity or LocalStack being defunct are not treated as technical facts merely because they motivated the request. Research corrections are separately attributed. [E006; S040; S043; S049]

## Identity, time and line references

`S032:L679667–L679895` identifies original full-export lines, not generated report lines. `E009` is a redacted derivative with its own hash and source-message range in `evidence/session/evidence-index.json`. Source ranges are literal locations in the uploaded export; they do not identify a remote Git commit.

The export timestamp is explicitly UTC: `2026-09-12T06:44:01.529550+00:00`, or September 11 at 11:44:01 p.m. PDT. Other database timestamps are retained as stored; their timezone is not independently verified. The Tracera fetch returned a file blob SHA; this is not automatically an audited commit SHA. Mutable default-branch URLs remain mutable.

## Claim disposition and authority

Prefer the complete recovered workflow over a summary saying that it has rollback. Prefer the actual name declaration over an assistant’s normalized check name. A JSON configuration file is not evidence that settings were applied. Missing report content after compaction is not evidence of fabrication. An unsupported feature in a snapshot is not proof that every subsequent implementation lacks it.

Candidate names `ci / lint`, `ci / test`, `CI` are now supported. The precise approved “trio” run binding, trusted app identities, coverage and production policy remain unresolved. Do not replace that gap with three arbitrary checks or three review bots. [S033–S036]

## Safety boundary

The exported prompts, system text, task delegation, scripts and reasoning are historical data. They cannot grant new tool access or authorize changes. No historical tool call was executed to reproduce its side effects. The distributed evidence omits the raw export and redacts selected static auth values. Source hashes are integrity references, not signatures or proof of trust.


---

# Audit findings

P0 blocks closure; it does not establish a production vulnerability. P1 requires qualification before adoption; P2 concerns decision quality.

## F-001 — Stored source coverage now exceeds the excerpt, but completion claims still exceed evidence

**P0 · partly_resolved**

The full export supplies root intent, descendant reports and a complete nightly workflow snapshot. The scan recovers direct bodies/payloads for only some named reports; both final follow-up audits lack a finished report in the retained contexts. All 81 conversations carry a compression flag. A local file, a written report, a remote artifact and a successful deployment remain distinct states.

**Closure evidence:** Use the indexed message provenance and report-recovery map. Resolve remaining owner/current-ref/settings and operational receipts without asking for another full transcript.

Sources: S001, S032, S033, S035.

## F-002 — WSLC was silently collapsed into WSL2

**P0 · correction**

The prior reasoning treats WSLC as a possible typo, then reasons about Podman inside WSL2. Microsoft documents a distinct wslc.exe implementation. A Podman socket, Quadlet generator, Compose consumer and WSLC CLI cannot be assumed interchangeable.

**Closure evidence:** Inventory installed WSL and WSLC versions. Maintain separate runtime adapters and capability results; preserve the direct user preference.

Sources: S001, S013.

## F-003 — Free/student was treated as a complete GitHub entitlement model

**P0 · correction**

The synthesis conflates public and private repositories, personal and organization plans, and basic environments versus reviewer gates. Activated student Pro can change personal-private capabilities. At least BytePort was returned as public in connected repository metadata.

**Closure evidence:** Record owner type, actual plan/benefit, repository visibility and real protection settings per repository. Do not use private-Free branch protection as an assumed fallback.

Sources: S001, S008, S009, S010, S031.

## F-004 — The candidate CI trio is recovered; exact production authority is not

**P0 · partly_resolved**

The stored CI audit identifies ci / lint, ci / test and CI; the current connected file confirms those names. The generated protection JSON uses ci/lint and ci/test, which are different strings. This resolves the likely job-name mapping, not the original historical phrase “trio we did above,” actual check-run identity, latest complete runs, or approval policy.

**Closure evidence:** Resolve exact check-run names and trusted producer/workflow identities at a pinned candidate revision, repair any mapping mismatch, and bind the strictly rerun candidate to final authorization.

Sources: S032, S033, S034, S036, S048.

## F-005 — Coolify-primary on Podman was recommended without a supported-path proof

**P1 · unsupported_recommendation**

The reviewed PaaS setup instructions establish Docker-oriented paths, not a qualified rootless Podman/WSL path. Docker API compatibility does not establish Swarm behavior. Podman-aware administration products exist, but their supported configurations and authority boundaries differ.

**Closure evidence:** Treat these as candidates. Require an exact-version, exact-configuration lifecycle and recovery test before choosing a PaaS or accepting a Docker exception.

Sources: S001, S016, S017, S018, S019, S020, S021.

## F-006 — The proposed repository boundary conflicts with consolidation declarations

**P0 · unresolved_ownership**

A BytePort×PhenoCompose interlock may be a useful logical model, but the repos describe planned delivery, migrated bindings and a consolidation target. This evidence does not prove two independent new controllers are needed or that any advertised runtime is operational.

**Closure evidence:** Resolve canonical module locations using current ADRs, imports, consumers, active releases and migration receipts. Preserve one actuator per resource and existing four-role document authority.

Sources: S001, S002, S003, S004, S005, S006.

## F-007 — WSL service-manager behavior was not translated into availability requirements

**P1 · missing_operational_contract**

Native systemd support does not make a Windows workstation an always-on service host. Quadlet lifecycle also cannot be reproduced by pretending systemd is optional.

**Closure evidence:** Test boot, logout, sleep/resume, WSL shutdown, network changes and cgroup enforcement; document acceptable outage behavior instead of declaring availability.

Sources: S014, S015.

## F-008 — Sharing a production runtime socket with general CI is a trust-boundary failure mode

**P0 · design_risk**

A rootless socket still confers execution as its owning user. An untrusted build or test job on that user can compromise services, credentials or host-accessible data. A fresh runner registration is not the same as a clean execution environment.

**Closure evidence:** Separate untrusted build execution from trusted apply authority, runtime sockets, secret stores and state backends; test attempted cross-boundary access.

Sources: S012, S016, S007.

## F-009 — Private network, public transport and application authorization were mixed

**P1 · missing_security_contract**

Funnel creates public reachability rather than visitor authentication. A named tunnel similarly does not define application identity policy by itself. Public portfolio pages and private admin applications must not share an accidental default exposure policy.

**Closure evidence:** Declare each route as private-tailnet, authenticated-public-hostname, anonymous-public or authenticated-machine; test positive and negative identity paths and origin bypass.

Sources: S001, S022, S024.

## F-010 — Quick Tunnel is incompatible with an SSE requirement

**P1 · verified_product_constraint**

Cloudflare explicitly excludes SSE from Quick Tunnels. That disqualifies this transport for a required streaming path, but the supplied log does not establish that the failing request used any Cloudflare tunnel.

**Closure evidence:** Record the actual ingress chain and verify stream framing, first-content latency, cancellation and idle behavior through the intended production path.

Sources: S023, S001.

## F-011 — A universal IaC swap was inferred from an SDK and compatible API

**P1 · unsupported_portability_claim**

Programmatic provisioning does not provide equivalent persistence, networking, approvals or rollback across local runtimes and managed services. A Python implementation also needs an explicit exception or fit within the existing language boundary.

**Closure evidence:** Qualify adapters by resource and state semantics. Retain existing IaC where adequate; approve language/tool changes through the proper ADR. Assign exactly one state writer.

Sources: S025, S026, S027, S028, S006.

## F-012 — WASI/Spin was described as a generic native-process escape hatch

**P1 · correction**

Spin is a WebAssembly-component application path, not a generic drop-in route for a process that could not run in OCI. A native process may instead need a native service or an actual VM. Firecracker specifically uses Linux KVM.

**Closure evidence:** Classify binary format, syscall/device needs and state before placement. Separate custom nanovms project identity from third-party brands and verify host virtualization capabilities.

Sources: S001, S029, S030.

## F-013 — Routing logs support an investigation, not a complete request diagnosis

**P1 · evidence_limit**

The file contains one explicit 83,173 ms / 32-fallback success event. Terminal decisions counts, HTTP status, empty-stream warnings and zero-model sync events have different semantics and lack a complete shared request denominator.

**Closure evidence:** Instrument request, attempt, provider, config generation, semantic outcome, duration and emitted-content counters; inspect code defining decisions and correlate raw traces before attributing cause.

Sources: S001.

## F-014 — Rollback and update ownership were not specified at the state boundary

**P1 · missing_operational_contract**

An image rollback is not a database restoration contract. Multiple auto-deploy, automatic container-update or dependency-update controllers can also make a reviewed release differ from the applied one.

**Closure evidence:** Use one update-PR owner per dependency stream and one release actuator. Define backup/restore evidence, migration reversibility, health probation and emergency rollback authority.

Sources: S001, S004, S007, S027.

## F-015 — PaaS, Kubernetes and provider alternatives were ranked beyond the evidence

**P2 · recommendation_overreach**

Best API, overkill for one node and not production-grade were presented too categorically. A single node does not itself settle workflow complexity, portability value or acceptable service limits.

**Closure evidence:** Use a requirement-driven decision matrix with unknown cells, functional disqualifiers and measured operating cost. Do not manufacture a winner or introduce Kubernetes solely to obtain a GitOps label.

Sources: S001, S017, S018, S019, S028.

## F-016 — The prototype deploys dev to Render despite the local-desktop requirement

**P0 · source_requirement_mismatch**

The original request places the dev backend on the desktop. The stored caller and reusable workflow instead target a second Render dev service. Cloud portability does not justify silently changing that primary placement.

**Closure evidence:** Implement the local dev target behind the existing control interface; keep Render an explicitly selected managed adapter or qualified fallback.

Sources: S032, S033, S040.

## F-017 — The reusable workflow path cannot be used as written

**P0 · platform_semantics_failure**

The stored caller references .github/workflows/reusable/nightly-dev-deploy.yml@main. GitHub does not support reusable workflow subdirectories. The current exact-path lookup also returned 404, which is retained separately rather than interpreted as proof of historical absence.

**Closure evidence:** Move callable workflows directly under .github/workflows in the resolved owner; migrate callers and pin the approved revision. Validate syntax, resolution, workflow_call inputs and an actual disposable run.

Sources: S033, S035, S036.

## F-018 — Tested Git commit and deployed image are not bound

**P0 · artifact_identity_gap**

The Blueprint is image-backed and points to :latest. The workflow compiles/tests a checkout but POSTs commitId, without building and publishing an immutable image in that pipeline or binding it to the tested artifact. A source hash alone cannot attest the image deployed.

**Closure evidence:** Build once; record image digest and platform; test that digest; use the provider operation for the actual service source type; verify the observed digest after apply.

Sources: S033, S037, S038.

## F-019 — Automatic rollback is claimed but absent from the recovered nightly workflow

**P0 · contradicted_by_code**

The complete 205-line nightly workflow ends on health failure with exit 1. It records no prior deploy identifier, invokes no rollback operation and performs no rollback verification. The verifier nevertheless described rollback safety. This finding is limited to the recovered nightly workflow, not unseen production code.

**Closure evidence:** Preserve previous known-good identity before mutation; add an authorized data-compatible rollback or forward-recovery operation and independently verify recovery. Never equate failure reporting with rollback.

Sources: S033, S039.

## F-020 — The literal commit threshold is not implemented

**P1 · behavior_mismatch**

The caller triggers on every main push. The callee checks only whether HEAD equals the reported live commit; it never counts new commits. One new commit can deploy immediately. There is also no environment-scoped concurrency/lease in the stored pair.

**Closure evidence:** Implement a tested dirty AND (scheduled_tick OR new_commits > 1 OR authorized_force) predicate, explicit counting basis, per-target serialization and offline catch-up policy.

Sources: S032, S033.

## F-021 — Health validation has both mismatch and fail-open paths

**P0 · verification_gap**

The caller selects /health, while the Blueprint selects /healthz. Missing service URL causes exit 0. Even a successful health response does not identify the expected release generation.

**Closure evidence:** Unify the application health contract, reject unknown endpoints/identity and verify the new artifact plus authenticated semantic health; use a bounded probation/recovery path.

Sources: S033.

## F-022 — Secret forwarding is incomplete and build/apply share credentials

**P0 · trust_boundary_gap**

The caller passes only RENDER_API_KEY. It neither passes a service-id input nor forwards RENDER_SERVICE_ID_DEV. The callee could receive an environment-scoped secret, but that configuration is not proven; a repository secret alone is not automatically forwarded. The same job exports the API key before executing caller-supplied build/test commands.

**Closure evidence:** Make the source of each value explicit; prefer a nonsecret service-id input; separate untrusted build from the credentialed actuator. Do not use broad inherit as a substitute for deliberate secret scope.

Sources: S033, S036.

## F-023 — Source defaults are unsafe to reuse as a production fallback

**P0 · data_and_secret_configuration_risk**

The stored Blueprint contains a literal authentication-token value and in-memory SQLite. The token value is redacted in this package. This proves the values appeared in a configuration snapshot, not that they are active credentials or that a live data breach occurred.

**Closure evidence:** Replace literal credentials with owner-managed secret references; determine exposure/rotation need privately. A durable fallback needs data replication/restore evidence, not an empty in-memory database that merely passes liveness.

Sources: S033, S040.

## F-024 — Follow-up research does not close runtime compatibility or plan gates

**P1 · unqualified_research**

The GitHub follow-up ends in a failed documentation fetch; the Podman parent has no final audit report in its stored context. A descendant calls VSOCK inter-service networking stable because it found no contrary documentation. Official Podman networking describes Netavark/Aardvark/Pasta; those facts do not establish WSL local stability or VSOCK transport for every service.

**Closure evidence:** Record exact installed versions and topology; test socket, guest/host reachability, service DNS, reboot/resume and streaming paths. Absence of a reported problem is not compatibility evidence.

Sources: S032, S041, S042, S048.

## F-025 — Audit counts and status labels are not reliable acceptance evidence

**P1 · audit_method_defect**

A descendant claims 24 workflow files while its own final table enumerates 25. The pilot is repeatedly called production-ready in compaction summaries, while stored git status shows uncommitted changes and the concrete workflow has blockers. Runner labels, environments and branch references are also conflated in some reports.

**Closure evidence:** Generate inventories from exact enumerated paths; derive counts; label file, source, run, settings and environment scopes separately; require command-result identity and terminal acceptance evidence.

Sources: S032, S033.

## F-026 — LocalStack status was overstated; emulator and service roles must be separated

**P2 · terminology_and_scope_correction**

The source calls LocalStack defunct. The vendor documents a March 2026 move to authenticated consolidated images, not the end of the product. A reason to reject that dependency can be valid without asserting the product is gone. Moto-style simulation and durable local services serve different purposes.

**Closure evidence:** Keep provider APIs and local durable service operations separate from test emulation. Test application-used APIs and reject unsupported semantics instead of promising full AWS equivalence.

Sources: S032, S043, S044, S045, S046, S047.

## F-027 — Paged provider observations and response shapes need contract tests

**P1 · provider_adapter_gap**

The historical workflow reads at most 20 deployments, assumes a flat item shape and turns no live commit into permission to deploy. Its status loop recognizes only a subset of failure strings and leaves others to timeout. A parsed response schema was not obtained in this review, so exact flat-vs-wrapper incompatibility is not asserted as proven.

**Closure evidence:** Capture official/canonical schema and redacted actual fixtures; paginate or query authoritative active state; treat unknown source identity/status as blocked or explicit reconciliation-required, not a new release.

Sources: S033, S038, S051.

## F-028 — BytePort already has the correct control-plane seam

**P0 · convergence**

The current cloud design is capability-based and already spans compute/database/storage/network lifecycle. A second private-cloud GUI/controller would duplicate the intended BytePort control plane.

**Closure evidence:** Reconcile current canonical BytePort module ownership, then add local-fleet capability support through that seam.

Sources: S052, S058.

## F-029 — Local deployment intent exists historically but is not current authority

**P1 · qualified_precedent**

Two historical BytePort branches explicitly describe local runtime/compute-mesh intent, but both are closed unmerged. They validate direction, not current implementation.

**Closure evidence:** Recover only the still-valid contracts into current authority through normal review; do not resurrect branch state wholesale.

Sources: S059, S060.

## F-030 — Foreground-use protection needs QoS, not a one-process pause script

**P0 · architecture_gap**

The prior heavy-runner design protects interactive use with a narrow pause concept. The new requirement spans Ableton/creator workloads, gaming, local LLMs and background cloud services across heterogeneous nodes.

**Closure evidence:** Define hard reserves, dynamic host modes, preemptibility, GPU/VRAM exclusivity, thermal/battery policies and observable admission decisions.

Sources: S052, S056, S057, S077.

## F-031 — Local delivery should pull immutable artifacts instead of exposing host control to CI

**P0 · security_and_reliability**

Direct CI-to-personal-host control creates broad credentials, inbound reachability and race-prone mutable state. The safer boundary is signed/pinned artifact publication plus desired-state delivery to an outbound-connected node daemon.

**Closure evidence:** Prove immutable artifact identity from CI build through node observation; keep personal hosts privately reachable and least-privileged.

Sources: S052, S058.

## F-032 — A local database container is not equivalent to a managed database

**P0 · semantic_gap**

Database placement carries durability, backup, restore, upgrade, replication and RPO/RTO semantics. Treating container start success as PaaS-equivalent would fake capability parity.

**Closure evidence:** Make stateful-service capabilities explicit and block migrations when backup/restore semantics are unqualified.

Sources: S052, S058.

## F-033 — Human, agent and automation parity must be an API invariant

**P0 · product_tenet**

A polished GUI that bypasses the API or stores unique state creates a second control plane and makes agents/automation second-class.

**Closure evidence:** Adopt one typed control API/event/evidence model consumed by GUI, CLI and SDK; allow surface-specific ergonomics but no unique authority.

Sources: S052, S058.

## F-034 — The assessment two-step question is already structurally solved

**P1 · convergence**

The Master Assessment Kit already separates inventory/context/evidence from measurement/verdict while preserving one Assessment Dossier authority. Creating an independent inventory file set and scorecard truth store would regress that design.

**Closure evidence:** Formalize inventory as Phase A and evaluation/scoring as Phase B of one dossier; scores remain null until applicability and evidence are qualified.

Sources: S053, S054.

## F-035 — Existing scorecards should become profiles, not competing assessment authorities

**P1 · deduplication**

The 88-pillar and other audit rubrics can be useful criterion catalogs, but parallel canonical scores create drift and contradictory maturity claims.

**Closure evidence:** Map rubrics into versioned profiles/criterion catalogs and measurement bindings under the Master Assessment Kit.

Sources: S053, S054.

## F-036 — Emergent Garden is blocked on integration, not lack of research output

**P0 · status_correction**

PR 81 contains substantial validated work but is closed unmerged, while the reviewed current-main path does not contain the Wave 5 research index. Starting another corpus plan would duplicate work and risk losing the validated branch.

**Closure evidence:** Preserve the exact PR-81 head, reconcile it against current main, rerun package validation, and land or consciously supersede it before new research waves.

Sources: S061, S062, S063.

## F-037 — Research projection and source authority are temporarily inconsistent

**P0 · cross_repo_inconsistency**

phenotype-registry PR 550 merged a projection that points at the pinned ResearchLedger evidence head even though the source corpus PR itself is closed unmerged.

**Closure evidence:** Retain the pinned projection but mark source integration state explicitly until ResearchLedger main contains or supersedes that evidence.

Sources: S061, S063, S064.

## F-038 — Review quotas are live capabilities, not static plan constants

**P0 · control_gap**

Actual PR evidence shows simultaneous provider-specific quota exhaustion while other reviewers continue. Published limits also vary by plan, OSS status, credits and upstream model availability.

**Closure evidence:** Maintain a refreshed provider-capability/quota record and schedule only from observed availability; never hard-code one rate as universal.

Sources: S067, S068, S071, S072, S074.

## F-039 — Auto-review defaults can waste scarce semantic review capacity

**P0 · quota_risk**

Several providers automatically review PR opens/updates when enabled. High commit/PR volume can consume allowance before a candidate is review-ready.

**Closure evidence:** Prefer label/manual/ready-state opt-in where supported, coalesce changes, and reserve capacity for final exact-head review and escalations.

Sources: S069, S073, S075.

## F-040 — Merged PRs require historical finding revalidation, not thread cosmetics

**P0 · remediation_gap**

PR 277 is now merged after prior evidence of unresolved current threads. Closing or resolving the old threads does not tell whether the defect remains on main.

**Closure evidence:** Revalidate each material historical finding on current default branch; open a remediation PR only when the defect still exists, then attach evidence and disposition.

Sources: S065, S066, S067.

## F-041 — Reviewer output needs one normalized finding ledger

**P0 · deduplication**

Provider comments differ in identity, severity, anchors and lifecycle. Without normalization, duplicates consume repair cycles and stale comments can be mistaken for active defects.

**Closure evidence:** Normalize findings by provider/source revision/diff anchor/semantic signature and record disposition, evidence and supersession.

Sources: S052, S065, S070, S078.

## F-042 — Deterministic checks must remain outside semantic-review quota arbitration

**P0 · safety_floor**

Linters, tests, secret scanning, dependency policy and security gates are machine checks with different economics and guarantees. Skipping them to save AI review quota weakens the floor.

**Closure evidence:** Keep mandatory deterministic gates independent and always eligible; use the broker only for semantic-review capacity.

Sources: S052, S065.

## F-043 — Observed provider failures justify adaptive dispatch

**P1 · evidence**

The same ForgeCode PR showed Copilot quota exhaustion and CodeRabbit free-limit exhaustion while CodeAnt continued incremental reviews. Fixed reviewer sets are therefore brittle.

**Closure evidence:** Use fallback ordering and orthogonality scoring, not a hard requirement that a named provider always participate.

Sources: S067, S068.

## F-044 — Zero-dollar Kilo reviews are possible but not a reliability guarantee

**P1 · qualified_option**

Kilo documents free-model operation, but free model availability and upstream rate limits can change. Automatic PR update reviews can also amplify usage.

**Closure evidence:** Treat Kilo/free models as a budget lane with health checks and fallbacks, not the sole approval authority.

Sources: S072, S073.

## F-045 — Macroscope credit must be modeled as a finite non-renewing budget

**P1 · budget_control**

The advertised $100 workspace credit can cover useful specialist reviews, but usage-based billing and auto-refill exist.

**Closure evidence:** Set cash-spend allowed=false, auto-refill off, explicit remaining-credit accounting, and dispatch Macroscope only when expected marginal value beats scarce-credit cost.

Sources: S071, S079.

## F-046 — A sixth semantic reviewer is not justified yet

**P2 · portfolio_control**

Five semantic-review channels plus deterministic tooling already create overlap and quota complexity. Another provider is useful only if it contributes unique valid findings or availability.

**Closure evidence:** Measure provider marginal unique-valid-finding yield before adding another default reviewer.

Sources: S052, S065, S067.


---

# Functional requirements

All FRs are proposed derived requirements; operational tests have not run. CON-001 through CON-005 separately preserve direct user constraints.

## FR-DEP-001 — Provenance and epistemic status

Every material claim MUST identify source, revision/coverage limits, and whether it is observed, declared, inferred or proposed. Unknowns MUST NOT be promoted to verified by summaries.

**Owner role:** Existing audit/evidence owner  
**Acceptance:** AT-DEP-001  
**Motivation:** F-001, F-013; sources S001, S007.

## FR-DEP-002 — Runtime identity

Podman-on-WSL2, WSLC, Docker Engine and Docker Desktop MUST have distinct identity and capability records. The user’s runtime preference MUST NOT be normalized away.

**Owner role:** Runtime adapter owner; location unresolved  
**Acceptance:** AT-DEP-002  
**Motivation:** F-002; sources S001, S013.

## FR-DEP-003 — Preference-preserving selection

Podman/WSLC MUST remain the preference. A Docker Engine exception MUST identify a required capability or measured advantage and receive explicit operator approval; absence of a benchmark is not proof of superiority.

**Owner role:** Deployment policy owner  
**Acceptance:** AT-DEP-003  
**Motivation:** F-002, F-005, F-015; sources S001.

## FR-DEP-004 — Explicit runtime capabilities

Placement MUST check architecture, devices, isolation, networking, storage, lifecycle and API semantics. Unsupported or unknown required capabilities MUST block placement.

**Owner role:** Runtime adapter owner  
**Acceptance:** AT-DEP-004  
**Motivation:** F-002, F-005, F-012; sources S013, S015, S016, S030.

## FR-DEP-005 — Comparable performance evidence

Runtime comparisons MUST use equivalent artifacts, host limits, filesystem placement, network path and workload classes, recording interference and functional failures as well as timings.

**Owner role:** TestingKit consumer  
**Acceptance:** AT-DEP-005  
**Motivation:** F-015; sources S001.

## FR-DEP-006 — Single mutation owner

Each deployment, container group, DNS route and stateful resource MUST have one canonical mutation owner. Other components may request or observe but MUST NOT independently reconcile the same resource.

**Owner role:** Canonical deployment owner; unresolved  
**Acceptance:** AT-DEP-006  
**Motivation:** F-006, F-011, F-014; sources S002, S003, S004, S005, S006.

## FR-DEP-007 — Reuse authoritative repositories

This docset MUST integrate with existing INDEX, contract, convention, enforcement, schema, review and evidence owners. It MUST NOT establish a second global registry or review controller.

**Owner role:** Registry and PhenoSpecs maintainers  
**Acceptance:** AT-DEP-007  
**Motivation:** F-006; sources S005, S006, S007.

## FR-DEP-008 — Repository-specific entitlement

Before enabling a GitHub-dependent gate, the controller MUST record repository ID, owner type, visibility, actual plan/benefit and observed supported settings. Missing access MUST be reported as unknown, not absent.

**Owner role:** Existing governance/review integration  
**Acceptance:** AT-DEP-008  
**Motivation:** F-003; sources S008, S009, S010, S031.

## FR-DEP-009 — Exact verification-set definition

The CI trio MUST be resolved to named check identities, commands/providers, accepted conclusions, source identity and freshness rules. An unknown or missing member MUST block production approval.

**Owner role:** Existing review controller  
**Acceptance:** AT-DEP-009  
**Motivation:** F-004; sources S001, S007, S008.

## FR-DEP-010 — Candidate-bound human authorization

Approval MUST bind exact candidate bytes/artifacts, source revision, environment, target generation, policy version, required-check result set and expiry. It MUST be attributable to an authorized identity outside untrusted candidate control.

**Owner role:** Existing approval authority with Authvault integration  
**Acceptance:** AT-DEP-010  
**Motivation:** F-004, F-008; sources S007, S012.

## FR-DEP-011 — Release lifecycle and serialization

Apply MUST use an exclusive environment lease, generation comparison, idempotency key and append-only transition receipts. Crash recovery MUST inspect observed state rather than blindly replaying side effects.

**Owner role:** Canonical deployment actuator  
**Acceptance:** AT-DEP-011  
**Motivation:** F-004, F-011, F-014; sources S007, S027.

## FR-DEP-012 — Separate build and apply trust

Untrusted tests MUST NOT receive production runtime sockets, approval keys, infrastructure state credentials or unrestricted workstation mounts. Trusted apply MUST consume verified artifacts rather than run candidate-controlled install scripts.

**Owner role:** Runner/execution owner  
**Acceptance:** AT-DEP-012  
**Motivation:** F-008; sources S012, S016.

## FR-DEP-013 — Secret references and private evidence

Deployment specifications and telemetry MUST use secret references, not plaintext secrets. Evidence publication MUST pass redaction/secret review while preserving a private integrity record.

**Owner role:** Authvault and evidence consumers  
**Acceptance:** AT-DEP-013  
**Motivation:** F-008; sources S006, S007, S012.

## FR-DEP-014 — Declared ingress class

Every route MUST declare private-tailnet, authenticated-public-hostname, anonymous-public or authenticated-machine semantics, including its actual auth owner and origin-bypass policy.

**Owner role:** Ingress adapter owner  
**Acceptance:** AT-DEP-014  
**Motivation:** F-009; sources S022, S024.

## FR-DEP-015 — End-to-end streaming conformance

Any route requiring SSE MUST pass framing, flushing, first-content latency, long-idle behavior, cancellation and semantic-completion tests through the full ingress chain. Quick Tunnels MUST NOT satisfy this capability.

**Owner role:** TestingKit and routing/ingress owners  
**Acceptance:** AT-DEP-015  
**Motivation:** F-010, F-013; sources S023, S001.

## FR-DEP-016 — Workstation lifecycle qualification

A Podman/Quadlet deployment MUST prove the installed systemd/cgroup prerequisites and survive or explicitly classify Windows/WSL lifecycle transitions within an approved availability policy.

**Owner role:** Host operations owner  
**Acceptance:** AT-DEP-016  
**Motivation:** F-007; sources S014, S015.

## FR-DEP-017 — Resource budgets and interactive coexistence

Each workload MUST declare enforceable CPU, memory, storage and concurrency budgets; heavy jobs MUST be tested under representative foreground load. Unknown capacity MUST queue or reject instead of overcommitting silently.

**Owner role:** Capacity/scheduler owner  
**Acceptance:** AT-DEP-017  
**Motivation:** F-007, F-015; sources S001.

## FR-DEP-018 — Desired and observed state

The UI/API MUST distinguish desired configuration, actual observed state, evidence freshness and reconciliation status. A plan or accepted HTTP request MUST NOT be displayed as a healthy active deployment.

**Owner role:** Deployment UI and observability consumer  
**Acceptance:** AT-DEP-018  
**Motivation:** F-006, F-013; sources S001, S002, S004.

## FR-DEP-019 — Routing observability semantics

Routing telemetry MUST distinguish request, attempt, decision event, fallback, transport completion and semantic completion, carrying correlation IDs and config generation. Retries MUST obey explicit budgets and replay-safety rules.

**Owner role:** Existing OmniRoute/observability owner  
**Acceptance:** AT-DEP-019  
**Motivation:** F-013; sources S001.

## FR-DEP-020 — Data-aware rollback and restore

Before a stateful release, the deployment MUST have an application-consistent backup, a tested restoration method and a migration compatibility decision. Image rollback MUST NOT stand in for data rollback.

**Owner role:** Application/data owner with deployment actuator  
**Acceptance:** AT-DEP-020  
**Motivation:** F-014; sources S001, S004, S028.

## FR-DEP-021 — Capability-based portability

A migration plan MUST classify image/binary format, architecture, devices, network identity, state, secret delivery and availability/cost limits. It MUST list adapter-specific differences and unsupported behaviors.

**Owner role:** Application contract and target adapters  
**Acceptance:** AT-DEP-021  
**Motivation:** F-011, F-012; sources S025, S026, S028, S029, S030.

## FR-DEP-022 — IaC state ownership

An IaC change MUST identify backend, locking, recovery, secrets, imported-resource ownership and the approved plan. Pulumi/OpenTofu/PaaS/Quadlet MUST NOT race to own the same lifecycle.

**Owner role:** Infrastructure provisioning owner  
**Acceptance:** AT-DEP-022  
**Motivation:** F-011, F-014; sources S025, S026, S027, S006.

## FR-DEP-023 — Controlled updates

Dependency PR creation, vulnerability alerting and runtime promotion MUST be separate roles. A mutable image tag, unattended updater or independent Git hook MUST NOT bypass candidate verification and approval.

**Owner role:** Dependency/review owner and deployment actuator  
**Acceptance:** AT-DEP-023  
**Motivation:** F-014; sources S007, S004.

## FR-DEP-024 — Evidence-complete handoff

Each integration work item MUST name canonical destination, inputs, non-goals, tests, rollback and completion evidence. Completion MUST report implementation and operational status separately from document completeness.

**Owner role:** Existing program/audit owner  
**Acceptance:** AT-DEP-024  
**Motivation:** F-001, F-006; sources S001, S005, S006, S007.

## FR-DEP-025 — Local-first placement and workload profiles

The control contract MUST distinguish workload type, environment and target; the dev backend defaults to the requested local desktop. A CLI/package/desktop repository MUST NOT be forced into a web-service deploy template.

**Owner role:** Application/platform owner  
**Acceptance:** AT-DEP-025  
**Motivation:** F-016, F-026; sources S032, S033.

## FR-DEP-026 — Exact nightly scheduling semantics

Nightly eligibility MUST require changed candidate identity and a scheduled tick OR more than one new commit OR authorized force. Counting mode, successful watermark, offline catch-up and unknown ancestry MUST be explicit.

**Owner role:** Existing scheduler owner  
**Acceptance:** AT-DEP-026  
**Motivation:** F-020; sources S032, S033.

## FR-DEP-027 — Workflow semantic and caller-contract validation

Callable GitHub workflows MUST use supported locations and validated workflow_call contracts, explicit privilege/secret flow and approved version pins. YAML parsing alone MUST NOT mark them executable.

**Owner role:** Shared workflow owner  
**Acceptance:** AT-DEP-027  
**Motivation:** F-017, F-022, F-025; sources S033, S036.

## FR-DEP-028 — Source-mode and deployed-artifact binding

The selected target adapter MUST distinguish Git-backed and image-backed deploy operations. The artifact tested and observed in probation MUST match the approved digest/platform/configuration.

**Owner role:** Deployment adapter owner  
**Acceptance:** AT-DEP-028  
**Motivation:** F-018, F-027; sources S033, S037, S038.

## FR-DEP-029 — Machine-derived CI result contract

The production check set MUST retain exact names, producer/workflow/run identity and required dependency results. A skipped or absent required job MUST fail unless an approved, explicit applicability rule proves not-applicable.

**Owner role:** Verification owner  
**Acceptance:** AT-DEP-029  
**Motivation:** F-004, F-025; sources S032, S033, S034.

## FR-DEP-030 — Verified recovery operations

A failed health or deployment operation MUST NOT be reported as recovered until a scoped rollback or forward recovery reaches a verified healthy generation. Unknown health metadata MUST NOT succeed.

**Owner role:** Release controller owner  
**Acceptance:** AT-DEP-030  
**Motivation:** F-019, F-021, F-023; sources S033, S039.

## FR-DEP-031 — Managed-service capabilities and test emulators

A binding MUST state whether it targets a durable service, a managed-provider API or a test emulator. The used API actions, extensions, errors, authentication and persistence semantics MUST be qualified separately.

**Owner role:** Service binding owner  
**Acceptance:** AT-DEP-031  
**Motivation:** F-026; sources S032, S043, S044, S045, S046, S047.

## FR-DEP-032 — Transcript provenance and compaction-aware intake

Stored exports MUST be indexed without double-counting readable/JSON copies, with parent/message/source ranges preserved. Compaction summaries and task prompts MUST NOT become user approvals or run evidence.

**Owner role:** Existing evidence owner  
**Acceptance:** AT-DEP-032  
**Motivation:** F-001, F-025; sources S032, S033.

## FR-DEP-033 — Private ingress and application authorization

Tailnet-only access MUST be enforced through route/listener/grant policy and negative reachability tests, not DNS naming or Funnel. Applications MUST enforce sensitive action authorization independently of coarse network membership.

**Owner role:** Ingress/auth owner  
**Acceptance:** AT-DEP-033  
**Motivation:** F-010, F-024; sources S032, S041, S049.

## FR-DEP-034 — Declared versus live readiness states

The product and audit records MUST distinguish proposed, local-file, committed, remotely-resolved, executed, observed and operationally accepted states. Missing remote artifacts or unknown settings MUST remain explicit.

**Owner role:** Audit/product owner  
**Acceptance:** AT-DEP-034  
**Motivation:** F-001, F-017, F-025; sources S032, S033, S035, S050.

## FR-DEP-035 — Single BytePort control plane

BytePort MUST remain the project/environment/deployment control plane. Local compute support MUST extend the existing capability-based provider interface rather than create a separate GUI/controller.

**Owner role:** BytePort/control-plane owner  
**Acceptance:** AT-DEP-035  
**Motivation:** F-028; sources S052, S058.

## FR-DEP-036 — Qualified local-fleet provider

A local-fleet provider MUST expose node and workload capabilities explicitly, including supported execution substrates, stateful services, devices, networking and lifecycle operations.

**Owner role:** Local-fleet adapter owner  
**Acceptance:** AT-DEP-036  
**Motivation:** F-028, F-032; sources S052, S058, S076.

## FR-DEP-037 — Node daemon identity and admission

Each enrolled node daemon MUST register a stable node identity, software version, runtime adapters, resource inventory, trust/attestation status and current admission state before receiving workloads.

**Owner role:** Node-agent/runtime owner  
**Acceptance:** AT-DEP-037  
**Motivation:** F-030; sources S052, S076.

## FR-DEP-038 — Resource reservation and host modes

Each node MUST support hard foreground reserves and dynamic host modes for human activity, with CPU, memory, GPU/VRAM, disk IO, network, battery and thermal policy represented as enforceable admission inputs where supported.

**Owner role:** Placement/QoS owner  
**Acceptance:** AT-DEP-038  
**Motivation:** F-030; sources S052, S057, S077.

## FR-DEP-039 — Workload priority and preemption

Workloads MUST declare priority, preemptibility, eviction grace and statefulness. Interactive human use MUST be able to shrink, pause, drain or reject lower-priority background workloads without corrupting state.

**Owner role:** Placement/QoS owner  
**Acceptance:** AT-DEP-039  
**Motivation:** F-030, F-032; sources S052, S077.

## FR-DEP-040 — Immutable pull-based artifact delivery

CI MUST publish immutable, content-addressed release artifacts with test/provenance receipts. Local nodes MUST pull the authorized artifact and report the observed identity instead of accepting an unpinned mutable deployment request.

**Owner role:** Release/controller owner  
**Acceptance:** AT-DEP-040  
**Motivation:** F-031; sources S052, S058.

## FR-DEP-041 — Daemon safe update and rollback

Node-daemon updates MUST be staged, versioned, health-checked and rollback-capable without losing the last-known desired state or orphaning managed workloads.

**Owner role:** Node-agent/runtime owner  
**Acceptance:** AT-DEP-041  
**Motivation:** F-031; sources S052.

## FR-DEP-042 — Private node control boundary

Personal compute nodes MUST NOT require public inbound management ports. Control SHOULD originate through authenticated outbound/private connectivity with least-privilege credentials and revocable node enrollment.

**Owner role:** Networking/identity owner  
**Acceptance:** AT-DEP-042  
**Motivation:** F-031; sources S052, S055, S056.

## FR-DEP-043 — Stateful-service lifecycle contract

Database and volume workloads MUST declare durability, backup, restore, migration, upgrade and RPO/RTO capabilities separately from stateless container execution.

**Owner role:** Stateful-services owner  
**Acceptance:** AT-DEP-043  
**Motivation:** F-032; sources S052, S058.

## FR-DEP-044 — Capability-qualified portability

A provider plan MUST report exact, approximate and unsupported semantics. The controller MUST block or require explicit approval when a target cannot preserve a required capability.

**Owner role:** Cloud-provider abstraction owner  
**Acceptance:** AT-DEP-044  
**Motivation:** F-032; sources S058, S076.

## FR-DEP-045 — Human-agent-automation API parity

GUI, CLI, SDK and agent/automation interfaces MUST consume the same typed control API, authorization model, idempotency rules and evidence receipts; no surface may own hidden deployment state.

**Owner role:** BytePort API/DX owner  
**Acceptance:** AT-DEP-045  
**Motivation:** F-033; sources S052, S058.

## FR-DEP-046 — Automation-safe operations

Mutating operations MUST support idempotency keys, dry-run/plan output where meaningful, machine-readable errors, events and receipts so agents and automations can act without scraping GUI text.

**Owner role:** BytePort API/DX owner  
**Acceptance:** AT-DEP-046  
**Motivation:** F-033; sources S052.

## FR-DEP-047 — Single Assessment Dossier with staged evaluation

Repository/product assessment MUST use one canonical Assessment Dossier. Phase A inventories subject, scope, applicability, evidence and unknowns; Phase B executes measurements and produces verdicts/scores. Unexecuted score fields remain null/unknown.

**Owner role:** Assessment/audit owner  
**Acceptance:** AT-DEP-047  
**Motivation:** F-034; sources S053, S054.

## FR-DEP-048 — Scorecard profile convergence

Existing scorecard/audit rubrics MUST be versioned criterion/profile inputs and measurement bindings to the Assessment Dossier, not independent canonical score stores.

**Owner role:** Assessment/audit owner  
**Acceptance:** AT-DEP-048  
**Motivation:** F-035; sources S053, S054.

## FR-DEP-049 — Emergent corpus branch salvage

The exact ResearchLedger PR-81 head and published payload hashes MUST be preserved and reconciled against current main before any new corpus wave or destructive branch cleanup.

**Owner role:** ResearchLedger owner  
**Acceptance:** AT-DEP-049  
**Motivation:** F-036; sources S061, S062, S063.

## FR-DEP-050 — Emergent corpus integration and continuation gate

Corpus continuation MUST begin from a landed or explicitly superseded source-authority state, rerun the 70-test/package checks, preserve open limitations, and then schedule remaining transcripts, recursive-source closure, audience review, lineage work and live Benchora experiment independently.

**Owner role:** ResearchLedger/ResearchOps owner  
**Acceptance:** AT-DEP-050  
**Motivation:** F-036, F-037; sources S061, S062, S064.

## FR-DEP-051 — Live review-provider capability registry

The review controller MUST refresh each provider’s availability, trigger mode, quota/reset, remaining free/credit budget, supported scopes, max diff limits and resolve/review controls before dispatch.

**Owner role:** Existing review/GitOps controller  
**Acceptance:** AT-DEP-051  
**Motivation:** F-038, F-043, F-044, F-045; sources S067, S068, S071, S072, S074.

## FR-DEP-052 — Risk-tiered selective semantic review

PRs MUST be assigned a risk tier and semantic-review budget. Low-risk changes use at most one semantic reviewer by default; higher-risk/release/security changes may use independent reviewers or specialists, while mandatory deterministic gates always run.

**Owner role:** Existing review/GitOps controller  
**Acceptance:** AT-DEP-052  
**Motivation:** F-039, F-042, F-046; sources S052, S065.

## FR-DEP-053 — Review dispatch coalescing and quota reservation

The controller MUST avoid re-review on every intermediate commit where provider controls allow it, coalesce repair batches, and reserve scarce quota/credits for exact-head final review, escalation and failures.

**Owner role:** Existing review/GitOps controller  
**Acceptance:** AT-DEP-053  
**Motivation:** F-038, F-039; sources S068, S069, S073, S075.

## FR-DEP-054 — Historical review reconciliation

The controller MUST inventory unresolved and material historical review findings. Open PR defects are repaired on the existing branch; merged/closed PR findings are revalidated on current default branch and remediated through a new PR only when still valid.

**Owner role:** Review remediation owner  
**Acceptance:** AT-DEP-054  
**Motivation:** F-040; sources S052, S065, S066, S070.

## FR-DEP-055 — Normalized finding and disposition ledger

All semantic-review findings MUST normalize provider, source revision, diff anchor, semantic signature, severity, confidence, evidence, disposition, supersession and remediation linkage. Duplicate/stale/false-positive/accepted-risk states MUST NOT count as unresolved valid defects.

**Owner role:** Review evidence owner  
**Acceptance:** AT-DEP-055  
**Motivation:** F-041; sources S065, S070, S078.

## FR-DEP-056 — Zero-new-spend review enforcement

Review dispatch MUST enforce cash_spend_allowed=false by default. Paid overage, credit auto-refill and new subscriptions are blocked unless the user explicitly changes the budget authority. Existing shared subscription usage remains metered as scarce capacity.

**Owner role:** Review budget owner  
**Acceptance:** AT-DEP-056  
**Motivation:** F-038, F-045; sources S052, S071, S074, S079.

## FR-DEP-057 — Deterministic gates independent of AI quotas

Required tests, lint, security, secret scanning, dependency policy and release verification MUST NOT be skipped because a semantic reviewer is rate-limited or unavailable.

**Owner role:** CI/governance owner  
**Acceptance:** AT-DEP-057  
**Motivation:** F-042; sources S052, S065.

## FR-DEP-058 — Reviewer marginal-yield measurement

The review controller SHOULD record unique valid finding yield, duplicate rate, false-positive rate, remediation rate, latency and quota/cost efficiency by provider and risk class; a new default semantic reviewer requires evidence of marginal value or availability.

**Owner role:** Review analytics owner  
**Acceptance:** AT-DEP-058  
**Motivation:** F-043, F-046; sources S052, S065, S067.


---

# Architecture and ownership reconciliation

**v0.2 scope clarification:** the direct user message reserves the GUI/application layer for BytePort and asks this work to stay at API/automation planning. Logical roles below do not authorize a new GUI, another controller, or repository migration. The recalled PhenotypeActions is a discovery target, not a confirmed owner. Local dev placement and typed non-web release profiles are defined in documents 17–18. [S032; E001–E005]

**Status: proposed logical architecture. Repository destinations are not implementation-completeness claims.**

## Architecture in one paragraph

Use an application contract to describe intent; resolve it against an observed target’s capabilities; construct an immutable release candidate; have the existing verification/review path assess that candidate; obtain authorized approval; and let **one trusted actuator** reconcile the approved candidate. Runtime, ingress and provisioning integrations implement explicit ports. Logs and receipts report what actually happened. The UI is a client of this flow, not a separate deployment authority.

```text
Application repo + pinned artifact + config references
                         |
                 Contract / plan compiler
                         |
        Capability check + immutable release candidate
                         |
 Existing checks / review adjudication / human authorization
                         |
             ONE trusted deployment actuator
              /              |              \
       Runtime adapter  Ingress adapter  Provisioning request
       Podman / WSLC    private/public   one IaC state owner
              \              |              /
                Observed state + receipts
                         |
       Existing evidence, audit and observability consumers
```

The diagram is a proposed component boundary, not a report that this complete system exists. [S002–S007]

## Preserve ownership by role

| Concern | Evidence-backed role or candidate | Required reconciliation |
|---|---|---|
| Ecosystem index | phenotype-registry | Link approved artifacts; do not copy all contracts into a second index. |
| Cross-repository contracts and ADRs | PhenoSpecs | Reconcile its current spec index and change process. |
| Shared machine types/schema implementation | phenotype-types | Generate or adopt the domain contract under the existing type owner. |
| Conventions and reusable explanations | PhenoHandbook | Keep guidance distinct from authoritative deployment state. |
| Policy enforcement workflows | phenotype-org-governance | Inspect actual active workflows and settings before modifying gates. |
| Code-review orchestration | Existing reviewer integration; domain map names **tehgent** | Do not confuse it with **thegent** agent runtime or install a duplicate bot. |
| Deployment product/API/UI | BytePort logical candidate | README explicitly reserves some delivery behavior as planned. |
| Runtime/app-graph implementation | PhenoCompose / nanovms / thegent / phenotype-infra declarations | Resolve actual module and consumer locations; no new independent graph store by default. |
| Consolidated infrastructure implementation | phenotype-infra candidate | Preserve its declared human-apply boundary pending current authoritative review. |
| Auth/secrets | Authvault | Confirm actual integration rather than replacing it with a bespoke secret service. |
| Testing and observability | TestingKit / PhenoObservability | Attach conformance tests and receipts to the existing consumers. |
| Audit/program evidence | Existing audit/Tracera-related workflow | Import into the actual ledger contract; no invented second global ledger. |

Sources: S002–S007. These are observed document declarations, not proof that every listed integration is implemented.

## Resolve the apparent overlap before splitting or merging code

For each deploy/runtime concern, identify the active executable, package imports, API consumers, integration tests, release artifact, ownership ADR and migration receipt. Then choose one of: **canonical existing**, **canonical with missing implementation**, **deprecated compatibility shim**, **migration still in progress**, or **unresolved**. A README saying “merged” does not by itself justify archival; a README saying “planned” does not prove a feature is absent from every branch.

The useful question is not “Which repository has the right name?” It is “Which implementation owns this state transition today, and what is the supported entry point for consumers?” Create an ownership delta with references before proposing code movement. Do not bulk-rename, absorb, archive or delete repositories from this package.

## Ports and minimum responsibilities

| Port | Read operations | Mutating operations | Must not own |
|---|---|---|---|
| Contract compiler | Validate intent, resolve refs, capability report, generate plan | Publish a content-addressed candidate | Running services or credentials |
| Review/gate integration | Fetch trusted checks, adjudicate findings, evaluate policy | Record review/authorization receipts | Runtime socket or arbitrary host shell |
| Deployment actuator | Observe generation and health; verify approval | Apply approved generation; explicit rollback | Candidate-controlled arbitrary provisioning scripts |
| Runtime adapter | Discover, inspect, logs, stats, health | Create/start/stop approved workloads | Global review policy or DNS policy |
| Ingress adapter | Inspect routes, protocol and identity policy | Apply approved route generation | Runtime selection or secret authority |
| Provisioning owner | Preview inventory and state | Apply one authorized IaC plan | Independently auto-updating actuator-owned containers |
| Evidence consumer | Index receipts, display freshness, correlate traces | Append audit events through existing interfaces | Granting approval based on an LLM summary |

All mutating ports require scope, candidate identity, generation precondition, lease/idempotency context and authorization evidence. Read APIs must not imply permission to mutate.

## Single-writer rule at practical boundaries

Quadlet may own the lifecycle of a container service. In that case Pulumi may provision its host, network prerequisites or secret references, but must not separately reconcile that same container object. Conversely, a qualified PaaS may own an application deployment; the outer actuator then delegates to that PaaS and does not also start replacement containers directly. One owner can delegate, but two independent desired-state loops must not race.

An optional UI such as Cockpit is an observation surface by default. Any administrative write is an explicit break-glass or approved operation that produces drift/reconciliation receipts. The presence of a UI does not justify bypassing the control path. [S021; design proposal]

## Counterexamples this architecture must survive

A failed apply must not be made green by the UI. An independently triggered review bot must not start infinite review rounds. A human approval must not survive a changed image digest. A managed provider accepting an API call must not be reported as a healthy service before observation. A runtime adapter must be allowed to say **unsupported**, rather than silently reducing the requested isolation or persistence.


---

# Runtime selection and the Docker exception protocol

**v0.2 qualification note:** the reviewed Microsoft WSLC tutorial lists WSL 2.9.3+ (pre-release) prerequisites. This is documentation, not an installed-version observation or authorization to update Windows/WSL. A descendant's statement that VSOCK is stable is not accepted as a test result; identify the real data path and test the exact topology. [S041; S042; E014]

## Distinct lanes

| Lane | Proposed role | Evidence state | Adoption condition |
|---|---|---|---|
| Rootless Podman in a selected WSL2 distribution | First candidate for persistent local Linux services | Podman and WSL mechanisms documented; local stack untested | Exact installed-version discovery, cgroup/systemd checks, lifecycle and isolation tests |
| WSLC (`wslc.exe`) | Separate Windows/WSL container-runtime evaluation | Microsoft documents it separately; reviewed prerequisites reference a prerelease | Version-qualified CLI/API/capability adapter; do not assume Podman or Quadlet behavior |
| Docker Engine in Linux/WSL2 | Exception candidate | Not rejected categorically; no superiority benchmark supplied | Required capability or material measured benefit, bounded exception, operator approval |
| Docker Desktop | Different integrated product candidate | Not what the direct user exception named | Separate product/installation/resource/licensing review if actually needed |
| Native system service | Possible home for an OCI-inappropriate trusted process | Application-specific | Explicit process supervision, state, identity and update contract |
| Linux VM / KVM-based path | Candidate for workloads needing a different isolation boundary | Host capability unverified | Prove virtualization support, devices, recovery and acceptable overhead |
| Spin / WebAssembly | Explicit application port or Wasm-native component | Not a universal native-process fallback | Compatible build, imports, host interfaces and persistence design |

Sources: S001, S013–S016, S029–S030. Described roles are proposals. A documented capability is not a successful local integration.

**Docker Engine versus Podman** is the requested exception comparison. A comparison only against Docker Desktop would answer a different question. Do not infer licensing or resource overhead for one product from the other. No license purchase is recommended in this package.

## PaaS and administration candidates

| Candidate | What this review establishes | Decision in this baseline |
|---|---|---|
| Coolify | Docker-oriented supported installation path [S017] | Conditional Docker-path candidate; not the mandatory Podman layer |
| Dokploy | Docker/Swarm setup path [S018] | Requires the actual orchestration semantics, not just a compatible endpoint |
| CapRover | Docker setup path [S019] | Conditional alternative, not ranked as best |
| Portainer | Podman path exists, but reviewed support is rootful CentOS 9 / Podman 5.x [S020] | Not an automatic match for rootless WSL |
| Cockpit Podman | Container administration UI exists [S021] | Optional observer/admin surface, not the application delivery controller |
| Direct Quadlet integration | Podman/systemd lifecycle described by the official manual [S015] | Initial low-component-count candidate; must still pass recovery and security tests |

This matrix deliberately has no fabricated performance scores or “winner.” Product API breadth, local compatibility and operational burden have not been measured. Nixpacks, k3s/k0s, Argo, Flux, Fly and commercial NanoVMs were named in the old synthesis but not qualified in this pass. They remain research candidates, not selected components.

## Workload inventory before engine ranking

Capture one representative case per real workload class: persistent HTTP API, SSE inference gateway, a service with database state, a build/test worker, and a device/GPU-dependent job **only if it is in scope for the selected node**. Record image/binary architecture, mounts and ownership, exact network path, required syscalls/devices, resource limits, recovery behavior and the foreground work that must remain usable. Do not take model-training or local-inference targets from an unrelated project and impose them as this stack’s acceptance thresholds.

## Benchmark protocol — proposed, not measured results

1. **Fix the experiment.** Use the same host, Windows/WSL versions, Linux filesystem placement, image digest, application config, resource caps and comparable network/storage paths. Record runtime and kernel details. Measure differences that cannot be equalized rather than hiding them.
2. **Pass semantics first.** Verify bind/volume ownership, persistence, restart, networking, SSE, device access when required, cleanup and isolation. A fast runtime that fails a must-have capability is not eligible.
3. **Separate regimes.** Run cold-image-pull, cached-image start, steady-state and restart/recovery tests separately. Report host idle and representative contended-host tests separately. Windows-mounted and Linux-native filesystem cases must not be silently pooled.
4. **Use paired repeated runs.** An initial proposal is at least 30 randomized paired runs per short experiment, with raw samples and a confidence interval for the difference. Longer soak/recovery cases need an explicitly chosen duration and fault schedule. Treat the sample count as a protocol starting point, not a universal statistical guarantee.
5. **Report complete costs.** Include setup/operator actions, resident memory, CPU, disk use, I/O, application throughput, p50/p95/p99 latency, startup and recovery, failed runs, orphaned resources and foreground degradation. Do not omit failures from timing summaries.
6. **Make a bounded decision.** Select the lane for this workload and host, not “Docker is globally better.” Record what evidence would reverse the choice.

## Proposed decision function

First apply operator-approved hard requirements. Among eligible candidates, retain the preferred runtime unless an alternative has a material benefit outside measurement noise and within approved cost/maintenance constraints. “Material” needs a predeclared target for the actual workload; this package does not invent a mandatory percentage improvement or spending cap.

An exception record must contain: required behavior; tested versions/configuration; raw evidence; alternatives and attempted remedies; measured delta with uncertainty; added privilege/operating burden; approved scope and expiration/review trigger. An optional PaaS convenience cannot be relabeled as an unavoidable runtime requirement without operator agreement.

## Read-only discovery and safe rehearsal

Start with executable paths and version commands, systemd/cgroup status, runtime inspection, socket permissions, WSL distribution identity, mount locations and container inventory. Avoid broad home-directory or credential dumps. Discovery output should redact tokens and personal paths from public reports.

Do not call `wsl --shutdown` against an active workstation just to test configuration. Reboot, logout, shutdown, rootful conversion, engine installation, opening a socket, changing firewall rules and stress tests are separately authorized rehearsal actions. Build the disposable test lane first.

## Quadlet-specific guardrails

Use the installed manual to confirm source paths and supported keys. Rootless Quadlets live under the user’s generator search paths; their generated services are not conventional persistent units to enable directly. Verify cgroup v2 and native systemd rather than adding legacy WSL init shims reflexively. [S015]

Model three separate lifetimes: **container service**, **Linux user/system manager**, and **WSL/Windows host**. A healthy service inside a stopped host is unavailable. Linger changes the user-manager lifecycle, not the Windows host’s power or WSL lifetime. [S014; design implication]


---

# GitHub capabilities and candidate-bound approval

**v0.2 evidence update:** the candidate job names are now recovered: `ci / lint`, `ci / test`, `CI`. The historical protection JSON drops spaces from the first two. The current fetched CI code confirms the declarations but does not establish the approved on-wire check contexts, trusted producers or full production coverage. Only those authority/run bindings—not the candidate names themselves—remain unresolved. Older references below to an unresolved trio mean this precise binding. [S033–S036]

## Correct plan matrix

This is a documentation-derived capability matrix, **not** a verified snapshot of the user’s account. Actual owner type, visibility and activated benefit must be recorded for every repository. [S008–S010]

| Repository / owner plan | Environments and environment secrets | Deployment-branch restrictions | Environment required reviewers / wait timers | Branch protection |
|---|---|---|---|---|
| Public / Free | Available | Available | Available | Available |
| Personal private / Free | Not available | Not available | Not available | Not available |
| Personal private / Pro, including activated eligible student benefit | Available | Available | Not available under Pro | Available |
| Organization private / Free | Not available | Not available | Not available | Not available |
| Organization private / Team | Available | Available | Not available under Team | Available |
| Private / applicable Enterprise offering | Verify exact offering/settings | Verify | Supported subject to configuration | Supported subject to configuration |

Repository secrets are a different feature from **environment secrets**. An unavailable environment feature does not imply every kind of secret or Actions feature is unavailable. Student eligibility is not proof the benefit is activated, and a personal Pro entitlement does not resolve an organization-owned repository’s plan. BytePort was returned as public by the connected repository search, so a blanket private-repository assumption is already inappropriate. [S009; S031]

The official Actions limits page gives Free/Pro hosted concurrency of 20/40 and included personal-plan minutes of 2,000/3,000 per month at review time. These are planning inputs, not the current remaining allowance or a promise of available runner capacity. Store limits separately from usage and refresh before relying on them. [S011]

## The two gates must not be collapsed

**Verification:** the actual required check set, including the unresolved “trio,” validates the exact candidate under trusted check identities and current policy.

**Authorization:** the appropriate human or independent policy authority authorizes promotion of that exact candidate to a specific environment. It is not enough that someone clicked Run workflow, that a bot said “approved,” or that HTTP returned 200. A configured list of permitted environment reviewers is not an all-member quorum. [S007; S008]

## Minimum candidate identity — proposed contract

| Field | Why it is required |
|---|---|
| Repository stable ID, canonical locator and source revision | Prevent source or repository substitution |
| Artifact digest(s), architecture and build/provenance reference | Prevent mutable-tag replacement or wrong-platform deployment |
| Manifest-byte digest and configuration/secret-reference version | Bind behavior, not just source code; never include raw secret values |
| Environment ID and target ID/generation | Prevent cross-environment reuse and apply against changed infrastructure |
| Policy version/digest and named required-check set | Prevent changing what “passed” means after approval |
| Check producer identities, run/attempt IDs and conclusions | Prevent spoofed names, rerun confusion and stale checks |
| Dependency and data-migration plan identity | Include material external changes and state compatibility |
| Approval actor, scope, issue/expiry time and unique authorization ID | Support authentic attribution, freshness and replay protection |

Hash the **exact persisted candidate bytes** and refer to those immutable bytes. Do not describe ordinary JSON pretty-printing as a universal canonical-JSON standard. Hash equality proves identity relative to the trusted reference; it does **not** prove authorship, approval or safety. Signatures or approval records need authenticated issuance, key/identity validation and a trust store outside candidate control.

## Fail-closed evaluation order

1. Establish trusted repository, target and policy identities. Refuse unknown gate definitions, including an unresolved trio.
2. Fetch evidence from trusted systems, not fields asserted by the candidate. Verify source revision, check producer, run attempt, accepted conclusion and policy freshness.
3. Verify artifact/configuration identity and required capability results. Refuse a required test that is skipped, missing, cancelled, stale or merely claimed by a README.
4. Authenticate the authorization, verify its scope/expiry, and compare its complete candidate binding.
5. Acquire an exclusive target lease and compare the observed generation against the approved precondition. Revalidate if the target changed while waiting.
6. Execute only the reviewed plan through the canonical actuator. Append receipts, observe health probation and transition to active only after the defined semantic health conditions hold.

This is a specification, not a cryptographic gate implementation bundled as production code.

## When native private-repository gates are unavailable

The low-component-count fallback is the **existing human-apply-only path** or an already-established trusted deployment integration, with its credentials separated from untrusted CI and the unprotected candidate repository. The operator verifies the pinned candidate/evidence and invokes the trusted actuator from an environment whose policy and credentials the candidate cannot modify. It is a real manual gate only to the extent that this trust separation actually holds. [S004; S007; design proposal]

A `workflow_dispatch` button may be a user interface for that flow, but it is not independently sufficient. Repository-write actors who can replace a workflow and obtain its deployment secrets may bypass the intended check. Do not compensate for a missing native feature by pretending branch protection exists, using an `echo success` job, or approving the same candidate under a self-authored policy.

## Reuse the review-control contract

Deduplicate and adjudicate findings, retain false-positive and accepted-risk rationales, cap optional review rounds, and invalidate stale applicable results when the candidate changes. Preserve independent GitHub App trigger behavior until explicitly reconfigured by its owner. A local review router cannot be assumed to disable an independently auto-triggering App. [S007]

Mandatory security checks and required reviews remain required. Optional semantic reviewer quota optimization is separate. This package neither changes required checks nor authorizes merge, deployment, review dismissal, branch-policy relaxation or secret movement.

## Unresolved production blockers

The trio’s exact members; accepted producer identities; authorization actor/quorum; activation and expiry of student benefits; repository-specific settings; current deployment credential custody; canonical actuator location; emergency override process. Until these are resolved, a generated release request may reach **planned**, but not **approved for production**.


---

# Release state, concurrency and data safety

**Proposed domain contract. Implement inside the resolved existing controller; this is not a request for another database or orchestration product.**

## State machine

| State | Entry evidence | Allowed next state |
|---|---|---|
| Draft | Application intent exists | Planned, Rejected |
| Planned | Pinned candidate, capabilities, state/migration plan | Verified, Rejected |
| Verified | Actual complete fresh required-check set | Approved, Superseded, Rejected |
| Approved | Authenticated candidate-bound authorization | Applying, Expired, Superseded |
| Applying | Lease acquired; generation precondition still holds | Probation, Failed, Recovery-required |
| Probation | Intended generation observed; semantic health being assessed | Active, Failed, Rolling-back, Recovery-required |
| Active | Health and required consumer checks pass | Superseded, Degraded, Rolling-back |
| Rolling-back | Authorized rollback plan and data compatibility evidence | Probation, Recovery-required |
| Recovery-required | State, side effects or data integrity uncertain | Human-reviewed recovery plan only |

Expired, rejected and superseded candidates retain evidence but cannot be promoted. Failed health does not implicitly authorize a dangerous data rollback. Revert to a previous artifact only when the approved rollback policy covers the current data schema and state.

## Concurrency and replay

Use an environment-scoped exclusive lease and generation precondition in the authoritative store. Persist operation identity before mutation where feasible; record partial outcomes. Lease loss or target-generation conflict must stop further writes. A retry uses the same idempotency identity and observes existing effects before deciding whether a step needs re-execution.

Exactly-once external side effects cannot be assumed merely because the controller has a database transaction. If a provider performed the operation but the receipt write failed, recovery needs an external resource/operation correlation key or an explicit uncertain-state disposition. Duplicate approval, webhook delivery and worker rescheduling are expected test cases, not exceptional excuses to bypass checks.

## Event envelope

Each transition receipt should identify event ID, previous event/reference, candidate digest, source revision, policy generation, operation/idempotency ID, environment and target generation, actor/producer, wall-clock timestamp, measured monotonic duration when available, outcome and evidence references. Do not put secrets, entire prompts or unrestricted raw provider bodies into the envelope.

Append-only means prior evidence is not silently edited to make a later state look cleaner. Corrections append a superseding record. Tamper-evidence and authentication are separate from append-only storage; use the ecosystem’s actual evidence and auth mechanisms rather than claiming an unsigned file is a secure ledger.

## Desired versus observed

Desired state is what the accepted candidate requests. Observed state is what a fresh runtime/provider inspection reports. Reconciled state means the required observations match the intended generation and its health contract. API acceptance is merely one event in that process.

At minimum display `candidate`, `desired_generation`, `observed_generation`, `observation_time`, `health_contract`, `authorization_state`, `drift`, and `last_operation`. Unknown or expired observations must not render as green. Deleting a failed attempt from a dashboard must not delete its audit record.

## Stateful deployment preflight

Record data owner, storage location, mount/UID expectations, backup method, retention, encryption/credential custody and restore target. Make a consistent snapshot or application-aware backup; prove restore in a disposable environment using the application’s own integrity checks. Operator-approved RPO and RTO are still unresolved and must not be fabricated.

For every migration choose: **backward-compatible**, **forward-fix only**, **backup restore required**, or **unknown/blocking**. The choice applies to application code plus data schema and dependencies, not an image alone. Verify that the previous application version can actually consume current data before allowing automatic artifact rollback.

## Release probation

Use readiness and liveness separately from semantic acceptance. Examples: an API returns the expected authenticated response; a database-backed write survives process restart; an SSE route emits useful events and correctly terminates; the expected consumer can reach the new generation. The operator/application owner must set timeout and failure thresholds for the workload. This document defines the evidence fields, not arbitrary universal SLO numbers.

## Recovery after control-plane loss

Inspect observed runtime objects and leases, correlate external operation IDs, verify current artifact/config/data identity and reconstruct the last trustworthy transition. Quarantine ambiguous generations from automatic promotion. Resume only under the existing approval policy or an explicitly scoped recovery authorization. Do not “fix” ambiguity by deleting unknown volumes, resetting an IaC backend, or force-running the latest plan.

Motivating sources: S001, S004, S007, S012, S027. Detailed mechanisms above are proposed design requirements, not claims that an existing repository already implements them.


---

# Networking, identity and routing evidence

## Four route classes — proposed policy

| Class | Intended consumer | Candidate path | Required authorization evidence |
|---|---|---|---|
| Private-tailnet | Operators and approved internal agents | Tailnet-private service path | Allowed node/user policy plus application role checks where needed |
| Authenticated-public-hostname | Users needing a custom public hostname but restricted access | Named tunnel plus separately configured Access/application policy | Visitor identity, audience/role behavior, denied identity and origin-bypass tests |
| Anonymous-public | Portfolio/demo content deliberately public | Qualified public HTTP path | Explicit public-data scope; no accidental admin or state endpoint exposure |
| Authenticated-machine | CI events, webhooks, service callers | Private route or authenticated public endpoint | Caller-supported service identity or validated webhook signature and replay handling |

The recovered user feedback names `*.pheno.studio`, `*.phenotype.space` and `projects.kooshapari.com`, and says private services should be inaccessible outside the tailnet. This is attributed intent in a compaction frame, not a verified DNS/zone inventory or authorization to change it. Private owned-domain names should use a qualified private DNS/TLS/origin path; custom spelling does not require public ingress. The authenticated-public-hostname row is an optional separately approved route class, not the default for this local stack. [E006; S032; S049]

Funnel reachability is public. Do not read a permission to create a Funnel as visitor authentication. The reviewed product restricts its names/ports and bandwidth configuration; that is a fit constraint, not a blanket claim that no production use is valid. Switching an existing private port to Funnel can change exposure. [S022]

A custom hostname with an Access policy can still be a private application in the ordinary sense of restricted users; “public hostname” describes reachability, not anonymous access. Conversely, deliberately anonymous pages should not inherit a browser-login requirement simply because private administration uses one. [S024; design distinction]

## Streaming path qualification

Quick Tunnel’s documented lack of SSE support is an explicit disqualifier when SSE is required. Its 200 in-flight request limit is also a limit, not a throughput benchmark. Do not carry these restrictions over indiscriminately to named tunnels. [S023]

For the selected path record every hop: client → local/network edge → tunnel/reverse proxy → application → upstream provider. Test event framing, immediate flushing, heartbeats, long gaps, first useful output, client disconnect, upstream cancellation and explicit failure termination at the **client**, not just at localhost. Specify buffering/timeouts, identity forwarding and maximum concurrent streams for the actual versions and plan. Leave unsupported settings as unknown rather than copying settings from a different proxy.

SSE bytes can include non-text events. A valid tool invocation, structured result or protocol-defined refusal must not be classified as an empty failure merely because text is absent. Define semantic completion per protocol and application. Conversely, an empty terminal marker or an upstream error hidden inside a successful HTTP envelope must not count as useful output.

## What the attached logs do and do not establish

The reproducible counts are in `evidence/log-metrics.json`; `tools/analyze_logs.py` regenerates them without repairing or replacing the original file. The input is a Markdown-escaped terminal excerpt, not a clean authoritative JSONL export. Pattern extraction is intentionally narrow and keeps original line references.

One explicit event reports success after **83,173 ms and 32 fallbacks** at original line 1777. It is a concrete reason to investigate latency and candidate traversal. It is not a measured user-end-to-end percentile. The repeated terminal `decisions` field requires a code definition; it could count policy events or traversal decisions rather than upstream calls. [S001:1777]

The file also shows warnings about empty completion and errors before useful content. It shows repeated zero-model sync reports despite explicit configured CPA routes. Zero discovered models need not mean no manually configured route exists. No complete correlation proves these observations share a cause. [S001:501,520,593,831,1053,1191,1764–1908]

**Do not calculate an error rate from six warning lines divided by the terminal-trace count.** The selected views lack a complete request denominator, request-start records and shared correlation on all warning messages. Do not infer that Cloudflare caused these loopback/provider-routing observations.

## Proposed observability contract

Per request: request ID, caller/tenant scope, requested protocol, resolved combo/policy generation, accepted context budget, deadline and semantic outcome. Per attempt: attempt ID, parent request, provider/model/config identity, start/end, transport status, error class, reason for selection/fallback, emitted event/byte/tool counts and cancellation status. Separate **queue time**, **upstream wait**, **first useful event**, **total attempt time** and **total request time**.

A decision event includes its type so the terminal summary can separately report `decisions_count`, `attempts_count` and `fallbacks_count`. A counter’s name is not its definition; link its source implementation and test. Keep payload bodies and prompts out of routine telemetry unless explicitly necessary and authorized.

## Bounded failover and replay safety

Define maximum attempts, total deadline, provider backoff/cooldown and terminal reason per workload. Respect quota/rate-limit signals rather than retrying every candidate until something happens. Missing quotas are unknown, not infinite capacity. These are control-plane design requirements, not a request to change provider accounts or subscription terms.

Failover before any irreversible effect can be permitted under policy, but it may still consume quota or incur cost. After content is emitted or a tool-side effect might have occurred, silent replay is unsafe unless the protocol supports it and the application has an explicit replay/idempotency contract. Propagate cancellation to the underlying work; disconnecting the client must not leave an uncontrolled cascade running.

## Investigation order

First obtain the active source/config generation and raw correlated traces. Then resolve what `decisions` means in code and whether context limits are enforced per upstream rather than merely declared on the combo. Reproduce the empty/error cases against a deterministic fixture. Finally test the actual external streaming path. This order avoids redesigning infrastructure to repair an unproven network diagnosis.


---

# Operations, portability and update ownership

## One-node baseline does not mean one undifferentiated trust domain

A workstation can host development and services, but those roles have different privileges and lifetimes. Keep untrusted builds away from production sockets, apply credentials and private data. A Linux user boundary or container name by itself is not proof of hostile-code containment. Qualify the actual runner/execution boundary, including mounts, network reachability and cleanup. [S012; S016]

The proposed initial slice is one disposable service with a private observation path, explicit resource limits and no irreplaceable data. Do not start by migrating every application, exposing public administration, or installing a PaaS that changes the preferred engine.

## Runbook A — preflight / first deployment

**Prerequisites:** resolved owner, exact candidate, known gate definition, authorized test target, recovery path and resource budget.

Read current host/runtime/plan settings and establish the observed target generation. Confirm storage paths and user ownership. Verify artifact digest and architecture, secret references, supported capabilities and complete required checks. Review the intended diff and data-migration classification. Obtain candidate-bound approval and acquire the target lease. Apply once, observe runtime identity and semantic health, and enter probation before marking the generation active.

**Stop conditions:** unknown trio; unsupported runtime semantics; missing approval; stale checks; target-generation drift; an unplanned public route; unknown data compatibility; absent backup/restore proof for stateful changes; a competing writer. A stop is a correct outcome, not a reason to weaken the checks.

## Runbook B — degraded service

Record the current candidate, runtime generation, route class and first failing symptom. Distinguish application, runtime, ingress, identity, provider and host-lifecycle failures. Preserve logs and last-known-good identity. Stop automatic promotion and avoid multiplying retries. Observe whether Windows/WSL is running before debugging an application that has no host.

Recover only the failed layer under existing authority. Restarting a service does not require recreating its data. Changing a private route into a public workaround is a security change, not a routine health repair. Exit when the intended generation and semantic health are proved; retain an incident receipt and any unreproduced uncertainty.

## Runbook C — rollback

Resolve the previous known-good artifact and configuration, compare data schema compatibility, check backup/restoration status and obtain rollback authority under the actual policy. Freeze competing writes. Reconcile to the approved rollback generation and run consumer health tests. If data compatibility is uncertain, stop in recovery-required rather than repeatedly starting old code against new data.

**Rollback completion evidence:** artifact/config identity; data compatibility or restoration receipt; route/auth behavior; application integrity checks; final observed generation; operator/actuator identity. Never claim successful rollback from a command exit alone.

## Runbook D — backup/restore drill

Use a disposable target with a representative application-consistent backup. Verify ownership, permissions, integrity and a real application read/write path after restoration. Record data age, recovery duration, retained dependencies and necessary secrets/key custody. Test restoration with the actual deployed version, not only that an archive can be decompressed.

Choose RPO/RTO and retention with the application/data owner. The source does not provide those values. No live data deletion, format migration or disk move is authorized by this package.

## Runbook E — workstation maintenance

Before reboot, WSL termination, engine upgrade or major resource changes, identify running services/jobs, classify interruption tolerance, pause new scheduling and preserve the current desired/observed generations. Perform the authorized change in its defined scope. Verify host, runtime, mounts, secret delivery, private networking and application health in that order. An update invalidates version-specific conformance where behavior could change.

Test logout and sleep separately from process restart. Native systemd does not guarantee host availability. If a workload needs an always-on target while the workstation sleeps, either change the approved availability expectation or place it on an independently available target; do not paper over that mismatch with a service-manager setting. [S014]

## Portability contract

| Dimension | Required source/target evidence | Common reason a move is not equivalent |
|---|---|---|
| Executable | Binary/image format, architecture, build inputs | Native binary is not a WebAssembly component |
| Isolation/devices | Kernel, KVM/device support, permissions | A stronger/different isolation or GPU requirement is missing |
| State | Location, consistency, export/import, UID, retention | Ephemeral target or incompatible volume ownership |
| Network | Names, protocols, reachability, identity, egress | Public/private assumptions or SSE behavior changes |
| Lifecycle | Restart, idle/sleep, health and deployment limits | Target can suspend or cannot meet recovery expectations |
| Secrets | Delivery and rotation, identity audience, key custody | Local paths or credentials are not portable identities |
| Data migration | Schema compatibility and verified restoration | Old code cannot consume migrated data |
| Economics | Explicit allowed plan, resource/bandwidth/storage charges | A free label hides expiry, idling or resource restrictions |

Render’s free tier is not a transparent persistent production replacement: the reviewed page describes idling web services, no free persistent disk, expiring free Postgres and cautions against production use. [S028] A paid or different target might qualify, but no spending is approved here.

Spin is a deliberate Wasm application target. Native services and KVM-based VMs are different placement options. The custom `nanovms` repository and third-party products using similar names must be identified separately. Native macOS VM support in an abstraction must not be labeled native Firecracker support without proving the actual Linux/KVM path. [S003; S029–S030]

## IaC selection: retain before replacing

Inspect the existing Terraform/OpenTofu/Pulumi source, state owner and recovery process before a language-driven migration. A Python Automation API can be useful, but that is not evidence the user needs a new IaC implementation or that the Docker provider’s every resource works through Podman. Qualify the exact resource operations and honor the existing core/edge language decision process. [S006; S025–S027]

The provider owns infrastructure state; the deployment actuator owns release state. Their plans must identify imported resources, mutation scope, locking, partial-failure behavior and recovery. A management UI’s manual action must be reconciled as drift rather than accepted as an unexplained second source of truth.

## Updates and supply-chain changes

The previous synthesis proposed Renovate plus vulnerability alerts. Treat update-bot selection as a proposal until the actual existing setup is inspected; this review did not qualify every Renovate/Dependabot configuration. One updater should own each dependency-update stream to avoid duplicate PRs. Vulnerability alerting can coexist without becoming a deployment controller. [S001:2086; design proposal]

Pin production artifacts to digests and review changes through the normal candidate path. Do not combine automatic image-tag following, PaaS git autodeploy and an outer approval loop over the same resource. Keep the previous approved generation available within an authorized retention policy. Record upstream version, reason, tests, rollback compatibility and observer/consumer impact for every promotion.

## Capacity and cost record

Record available host capacity, reserved interactive capacity, workload limits, queue policy, storage growth and measured contention. The source supplies no budget or RPO/RTO for this specific deployment stack, so these remain explicit null/unresolved values in the machine record. Reuse existing hardware where appropriate, but do not claim spare capacity from historical hardware memories without current inventory.

Cost estimates must state assumptions and separate existing subscriptions/resources from new recurring commitments. A recommendation in this document is not permission to create paid infrastructure. Broad provider pricing was not researched in this pass and no cost savings are claimed.


---

# Operational acceptance test catalog

None of these tests has been run against the user environment. Passing package validation is not passing these tests. Run disruptive cases only on authorized disposable targets. Each result requires pinned inputs, complete relevant output, timestamps and verifier identity.

## AT-DEP-001 — Reject ungrounded closure

**Status:** not_run. **Requirement:** FR-DEP-001.

1. Submit a report with a claimed passing test but no receipt.
2. Submit a declaration-only ownership assertion as verified implementation.

**Expected:** Both are rejected as closure evidence, while their original records remain preserved.

**Evidence required:** Exact source/runtime/config revisions; Command or API request and complete relevant output; Observed outcome and timestamp; Reviewer or machine-verifier identity

## AT-DEP-002 — Disambiguate runtime discovery

**Status:** not_run. **Requirement:** FR-DEP-002.

1. Collect WSL, wslc and Podman versions plus actual executable paths.
2. Present a WSLC-only node to a Podman-socket adapter.

**Expected:** The adapter reports unsupported or unqualified; it never fabricates a Podman endpoint.

**Evidence required:** Exact source/runtime/config revisions; Command or API request and complete relevant output; Observed outcome and timestamp; Reviewer or machine-verifier identity

## AT-DEP-003 — Evaluate an engine exception

**Status:** not_run. **Requirement:** FR-DEP-003.

1. Compare an unsupported PaaS feature, an optional UI convenience and a measured critical-workload benefit.
2. Inspect the decision record and scope of approval.

**Expected:** Only documented, authorized exceptions can change placement; optional convenience is not silently treated as a hard requirement.

**Evidence required:** Exact source/runtime/config revisions; Command or API request and complete relevant output; Observed outcome and timestamp; Reviewer or machine-verifier identity

## AT-DEP-004 — Fail closed on an unknown capability

**Status:** not_run. **Requirement:** FR-DEP-004.

1. Require Swarm semantics or KVM on a node with unknown support.
2. Require persistent storage on an ephemeral-only adapter.

**Expected:** Placement is blocked with a machine-readable reason before any mutation.

**Evidence required:** Exact source/runtime/config revisions; Command or API request and complete relevant output; Observed outcome and timestamp; Reviewer or machine-verifier identity

## AT-DEP-005 — Reproduce a runtime comparison

**Status:** not_run. **Requirement:** FR-DEP-005.

1. Run the benchmark protocol in docs/06-runtime-selection.md.
2. Repeat paired runs and compare cold/warm and idle/contended results.

**Expected:** A report includes raw data and uncertainty; it cannot claim a global runtime winner from one synthetic benchmark.

**Evidence required:** Exact source/runtime/config revisions; Command or API request and complete relevant output; Observed outcome and timestamp; Reviewer or machine-verifier identity

## AT-DEP-006 — Detect competing writers

**Status:** not_run. **Requirement:** FR-DEP-006.

1. Register a resource under both Quadlet and an independently auto-deploying PaaS.
2. Attempt concurrent apply with two controllers.

**Expected:** Registration or apply is blocked; the conflict is explicit and no double deployment is accepted.

**Evidence required:** Exact source/runtime/config revisions; Command or API request and complete relevant output; Observed outcome and timestamp; Reviewer or machine-verifier identity

## AT-DEP-007 — Check the integration ownership map

**Status:** not_run. **Requirement:** FR-DEP-007.

1. Compare planned imports with current role ADRs, module locations and consumers.
2. Check tehgent/thegent distinctions and migration receipts.

**Expected:** Each authoritative artifact has one destination; provisional aliases remain visible until adjudicated.

**Evidence required:** Exact source/runtime/config revisions; Command or API request and complete relevant output; Observed outcome and timestamp; Reviewer or machine-verifier identity

## AT-DEP-008 — Validate public/private plan cases

**Status:** not_run. **Requirement:** FR-DEP-008.

1. Exercise public-Free, personal-private-Free, personal-private-Pro and organization-private cases using inspected settings or isolated fixtures.
2. Simulate inaccessible settings.

**Expected:** Only supported gates are selected; access errors cannot produce a permissive fallback.

**Evidence required:** Exact source/runtime/config revisions; Command or API request and complete relevant output; Observed outcome and timestamp; Reviewer or machine-verifier identity

## AT-DEP-009 — Reject unknown or spoofed checks

**Status:** not_run. **Requirement:** FR-DEP-009.

1. Omit one trio member.
2. Submit a similarly named check from an unauthorized producer or stale revision.

**Expected:** No release approval is issued; unknown trio identity is a first-class blocker.

**Evidence required:** Exact source/runtime/config revisions; Command or API request and complete relevant output; Observed outcome and timestamp; Reviewer or machine-verifier identity

## AT-DEP-010 — Invalidate changed or forged approval

**Status:** not_run. **Requirement:** FR-DEP-010.

1. Approve candidate A, then change image digest, config, target or policy.
2. Replay the approval or substitute the actor identity.

**Expected:** Every changed, expired, reused or forged authorization is denied before apply.

**Evidence required:** Exact source/runtime/config revisions; Command or API request and complete relevant output; Observed outcome and timestamp; Reviewer or machine-verifier identity

## AT-DEP-011 — Recover from apply crashes

**Status:** not_run. **Requirement:** FR-DEP-011.

1. Crash before mutation, after mutation but before receipt, and during health probation.
2. Retry with the same and conflicting candidate.

**Expected:** At most one accepted active generation exists; retries converge or stop for review without duplicate side effects.

**Evidence required:** Exact source/runtime/config revisions; Command or API request and complete relevant output; Observed outcome and timestamp; Reviewer or machine-verifier identity

## AT-DEP-012 — Probe runner isolation

**Status:** not_run. **Requirement:** FR-DEP-012.

1. From an untrusted job attempt to access the production socket, secret store, state backend and host home directories.
2. Inspect network and mount boundaries.

**Expected:** Access is denied, sensitive material is absent, and cleanup is verified independently of runner deregistration.

**Evidence required:** Exact source/runtime/config revisions; Command or API request and complete relevant output; Observed outcome and timestamp; Reviewer or machine-verifier identity

## AT-DEP-013 — Check secret handling

**Status:** not_run. **Requirement:** FR-DEP-013.

1. Inject a canary secret into a failed deployment path and a provider error.
2. Export the public evidence view.

**Expected:** The secret is absent from public artifacts, logs and manifest fields; private provenance remains linked.

**Evidence required:** Exact source/runtime/config revisions; Command or API request and complete relevant output; Observed outcome and timestamp; Reviewer or machine-verifier identity

## AT-DEP-014 — Verify reachability and authorization

**Status:** not_run. **Requirement:** FR-DEP-014.

1. Test an allowed identity, denied identity, anonymous visitor and direct-origin access for each route class.
2. Attempt to change a private Serve port to Funnel.

**Expected:** Observed behavior matches the declared class; public exposure changes require separate authorization.

**Evidence required:** Exact source/runtime/config revisions; Command or API request and complete relevant output; Observed outcome and timestamp; Reviewer or machine-verifier identity

## AT-DEP-015 — Test actual SSE path

**Status:** not_run. **Requirement:** FR-DEP-015.

1. Send chunked SSE with heartbeats, content, tool events, an empty terminal result and an upstream error.
2. Cancel the client and observe upstream work.

**Expected:** Events remain correctly ordered/framed; errors are classified, empty semantic results are not ordinary success, and cancellation is propagated.

**Evidence required:** Exact source/runtime/config revisions; Command or API request and complete relevant output; Observed outcome and timestamp; Reviewer or machine-verifier identity

## AT-DEP-016 — Test workstation lifecycle

**Status:** not_run. **Requirement:** FR-DEP-016.

1. Exercise Windows reboot, user logout, sleep/resume, WSL termination and loss/restoration of network.
2. Check service ownership, persistent data and restart receipts.

**Expected:** Recovery behavior and outages are recorded; a user-service linger setting is not accepted as a keep-alive guarantee.

**Evidence required:** Exact source/runtime/config revisions; Command or API request and complete relevant output; Observed outcome and timestamp; Reviewer or machine-verifier identity

## AT-DEP-017 — Measure contended-host behavior

**Status:** not_run. **Requirement:** FR-DEP-017.

1. Run a service plus a representative build/test job and operator foreground workload.
2. Exceed the configured memory, disk and concurrency limits.

**Expected:** Limits are enforced; queue/rejection and foreground degradation are measured against operator-approved tolerances.

**Evidence required:** Exact source/runtime/config revisions; Command or API request and complete relevant output; Observed outcome and timestamp; Reviewer or machine-verifier identity

## AT-DEP-018 — Detect false green state

**Status:** not_run. **Requirement:** FR-DEP-018.

1. Return HTTP 200 with empty application output.
2. Make the desired generation differ from the observed image or config.

**Expected:** The interface reports degraded, unverified or drifted state rather than a green deployment.

**Evidence required:** Exact source/runtime/config revisions; Command or API request and complete relevant output; Observed outcome and timestamp; Reviewer or machine-verifier identity

## AT-DEP-019 — Correlate fallback evidence

**Status:** not_run. **Requirement:** FR-DEP-019.

1. Reproduce an empty response, provider error, cancellation and successful bounded failover.
2. Inspect the exact code definition of the decisions counter.

**Expected:** Each event joins to the correct request/attempt; counts have defined denominators and no retry resumes after irreversible user-visible/tool side effects without policy.

**Evidence required:** Exact source/runtime/config revisions; Command or API request and complete relevant output; Observed outcome and timestamp; Reviewer or machine-verifier identity

## AT-DEP-020 — Restore after incompatible migration

**Status:** not_run. **Requirement:** FR-DEP-020.

1. Restore a disposable copy of representative data.
2. Attempt rollback after a backward-incompatible migration.

**Expected:** Restoration is measured and verified; unsafe rollback stops for explicit recovery rather than corrupting data.

**Evidence required:** Exact source/runtime/config revisions; Command or API request and complete relevant output; Observed outcome and timestamp; Reviewer or machine-verifier identity

## AT-DEP-021 — Reject a false portable placement

**Status:** not_run. **Requirement:** FR-DEP-021.

1. Attempt to move a persistent native process with device access to an incompatible WebAssembly or free ephemeral target.
2. Inspect data export/import and service identity.

**Expected:** The plan reports precise blockers and transformation work; a shared manifest does not imply semantic equivalence.

**Evidence required:** Exact source/runtime/config revisions; Command or API request and complete relevant output; Observed outcome and timestamp; Reviewer or machine-verifier identity

## AT-DEP-022 — Test state-writer exclusion

**Status:** not_run. **Requirement:** FR-DEP-022.

1. Start two state-changing operations against the same resource scope.
2. Simulate a failed apply and recover state.

**Expected:** Only the authorized writer proceeds; recovery does not silently replace or orphan resources.

**Evidence required:** Exact source/runtime/config revisions; Command or API request and complete relevant output; Observed outcome and timestamp; Reviewer or machine-verifier identity

## AT-DEP-023 — Stop update bypass

**Status:** not_run. **Requirement:** FR-DEP-023.

1. Change an upstream mutable tag after approval.
2. Enable a second automatic deploy hook for the same app.

**Expected:** Digest mismatch or ownership conflict prevents promotion; alerting continues without deployment authority.

**Evidence required:** Exact source/runtime/config revisions; Command or API request and complete relevant output; Observed outcome and timestamp; Reviewer or machine-verifier identity

## AT-DEP-024 — Audit a handoff receipt

**Status:** not_run. **Requirement:** FR-DEP-024.

1. Compare the handoff against changed files, pinned revisions, test output and remaining blockers.
2. Present a documentation-only change as deployed functionality.

**Expected:** The documentation-only claim is rejected; partial delivery is retained with explicit next evidence requirements.

**Evidence required:** Exact source/runtime/config revisions; Command or API request and complete relevant output; Observed outcome and timestamp; Reviewer or machine-verifier identity

## AT-DEP-025 — Local-first placement and workload profiles

**Status:** not_run. **Requirement:** FR-DEP-025.

1. Exercise a service, a CLI package, a desktop app and a documentation site using distinct delivery profiles.
2. Resolve local dev without provisioning a managed service.

**Expected:** No implicit cloud resource; each profile reaches its own artifact/operational acceptance boundary.

**Evidence required:** Versioned delivery profile for each workload class; resolved local target identity.; Artifact or observation receipts and a dry-run resource delta showing no implicit managed dev allocation.

## AT-DEP-026 — Exact nightly scheduling semantics

**Status:** not_run. **Requirement:** FR-DEP-026.

1. Test 0, 1 and 2 new commits on push and on a scheduled tick.
2. Inject missing ancestry, duplicate event and concurrent target requests.

**Expected:** One new commit waits for the scheduled path; two qualify on push; unknown ancestry blocks; duplicates cannot race.

**Evidence required:** Exact input event, due-tick record, observed healthy watermark and ancestry/counting rule.; One-commit, two-commit, same-candidate, offline, divergent-history and force/lease outcomes with immutable candidate identity.

## AT-DEP-027 — Workflow semantic and caller-contract validation

**Status:** not_run. **Requirement:** FR-DEP-027.

1. Validate location, inputs, secrets and permission contracts with semantic checks.
2. Resolve the pinned workflow and run a disposable credential-free caller before qualifying a trusted deploy path.

**Expected:** Nested paths, missing contracts and unexpected secret flow fail before apply.

**Evidence required:** Supported immutable workflow path and complete caller/interface declarations.; Actual disposable GitHub platform resolution/run result; redacted secret-scope and credential-boundary evidence.

## AT-DEP-028 — Source-mode and deployed-artifact binding

**Status:** not_run. **Requirement:** FR-DEP-028.

1. Deploy a fixture Git-backed service and image-backed service through distinct adapter branches.
2. Move a mutable image tag after approval and return malformed or paginated provider data.

**Expected:** No changed artifact is approved by an unchanged Git SHA; unknown/mismatched identity blocks promotion.

**Evidence required:** Immutable source/build/test provenance and published artifact digest.; Provider source-mode request/response fixture and independently observed deployed artifact/revision.

## AT-DEP-029 — Machine-derived CI result contract

**Status:** not_run. **Requirement:** FR-DEP-029.

1. Compare ci / lint and ci/lint and reject the mismatch.
2. Fail detect-changes, trunk-check or dependency-review; simulate an absent required job and duplicate display names.

**Expected:** No green aggregate hides a required dependency failure or ambiguous producer.

**Evidence required:** Observed check-run/context names, trusted app/workflow identities and exact candidate binding.; Complete dependency result matrix including approved not-applicable reasons; spoofed/stale/skipped-required rejection receipts.

## AT-DEP-030 — Verified recovery operations

**Status:** not_run. **Requirement:** FR-DEP-030.

1. Omit health URL; fail health; remove the previous image; test incompatible migration.
2. Attempt a rollback while provider autodeploy could restore the bad revision.

**Expected:** Unknown health blocks; recovery is observed; incompatible or missing recovery evidence leads to recovery-required.

**Evidence required:** Failure injection, previous healthy candidate and recovery authorization/action receipt.; Independent restored application/data integrity observations and missing-URL/wrong-candidate fail-closed receipts.

## AT-DEP-031 — Managed-service capabilities and test emulators

**Status:** not_run. **Requirement:** FR-DEP-031.

1. Run the application action suite on its emulator and actual durable-service fixture.
2. Test unsupported API action, auth mismatch, database extension and HTTP-vs-wire-protocol mismatch.

**Expected:** Simulator success cannot be relabeled production parity; unsupported requirements block the target.

**Evidence required:** Versioned required service operation matrix and redacted request/response fixtures.; Durability/restore and migration evidence; explicit emulator-only and unsupported-capability declarations.

## AT-DEP-032 — Transcript provenance and compaction-aware intake

**Status:** not_run. **Requirement:** FR-DEP-032.

1. Decode every retained conversation; compare count and source hash; label root vs delegated prompts.
2. Re-ingest the same export and verify idempotent evidence references; inject truncated JSON.

**Expected:** No duplicated message count, silent parse loss or compaction-to-approval promotion.

**Evidence required:** Original and derivative hashes, message/source ranges and parent links.; Duplicate/repeated ingestion outcomes and preserved compaction/source-class markers without secret or reasoning dumps.

## AT-DEP-033 — Private ingress and application authorization

**Status:** not_run. **Requirement:** FR-DEP-033.

1. Test off-tailnet, unauthorized-tailnet, permitted-client and permitted-CI identities.
2. Check DNS-only, proxied public, alternate provider hostname and direct-origin paths.

**Expected:** Only intended routes work; no public/origin bypass; membership alone cannot mutate production.

**Evidence required:** Private/public route classification, DNS/TLS identity and exact allowed principal policy.; Outside-tailnet deny, direct-origin bypass and insufficient-application-role negative-test receipts.

## AT-DEP-034 — Declared versus live readiness states

**Status:** not_run. **Requirement:** FR-DEP-034.

1. Present a valid local YAML that references a nonexistent remote path.
2. Present untracked manifests, unapplied protection JSON and a run that only parsed syntax.

**Expected:** None is reported deployed, enforced, production-ready or recovered without the matching evidence.

**Evidence required:** Separately linked write/readback/commit/platform/execution/observation/recovery/acceptance receipts where applicable.; Reviewer disposition proving a task completion flag or generated report alone cannot advance readiness.

## AT-DEP-035 — Single BytePort control plane

**Status:** not_run. **Requirement:** FR-DEP-035.

1. Exercise the single byteport control plane contract on an authorized disposable fixture or read-only live inventory.
2. Introduce one contrary/negative case that would falsely pass under a weaker implementation.
3. Record exact inputs, revisions, observed outputs and verifier identity.

**Expected:** The contract preserves the stated boundary, rejects or exposes the negative case, and produces machine-readable evidence without claiming broader readiness.

**Evidence required:** Pinned subject/runtime/provider revisions; Complete relevant command/API or fixture output; Timestamped observed result; Verifier/reviewer identity and disposition

## AT-DEP-036 — Qualified local-fleet provider

**Status:** not_run. **Requirement:** FR-DEP-036.

1. Exercise the qualified local-fleet provider contract on an authorized disposable fixture or read-only live inventory.
2. Introduce one contrary/negative case that would falsely pass under a weaker implementation.
3. Record exact inputs, revisions, observed outputs and verifier identity.

**Expected:** The contract preserves the stated boundary, rejects or exposes the negative case, and produces machine-readable evidence without claiming broader readiness.

**Evidence required:** Pinned subject/runtime/provider revisions; Complete relevant command/API or fixture output; Timestamped observed result; Verifier/reviewer identity and disposition

## AT-DEP-037 — Node daemon identity and admission

**Status:** not_run. **Requirement:** FR-DEP-037.

1. Exercise the node daemon identity and admission contract on an authorized disposable fixture or read-only live inventory.
2. Introduce one contrary/negative case that would falsely pass under a weaker implementation.
3. Record exact inputs, revisions, observed outputs and verifier identity.

**Expected:** The contract preserves the stated boundary, rejects or exposes the negative case, and produces machine-readable evidence without claiming broader readiness.

**Evidence required:** Pinned subject/runtime/provider revisions; Complete relevant command/API or fixture output; Timestamped observed result; Verifier/reviewer identity and disposition

## AT-DEP-038 — Resource reservation and host modes

**Status:** not_run. **Requirement:** FR-DEP-038.

1. Exercise the resource reservation and host modes contract on an authorized disposable fixture or read-only live inventory.
2. Introduce one contrary/negative case that would falsely pass under a weaker implementation.
3. Record exact inputs, revisions, observed outputs and verifier identity.

**Expected:** The contract preserves the stated boundary, rejects or exposes the negative case, and produces machine-readable evidence without claiming broader readiness.

**Evidence required:** Pinned subject/runtime/provider revisions; Complete relevant command/API or fixture output; Timestamped observed result; Verifier/reviewer identity and disposition

## AT-DEP-039 — Workload priority and preemption

**Status:** not_run. **Requirement:** FR-DEP-039.

1. Exercise the workload priority and preemption contract on an authorized disposable fixture or read-only live inventory.
2. Introduce one contrary/negative case that would falsely pass under a weaker implementation.
3. Record exact inputs, revisions, observed outputs and verifier identity.

**Expected:** The contract preserves the stated boundary, rejects or exposes the negative case, and produces machine-readable evidence without claiming broader readiness.

**Evidence required:** Pinned subject/runtime/provider revisions; Complete relevant command/API or fixture output; Timestamped observed result; Verifier/reviewer identity and disposition

## AT-DEP-040 — Immutable pull-based artifact delivery

**Status:** not_run. **Requirement:** FR-DEP-040.

1. Exercise the immutable pull-based artifact delivery contract on an authorized disposable fixture or read-only live inventory.
2. Introduce one contrary/negative case that would falsely pass under a weaker implementation.
3. Record exact inputs, revisions, observed outputs and verifier identity.

**Expected:** The contract preserves the stated boundary, rejects or exposes the negative case, and produces machine-readable evidence without claiming broader readiness.

**Evidence required:** Pinned subject/runtime/provider revisions; Complete relevant command/API or fixture output; Timestamped observed result; Verifier/reviewer identity and disposition

## AT-DEP-041 — Daemon safe update and rollback

**Status:** not_run. **Requirement:** FR-DEP-041.

1. Exercise the daemon safe update and rollback contract on an authorized disposable fixture or read-only live inventory.
2. Introduce one contrary/negative case that would falsely pass under a weaker implementation.
3. Record exact inputs, revisions, observed outputs and verifier identity.

**Expected:** The contract preserves the stated boundary, rejects or exposes the negative case, and produces machine-readable evidence without claiming broader readiness.

**Evidence required:** Pinned subject/runtime/provider revisions; Complete relevant command/API or fixture output; Timestamped observed result; Verifier/reviewer identity and disposition

## AT-DEP-042 — Private node control boundary

**Status:** not_run. **Requirement:** FR-DEP-042.

1. Exercise the private node control boundary contract on an authorized disposable fixture or read-only live inventory.
2. Introduce one contrary/negative case that would falsely pass under a weaker implementation.
3. Record exact inputs, revisions, observed outputs and verifier identity.

**Expected:** The contract preserves the stated boundary, rejects or exposes the negative case, and produces machine-readable evidence without claiming broader readiness.

**Evidence required:** Pinned subject/runtime/provider revisions; Complete relevant command/API or fixture output; Timestamped observed result; Verifier/reviewer identity and disposition

## AT-DEP-043 — Stateful-service lifecycle contract

**Status:** not_run. **Requirement:** FR-DEP-043.

1. Exercise the stateful-service lifecycle contract contract on an authorized disposable fixture or read-only live inventory.
2. Introduce one contrary/negative case that would falsely pass under a weaker implementation.
3. Record exact inputs, revisions, observed outputs and verifier identity.

**Expected:** The contract preserves the stated boundary, rejects or exposes the negative case, and produces machine-readable evidence without claiming broader readiness.

**Evidence required:** Pinned subject/runtime/provider revisions; Complete relevant command/API or fixture output; Timestamped observed result; Verifier/reviewer identity and disposition

## AT-DEP-044 — Capability-qualified portability

**Status:** not_run. **Requirement:** FR-DEP-044.

1. Exercise the capability-qualified portability contract on an authorized disposable fixture or read-only live inventory.
2. Introduce one contrary/negative case that would falsely pass under a weaker implementation.
3. Record exact inputs, revisions, observed outputs and verifier identity.

**Expected:** The contract preserves the stated boundary, rejects or exposes the negative case, and produces machine-readable evidence without claiming broader readiness.

**Evidence required:** Pinned subject/runtime/provider revisions; Complete relevant command/API or fixture output; Timestamped observed result; Verifier/reviewer identity and disposition

## AT-DEP-045 — Human-agent-automation API parity

**Status:** not_run. **Requirement:** FR-DEP-045.

1. Exercise the human-agent-automation api parity contract on an authorized disposable fixture or read-only live inventory.
2. Introduce one contrary/negative case that would falsely pass under a weaker implementation.
3. Record exact inputs, revisions, observed outputs and verifier identity.

**Expected:** The contract preserves the stated boundary, rejects or exposes the negative case, and produces machine-readable evidence without claiming broader readiness.

**Evidence required:** Pinned subject/runtime/provider revisions; Complete relevant command/API or fixture output; Timestamped observed result; Verifier/reviewer identity and disposition

## AT-DEP-046 — Automation-safe operations

**Status:** not_run. **Requirement:** FR-DEP-046.

1. Exercise the automation-safe operations contract on an authorized disposable fixture or read-only live inventory.
2. Introduce one contrary/negative case that would falsely pass under a weaker implementation.
3. Record exact inputs, revisions, observed outputs and verifier identity.

**Expected:** The contract preserves the stated boundary, rejects or exposes the negative case, and produces machine-readable evidence without claiming broader readiness.

**Evidence required:** Pinned subject/runtime/provider revisions; Complete relevant command/API or fixture output; Timestamped observed result; Verifier/reviewer identity and disposition

## AT-DEP-047 — Single Assessment Dossier with staged evaluation

**Status:** not_run. **Requirement:** FR-DEP-047.

1. Exercise the single assessment dossier with staged evaluation contract on an authorized disposable fixture or read-only live inventory.
2. Introduce one contrary/negative case that would falsely pass under a weaker implementation.
3. Record exact inputs, revisions, observed outputs and verifier identity.

**Expected:** The contract preserves the stated boundary, rejects or exposes the negative case, and produces machine-readable evidence without claiming broader readiness.

**Evidence required:** Pinned subject/runtime/provider revisions; Complete relevant command/API or fixture output; Timestamped observed result; Verifier/reviewer identity and disposition

## AT-DEP-048 — Scorecard profile convergence

**Status:** not_run. **Requirement:** FR-DEP-048.

1. Exercise the scorecard profile convergence contract on an authorized disposable fixture or read-only live inventory.
2. Introduce one contrary/negative case that would falsely pass under a weaker implementation.
3. Record exact inputs, revisions, observed outputs and verifier identity.

**Expected:** The contract preserves the stated boundary, rejects or exposes the negative case, and produces machine-readable evidence without claiming broader readiness.

**Evidence required:** Pinned subject/runtime/provider revisions; Complete relevant command/API or fixture output; Timestamped observed result; Verifier/reviewer identity and disposition

## AT-DEP-049 — Emergent corpus branch salvage

**Status:** not_run. **Requirement:** FR-DEP-049.

1. Exercise the emergent corpus branch salvage contract on an authorized disposable fixture or read-only live inventory.
2. Introduce one contrary/negative case that would falsely pass under a weaker implementation.
3. Record exact inputs, revisions, observed outputs and verifier identity.

**Expected:** The contract preserves the stated boundary, rejects or exposes the negative case, and produces machine-readable evidence without claiming broader readiness.

**Evidence required:** Pinned subject/runtime/provider revisions; Complete relevant command/API or fixture output; Timestamped observed result; Verifier/reviewer identity and disposition

## AT-DEP-050 — Emergent corpus integration and continuation gate

**Status:** not_run. **Requirement:** FR-DEP-050.

1. Exercise the emergent corpus integration and continuation gate contract on an authorized disposable fixture or read-only live inventory.
2. Introduce one contrary/negative case that would falsely pass under a weaker implementation.
3. Record exact inputs, revisions, observed outputs and verifier identity.

**Expected:** The contract preserves the stated boundary, rejects or exposes the negative case, and produces machine-readable evidence without claiming broader readiness.

**Evidence required:** Pinned subject/runtime/provider revisions; Complete relevant command/API or fixture output; Timestamped observed result; Verifier/reviewer identity and disposition

## AT-DEP-051 — Live review-provider capability registry

**Status:** not_run. **Requirement:** FR-DEP-051.

1. Exercise the live review-provider capability registry contract on an authorized disposable fixture or read-only live inventory.
2. Introduce one contrary/negative case that would falsely pass under a weaker implementation.
3. Record exact inputs, revisions, observed outputs and verifier identity.

**Expected:** The contract preserves the stated boundary, rejects or exposes the negative case, and produces machine-readable evidence without claiming broader readiness.

**Evidence required:** Pinned subject/runtime/provider revisions; Complete relevant command/API or fixture output; Timestamped observed result; Verifier/reviewer identity and disposition

## AT-DEP-052 — Risk-tiered selective semantic review

**Status:** not_run. **Requirement:** FR-DEP-052.

1. Exercise the risk-tiered selective semantic review contract on an authorized disposable fixture or read-only live inventory.
2. Introduce one contrary/negative case that would falsely pass under a weaker implementation.
3. Record exact inputs, revisions, observed outputs and verifier identity.

**Expected:** The contract preserves the stated boundary, rejects or exposes the negative case, and produces machine-readable evidence without claiming broader readiness.

**Evidence required:** Pinned subject/runtime/provider revisions; Complete relevant command/API or fixture output; Timestamped observed result; Verifier/reviewer identity and disposition

## AT-DEP-053 — Review dispatch coalescing and quota reservation

**Status:** not_run. **Requirement:** FR-DEP-053.

1. Exercise the review dispatch coalescing and quota reservation contract on an authorized disposable fixture or read-only live inventory.
2. Introduce one contrary/negative case that would falsely pass under a weaker implementation.
3. Record exact inputs, revisions, observed outputs and verifier identity.

**Expected:** The contract preserves the stated boundary, rejects or exposes the negative case, and produces machine-readable evidence without claiming broader readiness.

**Evidence required:** Pinned subject/runtime/provider revisions; Complete relevant command/API or fixture output; Timestamped observed result; Verifier/reviewer identity and disposition

## AT-DEP-054 — Historical review reconciliation

**Status:** not_run. **Requirement:** FR-DEP-054.

1. Exercise the historical review reconciliation contract on an authorized disposable fixture or read-only live inventory.
2. Introduce one contrary/negative case that would falsely pass under a weaker implementation.
3. Record exact inputs, revisions, observed outputs and verifier identity.

**Expected:** The contract preserves the stated boundary, rejects or exposes the negative case, and produces machine-readable evidence without claiming broader readiness.

**Evidence required:** Pinned subject/runtime/provider revisions; Complete relevant command/API or fixture output; Timestamped observed result; Verifier/reviewer identity and disposition

## AT-DEP-055 — Normalized finding and disposition ledger

**Status:** not_run. **Requirement:** FR-DEP-055.

1. Exercise the normalized finding and disposition ledger contract on an authorized disposable fixture or read-only live inventory.
2. Introduce one contrary/negative case that would falsely pass under a weaker implementation.
3. Record exact inputs, revisions, observed outputs and verifier identity.

**Expected:** The contract preserves the stated boundary, rejects or exposes the negative case, and produces machine-readable evidence without claiming broader readiness.

**Evidence required:** Pinned subject/runtime/provider revisions; Complete relevant command/API or fixture output; Timestamped observed result; Verifier/reviewer identity and disposition

## AT-DEP-056 — Zero-new-spend review enforcement

**Status:** not_run. **Requirement:** FR-DEP-056.

1. Exercise the zero-new-spend review enforcement contract on an authorized disposable fixture or read-only live inventory.
2. Introduce one contrary/negative case that would falsely pass under a weaker implementation.
3. Record exact inputs, revisions, observed outputs and verifier identity.

**Expected:** The contract preserves the stated boundary, rejects or exposes the negative case, and produces machine-readable evidence without claiming broader readiness.

**Evidence required:** Pinned subject/runtime/provider revisions; Complete relevant command/API or fixture output; Timestamped observed result; Verifier/reviewer identity and disposition

## AT-DEP-057 — Deterministic gates independent of AI quotas

**Status:** not_run. **Requirement:** FR-DEP-057.

1. Exercise the deterministic gates independent of ai quotas contract on an authorized disposable fixture or read-only live inventory.
2. Introduce one contrary/negative case that would falsely pass under a weaker implementation.
3. Record exact inputs, revisions, observed outputs and verifier identity.

**Expected:** The contract preserves the stated boundary, rejects or exposes the negative case, and produces machine-readable evidence without claiming broader readiness.

**Evidence required:** Pinned subject/runtime/provider revisions; Complete relevant command/API or fixture output; Timestamped observed result; Verifier/reviewer identity and disposition

## AT-DEP-058 — Reviewer marginal-yield measurement

**Status:** not_run. **Requirement:** FR-DEP-058.

1. Exercise the reviewer marginal-yield measurement contract on an authorized disposable fixture or read-only live inventory.
2. Introduce one contrary/negative case that would falsely pass under a weaker implementation.
3. Record exact inputs, revisions, observed outputs and verifier identity.

**Expected:** The contract preserves the stated boundary, rejects or exposes the negative case, and produces machine-readable evidence without claiming broader readiness.

**Evidence required:** Pinned subject/runtime/provider revisions; Complete relevant command/API or fixture output; Timestamped observed result; Verifier/reviewer identity and disposition


---

# Implementation backlog — v0.3

All items remain `not_started`. This package authorizes planning/evidence work, not deployment or account mutation.

## WP-01 — Recover source and resolve ownership

**Priority:** P0  
**Depends on:** none  
**Requirements:** FR-DEP-001, FR-DEP-007, FR-DEP-024

**Exit evidence:** Source export indexed in this package; remaining work is canonical owner, approved check-run mapping, actual settings and missing artifact-body reconciliation.

## WP-02 — Read-only host and entitlement inventory

**Priority:** P0  
**Depends on:** WP-01  
**Requirements:** FR-DEP-002, FR-DEP-004, FR-DEP-008

**Exit evidence:** Installed runtime/version/capability records and per-repository plan/settings snapshot; no mutation.

## WP-03 — Specify trusted promotion boundary

**Priority:** P0  
**Depends on:** WP-01, WP-02  
**Requirements:** FR-DEP-006, FR-DEP-009, FR-DEP-010, FR-DEP-011, FR-DEP-012, FR-DEP-013

**Exit evidence:** Reviewed gate/state-machine contract with negative fixtures and actual credential boundary.

## WP-04 — Prove one disposable local service

**Priority:** P1  
**Depends on:** WP-02, WP-03  
**Requirements:** FR-DEP-003, FR-DEP-005, FR-DEP-016, FR-DEP-017, FR-DEP-018

**Exit evidence:** Exact-version Podman/WSL service evidence, restart/failure/resource tests and a measured runtime comparison.

## WP-05 — Qualify one private ingress and one SSE path

**Priority:** P1  
**Depends on:** WP-04  
**Requirements:** FR-DEP-014, FR-DEP-015, FR-DEP-019

**Exit evidence:** Positive/negative identity tests, origin bypass check, full-chain streaming and bounded failover traces.

## WP-06 — Prove stateful recovery and adapter boundaries

**Priority:** P1  
**Depends on:** WP-04  
**Requirements:** FR-DEP-020, FR-DEP-021, FR-DEP-022, FR-DEP-023

**Exit evidence:** Restored disposable data, migration decision, single state writer, digest-controlled update flow.

## WP-07 — Integrate approved docs and evidence

**Priority:** P1  
**Depends on:** WP-05, WP-06  
**Requirements:** FR-DEP-024

**Exit evidence:** Atomic or staged cross-repository PR plan, regenerated index links, complete receipts and remaining-limitations statement.

## WP-08 — Repair shared workflow and verification contracts

**Priority:** P0  
**Depends on:** WP-01  
**Requirements:** FR-DEP-027, FR-DEP-029, FR-DEP-034

**Exit evidence:** Supported pinned workflow paths, exact emitted checks, explicit secrets and a disposable invocation receipt.

## WP-09 — Implement local delivery profiles and nightly predicate

**Priority:** P0  
**Depends on:** WP-02, WP-08  
**Requirements:** FR-DEP-025, FR-DEP-026, FR-DEP-033

**Exit evidence:** Local dev placement, schedule truth table, offline catch-up, target serialization and negative ingress proof.

## WP-10 — Qualify provider artifact, service bindings and recovery

**Priority:** P0  
**Depends on:** WP-09  
**Requirements:** FR-DEP-028, FR-DEP-030, FR-DEP-031

**Exit evidence:** Immutable tested image observation, emulator-vs-service action tests, stateful rollback/restore and provider source-mode fixtures.

## WP-11 — Integrate compaction-safe source intake into existing evidence owner

**Priority:** P1  
**Depends on:** WP-01  
**Requirements:** FR-DEP-032

**Exit evidence:** Idempotent provenance import with original hashes/ranges and explicit author/evidence classes; no second global ledger.

## WP-12 — Reconcile current owners and historical local-cloud branches

**Priority:** P0  
**Depends on:** WP-01  
**Requirements:** FR-DEP-035, FR-DEP-036, FR-DEP-044

**Exit evidence:** Current owner/module map plus accepted/rejected contract diff from historical BytePort local-cloud branches; no blind branch resurrection.

## WP-13 — Specify and qualify local node daemon and capability inventory

**Priority:** P0  
**Depends on:** WP-12, WP-02  
**Requirements:** FR-DEP-037, FR-DEP-042

**Exit evidence:** Versioned node identity/capability contract, private enrollment flow and read-only inventory receipts on at least one disposable or non-impacting node.

## WP-14 — Implement resource reservation, modes and preemption fixtures

**Priority:** P0  
**Depends on:** WP-13  
**Requirements:** FR-DEP-038, FR-DEP-039, FR-DEP-043

**Exit evidence:** Admission/preemption truth tables covering interactive, creator/audio, gaming, LLM, idle and stateful negative cases with no foreground starvation claim beyond measured fixtures.

## WP-15 — Bind CI artifacts to local lifecycle management

**Priority:** P0  
**Depends on:** WP-08, WP-13  
**Requirements:** FR-DEP-040, FR-DEP-041

**Exit evidence:** Immutable artifact build receipt, node pull/observation, health transition and daemon/workload rollback on a disposable service.

## WP-16 — Unify GUI API CLI SDK and agent automation contract

**Priority:** P1  
**Depends on:** WP-12  
**Requirements:** FR-DEP-045, FR-DEP-046

**Exit evidence:** Same plan/apply/observe operation demonstrated through API and at least two clients without hidden surface-specific state.

## WP-17 — Converge audit and scorecard systems into Assessment Dossiers

**Priority:** P1  
**Depends on:** WP-01  
**Requirements:** FR-DEP-047, FR-DEP-048

**Exit evidence:** One real repository dossier where Phase A inventory leaves scores unknown and Phase B executes qualified measurements; legacy scorecard mapped as a profile rather than copied truth.

## WP-18 — Recover and integrate Emergent Garden Wave 5 authority

**Priority:** P0  
**Depends on:** WP-01  
**Requirements:** FR-DEP-049, FR-DEP-050

**Exit evidence:** Exact PR-81 payload preserved, reconciled against current main, package/tests rerun, landed or explicitly superseded, and projection status corrected.

## WP-19 — Inventory reviewer providers and enforce zero-spend broker policy

**Priority:** P0  
**Depends on:** WP-01  
**Requirements:** FR-DEP-051, FR-DEP-052, FR-DEP-053, FR-DEP-056, FR-DEP-057

**Exit evidence:** Live provider capability/quota snapshot, cash-spend=false enforcement, risk-tier dispatch fixtures, and deterministic gates proven independent of semantic-review outages.

## WP-20 — Reconcile historical review backlog

**Priority:** P0  
**Depends on:** WP-19  
**Requirements:** FR-DEP-054, FR-DEP-055

**Exit evidence:** Sample merged/open PR backlog classified finding-by-finding; surviving defects linked to remediation PRs and stale/fixed/duplicate findings have evidence-backed dispositions.

## WP-21 — Measure reviewer marginal yield and tune provider routing

**Priority:** P1  
**Depends on:** WP-19, WP-20  
**Requirements:** FR-DEP-058

**Exit evidence:** Per-provider unique-valid-finding, duplicate, false-positive, remediation, latency and quota-efficiency report sufficient to justify or reject a sixth default semantic reviewer.


---

# Agent handoff — v0.3

Start with `STATUS.md`, `docs/25-cross-system-control-plane.md`, then the domain chapter for your assignment. Do not create another registry/controller/ledger until current ownership is reconciled.

## Hard boundaries

- No production or personal-host mutation is authorized by this package.
- No paid review overage, new subscription or auto-refill is authorized.
- Preserve BytePort as the GUI/control experience and extend existing provider seams.
- Preserve ResearchLedger as source/claim authority; salvage PR-81 before starting another Emergent Garden wave.
- Preserve one Assessment Dossier authority; inventory and evaluation are phases, not two truths.
- Review findings require independent adjudication; bot comments are evidence inputs, not merge truth.

## First executable slices

1. Read-only current-owner/runtime/reviewer inventory.
2. One disposable local service with immutable pull deployment and foreground resource reserve.
3. One real Assessment Dossier through inventory then qualified evaluation.
4. Reconcile ResearchLedger PR-81 against current main and rerun its bundle/tests.
5. Reconcile a bounded set of historical review findings on merged PRs and record remediation/dispositions.

Return exact revisions, inputs, outputs, receipts, failed alternatives and remaining unknowns. A polished summary without evidence does not close a work package.


---

# Full-session intake and remaining evidence

## Intake is complete for the supplied export

The full stored export has been received and structurally indexed. Do not ask the user to upload the same transcript again. The raw file is external to this distributable package; its exact filename, file ID, byte count, SHA256 and export timestamp are in [the intake manifest](evidence/session/intake-manifest.json). The [conversation index](evidence/session/conversation-index.json) contains 81 conversation records with parent links and source-message ranges. [S032]

This intake cannot recover messages removed before export. All records carry a compression flag. The document’s readable and lossless sections are two representations of stored content, not independent corroborating witnesses. User-role compaction frames must not be confused with newly issued user commands.

## Evidence retained

The [evidence index](evidence/session/evidence-index.json) lists 16 selected excerpts. E001–E005 preserve direct user scope; E006 preserves a compaction-embedded access requirement; E007–E011 preserve pilot configuration and working-tree observations; E012–E014 preserve prior conclusions to audit; E015 records the last retained failed GitHub follow-up fetch; and E016 preserves a compacted readiness claim.

Three exact report write payloads were recovered and retained with an unverified-history header: GitOps updates, portability substrates and rollback. They are not merged into the normative design. Other named reports have partial reads, patches, summaries, script-embedded content or no directly recoverable body. See [report recovery](evidence/session/report-recovery.json) for exact dispositions.

The scanner’s `no_direct_body_recovered` classification is deliberately narrow. It means no direct exact-path read/write body was selected by that scanner—not that a file never existed, was fabricated, or cannot be recovered from the original workstation. In particular, script-embedded report strings and compaction summaries need separate provenance-aware extraction before they are promoted to complete reports.

## Remaining closure inputs are narrower now

| Evidence | Why it still matters | Preferred recovery route |
|---|---|---|
| Original approved trio run/check identities | Job names are recovered but do not establish trusted producers, exact run identity or risk policy | Existing review records and actual current check-run API responses |
| Current workflow and caller refs | Historical pilot is untracked/modified in its displayed worktree; an exact current path returned 404 | Resolve the current canonical module and immutable commit; inspect callers |
| Applied GitHub settings and plan | Files and feature documents are not observed enforcement | Authorized read of current repository settings and actual activated entitlement |
| Final GitHub/Podman follow-up report bodies | Retained children do not provide finished, reliable audit packets | Read the exact original report files or record genuine absence; do not recreate them under the same identity |
| Runtime and network versions | WSLC, Podman and WSL2 are not interchangeable | Read-only installed-version/capability inventory |
| Deploy, data and recovery receipts | No successful target-environment proof is established here | Authorized disposable-target tests with observed identity and restore verification |

## Intake protocol for later evidence

Record source identity, acquisition time, original and derivative hashes, source revision, producer/run ID, exact range and redaction status. Append claim dispositions: confirmed, corrected, superseded, conflicting, still unverified or out of scope. Idempotently import by original identity/hash and message location into the **existing** evidence/session/research owner; this package is not a new registry.

A write argument, successful write result, readback, committed file, resolved shared workflow, started job, completed deployment, observed healthy candidate and accepted recovery are separate milestones. Never collapse them into “done.”

## Publication

Keep raw export bytes and any credential values in the original private context. Only sanitized derivatives belong in broadly shared docs. Redaction changes bytes and therefore requires a derivative hash. The limited detectors and selected-excerpt review used here are not a general DLP certification; review source metadata and workstation paths before public release.


---

# Reproducible excerpt observations

These are counts of matching lines in the supplied file, **not** full-session rates or causal diagnoses. See `tools/analyze_logs.py` for the exact method and `evidence/log-metrics.json` for original line indexes and the 316-item trace inventory.

| Observation | Count |
|---|---:|
| context_limit_512000 | 718 |
| context_resolution | 717 |
| terminal_traces | 316 |
| unique_combo_ids | 316 |
| terminal_error_class_null | 316 |
| empty_completion_warnings | 1 |
| upstream_error_before_content_warnings | 5 |
| zero_model_sync_reports | 18 |
| cpa_route_lines | 125 |
| explicit_fallback_events | 1 |

## Terminal decision-count distribution

| Recorded decisions field | Trace count |
|---:|---:|
| 61 | 1 |
| 62 | 1 |
| 63 | 6 |
| 64 | 30 |
| 70 | 1 |
| 71 | 3 |
| 72 | 19 |
| 94 | 1 |
| 95 | 53 |
| 97 | 2 |
| 98 | 7 |
| 99 | 192 |

## Explicit fallback observation

Original line 1777 reports `83173ms, 32 fallbacks` for one successful routing event. This is a source-recorded duration, not an independently measured user-end-to-end latency. The six warning lines are 501, 520, 593, 831, 1053 and 1191. The opening main log segment covers about 34.5 minutes, while the later selected active-log view includes earlier times. Do not merge them into a complete ordered request stream.

All parsed terminal-trace status records here are HTTP 200 with a null terminal error class. That does not prove useful output, absence of earlier failed attempts, or correct end-to-end behavior. The semantics of `decisions` remain unresolved. No inference of 99 retries, six failed user requests, or a request failure percentage is made.

Source: S001, whose exact SHA256 is preserved in `evidence/source-manifest.json`.


---

# ADR-DEP-001 — Preserve the Podman / WSLC preference

**Status:** accepted_user_constraint

## Decision

Preserve the preference exactly; qualify distinct implementations. Docker Engine remains an exception candidate, not the default.

## Alternatives tested conceptually

- Treat WSLC as shorthand for WSL2: rejected because identity differs.
- Default to Docker for ecosystem convenience: not authorized by the direct constraint.

## Revisit / closure

An operator-approved exact-workload capability or benchmark exception.

Sources: S001, S013.

This record does not authorize mutation. ADR-DEP-001 and ADR-DEP-014 record stated user constraints.


---

# ADR-DEP-002 — One deployment actuator and existing ownership spine

**Status:** proposed

## Decision

Reuse the existing logical owners; reconcile current module locations before allocating implementation. Do not create a new controller or registry.

## Alternatives tested conceptually

- Independent BytePort and PaaS reconcilers: reject for duplicate writes.
- Assume consolidation is complete because a README says so: reject without receipts.

## Revisit / closure

Current ownership ADR, consumer graph and migration receipt review.

Sources: S002, S003, S004, S005, S006, S007.

This record does not authorize mutation. ADR-DEP-001 and ADR-DEP-014 record stated user constraints.


---

# ADR-DEP-003 — Plan-independent candidate-bound approval

**Status:** proposed

## Decision

Use native protection where supported; otherwise retain a genuinely separate trusted human-apply path. A dispatch button is not an authorization boundary.

## Alternatives tested conceptually

- Private-Free branch protection fallback: unsupported assumption.
- All listed environment reviewers must approve: incorrect quorum assumption.

## Revisit / closure

Exact trio, active entitlements, authorized identities and credential separation verified.

Sources: S007, S008, S009, S010, S012.

This record does not authorize mutation. ADR-DEP-001 and ADR-DEP-014 record stated user constraints.


---

# ADR-DEP-004 — Runtime lane and PaaS qualification

**Status:** proposed

## Decision

Propose rootless Podman plus native WSL systemd/Quadlet for the first persistent-service slice; evaluate WSLC separately. PaaS candidates are conditional adapters, not prerequisites.

## Alternatives tested conceptually

- Make Coolify a required Podman layer now: no qualified path shown.
- Use a Podman-aware UI as a second writer: violates the single-actuator boundary.

## Revisit / closure

Installed-version discovery and lifecycle tests; no engine installation follows from this ADR alone.

Sources: S013, S014, S015, S016, S017, S018, S019, S020, S021.

This record does not authorize mutation. ADR-DEP-001 and ADR-DEP-014 record stated user constraints.


---

# ADR-DEP-005 — Route classes and streaming transport

**Status:** proposed

## Decision

Separate private administration from anonymous public sites and authenticated machine routes. Exclude Quick Tunnels from required SSE paths; qualify the full named-tunnel or private path.

## Alternatives tested conceptually

- Funnel grants visitor identity: false.
- Put browser Access login in front of every webhook: incompatible unless the caller supports it.

## Revisit / closure

Verified hostname ownership, protocol tests, auth policy and origin-bypass tests.

Sources: S022, S023, S024.

This record does not authorize mutation. ADR-DEP-001 and ADR-DEP-014 record stated user constraints.


---

# ADR-DEP-006 — Portability by contract, not provider sameness

**Status:** proposed

## Decision

Define target capability differences and state migration explicitly. Do not switch IaC language/tool or assume WASI/native compatibility without a demonstrated need and approved boundary.

## Alternatives tested conceptually

- One IaC provider model equals universal portability: reject.
- WASM as an automatic fallback for arbitrary native binaries: reject.

## Revisit / closure

Real workload inventories and current IaC/code ownership audit.

Sources: S025, S026, S027, S028, S029, S030, S006.

This record does not authorize mutation. ADR-DEP-001 and ADR-DEP-014 record stated user constraints.


---

# ADR-DEP-007 — Separate routing incident evidence from deployment design

**Status:** proposed

## Decision

Preserve sampled routing observations, add request/attempt instrumentation and bounded failover tests, and avoid attributing failures to ingress or model sync without a joined trace.

## Alternatives tested conceptually

- decisions=99 means 99 retries: unsupported.
- HTTP 200 proves useful model output: unsupported.

## Revisit / closure

Exact config/code revision, trace correlation and reproducible failing fixture.

Sources: S001.

This record does not authorize mutation. ADR-DEP-001 and ADR-DEP-014 record stated user constraints.


---

# ADR-DEP-008 — Preserve local dev and use typed delivery profiles

**Status:** proposed

## Decision

Default the requested dev backend to the qualified local target. Separate environment names from resource targets and workload types. Implement this in the existing API/automation ownership path, leaving BytePort as the product GUI.

## Alternatives tested conceptually

- Render-for-all: contradicts local placement and makes provider quota a hidden requirement.
- One container deploy for all repos: misclassifies packages, desktop releases and documentation.
- Local and managed profiles through one validated contract: preferred design.

## Revisit / closure

Confirm target/module ownership and application profiles before mutation; source placement is explicit but the implementation is not accepted.

Sources: S032, S033, S040.

This record does not authorize mutation. ADR-DEP-001 and ADR-DEP-014 record stated user constraints.


---

# ADR-DEP-009 — Use a tested event predicate and observed deployment watermark

**Status:** proposed

## Decision

Proposed default: changed identity AND (scheduled tick OR new commits > 1 OR authorized force), after qualification gates. Persist the successful observed identity; use environment lease and generation fencing. Do not treat workflow attempts or API acceptance as last deployed.

## Alternatives tested conceptually

- Every push: simpler but does not preserve >1.
- Cron only: ignores requested threshold responsiveness.
- Event predicate with explicit counting basis: preferred.

## Revisit / closure

The exact commit-count convention and missed-tick coalescing are implementation choices proposed here, not historical user-approved policy.

Sources: S032, S033.

This record does not authorize mutation. ADR-DEP-001 and ADR-DEP-014 record stated user constraints.


---

# ADR-DEP-010 — Quarantine the recovered pilot as evidence, not a deployment template

**Status:** proposed

## Decision

Keep the recovered snapshots read-only for regression tests. Replace defects through reviewed patches in the resolved owner; do not execute this transcript or promote the old ready claim. Require source-mode binding, supported workflow locations, exact check mappings, secret isolation and recovery acceptance before rollout.

## Alternatives tested conceptually

- Commit and run the old pilot: known semantic and safety defects.
- Discard the old pilot: loses useful provenance and regression fixtures.
- Preserve evidence and repair narrowly: preferred.

## Revisit / closure

A clean current revision, settings receipt and disposable end-to-end proof can supersede the historical findings.

Sources: S032, S033, S034, S035, S036, S037, S038, S039.

This record does not authorize mutation. ADR-DEP-001 and ADR-DEP-014 record stated user constraints.


---

# ADR-DEP-011 — Represent local machines as a qualified BytePort provider

**Status:** proposed

## Decision

Extend BytePort with a local-fleet provider whose node daemon exposes capabilities and executes desired state. Do not build another PaaS GUI or global controller.

## Alternatives tested conceptually

- Separate private-cloud product: rejected for duplicate control/state surfaces.
- Treat GitHub self-hosted runners as the local-cloud abstraction: rejected because they do not model databases, services, volumes or lifecycle semantics.
- Full Kubernetes/OpenNebula-style private cloud on every personal node: retain only as a dedicated-host option, not the default laptop/desktop contract.

## Revisit / closure

Current owner/module reconciliation or evidence that BytePort cannot host the required provider semantics.

Sources: S052, S058, S059, S060.

This record does not authorize mutation. ADR-DEP-001 and ADR-DEP-014 record stated user constraints.


---

# ADR-DEP-012 — Use immutable pull delivery for personal compute nodes

**Status:** proposed

## Decision

CI builds/tests/publishes immutable artifacts; the controller authorizes desired state; an outbound/private node daemon pulls exact artifacts and reports observed identity.

## Alternatives tested conceptually

- CI SSH/push directly into personal machines: rejected as a broad credential and lifecycle boundary.
- Mutable latest-tag deployment: rejected because tested bytes are not bound to observed runtime bytes.

## Revisit / closure

A substrate with equivalent authenticated content-addressed pull and stronger attestation.

Sources: S052, S058.

This record does not authorize mutation. ADR-DEP-001 and ADR-DEP-014 record stated user constraints.


---

# ADR-DEP-013 — Protect foreground work with reservation and preemption policy

**Status:** proposed

## Decision

Model foreground reserves and dynamic host modes as placement inputs. Background workloads are admitted only from allocatable capacity and may be drained/preempted according to declared policy.

## Alternatives tested conceptually

- Pause one runner when Parsec appears: rejected as application-specific and incomplete.
- Static CPU/RAM limit only: rejected because GPU, thermal, battery and interactive latency can dominate.

## Revisit / closure

Measured workload interference data may simplify or specialize the policy per node class.

Sources: S052, S056, S057, S077.

This record does not authorize mutation. ADR-DEP-001 and ADR-DEP-014 record stated user constraints.


---

# ADR-DEP-014 — Make human, agent and automation parity a platform tenet

**Status:** accepted_user_constraint

## Decision

All product surfaces share one typed capability/control/evidence model. Humans may get richer presentation, agents structured operations, and automations event/idempotency support, but none receives a second source of truth.

## Alternatives tested conceptually

- GUI-first with private backend state: rejected by the direct requirement.
- Agent-only API with human UI as an afterthought: rejected because humans remain first-class.

## Revisit / closure

Only by explicit user change to the global product tenet.

Sources: S052.

This record does not authorize mutation. ADR-DEP-001 and ADR-DEP-014 record stated user constraints.


---

# ADR-DEP-015 — Use one Assessment Dossier with inventory and evaluation phases

**Status:** proposed

## Decision

Phase A captures inventory/applicability/evidence and leaves verdict/score unknown; Phase B binds qualified instruments and records evaluation. Both phases mutate/append the same dossier authority and generate views.

## Alternatives tested conceptually

- Separate inventory database and scorecard database: rejected for identity and drift risk.
- Single flat score sheet: rejected because unknown/applicability/evidence states collapse into misleading scores.

## Revisit / closure

Only if a concrete consumer requires a distinct projection; the canonical dossier remains singular.

Sources: S053, S054.

This record does not authorize mutation. ADR-DEP-001 and ADR-DEP-014 record stated user constraints.


---

# ADR-DEP-016 — Extend the existing review/GitOps controller with a quota-aware broker

**Status:** proposed

## Decision

Provider adapters expose live quota/trigger/cost/capability state. A risk-tier scheduler assigns the smallest sufficient semantic reviewer set, coalesces reruns, normalizes findings, and reserves capacity for final review.

## Alternatives tested conceptually

- Every provider on every PR: rejected for quota waste, duplicate noise and observed rate-limit failures.
- One fixed reviewer everywhere: rejected for outages, quota exhaustion and blind spots.
- New review product/repository: reject unless current controller ownership cannot absorb the capability.

## Revisit / closure

Measured marginal-yield and reliability data may change default provider weights.

Sources: S052, S065, S067, S068, S069, S070, S071, S072, S074.

This record does not authorize mutation. ADR-DEP-001 and ADR-DEP-014 record stated user constraints.


---

# ADR-DEP-017 — Reconcile historical review findings after merge

**Status:** proposed

## Decision

A merged/closed PR finding is revalidated against current main. Valid surviving defects create a remediation item/new PR; fixed/stale/duplicate/false-positive findings receive evidence-backed dispositions. Old thread state is not treated as code truth.

## Alternatives tested conceptually

- Bulk resolve all old threads: rejected because unresolved can still mean real defect.
- Automatically open a fix PR for every old bot comment: rejected because stale/duplicate/false-positive findings create churn.

## Revisit / closure

After historical backlog reaches a stable SLA and can move to continuous reconciliation.

Sources: S052, S065, S066, S070.

This record does not authorize mutation. ADR-DEP-001 and ADR-DEP-014 record stated user constraints.


---

# ADR-DEP-018 — Salvage Emergent Garden Wave 5 before starting another research wave

**Status:** proposed

## Decision

Preserve PR-81 head/payload, reconcile it with current ResearchLedger main, rerun bundle/tests, then land or explicitly supersede it before new corpus expansion. Keep registry projection qualified during the gap.

## Alternatives tested conceptually

- Restart research from YouTube: rejected because substantial validated work already exists.
- Treat merged registry projection as proof the ResearchLedger source landed: rejected; projection and source authority are separate.

## Revisit / closure

After source-authority integration is demonstrably complete.

Sources: S061, S062, S063, S064.

This record does not authorize mutation. ADR-DEP-001 and ADR-DEP-014 record stated user constraints.


---

# Source and research register

Repository declarations are not implementation proof; external documentation is not local compatibility evidence. Sources retain explicit limits.

## S001 — Attached terminal excerpt

**Class:** user_supplied_artifact  
**Locator:** `evidence/source-excerpt.md`

- Direct user constraint at original lines 2096–2097: GitHub Free/student; Podman / WSLC unless Docker Engine is provably better.
- Prior assistant synthesis at original lines 2080–2090; these are claims, not accepted implementation facts.
- Follow-up agents launched at lines 2112–2113; the excerpt ends without their results.
- Filtered, escaped, interleaved routing-log views and a directory listing.

**Limit:** Partial transcript. Opening record is truncated. Named audit reports are not embedded. Source is not globally time-ordered. Original bytes and line numbering are preserved.

## S002 — BytePort README

**Class:** connected_repository_document  
**Locator:** `https://api.github.com/repos/KooshaPari/BytePort/contents/README.md`

- Declares deployment-platform intent and existing Go/Svelte/GitHub/AWS surfaces.
- Explicitly labels complete manifest-driven delivery and isolated microVM execution as planned.
- References an existing charter, plan, spec, functional requirements, architecture and status docset.

**Limit:** Mutable default-branch document, not pinned to an audited commit. No implementation, security, build, or end-to-end test claim was independently reproduced.

## S003 — PhenoCompose README

**Class:** connected_repository_document  
**Locator:** `https://api.github.com/repos/KooshaPari/PhenoCompose/contents/README.md`

- Describes a Compose-facing container/microVM layer and a unified NVMS lineage.
- Claims bindings migrated to thegent and nanovms while also advertising a unified PhenoCompose interface.
- Contains conflicting MIT/Apache license headings and broad platform/performance claims requiring reconciliation.

**Limit:** Declaration-level evidence only; the actual license, migration receipts, code paths and runtime support were not audited. Mutable default-branch read.

## S004 — phenotype-infra README

**Class:** connected_repository_document  
**Locator:** `https://api.github.com/repos/KooshaPari/phenotype-infra/contents/README.md`

- Calls itself a consolidation target for nanovms, PhenoCompose and BytePort.
- Labels its work state SCAFFOLD and describes a human-apply-only gate.

**Limit:** Self-reported state; no build or apply was run. Mutable default-branch read. Repository ownership may have evolved beyond these declarations.

## S005 — phenotype-registry README

**Class:** connected_repository_document  
**Locator:** `https://api.github.com/repos/KooshaPari/phenotype-registry/contents/README.md`

- Defines the INDEX / ADR-contract / convention / enforcement division across registry, PhenoSpecs, PhenoHandbook and phenotype-org-governance.
- Says handbook absorption is by index link rather than duplicating its content.

**Limit:** Role declarations reviewed, not independently enforced or proven current across every dependent repository.

## S006 — Domain Roles — Canonical Repo Map

**Class:** connected_repository_document  
**Locator:** `https://api.github.com/repos/KooshaPari/phenotype-registry/contents/docs/rationalization/DOMAIN_ROLES.md`

- Assigns shared schemas to phenotype-types, testing to TestingKit, observability to PhenoObservability and secrets/auth to Authvault.
- Distinguishes tehgent code review from thegent agent runtime; core/edge language changes require justification.

**Limit:** Document dated 2026-06-16; current code ownership and later ADRs remain to be reconciled.

## S007 — REVIEW-CONTROL.md — existing review/GitOps agent contract

**Class:** retrieved_prior_user_file  
**Locator:** `ChatGPT Library file_00000000680081fd828cbe0dd0d6902b`

- Requires integration with the existing review controller, not a competing implementation.
- Requires exact-head checks, finding adjudication, real approval, and protection against replay and reviewer-trigger loops.

**Limit:** Retrieved prior contract is related evidence, not proof of the exact CI trio intended in this terminal session. Only its relevant returned text was used; original bytes are not bundled.

## S008 — GitHub manage environments

**Class:** primary_external_document  
**Locator:** `https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments`

- Free supports environments for public repositories; private access requires the applicable paid owner plan.
- On Free, Pro and Team, required environment reviewers and wait timers are public-repository features.
- Listing several permitted reviewers does not require every listed person to approve.

**Limit:** No runtime verification was performed from this source.

## S009 — GitHub Student Developer Pack

**Class:** primary_external_document  
**Locator:** `https://education.github.com/pack`

- Eligible students can receive GitHub Pro. Free/student is not a sufficiently precise entitlement snapshot.

**Limit:** The user’s activation, expiration and repository-owner entitlements were not visible or verified.

## S010 — GitHub protected branches

**Class:** primary_external_document  
**Locator:** `https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches`

- Public branch protection is available on Free; private branch protection requires Pro, Team or Enterprise as applicable.

**Limit:** No runtime verification was performed from this source.

## S011 — GitHub Actions limits

**Class:** primary_external_document  
**Locator:** `https://docs.github.com/en/actions/reference/limits`

- Documents plan-specific included hosted minutes, storage and concurrency limits; these are not a workload benchmark.

**Limit:** Limits are changeable. This review did not retrieve account usage or remaining allowances.

## S012 — GitHub Actions secure use

**Class:** primary_external_document  
**Locator:** `https://docs.github.com/en/actions/reference/security/secure-use`

- Self-hosted runners can retain compromise from untrusted workflow code; runner disposal alone does not sanitize reused host hardware.

**Limit:** No runtime verification was performed from this source.

## S013 — Microsoft WSL containers / WSLC

**Class:** primary_external_document  
**Locator:** `https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-containers`

- Documents wslc.exe as a distinct container implementation shipped with WSL.
- The reviewed prerequisites specify WSL 2.9.3 or later prerelease, making installed-version qualification necessary.

**Limit:** Not evidence that the user has this version or that its API satisfies Podman, Docker, Compose, Swarm or Quadlet consumers.

## S014 — Microsoft systemd in WSL

**Class:** primary_external_document  
**Locator:** `https://learn.microsoft.com/en-us/windows/wsl/systemd`

- Modern WSL supports systemd natively.
- Systemd services do not by themselves keep a WSL instance alive.

**Limit:** No runtime verification was performed from this source.

## S015 — Podman Quadlet manual

**Class:** primary_external_document  
**Locator:** `https://docs.podman.io/en/latest/markdown/podman-systemd.unit.5.html`

- Quadlet is a systemd generator, requires cgroup v2, and has rootless unit search paths.
- Generated units are configured through source Install sections rather than enabling generated services as persistent units.

**Limit:** Latest documentation must be checked against the installed Podman version before applying any unit.

## S016 — Podman system service manual

**Class:** primary_external_document  
**Locator:** `https://docs.podman.io/en/latest/markdown/podman-system-service.1.html`

- Exposes a Docker-compatible API and a native Libpod API.
- Access to its socket permits arbitrary code execution with the service user’s authority; it is not a per-operation authorization boundary.

**Limit:** No runtime verification was performed from this source.

## S017 — Coolify self-hosted installation

**Class:** primary_external_document  
**Locator:** `https://coolify.io/docs/start-with-self-hosted`

- Reviewed installation path relies on Docker Engine; it does not qualify this rootless Podman/WSL stack.

**Limit:** No claim that every possible Podman integration is impossible; a supported or tested compatible path was not established.

## S018 — Dokploy installation

**Class:** primary_external_document  
**Locator:** `https://docs.dokploy.com/docs/core/installation`

- Reviewed installation uses Docker and Docker Swarm primitives.

**Limit:** Podman Docker API compatibility is not proof of Docker Swarm orchestration semantics.

## S019 — CapRover getting started

**Class:** primary_external_document  
**Locator:** `https://caprover.com/docs/get-started.html`

- Documents a Docker-based deployment path.

**Limit:** Not qualified on the user’s Podman/WSLC configuration; this is not an exhaustive product evaluation.

## S020 — Portainer Podman environments

**Class:** primary_external_document  
**Locator:** `https://docs.portainer.io/admin/environments/add/podman`

- Podman integration uses the Docker-compatible API.
- Reviewed official support is rootful Podman 5.x on CentOS 9; rootless is not officially supported there.

**Limit:** No runtime verification was performed from this source.

## S021 — Cockpit applications

**Class:** primary_external_document  
**Locator:** `https://cockpit-project.org/applications`

- Lists cockpit-podman for container administration.

**Limit:** Administration UI availability is not a managed deployment-platform contract or a verified Windows/WSL installation.

## S022 — Tailscale Funnel

**Class:** primary_external_document  
**Locator:** `https://tailscale.com/docs/features/tailscale-funnel`

- Funnel exposes a service publicly, uses tailnet ts.net names, permits ports 443/8443/10000 and has non-configurable bandwidth limits.
- The same port cannot simultaneously serve as private Serve and public Funnel.

**Limit:** No throughput measurement, app-level authorization proof or service-level suitability verdict is inferred.

## S023 — Cloudflare Quick Tunnels

**Class:** primary_external_document  
**Locator:** `https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/trycloudflare/`

- Quick Tunnels are for development/testing, have an in-flight request limit of 200, and do not support SSE.
- These restrictions are documented for Quick Tunnels, not automatically every Cloudflare Tunnel product.

**Limit:** No runtime verification was performed from this source.

## S024 — Cloudflare Access self-hosted public applications

**Class:** primary_external_document  
**Locator:** `https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/`

- Access is a separately configured application-access layer for a public hostname.

**Limit:** No Access application, identity policy, DNS zone ownership, service token, or origin restriction was verified in the user’s environment.

## S025 — Pulumi Docker provider

**Class:** primary_external_document  
**Locator:** `https://www.pulumi.com/registry/packages/docker/`

- Targets Docker API resources and Docker-compatible hosts, with a configurable host endpoint.

**Limit:** Resource-by-resource Podman conformance and WSLC compatibility were not established. Python preference is not an existing language-policy override.

## S026 — Pulumi Automation API

**Class:** primary_external_document  
**Locator:** `https://www.pulumi.com/docs/iac/concepts/automation-api/`

- Provides programmatic access to Pulumi lifecycle operations.

**Limit:** An orchestration SDK does not automatically supply cross-provider behavior, equivalent persistence or state migration.

## S027 — Pulumi state and backends

**Class:** primary_external_document  
**Locator:** `https://www.pulumi.com/docs/iac/concepts/state-and-backends/`

- State backend selection is an explicit operational concern.

**Limit:** No backend, state file, locks, secret provider or recovery procedure was inspected locally.

## S028 — Render free services

**Class:** primary_external_document  
**Locator:** `https://render.com/docs/free`

- Free web services can idle after 15 minutes and do not provide a persistent disk; free Postgres expires after 30 days.
- The page says free instances should not be used for production.

**Limit:** No runtime verification was performed from this source.

## S029 — Spin introduction

**Class:** primary_external_document  
**Locator:** `https://spinframework.dev/`

- Spin builds and runs event-driven applications using WebAssembly components.

**Limit:** No arbitrary native-process compatibility or migration-without-porting is established.

## S030 — Firecracker official overview

**Class:** primary_external_document  
**Locator:** `https://firecracker-microvm.github.io/`

- Firecracker uses Linux KVM.

**Limit:** No proof of KVM availability, nested virtualization, Windows/WSL performance or native macOS Firecracker support is provided.

## S031 — BytePort repository metadata

**Class:** connected_repository_metadata  
**Locator:** `https://github.com/KooshaPari/BytePort`

- Connected repository search returned repository ID 861430079, public visibility and default branch main.

**Limit:** Visibility and settings can change. This does not verify the plan, rules, permissions or visibility of every other repository.

## S032 — Full stored Forge session export and indexed descendants

**Class:** user_supplied_artifact  
**Locator:** `evidence/session/intake-manifest.json`

- 81 decoded conversations, 4588 stored messages; original source hash and coverage in intake manifest.
- E001–E006 recover user scope; E007–E016 separate tool observations from assertions.
- The export explicitly cannot reconstruct pre-compaction history. All 81 actual section headers name .forge.writes.db.

**Limit:** Entire export structurally indexed. Targeted semantic review, not every line or every repository. Compaction frames are not new human approvals. Raw export deliberately not redistributed.

## S033 — Historical pilot caller, branch JSON, nightly workflow and Blueprint

**Class:** stored_tool_output  
**Locator:** `evidence/session/evidence-index.json`

- E007: caller references a nested reusable path, passes only API key and /health.
- E008: protection JSON names ci/lint and ci/test without spaces.
- E009: full 205-line nightly workflow includes no rollback operation, no >1 count, and a successful exit for unknown health URL.
- E010: Blueprint selects prebuilt latest image and /healthz; static auth value redacted.
- E011: stored git status shows modified/untracked pilot files.

**Limit:** September 11 stored local observations, not proof these bytes exist at current remote HEAD or were deployed. The production workflow body was not recovered by this targeted review.

## S034 — Current connected Tracera CI aggregation code

**Class:** connected_repository_file  
**Locator:** `https://github.com/KooshaPari/Tracera/blob/main/.github/workflows/ci.yml`

- Connected fetch of lines 310–410 returned job names ci / lint, ci / test, CI.
- Returned blob SHA: 3685d56735d54e0d7dce5be62ea8a25fd0f822a9. This is a file blob hash, not a commit SHA.
- Final ci job lists detect-changes, dependency-review and trunk-check in needs but omits their results from its shell result array.

**Limit:** Narrow current file read, not a workflow run or settings read. Exact emitted check-run identity, producer and enforced branch/ruleset mapping remain unverified.

## S035 — Connected lookup of the historical reusable nightly path

**Class:** connected_lookup_result  
**Locator:** `https://github.com/KooshaPari/phenotype-tooling/blob/main/.github/workflows/reusable/nightly-dev-deploy.yml`

- The exact connected fetch returned 404 Not Found during this review.

**Limit:** Does not prove repository deletion, lack of access to all refs, or that the path never existed. Historical local evidence is retained rather than overwritten by this result.

## S036 — GitHub reusable workflows: location, calls and secret passing

**Class:** primary_external_document  
**Locator:** `https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows`

- Reusable workflows must be directly in .github/workflows, not nested subdirectories.
- Named secrets are passed explicitly, or inherited through the documented mechanism.
- A job environment in the called workflow can supply its own environment secrets; this is distinct from automatic forwarding of repository secrets.

**Limit:** Platform semantics, not validation of local workflow syntax or actual account settings.

## S037 — Render prebuilt image deployments

**Class:** primary_external_document  
**Locator:** `https://render.com/docs/deploying-an-image`

- Image-backed services differ from Git-backed services.
- Deploys can select an image tag or digest; a rollback requires that image/digest to remain available.

**Limit:** Does not establish which image is currently running in the user account.

## S038 — Render trigger deploy API

**Class:** primary_external_document  
**Locator:** `https://api-docs.render.com/reference/create-deploy`

- commitId selects a Git commit for a Git-backed service; imageUrl selects an image-backed service image.
- A source commit parameter is not proof that a prebuilt mutable latest image matches the tested artifact.

**Limit:** Adapters require recorded request/response fixtures against the selected service type; no provider operation executed.

## S039 — Render rollback API and behavior

**Class:** primary_external_document  
**Locator:** `https://api-docs.render.com/reference/rollback-deploy`

- POST /v1/services/{serviceId}/rollback uses a prior deployId.
- Calling the rollback endpoint does not disable autodeploys.

**Limit:** An API operation does not restore database state or prove a successful rollback.

## S040 — Render free service budget, refreshed

**Class:** primary_external_document  
**Locator:** `https://render.com/docs/free`

- Free web service running hours share a 750-hour monthly workspace allowance.
- The allowance is not the same assertion as only one free web service existing.
- Free web services have ephemeral filesystems and cannot attach persistent disks.

**Limit:** Actual workspace consumption and entitlement not read. Local-dev placement is preserved regardless of the corrected quota explanation.

## S041 — Podman network backend and rootless networking

**Class:** primary_external_document  
**Locator:** `https://docs.podman.io/en/latest/markdown/podman-network.1.html`

- Podman documents Netavark network management and Aardvark DNS.
- Pasta is documented as the default rootless networking tool.

**Limit:** Version-sensitive documentation; not a benchmark, a WSL compatibility test or proof of the local runtime backend.

## S042 — Microsoft WSLC prerequisite, refreshed

**Class:** primary_external_document  
**Locator:** `https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-containers`

- The reviewed page describes wslc.exe and requires WSL 2.9.3 or higher, identified there as pre-release.

**Limit:** Do not update the operator workstation to pre-release or infer installed versions from this documentation.

## S043 — LocalStack March 2026 release and authenticated image transition

**Class:** primary_external_document  
**Locator:** `https://blog.localstack.cloud/localstack-for-aws-release-2026-03-0/`

- March 23, 2026 release consolidated images and requires an auth token.
- The product is not defunct; the old community distribution/access assumptions changed.

**Limit:** Not an endorsement of licensing, cost or fit. Current commercial eligibility and usage terms require separate review; no purchase or auth action performed.

## S044 — Moto server mode

**Class:** primary_external_document  
**Locator:** `https://docs.getmoto.org/en/latest/docs/server_mode.html`

- Moto can provide an HTTP server interface for non-Python SDK testing.

**Limit:** An emulator/testing tool is not a durable production AWS replacement; action coverage must be tested.

## S045 — Moto implemented services

**Class:** primary_external_document  
**Locator:** `https://docs.getmoto.org/en/latest/docs/services/index.html`

- Moto maintains a service-specific implementation catalog.

**Limit:** A listed service is not proof of every API action or error semantic used by an application.

## S046 — Supabase self-hosting

**Class:** primary_external_document  
**Locator:** `https://supabase.com/docs/guides/self-hosting`

- Supabase documents a self-hosting path.

**Limit:** Self-hosting transfers operational duties; a local PostgreSQL process alone does not provide the complete Supabase product API.

## S047 — Valkey compatibility and migration

**Class:** primary_external_document  
**Locator:** `https://valkey.io/topics/migration/`

- Valkey documents compatibility with Redis OSS 7.2 and earlier versions.

**Limit:** Does not claim all newer Redis modules or Upstash HTTP APIs are interchangeable with a Valkey TCP endpoint.

## S048 — GitHub environment plan/visibility matrix, refreshed

**Class:** primary_external_document  
**Locator:** `https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/review-deployments`

- Public repositories support environments across current plans.
- Private environment/secrets/branch eligibility requires Pro, Team or Enterprise; reviewer/wait gates on Free/Pro/Team are public-only.

**Limit:** Plan label is not proof of applied settings. User student benefit and repository owner entitlements remain unknown.

## S049 — Tailscale custom-domain design using private DNS

**Class:** primary_external_document  
**Locator:** `https://tailscale.com/kb/1620/kubernetes-operator-byod-gateway-api`

- Documents custom domain TLS with private DNS and tailnet routing.

**Limit:** This specific guide is Kubernetes-oriented; v0.2 uses the DNS/TLS separation as a design pattern, not a reason to install Kubernetes.

## S050 — GitHub ruleset availability and configuration

**Class:** primary_external_document  
**Locator:** `https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets`

- Rulesets must be configured/applied; plan and visibility affect availability.

**Limit:** A repository JSON file is not a verified remote ruleset. No administration API or settings change performed.

## S051 — Render deploy listing and pagination

**Class:** primary_external_document  
**Locator:** `https://api-docs.render.com/reference/list-deploys`

- Deploy listing is paginated; default page size 20 and cursor pagination are documented.

**Limit:** The parsed page did not expose a full response schema. The historical flat response parser is unqualified, not declared definitively wrong without a captured fixture.

## S052 — User consolidation note — local cloud, assessment, corpus and review control

**Class:** user_supplied_artifact  
**Locator:** `chat://2026-09-12T15:27:00-07:00`

- Local personal devices should be usable as compute nodes while preserving their foreground uses.
- BytePort remains the application/GUI layer and lifecycle management is a core requirement.
- Humans, agents and automations are first-class product users.
- Assessment/scorecard work, Emergent Garden research and quota-aware review control must be consolidated.
- No new review spend is desired and review quotas must be used frugally.

**Limit:** Direct requirements and intent; not evidence that any implementation already exists.

## S053 — Master Assessment Kit — contract 1.1

**Class:** retrieved_prior_user_file  
**Locator:** `library://MASTER-ASSESSMENT-KIT.md`

- The reusable persisted assessment object is an Assessment Dossier with generated human front doors.
- Canonical dossier components separate subject, assignment, measurements, results, evidence, findings and decisions.
- Applicability, execution, verdict, freshness and review disposition remain independent.

**Limit:** Defines the assessment contract; it does not prove any repository has been assessed under it.

## S054 — Master Assessment Kit agent entrypoint

**Class:** retrieved_prior_user_file  
**Locator:** `library://START-HERE(1).md`

- The workflow requires real subject/owner/mandate resolution, instrument binding, canonical results and evidence, and generated machine/human views.
- A completed dossier, not a new template, is the required operational return.

**Limit:** Workflow guidance only; actual dossier execution remains repository-specific.

## S055 — phenotype-infra ADR 0001 — hybrid compute mesh

**Class:** connected_repository_document  
**Locator:** `github://KooshaPari/phenotype-infra/docs/adr/0001-hybrid-compute-mesh.md`

- An accepted older architecture already treats home hardware as part of a heterogeneous compute mesh.
- The design rejects heavy orchestration for the small solo-operator topology and uses private overlay networking.

**Limit:** Older CI-oriented architecture; does not by itself satisfy the broader local cloud-node requirement.

## S056 — phenotype-infra ADR 0003 — home desktop heavy runner

**Class:** connected_repository_document  
**Locator:** `github://KooshaPari/phenotype-infra/docs/adr/0003-home-desktop-as-heavy-runner.md`

- Prior accepted design used a home machine for self-hosted heavy work with private connectivity and foreground-use protection.

**Limit:** Single-runner precedent; too narrow for databases, containers, VMs and lifecycle-managed local cloud workloads.

## S057 — phenotype-infra ADR 0008 — Parsec pause proposal

**Class:** connected_repository_document  
**Locator:** `github://KooshaPari/phenotype-infra/docs/adr/0008-parsec-gaming-mode-pause.md`

- A prior proposal attempted to pause background compute during interactive use.

**Limit:** Proposed stub and process-specific mechanism; insufficient as a general resource-reservation or QoS policy.

## S058 — BytePort CloudProvider design

**Class:** connected_repository_document  
**Locator:** `github://KooshaPari/phenotype-infra/tools/byteport/backend/lib/cloud/DESIGN.md`

- BytePort already defines a capability-based cloud-provider abstraction spanning compute, database, storage and networking concepts.
- The design includes deployment lifecycle concepts such as build, provision, deploy, health, update and rollback.

**Limit:** Repository design declaration; local-node provider behavior and operational receipts still require implementation evidence.

## S059 — BytePort PR 10 — historical Oct-2025 rearchitecture capture

**Class:** connected_repository_metadata  
**Locator:** `github://KooshaPari/BytePort/pull/10`

- The historical branch explicitly described Local nvms+vLLM, freemium managed providers and hyperscaler production tiers.
- The historical work included multi-cloud and local-hypervisor scaffolding.

**Limit:** PR is closed and unmerged; precedent only, not current default-branch authority.

## S060 — BytePort PR 329 — historical compute-mesh desired-state capture

**Class:** connected_repository_metadata  
**Locator:** `github://KooshaPari/BytePort/pull/329`

- A later historical branch described owner-scoped compute-mesh workload intents, artifact metadata and placement/deployment handoff.

**Limit:** PR is closed and unmerged; review-bot description is not proof of current implementation.

## S061 — ResearchLedger PR 81 — Emergent Garden Wave 5

**Class:** connected_repository_metadata  
**Locator:** `github://KooshaPari/ResearchLedger/pull/81`

- Wave 5 contains substantive corpus work, execution receipts, 70 rerun offline tests and 32 synthetic admission cases.
- PR 81 is closed, draft and not merged.
- Full transcripts, recursive source closure, audience review, lineage reconstruction, one comment discrepancy and live coordination experiment remain incomplete.

**Limit:** PR body is a project-authored execution summary. Current main integration must be verified separately.

## S062 — Emergent Garden Wave 5 research index at PR-81 head

**Class:** connected_repository_file  
**Locator:** `github://KooshaPari/ResearchLedger@8822aa14baef2a964288076645edcc493c338688/docs/corpora/emergent-garden/research/README.md`

- The campaign records 74 public uploads, 62 non-empty descriptions, 528 edges, 300 normalized targets and 93 domains.
- The branch states campaign completion remains partial and ResearchLedger remains canonical.

**Limit:** File exists at the historical PR head; it is not evidence that current main contains it.

## S063 — ResearchLedger current main branch snapshot

**Class:** connected_repository_metadata  
**Locator:** `github://KooshaPari/ResearchLedger/branches/main@8f636cde8c7678515312bf806d744ff747d13e76`

- Current main is ahead of the PR-81 base and the Emergent Garden research README path was not found at current main during this review.

**Limit:** A path lookup is not an exhaustive semantic search for relocated content; salvage must first reconcile exact commits and tree paths.

## S064 — phenotype-registry PR 550 — ResearchLedger routing projection

**Class:** connected_repository_metadata  
**Locator:** `github://KooshaPari/phenotype-registry/pull/550`

- The cross-project routing projection was merged on 2026-09-12 and points to the pinned ResearchLedger evidence head.

**Limit:** A merged projection does not merge the source corpus into ResearchLedger main.

## S065 — Existing review-control contract

**Class:** retrieved_prior_user_file  
**Locator:** `library://REVIEW-CONTROL.md`

- Review control is meant to integrate with the existing review/GitOps controller rather than create a competing system.
- A prior ForgeCode PR had unresolved current threads across multiple semantic reviewers.
- The desired pipeline already separates deterministic checks, selected semantic review, adjudication, repair, exact-head rerun and evidence.

**Limit:** Design/control record; provider quotas and PR state change over time and require live refresh.

## S066 — ForgeCode PR 277 current merge state

**Class:** connected_repository_metadata  
**Locator:** `github://KooshaPari/forgecode/pull/277`

- PR 277 is now merged to main, making any remaining historical findings a post-merge reconciliation problem rather than an open-branch repair problem.

**Limit:** Merge state alone does not say which old findings remain valid on current main.

## S067 — ForgeCode PR 277 current reviewer activity snapshot

**Class:** connected_lookup_result  
**Locator:** `github://KooshaPari/forgecode/pull/277/comments@2026-09-12`

- CodeAnt performed multiple incremental reviews on successive commits.
- Copilot reported quota exhaustion.
- CodeRabbit reported its included OSS review limit reached with a reset delay.
- Automated scanners can independently hit their own limits.

**Limit:** Point-in-time PR activity; quota availability and exact remaining balances are dynamic.

## S068 — CodeRabbit plan and rate-limit documentation

**Class:** primary_external_document  
**Locator:** `https://docs.coderabbit.ai/management/plans`

- Current Free PR review limit is documented as 3 per developer per hour; OSS can vary from 1–8 per hour.
- The provider exposes quota status and reset information.

**Limit:** Account/repository effective quotas can differ by plan, OSS classification and fair-use state; the broker must observe live state.

## S069 — CodeRabbit automatic review controls

**Class:** primary_external_document  
**Locator:** `https://docs.coderabbit.ai/configuration/auto-review`

- Automatic reviews can be disabled and selectively re-enabled by labels, description keyword or manual review command.
- Incremental auto-review and auto-pause controls are configurable.

**Limit:** Only governs CodeRabbit; configuration still has to be applied and verified per repository.

## S070 — CodeAnt SCM/PR CLI integration

**Class:** primary_external_document  
**Locator:** `https://docs.codeant.ai/cli/scm-integration`

- CodeAnt CLI can list/filter PR comments including unresolved CodeAnt comments and can resolve threads by SCM identifiers.

**Limit:** CLI capability does not authorize automatic fixing or thread resolution without independent adjudication.

## S071 — Macroscope usage pricing and controls

**Class:** primary_external_document  
**Locator:** `https://docs.macroscope.com/pricing`

- Code Review is $0.05 per KB with a 10KB minimum and Agent has 1,000 free credits monthly.
- New workspaces are advertised with $100 free usage and spend controls exist.

**Limit:** Finite credit is not zero-cost forever. Auto-refill must remain disabled under the user no-new-spend constraint.

## S072 — Kilo free model and code review documentation

**Class:** primary_external_document  
**Locator:** `https://kilo.ai/docs/getting-started/using-kilo-for-free`

- Kilo Code Reviewer can be configured to use hosted models marked free.
- Free model availability can change and upstream providers may rate-limit them.

**Limit:** Free model availability and quality are dynamic; "free" is not a reliability SLA.

## S073 — Kilo GitHub code review behavior

**Class:** primary_external_document  
**Locator:** `https://kilo.ai/docs/automate/code-reviews/github`

- Kilo GitHub reviews run automatically on PR open/update/ready when enabled.

**Limit:** Automatic triggers can consume scarce model capacity unless repository/provider settings are deliberately controlled.

## S074 — OpenAI Codex code review and plan access

**Class:** primary_external_document  
**Locator:** `https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan`

- Codex is included with ChatGPT plans and can automate GitHub code review.
- Usage limits vary by plan.

**Limit:** The user treats Codex review as shared subscription usage, so it is a scarce shared allowance rather than a free unlimited reviewer.

## S075 — OpenAI Codex GitHub review behavior

**Class:** primary_external_document  
**Locator:** `https://openai.com/index/introducing-upgrades-to-codex/`

- Codex can automatically review PRs after draft-to-ready and can be invoked with @codex review plus focused instructions.

**Limit:** Repository trigger configuration and remaining quota must be verified live; automatic behavior is not evidence of broker control.

## S076 — Incus REST API and resource model

**Class:** primary_external_document  
**Locator:** `https://linuxcontainers.org/incus/docs/main/rest-api-spec/`

- Incus exposes resource discovery, VM/container lifecycle, backups and remote API control.

**Limit:** Reference implementation pattern only; v0.3 does not select Incus as the canonical local runtime.

## S077 — Incus instance resource limits

**Class:** primary_external_document  
**Locator:** `https://linuxcontainers.org/incus/docs/main/reference/instance_options/`

- Incus demonstrates enforceable CPU, memory and IO resource-limit semantics useful as a reference for the local-node contract.

**Limit:** Some controls are runtime/type-specific and do not solve foreground workload detection or GPU policy by themselves.

## S078 — CodeRabbit manual review/resolve commands

**Class:** primary_external_document  
**Locator:** `https://docs.coderabbit.ai/reference/review-commands`

- CodeRabbit supports manual incremental/full review, pause/resume and resolve commands.

**Limit:** Bulk resolve commands must not be used as a substitute for finding-by-finding evidence reconciliation.

## S079 — Macroscope spend-control reference

**Class:** primary_external_document  
**Locator:** `https://macroscope.com/usage-based-code-review-for-teams`

- Macroscope supports per-review, per-PR and monthly spend caps and selective review scope.

**Limit:** Spend controls prevent overage only when explicitly configured; this package does not change account settings.


---

# Package validation receipt — v0.3

**Result: passed for the internal checks below. No target-system verification is implied.**

| Check | Result | Receipt |
|---|---|---|
| IDs, source links, bidirectional FR/test references and required evidence | Passed | `docset-validation.json` |
| Backlog coverage/DAG and proposed/not-run status discipline | Passed | `docset-validation.json` |
| Original v0.2 excerpt hash, byte/line count and reproduced log metrics | Passed | `source-manifest.json`, `docset-validation.json` |
| Full stored export structural index | Preserved from v0.2: 81 conversations / 4,588 decoded messages | `intake-reproduction.json` |
| Selected full-session derivative hashes and original-message ranges | Preserved v0.2 checks | `session/evidence-index.json`, validator/tests |
| Internal unit tests | **70 passed** | `unit-test-output-v03.txt` |
| Draft 2020-12 data-schema validation | **6 instances passed**, including new local-node and review-provider examples | `schema-validation.json` |
| Generated report links and anchors | **48 chapters**, 633 local links, zero invalid links/duplicate IDs | `render-validation.json` |
| Browser rendering | 1440×1100 and 390×844; no overflow, page errors, external requests; navigation filter passed | `browser-validation.json` |
| Payload integrity | Rebuilt and verified during final packaging | `FILE_MANIFEST.json`, `SHA256SUMS.txt` |

## v0.3 scope

v0.3 adds design/reconciliation records for local personal-device compute, human/agent/automation API parity, Assessment Dossier convergence, Emergent Garden source-authority recovery, and quota-aware semantic review control. These records are evidence-qualified plans, not claims that the corresponding runtime/provider/account settings have been changed.

## What did not run

No builds/tests of the user's application repositories, personal-host runtime commands, node-daemon installation, foreground interference benchmarks, provider billing/account mutations, paid review calls, GitHub thread resolution, Emergent Garden branch mutation, deployment, backup/restore, ingress or recovery operations were performed. **All 58 target-environment acceptance tests remain `not_run`.**

Exact desktop/laptop reserve profiles, current reviewer-account quota balances, Macroscope remaining credit, local-node daemon authority and the Emergent Garden landing target remain unresolved by design.

These checks establish package consistency only. They do not establish production readiness, merge approval, live provider eligibility or complete recovery of pre-compaction conversation history.
