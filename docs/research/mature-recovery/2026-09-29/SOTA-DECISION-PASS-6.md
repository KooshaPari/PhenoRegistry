# SOTA decision pass 6 — ownership boundaries after REAPI/Crossplane/Ironic comparison

Date: 2026-10-01.

## ShareCLI

### Action identity / coalescing
REAPI confirms a strong reusable decomposition:
- reproducible action identity;
- content-addressed input root;
- ActionCache separate from CAS;
- in-flight merging separately controllable from durable caching.

Decision:
- evolve EquivalenceAdapter toward structured ActionIdentity for qualified adapters;
- retain BYPASS for opaque commands;
- scheduling/packing remains available even when equivalence is unknown;
- never derive durable equivalence merely from scheduler metadata.

### Existing branch review
Current spec branch already contains:
- ResourceVector/Envelope/WorkItem/SchedulePlan domain;
- deterministic bounded FIFO and fit-scan simulator;
- benchmark proving naive all-at-once violates envelope;
- fragmentation fixture where fit-scan improves makespan over strict FIFO;
- GNU jobserver descriptor parsing including POSIX FIFO/FD and Windows semaphore.

These are **candidate implementations**, not automatically qualified. They align with v1.2 and should be graded rather than duplicated.

### Next ShareCLI gate
Qualify A06/B05 candidate tests, then extend:
- dependency readiness;
- discrete device/capability feasibility;
- backfill with duration provenance;
- queue fairness/aging;
- scheduler overhead receipt;
- native jobserver token acquisition/release (not only parsing).

## BytePort

### External resource safety
Crossplane independently reinforces:
- desired object vs external resource identity;
- observe-only/import modes;
- explicit management/delete policy;
- create-pending/succeeded/failed markers to avoid leaked resources;
- stopping reconciliation when create outcome cannot be determined.

Decision:
BytePort B08 should adopt a generalized **creation ambiguity guard**:
persist intent/pending marker before create; if provider identity cannot be recovered after ambiguous create, do not blindly recreate/destruct.

This generalizes B02 from app deployment to all infrastructure resources.

### Bare metal
Ironic standalone supports direct API use without full OpenStack. Its state machine distinguishes enroll/manage/inspect/clean/provide/deploy/adopt/delete and failure/wait states.

Decision:
Ironic standalone remains leading B09 engine candidate.
BytePort must not flatten:
- delete inventory record;
- undeploy workload;
- clean hardware;
- power off;
- retire/adopt

into one generic Delete.

### Existing branch review
BytePort A07 already exists and includes:
- mixed DesiredResource kinds;
- lifecycle policies including observe-only/orphan/explicit destruction;
- TargetCapabilities;
- ResourcePlan vs RealizedResource;
- UNKNOWN reconciliation;
- exact DestructionIntent matching.

This is candidate implementation to qualify, not duplicate.

## Next work

1. Qualify ShareCLI A06/B05 existing candidate.
2. Qualify BytePort A07 existing candidate.
3. Extend BytePort B08 reference reconciler with creation ambiguity and lifecycle-policy controls.
4. Extend ShareCLI structured ActionIdentity only after A06/B05 qualification.
5. Keep bare-metal B09 engine integration blocked until MAAS/Ironic/Tinkerbell operational comparison is complete.
