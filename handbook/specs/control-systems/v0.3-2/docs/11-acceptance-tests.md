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
