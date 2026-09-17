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
