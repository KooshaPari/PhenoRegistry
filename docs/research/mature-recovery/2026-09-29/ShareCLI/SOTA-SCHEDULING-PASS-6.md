# ShareCLI SOTA scheduling pass 6 — optimization hardness and execution/cache boundaries

Date: 2026-09-30.

## Vector bin packing / multidimensional scheduling

The resource-packing problem maps naturally to vector bin packing/vector scheduling when WorkItems consume CPU, memory, I/O, GPU/VRAM and other dimensions.

Established literature shows this family is computationally hard; even low-dimensional vector bin packing has strong approximation limits.

Decision consequence:
- mature contract must NOT promise globally optimal packing for arbitrary workloads;
- SchedulerStrategy quality is measured empirically and may be heuristic/approximate;
- correctness means respecting hard constraints and policy, not achieving mathematical optimum;
- exact/expensive solvers may be valid for small offline batches but are not universal runtime requirements.

Initial strategy posture:
- bounded FIFO correctness baseline;
- first-fit/best-fit decreasing or score-based vector packing;
- backfill when duration estimates qualify;
- fairness/deadline strategies as independent policies;
- learned strategies only against these transparent baselines.

## REAPI/Buck2 execution-cache boundary

Buck2/REAPI reinforce:
- Action identity is command + complete input identity;
- ActionCache and CAS are different services;
- execution placement/policy is separate from cache identity;
- local/remote/hybrid are execution strategies;
- cache entries may expire independently of artifacts.

Decision consequence:
ShareCLI must keep:
EquivalenceAdapter != SchedulerStrategy != ExecutionProvider != ResultStore.

A generic process command cannot gain durable-cache semantics merely because it is schedulable.

Potential future bootstrap:
- REAPI execution/cache adapter for build-like actions with closed input graphs;
- CAS adapter reusable independently of scheduler;
- remote execution queue/time thresholds as SchedulingPolicy inputs.

## CVP/B05 implication

The first product-value proof should compare transparent deterministic heuristics, not claim “smart scheduling.”

A candidate must report:
- feasibility/correctness;
- scheduler overhead;
- packing/utilization;
- makespan/throughput;
- wait/fairness;
- fragmentation;
- regressions vs bounded FIFO.

No optimum gap is required unless the fixture is small enough to compute one as an oracle.
