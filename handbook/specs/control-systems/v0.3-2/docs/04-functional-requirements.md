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
