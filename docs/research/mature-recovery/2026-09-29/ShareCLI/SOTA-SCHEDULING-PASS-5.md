# ShareCLI SOTA scheduling pass 5 — build execution, cache identity, native coordination

Date: 2026-09-30.
Scope: corrected workload-defragmentation thesis.

## GNU make jobserver

Source: GNU make manual, current web docs.
Observed:
- recursive/nested parallel tools can share one slot pool;
- POSIX uses pipe/FIFO tokens;
- Windows uses named semaphores via MAKEFLAGS;
- participants must return acquired tokens even on error;
- one implicit slot semantics must not be double-returned.

Decision:
**INTEGRATE directly when detected**. Native jobserver participation is a provider capability, not an implementation detail to replace merely for uniformity.

Implications:
- slot ownership/release correctness is safety-critical;
- ShareCLI ProductLeaseProvider remains for non-cooperating workloads;
- policy must avoid double-throttling nested jobserver-aware tools.

## Bazel dynamic execution

Source: Bazel dynamic execution docs.
Observed:
- local and remote execution of the same action may race;
- first successful branch wins, loser is cancelled;
- local execution may be delayed after likely remote cache hits;
- action suitability and local resource cost matter.

Decision:
**ADAPT later as SpeculationStrategy**, after equivalence and deterministic scheduling are proven.

Implications:
- speculation delay policy;
- eligibility by adapter/action semantics;
- explicit resource reservation for both branches;
- loser cleanup/wasted-work accounting;
- outcome comparison to non-speculative baseline.

## Buck2 / REAPI

Sources: Buck2 remote execution/architecture docs and Bazel Remote Execution API.
Observed:
- action identity hashes command + inputs;
- ActionCache is distinct from CAS;
- local/remote/hybrid execution are explicit policy modes;
- cache and execution services are separable;
- queue-time/resource properties affect remote choice;
- REAPI permits standard remote cache/execution interoperability.

Decision:
**LEARN FROM and potentially integrate REAPI-compatible adapters** for workloads that can produce exact action/input identities.

Critical distinction:
ShareCLI MUST NOT generalize build-system action digest semantics to arbitrary commands. REAPI-style Durable reuse applies only through adapters whose input closure is established.

## Architectural consequence

Separate:
- SchedulerStrategy: when/where work should run;
- AdmissionProvider: whether capacity can be acquired;
- EquivalenceAdapter: whether work/results may be shared;
- ExecutionProvider: local/native/remote mechanism;
- ResultStore/CAS adapter: artifact storage;
- SpeculationStrategy: whether multiple eligible attempts race.

These interfaces may compose but are not interchangeable.

## Benchmark implications

Scheduling vertical must measure:
- scheduler overhead;
- peak resource use;
- completed useful work;
- deadline/elapsed behavior;
- queue wait/fairness;
- duplicate execution avoided;
- speculative waste;
- cache correctness/hit quality;
- native-tool interference.

## Next

- online multidimensional bin packing algorithms;
- deadline/critical-path scheduling;
- pressure-aware policy;
- GPU/VRAM placement and oversubscription;
- decide initial deterministic B05 strategies after benchmark fixture exists.
