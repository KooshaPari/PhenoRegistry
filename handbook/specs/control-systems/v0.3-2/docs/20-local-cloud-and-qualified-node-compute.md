# Local cloud and qualified personal compute nodes

## Decision brief

Treat a personal desktop, laptop, workstation or future small node as a **qualified local provider target**, not as a generic self-hosted runner and not as a new public cloud. BytePort remains the experience/control plane; a privately connected node daemon exposes capabilities, receives desired state and pulls immutable artifacts. S052, S058.

This deliberately separates three layers:

| Layer | Owns | Must not own |
|---|---|---|
| BytePort control plane | project/repository linkage, environments, desired state, provider selection, lifecycle, evidence, GUI/API/CLI/SDK | hypervisor/runtime internals unique to one node |
| local-fleet provider | node inventory, placement, capability matching, lease/admission, provider-specific plans | a second project registry or GUI truth store |
| node daemon/runtime adapters | artifact pull, local execution, health, resource enforcement, volume/device hooks, safe daemon update | portfolio-wide deployment authority |

Historical BytePort work already described a local `nvms + vLLM` tier and later compute-mesh desired state, but both inspected PRs are closed and unmerged. They are design ancestry, not current implementation authority. S059, S060.

## Why not just install a full private cloud?

The alternatives are useful references but fail as a universal default:

- **Kubernetes/Nomad/OpenNebula-style cluster everywhere**: good for dedicated servers; poor fit for a laptop or gaming/LLM workstation that must remain primarily a human machine.
- **Incus/Proxmox as the product boundary**: useful execution substrates and excellent reference semantics for VM/container/resource limits, but they do not replace BytePort's cross-provider lifecycle. Incus is therefore an adapter candidate, not the canonical API. S076, S077.
- **GitHub self-hosted runner as the abstraction**: handles jobs, not durable databases, volumes, service health, VM lifecycle or provider portability.
- **CI pushes over SSH/root runtime socket**: easy to prototype, but expands credentials and inbound/control authority on personal machines.

The selected shape survives these contradictions: BytePort plans; provider adapters qualify; the daemon executes.

## Node capability record

A node record should include at least:

```text
node_id / owner / trust_state / agent_version
os / arch / virtualization / container / wasm / native adapters
cpu topology + allocatable / memory total+reserve / disks+IO / network
GPU devices / VRAM / passthrough or exclusive-lease capability
battery / power / thermal observability where available
runtime versions and feature flags
volume/back-up capabilities
private connectivity and identity state
current host mode / drain state / workload leases
```

A missing capability is **unknown/unsupported**, never inferred from operating-system family.

## Foreground reservations and modes

The old runner design's process-pause idea is too narrow. Use explicit host modes whose values feed admission and preemption, for example:

| Mode | Typical intent | Background policy |
|---|---|---|
| `interactive` | normal foreground use | preserve CPU/RAM latency reserve; no surprise exclusive devices |
| `creator_audio` | Ableton/low-latency audio | large CPU/RAM reserve, protect real-time scheduling and disk IO, normally no disruptive updates |
| `gaming` | foreground game | reserve GPU/VRAM exclusively and substantial CPU/RAM; preempt eligible GPU workloads |
| `llm_local` | local inference | explicit GPU/VRAM lease; competing GPU deployments blocked or drained |
| `idle` | machine available | highest allocatable background envelope |
| `maintenance` | upgrades/recovery | drain normal workloads; allow lifecycle operations only |

The mode is only one signal. Battery state, thermals, disk pressure and user-defined per-node reserves also gate placement. Laptop defaults should be substantially more conservative than a desktop, but this docset does **not** invent exact percentages before measurement.

## Workload contract

Every workload declares resource requests/limits plus `priority`, `preemptible`, `eviction_grace`, `stateful`, device requirements and recovery expectations. Stateful workloads additionally declare volume identity, backup/restore behavior and RPO/RTO. A containerized Postgres instance is not automatically equivalent to RDS, Supabase or Neon.

## Release and update path

```text
Git commit
  -> deterministic CI + selected review gates
  -> immutable artifact + SBOM/provenance
  -> registry/artifact store
  -> BytePort desired-state authorization
  -> private/outbound node notification or reconciliation
  -> node pulls exact digest
  -> local runtime adapter stages/restarts/health-checks
  -> node reports observed digest + health + resources
  -> controller commits deployment receipt
```

Daemon updates use the same discipline: staged version, compatibility check, health, rollback. A daemon upgrade must not erase desired state or orphan workloads.

## Production versus local placement

Local nodes are first-class **targets**, not automatically production-quality targets. The same workload can be planned against local, PaaS, VPS or hyperscaler providers. The planner returns exact/approximate/unsupported semantics and costs/risks. Promotion can move a workload without pretending every provider offers identical managed behavior.
