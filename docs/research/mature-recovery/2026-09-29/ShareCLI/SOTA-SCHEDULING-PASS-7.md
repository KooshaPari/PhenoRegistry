# ShareCLI SOTA scheduling pass 7 — OS-native pressure and enforcement

Date: 2026-09-30.

## Linux PSI

Linux Pressure Stall Information exposes CPU, memory and I/O contention as "some" and "full" stall time, globally and per cgroup v2.

Key product implication:
- pressure is not equivalent to raw utilization;
- sustained full pressure can indicate thrashing/productivity loss;
- PSI is suited to policy inputs for load shedding, pausing, migration or killing restartable low-priority work;
- pressure samples need timestamp/window/source identity.

Decision:
**INTEGRATE Linux PSI as a PressureProvider** where available.

## Linux cgroup v2

Cgroup v2 provides per-group CPU/memory/I/O control and per-cgroup PSI.

Decision:
**INTEGRATE as a Linux ResourceControlProvider** for owned workloads where ShareCLI has authority.
Do not claim enforcement when only observing system-wide PSI.

## Windows Job Objects

Windows Job Objects provide group-level CPU rate control including weight, hard cap and min/max modes. Job identity/hierarchy is native OS state.

Decision:
**ADAPT as Windows ResourceControlProvider**, preserving exact Job Object identity and distinguishing weight-based policy from hard caps.

The Windows provider should not pretend unsupported/obsolete I/O controls are universal; capability detection is required.

## NVIDIA MPS

NVIDIA MPS supports cooperative CUDA multi-process/application execution, reduced context-switch overhead, memory/SM partitioning and priority/dynamic resource adjustment.

Decision:
**OPTIONAL GPU provider/integration candidate** for eligible CUDA workloads.
Do not make MPS a universal GPU scheduler or use it for non-CUDA workloads.

## Cross-platform architecture implication

Separate:
- PressureProvider: observe contention/productivity loss;
- ResourceControlProvider: enforce cap/weight/allocation;
- SchedulerStrategy: choose actions;
- WorkloadAdapter: knows interruptibility/restartability/equivalence;
- GPUProvider: optional device-specific coordination.

Capability truth examples:
- PSI observed != cgroup enforced;
- Job Object membership != CPU hard cap;
- NVIDIA GPU visible != MPS managed.

## Pressure-response safety

Pressure policy may:
- defer admission;
- reduce concurrency;
- throttle where provider supports it;
- pause/cancel restartable low-priority work;
- replan.

It MUST preserve:
- exact affected WorkItem/ExecutionAttempt;
- provider capability/evidence;
- reason and threshold/policy revision;
- before/after pressure sample;
- no automatic destructive action on stale/unknown pressure.

## Next prototype

Add additive PressureSample/PressureProvider model and Linux PSI parser.
No production pressure-response loop until native fixture proves:
- pressure is observed;
- action actually changes workload state;
- pressure response improves stability without unacceptable throughput/fairness regression.
