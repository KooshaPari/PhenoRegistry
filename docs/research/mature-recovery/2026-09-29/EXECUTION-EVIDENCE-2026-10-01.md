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
