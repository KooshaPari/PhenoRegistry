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
