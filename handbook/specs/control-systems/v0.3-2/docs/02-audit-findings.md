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
