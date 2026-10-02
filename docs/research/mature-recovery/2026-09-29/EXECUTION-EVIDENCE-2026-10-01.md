# Execution Evidence Boundary — 2026-10-01

Scope: **KooshaPari/ShareCLI + KooshaPari/BytePort only**.  
This is an evidence-status receipt, not a completion claim.

## ShareCLI

Current exact product candidate observed for this receipt:

- branch: `spec/mature-recovery-2026-09-29`
- head: `056cbb21790d312503de34abb1dba27a6a12ff15`

New candidate semantics on that head include:

- multidimensional bounded packing across CPU, RAM, GPU count, VRAM, disk, I/O weight and required capabilities;
- dependency/fairness/backfill reference policy;
- real-subprocess B05 plan-to-Hypervisor execution oracle;
- native jobserver lease + Hypervisor child-propagation oracle;
- capability-bounded pressure-response reference policy;
- bounded speculation eligibility/budget/delay/wasted-work accounting.

Exact-head CI is **PENDING/QUEUED**. None of those additions are qualified by this receipt.

Older native counterexamples for generic durable equivalence remain valid only for the exact historical candidates/runs already recorded in the product dossier. They do not qualify the new scheduling candidate.

## BytePort

Current exact product candidate observed for this receipt:

- branch: `spec/mature-recovery-2026-09-29`
- head at latest product change: `a9b0749b3146400934b09237ab625d0952692ae4`

### Superseded diagnostic green

Recovery-oracle run `36916423703` completed on an older candidate and showed green jobs for:

- B03 source/manifest prototype;
- BP-WP-A07 infrastructure graph;
- B08 reconciliation reference model;
- BP-WP-B01 exact provider-stop remediation;
- B02 runtime reconciliation;
- B02 production operation journal;
- BP-AD-01 operation journal model;
- duplicate-deploy and persistence-window probes;
- session-token expiry.

That run is **STALE for the current candidate**. It is useful diagnostic evidence that the pre-provider-execution reference model compiled and passed, but it cannot qualify later B03/B08 changes.

The same run's old BP-F03 "counterexample must reproduce" job failed because the defect is already remediated. The workflow has since been corrected to a regression gate; the historical counterexample remains evidence, not a requirement that current code stay broken.

### Artifact chain

The repaired mature artifact-chain run on the earlier exact candidate completed green after separating local immutable artifact/runtime identity from provenance attestation. This does **not** close B04 provenance verification.

### New unqualified candidate work

Since the superseded green run, BytePort added or tightened:

- BUILD/ENV remain byte-visible in ManifestRevision but inert in desired-graph authorization;
- canonical provider-backed B08 execution using the checked/interruption-aware planner;
- DELETE supports nil desired state plus exact realized-resource identity rather than fabricated desired state;
- pre-mutation target/provider validation;
- provider identity in InfrastructureObservation;
- wrong-target observations become UNKNOWN;
- heterogeneous target dependency-stage planning.

These changes require a new exact-candidate recovery run.

### Workflow integrity incident

The recovery workflow temporarily became invalid because an edit left duplicated job blocks. Invalid push run `36926634279` is **COLLECTOR/WORKFLOW FAILURE**, not product evidence.

The workflow was rebuilt from the last known-valid 188-line version. On head `e16970bc92a2e7a79d509d03fad6a30708e0b3cf`, GitHub again registered it as **BytePort Mature Recovery Oracle**; that run was cancelled only because the branch advanced again.

## Evidence rule

For both products:

`PENDING`, `QUEUED`, `CANCELLED`, stale-candidate green, invalid-workflow runs, and unrelated repository CI are not acceptance evidence.

The next promotion event is an exact-head executed oracle for the new candidate semantics.


## Deferred qualification-infrastructure repair

BytePort `.github/workflows/mature-recovery-contract.yml` is currently invalid on the product branch:

- its A07 `go test` command is truncated before the closing quote/options;
- a standalone `-count=1 -v` fragment follows on the next line;
- GitHub reports the resulting push run under the workflow filename with conclusion `failure`.

This is classified as **COLLECTOR/WORKFLOW FAILURE**, not product evidence.

The repair is deliberately deferred until the currently registered exact **BytePort Mature Recovery Oracle** run for head `a9b0749b3146400934b09237ab625d0952692ae4` executes or otherwise terminates, because changing the BytePort head now would cancel that exact-candidate oracle again.


## CI saturation diagnosis

The exact-head qualification delay is now attributable to repository-wide GitHub Actions saturation rather than the two recovery workflows themselves.

Observed via GitHub Actions run inventory:

### ShareCLI

- queued workflow runs: **407**
- in-progress workflow runs: **16**
- exact recovery-carrying CI run: `36926431574`, status `pending`
- multiple stale recovery-branch SHAs still had long-running workflows occupying runners

Representative stale active workflows inspected on the recovery branch include:

- `live-pool-soft.yml`
- `load-soft.yml`
- `soak-soft.yml`
- `visual-soft.yml`
- `visual.yml`
- `rss.yml`

Their current workflow headers do not define an effective top-level concurrency/cancel policy, so newer recovery-head churn does not reliably evict older expensive runs.

### BytePort

- queued workflow runs: **355**
- in-progress workflow runs: **1** at observation time
- pending runs: **4**, including exact recovery oracle `36927029714`
- the only active run observed was main-branch CI; the recovery oracle itself was registered correctly and pending

### Consequence

This is **qualification infrastructure saturation**, not product pass/fail evidence. It also explains why repeatedly advancing the product heads worsened evidence latency: each commit generated another large workflow fan-out while old expensive workflows remained active or queued.

### Deferred CI remediation

After the exact candidate oracle either executes or terminates, the product repos should receive a bounded CI hygiene pass:

1. add stable PR/branch concurrency groups to expensive duplicate workflows;
2. set `cancel-in-progress: true` for soft/advisory PR workflows where stale runs have no evidentiary value;
3. keep non-cancellable behavior only where historical/soak evidence genuinely requires completion;
4. avoid workflow-level path filters for required checks that would leave required checks permanently pending;
5. isolate mature-recovery qualification from unrelated full-repo fan-out where possible;
6. repair BytePort `mature-recovery-contract.yml` syntax before relying on it.

No product head is being advanced solely to perform this cleanup while exact qualification runs remain pending.


## Qualification update — 2026-10-02

### BytePort exact green

Exact recovery oracle run `36927029714` completed **SUCCESS** on candidate `a9b0749b3146400934b09237ab625d0952692ae4`.

Successful jobs include B03 source/manifest, A07 generalized infrastructure graph, B08 reconciliation reference/provider-fixture execution, B01 exact provider stop, B02 journal/reconciliation, operation-journal model, duplicate-deploy/persistence probes, and session expiry.

Machine work-package state was updated so:

- B03 is qualified for immutable source + strict manifest + inert BUILD/ENV graph projection;
- A07 is qualified;
- B08 is qualified at **reference + provider-fixture** level only.

This does **not** qualify production provider adapters, production destructive execution, or unresolved network/security authority.

The previously broken `mature-recovery-contract.yml` A07 command has now been repaired on the post-qualification branch head.

### ShareCLI exact failure and repair

Run `36926431574` completed with ordinary Rust/lint/test gates green, but mature-recovery qualification failed **before Rust recovery tests executed** because `validate_work_packages.py` rejected missing `critical` lists on SC-WP-B01 through SC-WP-B04.

This was machine-contract/schema drift, not a B05/B06 scheduler failure.

The four Tier-B packages now have substantive `critical` invariant lists on candidate `653f3d37f03a5a758869791c020f394f9d1f71e6`. New CI run `36981940615` is active; mature-recovery job `110758197550` is queued.

The same older ShareCLI run also showed a separate Cargo Deny source-policy failure: exact-revision PhenoInfra git dependencies are present while `deny.toml` disallows git sources. This is classified separately from mature-recovery qualification and has not been weakened as part of scheduler recovery.


## Qualification update — 2026-10-02 11:28 CEST

### ShareCLI runtime-oracle failure localized

Exact run `36981940615` on candidate `653f3d37f03a5a758869791c020f394f9d1f71e6` passed the work-package schema after the Tier-B repair and progressed through the recovery semantic tests.

The first product-candidate failure was in the newly added real-subprocess runtime fixture:

- `recovery_scheduling_runtime_vertical.rs` contained an invalid Rust string around the shell command;
- the adjacent `recovery_jobserver_hypervisor.rs` fixture had the same quoting class.

Both are test-fixture compile defects, not evidence that scheduling semantics failed. They were corrected using raw Rust strings on candidate `fe05a23dcf2b655dbb307a0982508fcc0dad5de5`. New CI run `36990039958` is pending.

The same run also emitted duplicate-key errors from a transitive PhenoShared/AgilePlus checkout, but the direct failure that terminated the mature-recovery job was the ShareCLI runtime fixture compile error. Treat transitive manifest corruption as separate dependency health debt unless it becomes the next blocking exit.

### BytePort post-qualification adapter step

After B03/A07/B08 reference+fixture qualification, BytePort added a non-live NanoVMS infrastructure adapter boundary.

It is intentionally not wired into `/deploy`. The adapter:

- requires a typed `BuildArtifactID` and resolves it through an artifact resolver;
- refuses CREATE if the artifact is missing or lacks an immutable reference;
- preserves target/provider/external sandbox identity;
- does not claim UPDATE or REPLACE;
- requires exact provider/target/sandbox identity before DELETE;
- represents missing provider observation as non-fresh UNKNOWN.

This is a candidate production-adapter boundary under fixture qualification, not production-provider acceptance.


## Runtime qualification advance — 2026-10-02

### ShareCLI

On exact candidate `fe05a23dcf2b655dbb307a0982508fcc0dad5de5`, mature-recovery run `36990039958` executed both newly added real runtime oracles successfully:

- `planned_dependency_ready_work_reaches_real_hypervisor_execution`: PASS;
- `unknown_resource_demand_never_reaches_spawn`: PASS;
- `native_jobserver_token_and_child_propagation_compose_with_hypervisor`: PASS.

The job then failed in the native memory-pressure fixture because a child exited between `poll()` and reading `/proc/<pid>/status`. The collector raised `VmRSS unavailable`; this is a measurement race, not an envelope counterexample.

The sampler now returns an explicit no-sample result only when `/proc/<pid>` disappeared after the process-exit race; a live process without `VmRSS` still fails. Missing observation is not converted into zero.

Additional next-gate work now on branch:

- externally inherited GNU-make jobserver oracle (`make -j2` owns the provider);
- same-workload benchmark records naive/FIFO/fit-scan makespan, envelope violations, completion, and planner item-check cost without inventing an optimality threshold.

### BytePort

The non-live NanoVMS adapter recovery oracle passed on candidate `e17b4c0cf4f251e342e75d8e9ee133dd0b34d690`, alongside the already-green recovery contract/build/artifact chains.

A follow-up delayed-visibility fixture now models:

1. exactly one NanoVMS CREATE;
2. first observation not yet visible => non-fresh UNKNOWN;
3. later observation converges to the same sandbox identity;
4. deploy count remains exactly one.

This is still fake-transport/provider-adapter evidence. Production `/deploy` remains untouched.


## Execution-slice advance — 2026-10-02 late morning CEST

### ShareCLI current execution slice

Product branch candidate contains all of the following pending exact qualification:

- reference dependency/device/fairness/backfill scheduling;
- true externally supplied GNU-make jobserver discovery/reuse;
- same-workload naive vs FIFO vs fit-scan benchmark with planner-item-check accounting;
- native Linux pressure comparison;
- 50-real-process same-workload admission-envelope comparison;
- RAII multidimensional resource reservations across CPU/RAM/GPU/VRAM/disk/I/O/capabilities;
- opt-in Hypervisor queued execution that holds the resource lease across the actual subprocess lifetime;
- rejected admission proven not to spawn;
- CI Success Gate now directly depends on the mature-recovery qualification job, closing the prior false-green aggregate path.

The admission/runtime integration remains **opt-in**. Default `Hypervisor::run` has not been silently switched to the new scheduler.

Exact recovery evidence is still pending because GitHub Actions has not assigned the decisive job.

### BytePort current execution slice

Product branch candidate now extends the previously qualified B03/A07/B08 reference/provider-fixture model with:

- `RuntimeOperationID` separated from `DesiredResourceID` on mutation actions;
- execution-time operation binding rather than planner-fabricated identity;
- generic `BuildArtifactResolver` in the build domain;
- graph-to-artifact manifest-lineage validation before provider mutation;
- NanoVMS observation carrying exact config digest for restart reconciliation;
- explicit apply outcomes `REALIZED` vs `UNKNOWN`;
- typed unknown-after-send NanoVMS transport error;
- ambiguous CREATE returning UNKNOWN + reconciliation identity, with no fabricated realized resource;
- contradictory/missing apply outcomes rejected by the generic executor;
- disposable lifecycle fixture:
  `SourceSnapshot -> ManifestRevision -> DesiredResourceGraph -> BuildArtifact -> CREATE -> OBSERVE -> restart NOOP -> exact authorized DELETE`;
- the lifecycle asserts one and only one provider CREATE across restart reconciliation.

Live `/deploy` remains untouched. Production destructive authority, network/security policy, and real NanoVMS HTTP wiring remain separate gates.

### CI infrastructure state

Latest observed queue pressure:

- ShareCLI: 253 queued, 10 in progress, 3 pending.
- BytePort: 233 queued, 5 in progress, 6 pending.

The GitHub connector exposes rerun operations but no cancel-workflow-run action, so stale-run queue cleanup cannot be performed directly from this session without modifying workflow concurrency behavior and thereby advancing/cancelling the exact product candidates.

Both product heads are therefore intentionally frozen until the registered exact recovery runs execute.
