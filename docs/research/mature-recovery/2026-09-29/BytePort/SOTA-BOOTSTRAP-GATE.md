# BytePort — SOTA, alternatives and bootstrap gate, pass 1

Research date2026-09-29. Product source `0232cca16fedb7963a8c6f556dc5eee5c8c1674e`; registry source `85d7cd00cf59c379c05b740e8130a85b0d5bd31b`. **OPEN: mature scope and architecture are not frozen.** Research covers deployment/productization, not just desktop container competitors. Source URLs are current documentation retrieval identities; version gaps are explicit and prevent adoption approval.

## Primary source / competitor / primitive matrix

| ID / source | Version/date and inspected extent | Supported factual claim | Interpretation, limitation and consequence |
|---|---|---|---|
| BP-R01 https://podman-desktop.io/docs/compose | Current Compose overview retrieved2026-09-29; exact release not pinned | Desktop management of Compose multi-container applications and grouped resources | Broad desktop/local container management is not unique. Does not prove BytePort's source-to-cloud/portfolio journey is fully replaced. |
| BP-R02 https://docs.docker.com/reference/compose-file/ | Current specification overview; not every schema section | Compose models services, networks, volumes and other application configuration; Docker implementation and normative spec are distinguished | Consider standard import/adaptation before maintaining a parallel manifest language. Not a universal AWS/provisioning model or proof of cross-runtime compatibility. |
| BP-R03 https://opentofu.org/docs/intro/ | Current docs, page banner1.12.0; introduction/workflow/state overview | Declarative provider-backed cloud/on-prem resource lifecycle with plan/apply/state | Mature provisioning already exists. Compare as alternative engine; custom resource planner needs justification. Exact provider versions, state details and licenses not reviewed here. |
| BP-R04 https://www.pulumi.com/docs/iac/concepts/state-and-backends/ | Current docs; state refresh/checkpoint/backend failure sections inspected | Recorded state differs from fresh provider state; checkpoints support recovery; hosted and DIY backend failure behavior differ | Learn/integrate state and recovery rather than treating DB+HTTP as one transaction. Vendor backend claims unbenchmarked; review full APIs/version/license/cost before embedding. |
| BP-R05 https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html | Current EC2 API guidance; token/parameter/scope/retry sections | Some mutations support client-token idempotency; parameter mismatch and regional/zonal scope matter; returned request success can precede async workflow completion | A stable operation ID alone does not guarantee cross-region or cross-service exactly-once deployment. Reuse provider semantics and expose uncertainty. |
| BP-R06 https://github.com/opencontainers/image-spec/blob/main/descriptor.md | Main descriptor text retrieved2026-09-29; required digest/size and verification sections; commit not pinned | Descriptors identify content by digest, with size/type and verification rules | Prefer standard content identity to mutable-image-name evidence. Digest equality proves bytes, not desired behavior, safety or ownership. |
| BP-R07 https://v2.tauri.app/security/permissions/ | Tauri2 docs, page last_updated2026-07-20; permissions/scopes/capability linkage and config examples | Explicit command permissions/scopes are granted to windows/webviews through capabilities | Reuse supported permission primitives. They do not automatically secure a separately listening Go HTTP server. Actual config/runtime tests still needed. |
| BP-R08 https://coolify.io/docs/ | Current overview retrieved2026-09-29; self-host/cloud/app deployment and API/CLI/MCP navigation | Documents Docker-packageable app/database/service deployment and machine interfaces | Strong practical alternative, not dismissed because its UI is web-based. Docker/runtime/operating-burden constraints must be counted honestly; overview is not a full API/security/health review. |
| BP-R09 https://docs.astro.build/en/guides/content-collections/ | Current docs; overview/schema/loading and build-time-vs-live sections, not entire guide; installed version not pinned | Structured content collections can load/query/render local or remote data, with different freshness behavior | Portfolio rendering need not be a custom CMS or mandatory LLM pipeline. Source/deployment authority, publication and freshness remain BytePort-specific concerns. |

Current documentation is not a maintained-project certificate. Exact releases/commits, full licenses and transitive compatibility, vulnerability history, maintenance health, extension APIs, platform support, operational costs and integration effort remain unverified. No previous README competitor price is reused.

## Best realistic alternative composition

**Primary recovered-horizon baseline proposal:** selected Git repository and ordinary CI produce an identified application artifact; **Pulumi on the user's AWS target** manages declared resources and recorded state; an ordinary runtime/build path runs the application; an **Astro content template** renders reviewed project metadata and deployment output. This is a proposed composition of inspected primitives, not a completed installation or measured winner. Preserve the cost of integrating artifact identity, secrets, provider state and content freshness rather than declaring integration free.

**Local-stage alternative:** Podman Desktop plus Compose for supported local container applications. **Lower-integration deployment alternative:** Coolify plus a portfolio template, where Docker/server/operational constraints are acceptable. **Alternative engine comparison:** OpenTofu rather than Pulumi; do not demand both simultaneously. BytePort must beat the best suitable composition, not only a weak hand-written script. NanoVMS integration can remain an adapter candidate without assuming it is the optimal universal runtime.

## Differentiation ledger

| Class | Claim | Direct attack / disposition |
|---|---|---|
| Commodity/contested | Desktop local container deployment | BP-R01 already covers substantial behavior; own-ecosystem-only wording is not external differentiation |
| Commodity/contested | Manifest-driven provisioning, state and machine interfaces | BP-R02–05/08 substantially address components |
| Commodity/contested | Generated project pages | BP-R09 provides content rendering primitives; an LLM description alone is not a product moat |
| Falsified as broad novelty | No meaningful desktop/open-source or self-service deployment alternative exists | Podman Desktop and Coolify defeat the broad assertion; this does not establish full journey equivalence |
| Falsified implementation shortcut | Allocating any sandbox demonstrates selected-project deployment | BP-F02's unrelated alpine payload is a counterexample to that acceptance rule |
| Candidate | Coherent low-friction source→owned deployment→truthful operation/recovery→portfolio experience | Could justify a thin integrative product or extension; no comparative user evidence yet |
| Unverified | A desktop-first interface materially reduces setup, operator burden and wrong-target/false-success outcomes over the composed stack | Requires pilot after built-stage acceptance; architecture gate requires prototypes beforehand |
| Unverified | A custom NVMS manifest/runtime or standalone product is better than adapters around established tools | Scope, interoperability and controlled comparison remain open |

## Bootstrap decisions (provisional, not approved architecture)

| Capability | USE/INTEGRATE/FORK/ADAPT/COMPOSE/LEARN/REJECT/CUSTOM evaluation | Next gate |
|---|---|---|
| Provisioning and desired state | INTEGRATE/COMPOSE Pulumi or OpenTofu; LEARN refresh/checkpoints. REJECT duplicating a generic cloud planner without an accepted unmet requirement. FORK only after extension incompatibility is demonstrated. | Resource/state ownership, provider version and partial-failure prototype |
| Manifest/schema | USE standard Compose/OCI where semantics fit; ADAPT recovered .nvms intent where distinct. BUILD custom syntax only for obligations standards cannot represent economically. | Semantic mapping and invalid/unsupported field behavior, version migration |
| Runtime | INTEGRATE existing NanoVMS or other supported runtime behind an explicit adapter; do not rebrand the runtime as the product or assume every target is a microVM | Freeze actual dependency/API; artifact identity, runtime-ID separation and stop/restart tests |
| Desktop/control plane | USE current Tauri/Svelte where it serves accepted journeys; compare Podman extension or external UI integration before replacing or rebuilding | Actual packaged flow, trust boundary, permissions, sidecar recovery and platform matrix |
| Operation durability | LEARN provider idempotency/checkpoint semantics; BUILD minimal product operation/provenance model only where engine state cannot express project-level acceptance | Crash after remote accept/before DB receipt; distinct provider identity, retry scope and reconciliation |
| Portfolio | COMPOSE standard renderer/content schema and reviewed projection; ADAPT current integration if viable; REJECT making generative text a substitute for verified deployment facts | Stale/wrong-project/secret/publish controls; freshness and export behavior |
| Credentials/security | USE established OS/framework/provider mechanisms; no new bespoke crypto justified by this pass | Actual credential flow, config/secret storage, capability and network exposure review |
| Oracle/evidence | BUILD narrowly scoped product-subject adapters; COMPOSE independent grading/artifact storage rather than a new general task platform | Exact candidate/artifact/target/provider evidence, immutable independent policy |

## Academic evidence matrix and limits

The author abstract of Mokhov/Mitchell/Peyton Jones, *Build systems a la carte* (ICFP2018; expanded2020 work linked), at https://simon.peytonjones.org/build-systems-a-la-carte/ was inspected as adjacent knowledge for deployment/build dependency decomposition. Task: executable framework for comparing/recombining build systems. Dataset/sample, full baselines, quantitative metrics and evaluation design were **not extracted from the abstract**. It establishes a research direction, not correctness/performance of BytePort's deployment lifecycle. No full-text deployment transaction/saga or current2026 empirical paper review is complete; these are blocking research obligations, not empty green rows.

## Risk experiments and remaining gate

Before selecting an architecture, compare real selected-artifact deployment, distinct product/provider IDs, side-effect-before-local-commit crash recovery, provider-scope idempotency, stale provider state, installed desktop security and evidence-derived portfolio behavior. Account for ecosystem/license/platform/maintenance/integration costs. After a built usable stage, compare product vs best fitting alternative vs status quo on correctness, cost/time, human intervention, wrong targets, false greens, recovery, usability and operating burden. That pilot cannot replace the pre-build existence/design gate.
