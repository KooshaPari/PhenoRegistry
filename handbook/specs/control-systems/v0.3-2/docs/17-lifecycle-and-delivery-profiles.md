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
