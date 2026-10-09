# Session-end handoff — ShareCLI + BytePort mature-first recovery

Date: 2026-09-30.

## Program invariant

Exactly two products remain in scope:
- KooshaPari/ShareCLI
- KooshaPari/BytePort

Do not begin repository #3.

## Direct-user thesis correction at session end

### ShareCLI
Mature product is a workload/resource coordination + optimization plane motivated by running very large agent workloads on machines that have aggregate capacity but fail under fragmented/uncoordinated execution.

Core mature families:
scheduling, dynamic queues, admission, packing, coalescing, in-flight sharing, safe caching, speculation, pressure/thermal/resource response, cancellation/replanning, and local process/session/worktree coordination.

Earlier local-coordination boundary only excludes accidental generic distributed-agent consensus/planning scope. It does NOT demote optimization breadth.

### BytePort
Mature product is generalized declarative infrastructure/deployment lifecycle:
repository + compact YAML/manifest → desired infrastructure/resource graph → build/plan → heterogeneous targets → observe/reconcile/update/rollback/destroy.

It began as a Netlify/Vercel/IaC learning project, expanded from cloud to bare metal, and aims to cover infrastructure/deployment needs generally.

Selected-app deployment remains a verification vertical slice, not mature product boundary.

## ShareCLI durable state

Implemented Tier A:
- A01 semantic identities;
- A02 RecoverySubject/Operation;
- A03 CapabilityTruth;
- A04 EquivalenceAdapter default unknown→Bypass;
- A05 trace/evidence validators.

Native falsification:
- generic durable reuse unsafe across changed bytes/workspace/external input/environment.

Qualification issue:
- recovery/contract workflows do not register on latest spec-branch commits; do not infer pass/fail.

Ontology:
- v1.2 adds WorkItem/WorkGraph/ResourceVector/Envelope/SchedulingPolicy/SchedulePlan/Placement/QueueEntry/OptimizationDecision/SpeculationGroup/PressureEvent/SchedulingReceipt.

New required CVP proof:
- deterministic resource-envelope scheduling/packing vertical slice with realistic naive baseline;
- session recovery remains identity/recovery slice but is not sufficient CVP alone.

Still open:
- Tier-A CI qualification;
- in-flight-vs-durable exact run;
- queue fairness/PID reuse;
- native jobserver comparison;
- required FUSE;
- session Exited semantics;
- scheduler/packing SOTA + alternatives expanded under corrected thesis;
- measurable scheduling vertical slice;
- fresh independent review.

## BytePort durable state

Qualified:
- B01 exact persisted ProviderResource stop; zero/multi fail closed; no ProjectID fallback.
- B02 mounted production operation journal:
  caller-stable optional operation_id,
  deterministic fingerprint,
  APPLYING persisted before mutation,
  UNKNOWN on transport ambiguity,
  provider identity persisted,
  realized replay,
  conflict on same ID/different request.
- full journal/restart model and lost-response/delayed-visibility model.
- Tier-A A01-A06 contract suite.

Build:
- delegated build P0 + live source/manifest probe passed;
- portable image archive digest passed;
- provenance attestation remains OPEN, so B04 closed.

B03:
- candidate historical odin schema recovered from SPEC.md + setup-windows.ps1;
- strict parser prototype implemented;
- exact Git ref→commit SourceSnapshot resolver implemented;
- branch-move and invalid-manifest tests wired;
- latest B03 oracle execution pending/unregistered at last check;
- do not integrate live /deploy until qualified.

Ontology:
- v1.2 adds DesiredResource/DesiredResourceGraph/Target/PlacementConstraint/ResourcePlan/RealizedResource/InfrastructureObservation/ReconciliationPlan/DestructionIntent.

New mature requirement:
- selected-app slice must grow into generalized desired-resource lifecycle;
- prove heterogeneous resources and later materially different target families, with bare metal a priority.

Still open:
- qualify B03;
- integrate source/manifest after qualification;
- provenance attestation then reconsider B04;
- network mode + health/metrics exposure;
- portfolio publisher;
- generalized infrastructure graph implementation;
- bare-metal adapter research/prototype;
- fresh independent review.

## Claude corpus

User intends to provide highly relevant Claude.ai conversations later.
No direct Claude-history plugin found.
When available through export or Computer Use/Work:
- ingest as separate source family;
- user messages = candidate user intent;
- Claude messages = assistant suggestion unless accepted;
- preserve conversation/timestamp/speaker provenance;
- rerun aliases, contradictions, source denominator and authority for these two products;
- do not restart or discard current work automatically.

## Next work order

1. Persist thesis correction in Registry and refresh completion gates/current-state ledgers.
2. Re-run SOTA/alternatives specifically for:
   - ShareCLI high-concurrency workload scheduling/packing/coalescing/speculation;
   - BytePort generalized IaC/deployment control planes + bare metal.
3. Expand ontology/obligations only where new research/authority creates distinct semantics.
4. Qualify BytePort B03.
5. Build ShareCLI deterministic scheduling vertical-slice oracle before more feature implementation.
6. Add BytePort DesiredResourceGraph prototype after B03 qualification; do not couple it to one cloud.
7. Keep B04 provenance, B05 network and B06 publication independently gated.
8. Update machine work-package DAGs to reflect corrected thesis/new packages.
9. Continue implementation mapping/orphan review under v1.2.
10. Run fresh independent adversarial review only after source denominator and architecture experiments are genuinely closed.

No completion percentage. Both products remain specification/design incomplete.
