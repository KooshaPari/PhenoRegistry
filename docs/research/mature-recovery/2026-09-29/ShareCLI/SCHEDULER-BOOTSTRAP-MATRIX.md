# ShareCLI scheduling / execution bootstrap matrix — v0.1

Date: 2026-09-30.
Scope: workload/resource defragmentation thesis.

| System / primitive | Strong primitives | Weak fit / limitation | ShareCLI decision |
|---|---|---|---|
| GNU make jobserver | cross-process slot coordination; nested cooperation; POSIX FIFO/fd; Windows named semaphore | scalar slot model; cooperating tools only; no multidimensional packing | **INTEGRATE directly when detected** as NativeJobserverProvider |
| Slurm | priority, reservations, backfill, multifactor scheduling, mature queueing | cluster/batch orientation; operationally far larger than local ShareCLI | **ADAPT scheduling semantics/algorithms**, not runtime |
| Volcano | enqueue/allocate/backfill/preempt/reclaim pipeline; binpack; DRF; gang; queue policies | Kubernetes-centric control plane | **LEARN FROM plugin/action architecture**, do not require Kubernetes |
| Ray | logical CPU/GPU/custom resources; placement groups; PACK/SPREAD; observability | Ray task/actor runtime cannot represent arbitrary native commands universally | **ADAPT resource/placement semantics**, optional adapter only |
| Nomad | feasibility + scoring; binpack default; spread/affinity; device/GPU constraints | cluster/service scheduler rather than local agent-work substrate | **LEARN FROM placement scoring/device semantics** |
| Bazel dynamic execution | local/remote race; winner selection; loser cancellation; delay tuning; profiling | build actions with closed semantics; remote infra assumption | **ADAPT SpeculationStrategy** only for eligible adapters |
| Bazel REAPI | standard action/cache/CAS/remote execution protocol | exact action/input closure required | **POTENTIAL INTEGRATION** for build-like workloads |
| Buck2 | explicit local/remote/hybrid executor; action digest; ActionCache/CAS separation; queue/resource properties | build-system action model | **LEARN FROM / potential REAPI adapter** |
| Vector bin packing literature | principled multidimensional packing model | general optimum/strong approximation computationally hard | **Use transparent heuristics + empirical quality**, no universal optimum claim |
| Existing ShareCLI SlotQueue/leases | already local/product-integrated | fairness/PID ownership defects; scalar/legacy semantics | **TRANSITION / replace behind provider contract after oracles** |
| Existing ShareCLI Hypervisor/cache | existing coalescing/cache path | generic semantic identity falsified | **QUARANTINE durable reuse; salvage only through adapters** |

## Proposed compositional architecture

`WorkGraph`
→ `SchedulingPolicy`
→ `SchedulerStrategy`
→ `SchedulePlan`
→ `AdmissionProvider`
→ `ExecutionProvider`
→ `ExecutionAttempt`
→ `ResultSelection`

Orthogonal:
- `EquivalenceAdapter` decides coalescing/cache eligibility;
- `ResultStore/CAS` stores qualified artifacts;
- `SpeculationStrategy` may create multiple attempts;
- `Observation/PressureProvider` feeds replanning.

No layer may silently substitute for another.

## Initial build/custom decisions

### Build custom
- product-level WorkItem/WorkGraph/ResourceEnvelope/SchedulingPolicy identities;
- strategy/provider composition;
- local evidence and policy loop;
- operator UX and agent-aware workload adapters.

### Integrate/adapt
- GNU jobserver protocol;
- REAPI/CAS where semantic closure exists;
- deterministic scheduling algorithms inspired by Slurm/Volcano/Nomad;
- native OS resource/process primitives.

### Defer
- learned scheduler;
- universal remote execution;
- distributed cluster consensus;
- speculative execution beyond qualified adapters.

## Falsification conditions

ShareCLI scheduling thesis weakens if:
- bounded native schedulers/jobservers already solve target agent workloads with negligible coordination gaps;
- ShareCLI scheduling overhead erases packing gains;
- workload demand estimates are too poor to outperform bounded FIFO;
- agent workloads cannot expose safe equivalence/interruptibility/pressure hooks.

These require benchmark evidence, not assumption.
