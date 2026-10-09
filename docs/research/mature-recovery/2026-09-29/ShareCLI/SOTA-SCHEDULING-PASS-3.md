# ShareCLI SOTA pass 3 — workload scheduling / packing primitives

Date: 2026-09-30.
Scope: corrected direct-user thesis.

## Ray

Observed primitives:
- logical CPU/GPU/memory/custom resource requests;
- placement groups with atomic bundles;
- PACK/SPREAD/STRICT variants;
- detached lifetime;
- state APIs/observability;
- autoscaler demand simulation using bin-packing.

Decision consequence:
**LEARN FROM / ADAPT**, not embed Ray as mandatory runtime.
ShareCLI workloads span arbitrary local processes/tools, so Ray cannot be the universal execution substrate. Its resource-vector, bundle, placement, lifetime and observability semantics are strong prior art for SC-WP-A06/B05.

## Volcano

Observed scheduling pipeline:
- enqueue;
- allocate;
- backfill;
- preempt;
- reclaim;
- configurable plugin tiers.

Relevant plugins/primitives:
- binpack with weighted CPU/memory/GPU resources;
- DRF/fairness;
- gang scheduling;
- queue capacity/proportion;
- predicates for pressure/feasibility.

Decision consequence:
**LEARN FROM / ADAPT ALGORITHMS AND CONTROL MODEL**.
Do not recreate a Kubernetes scheduler inside ShareCLI. Reuse the separation of scheduling actions from policy plugins and benchmark deterministic ShareCLI policy against binpack/backfill/fairness concepts.

## Bootstrap model

Candidate ShareCLI scheduler architecture:
`WorkGraph + ResourceEnvelope + SchedulingPolicy -> SchedulerStrategy -> SchedulePlan -> AdmissionProvider/Placement -> Observation -> SchedulingReceipt`.

SchedulerStrategy should be pluggable:
- FIFO/bounded baseline;
- best-fit/binpack;
- backfill;
- priority/deadline;
- fairness/DRF-inspired;
- pressure-aware;
- later learned/predictive strategy.

Native jobserver/provider remains an admission primitive beneath the scheduler where applicable.

## Rejected shortcuts

- Kubernetes/Volcano as mandatory local runtime;
- Ray as mandatory task model;
- one hard-coded “smart” scheduler;
- treating process count as resource demand;
- calling binpack optimal without workload evidence.

## Next research

- Slurm backfill/multifactor priority;
- Bazel/Buck2/Ninja remote/dynamic execution and cache semantics;
- buildfarm/REAPI duplicate suppression;
- speculative execution literature;
- multidimensional online bin packing/deadline scheduling;
- learned scheduling only after deterministic baselines.
