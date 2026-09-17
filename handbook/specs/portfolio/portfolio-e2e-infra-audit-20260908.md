# Portfolio E2E OCI/runtime infrastructure audit

Date: 2026-09-07 Pacific / 2026-09-08 UTC
Scope: read-only inspection of `repos/nanovms` plus local runtime availability. No runtime was started, stopped, installed, or modified.

## Executive finding

NanoVMS has source-level support for Podman, Apple's `container` CLI, and a WSL Containers backend, while legacy Docker and Docker-dependent gVisor tiers remain in the tree. On this macOS arm64 host, Colima's Docker runtime is verified working; Podman is installed but its machine/socket is unavailable; Apple's CLI is installed but its API server is stopped; and no WSL Containers executable is available. The Windows/WSLC contract is ambiguous and must be resolved before Docker removal.

## Runtime evidence (2026-09-07 18:07 PDT)

| Capability | Command/evidence | Result | Status |
|---|---|---|---|
| Podman binary/engine | `podman version`; `podman machine list` | Podman 6.1.1 on PATH; machine list empty; version cannot connect to `podman.sock` | `PARTIAL: binary only` |
| Apple Containers | `container system version`; `container system status`; `container system --help` | CLI 1.0.0; `apiserver is not running and not registered with launchd`; lifecycle commands are present | `PARTIAL: CLI, service down` |
| Colima/Docker | `colima status`; `docker version` | Colima running with QEMU, Docker runtime, arm64; Docker client 29.4.1/server 29.2.1, API 1.53 | `VERIFIED` |
| WSL Containers | `command -v wslc`, `command -v container.exe`, `wslc --version`, `container.exe --version` | Neither executable was found/invocable on this macOS host | `UNKNOWN/UNVERIFIED` |

The successful Docker result verifies the local Docker-compatible path through Colima only. It does not prove Podman, Apple Containers, or Windows WSL Containers parity.

## Static source support and gaps

- `nanovms/pkg/runtime/probe.go:63-72` maps Podman to `podman`, Apple Containers to `container`, and WSL Containers to candidates `container.exe` then legacy `wslc.exe`. Probe availability is executable/version discovery, not a lifecycle or image/run proof (`:75-106`).
- `nanovms/internal/adapters/containers/containers.go:67-90` defaults Apple to `container` and WSL to `wslc.exe`, with `NVMS_WSLC_BINARY` override. This conflicts with the runtime probe's preferred `container.exe` candidate and leaves the shipped Windows name unresolved.
- The native adapter uses Apple `system version --format json` (`:106-127`) and native create/start/stop/delete operations. Tests cover fake command dialects, but no host-level Apple service was exercised in this audit.
- `nanovms/pkg/tier/podman.go` and `internal/adapters/podman/podman.go` use Podman CLI lifecycle operations. The former probe uses `podman ps --all`; the latter uses `podman version`; neither can pass on the observed stopped/no-machine state.
- `nanovms/pkg/tier/docker.go:41-93` is a direct Docker CLI/daemon adapter. `pkg/tier/gvisordocker.go:43-97` explicitly requires Docker plus `runsc`; these are migration blockers if Docker is removed.
- `nanovms/docs/guides/quickstart.md:72-86` calls Podman supported, says Docker is not required, and calls Windows `wslc` plus macOS `container` capability-gated. The Windows source and probe naming do not yet make that claim reproducible.
- `nanovms/internal/adapters/windows/windows.go` detects `wsl.exe`, `hvlaunch.exe`, and `cloud-hypervisor.exe`; it does not detect or invoke `container.exe`/`wslc.exe`. Thus “WSL tier” and “WSL Containers CLI” are separate concepts in source and should not be treated as equivalent.

## Consumer/capability gaps

1. A common OCI capability contract is missing: image pull/create/start/stop/delete, inspect, logs, exec, networks, volumes, environment, mounts, and exit/status semantics need an adapter-level parity matrix.
2. Runtime discovery can report an executable as available even when its service/API is down. Add a bounded, non-mutating capability probe and distinguish `binary`, `service`, and `lifecycle` readiness.
3. Podman macOS requires an active VM/machine; the current host shows none. Apple Containers requires its API server; the current host shows it stopped.
4. Docker-dependent gVisor and distroless tiers have no demonstrated Podman/Apple/WSLC replacement. They must be isolated or ported before removing Docker.
5. Windows support is underspecified: source defaults to `wslc.exe`, generic probe prefers `container.exe`, docs say `wslc`, and the Windows adapter only detects `wsl.exe`.

## Docker CLI/API removal plan

1. Inventory every direct Docker invocation and API assumption, including `docker.go`, `gvisordocker.go`, `distroless.go`, docs, scripts, CI, and downstream PhenoCompose callers. Classify each by required OCI capability.
2. Define a versioned provider contract and conformance suite. Run the same fixture matrix against Podman, Apple Containers, and the resolved Windows provider; require create/start/inspect/logs/exec/stop/delete plus failure and cleanup behavior.
3. Implement provider-neutral orchestration and route non-Docker workloads through native adapters. Keep Docker as an explicitly selected compatibility provider during migration.
4. Resolve gVisor: either a native non-Docker runsc/containerd path with equivalent security proof, or retain `gvisordocker` as a documented compatibility tier. Do not silently map it to plain OCI execution.
5. Gate removal on: all consumers migrated; conformance green on Linux Podman, macOS Apple Containers, and Windows provider; image, volume, network, rootless, logging, and exit-code parity; CI and dogfood evidence; and a published rollback switch.

### Rollback

Keep the Docker provider, tier registrations, and configuration flag in the release immediately preceding removal. If a parity gate regresses, restore provider selection to Docker without changing workload manifests, retain captured IDs/logs for diagnosis, and reverse only after the failing capability has a passing fixture. No forceful runtime cleanup is part of rollback.

## Windows ambiguity decision gate

Before claiming WSLC support, obtain authoritative Windows evidence for the shipped executable and command grammar. Decide one canonical name (`container.exe` or `wslc.exe`), update `DefaultBinaryProbe`, `NewWSLAdapter`, docs, and Windows adapter detection together, then run the provider conformance suite on Windows. Until then, mark WSL Containers `UNKNOWN`, not available.

## Recommended next gates

- Start no runtime as part of this audit. Earlier sponsor authorization already covers Podman setup and migration direction; a later bounded implementation pass should use that authorization without asking again, while retaining current audit-only mode until that pass begins.
- Add read-only service/lifecycle probes and capability-specific readiness states.
- Resolve the Windows naming/ownership contract with a Windows-host verification.
- Produce the provider parity matrix before deleting Docker code or changing defaults.

