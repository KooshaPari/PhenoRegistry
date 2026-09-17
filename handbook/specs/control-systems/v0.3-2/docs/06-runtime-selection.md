# Runtime selection and the Docker exception protocol

**v0.2 qualification note:** the reviewed Microsoft WSLC tutorial lists WSL 2.9.3+ (pre-release) prerequisites. This is documentation, not an installed-version observation or authorization to update Windows/WSL. A descendant's statement that VSOCK is stable is not accepted as a test result; identify the real data path and test the exact topology. [S041; S042; E014]

## Distinct lanes

| Lane | Proposed role | Evidence state | Adoption condition |
|---|---|---|---|
| Rootless Podman in a selected WSL2 distribution | First candidate for persistent local Linux services | Podman and WSL mechanisms documented; local stack untested | Exact installed-version discovery, cgroup/systemd checks, lifecycle and isolation tests |
| WSLC (`wslc.exe`) | Separate Windows/WSL container-runtime evaluation | Microsoft documents it separately; reviewed prerequisites reference a prerelease | Version-qualified CLI/API/capability adapter; do not assume Podman or Quadlet behavior |
| Docker Engine in Linux/WSL2 | Exception candidate | Not rejected categorically; no superiority benchmark supplied | Required capability or material measured benefit, bounded exception, operator approval |
| Docker Desktop | Different integrated product candidate | Not what the direct user exception named | Separate product/installation/resource/licensing review if actually needed |
| Native system service | Possible home for an OCI-inappropriate trusted process | Application-specific | Explicit process supervision, state, identity and update contract |
| Linux VM / KVM-based path | Candidate for workloads needing a different isolation boundary | Host capability unverified | Prove virtualization support, devices, recovery and acceptable overhead |
| Spin / WebAssembly | Explicit application port or Wasm-native component | Not a universal native-process fallback | Compatible build, imports, host interfaces and persistence design |

Sources: S001, S013–S016, S029–S030. Described roles are proposals. A documented capability is not a successful local integration.

**Docker Engine versus Podman** is the requested exception comparison. A comparison only against Docker Desktop would answer a different question. Do not infer licensing or resource overhead for one product from the other. No license purchase is recommended in this package.

## PaaS and administration candidates

| Candidate | What this review establishes | Decision in this baseline |
|---|---|---|
| Coolify | Docker-oriented supported installation path [S017] | Conditional Docker-path candidate; not the mandatory Podman layer |
| Dokploy | Docker/Swarm setup path [S018] | Requires the actual orchestration semantics, not just a compatible endpoint |
| CapRover | Docker setup path [S019] | Conditional alternative, not ranked as best |
| Portainer | Podman path exists, but reviewed support is rootful CentOS 9 / Podman 5.x [S020] | Not an automatic match for rootless WSL |
| Cockpit Podman | Container administration UI exists [S021] | Optional observer/admin surface, not the application delivery controller |
| Direct Quadlet integration | Podman/systemd lifecycle described by the official manual [S015] | Initial low-component-count candidate; must still pass recovery and security tests |

This matrix deliberately has no fabricated performance scores or “winner.” Product API breadth, local compatibility and operational burden have not been measured. Nixpacks, k3s/k0s, Argo, Flux, Fly and commercial NanoVMs were named in the old synthesis but not qualified in this pass. They remain research candidates, not selected components.

## Workload inventory before engine ranking

Capture one representative case per real workload class: persistent HTTP API, SSE inference gateway, a service with database state, a build/test worker, and a device/GPU-dependent job **only if it is in scope for the selected node**. Record image/binary architecture, mounts and ownership, exact network path, required syscalls/devices, resource limits, recovery behavior and the foreground work that must remain usable. Do not take model-training or local-inference targets from an unrelated project and impose them as this stack’s acceptance thresholds.

## Benchmark protocol — proposed, not measured results

1. **Fix the experiment.** Use the same host, Windows/WSL versions, Linux filesystem placement, image digest, application config, resource caps and comparable network/storage paths. Record runtime and kernel details. Measure differences that cannot be equalized rather than hiding them.
2. **Pass semantics first.** Verify bind/volume ownership, persistence, restart, networking, SSE, device access when required, cleanup and isolation. A fast runtime that fails a must-have capability is not eligible.
3. **Separate regimes.** Run cold-image-pull, cached-image start, steady-state and restart/recovery tests separately. Report host idle and representative contended-host tests separately. Windows-mounted and Linux-native filesystem cases must not be silently pooled.
4. **Use paired repeated runs.** An initial proposal is at least 30 randomized paired runs per short experiment, with raw samples and a confidence interval for the difference. Longer soak/recovery cases need an explicitly chosen duration and fault schedule. Treat the sample count as a protocol starting point, not a universal statistical guarantee.
5. **Report complete costs.** Include setup/operator actions, resident memory, CPU, disk use, I/O, application throughput, p50/p95/p99 latency, startup and recovery, failed runs, orphaned resources and foreground degradation. Do not omit failures from timing summaries.
6. **Make a bounded decision.** Select the lane for this workload and host, not “Docker is globally better.” Record what evidence would reverse the choice.

## Proposed decision function

First apply operator-approved hard requirements. Among eligible candidates, retain the preferred runtime unless an alternative has a material benefit outside measurement noise and within approved cost/maintenance constraints. “Material” needs a predeclared target for the actual workload; this package does not invent a mandatory percentage improvement or spending cap.

An exception record must contain: required behavior; tested versions/configuration; raw evidence; alternatives and attempted remedies; measured delta with uncertainty; added privilege/operating burden; approved scope and expiration/review trigger. An optional PaaS convenience cannot be relabeled as an unavoidable runtime requirement without operator agreement.

## Read-only discovery and safe rehearsal

Start with executable paths and version commands, systemd/cgroup status, runtime inspection, socket permissions, WSL distribution identity, mount locations and container inventory. Avoid broad home-directory or credential dumps. Discovery output should redact tokens and personal paths from public reports.

Do not call `wsl --shutdown` against an active workstation just to test configuration. Reboot, logout, shutdown, rootful conversion, engine installation, opening a socket, changing firewall rules and stress tests are separately authorized rehearsal actions. Build the disposable test lane first.

## Quadlet-specific guardrails

Use the installed manual to confirm source paths and supported keys. Rootless Quadlets live under the user’s generator search paths; their generated services are not conventional persistent units to enable directly. Verify cgroup v2 and native systemd rather than adding legacy WSL init shims reflexively. [S015]

Model three separate lifetimes: **container service**, **Linux user/system manager**, and **WSL/Windows host**. A healthy service inside a stopped host is unavailable. Linger changes the user-manager lifecycle, not the Windows host’s power or WSL lifetime. [S014; design implication]
