# Historical write payload — unverified

Recovered from 9c31e321-a8ca-4154-8691-333247a694ec message 35. Do not adopt its recommendations without the v0.2 audit.

# Portability / Migration Substrates Audit

**Date:** 2026-09-11  
**Scope:** Candid evaluation of substrates enabling stateful/process workloads to move local<->managed when containers are insufficient.  
**Baseline Assumption:** `podman+quadlet` is the default/local substrate for OCI containers.  
**Goal:** Recommend a single escape hatch to standardize for workloads that container+Podman cannot carry.

---

## (A) Tiny Kubernetes on WSL2 (k3s, k0s, k3d, MicroK8s)

**Fitness for single-node dev parity + managed prod:**  
- **k3s:** Designed for edge/IoT; single binary (<100m), embedded SQLite, simple HA with external datastore. Runs natively on Windows via k3s.exe or inside WSL2. Dev/prod parity excellent if you accept the k3s-specific defaults (flannel, local-path, traefik).  
- **k0s:** Zero-friction, single-binary, CNCF-certified K8s. Installs controller+worker in one command (`sudo k0s install controller --single && sudo k0s start`). Works on WSL2; identical binary for dev and prod.  
- **k3d:** Runs k3s inside Docker; primarily for CI/testing. Adds a Docker layer, so node startup slower and image pulling nested. Less ideal for long-running dev parity but useful for disposable clusters.  
- **MicroK8s:** Canonical’s Ubuntu‑focused K8s; snap delivers all services (etcd, apiserver, etc.) as a single snap. Officially supports WSL2 via `multipass` or direct install in WSL2 Linux distro. Provides addons (DNS, storage, ingress) with `microk8s enable`.  

**Maturity:** All are production‑used; k0s and k3s have the strongest single‑binary story. MicroK8s benefits from Ubuntu LTS backing.  
**Learning cost:** Low‑medium. You must learn basic K8s concepts (pods, services, storage classes) but the distributions hide much of the ops complexity.  

**Verdict:** For a single‑node dev cluster that mirrors a managed K8s (EKS, AKS, GKE) as closely as possible, **k0s** or **k3s** inside WSL2 is justified when you need the full K8s API (CRDs, operators, Helm) and cannot express the workload as a plain container. Overkill if you only need process isolation; then podman+quadlet wins.

---

## (B) WASM Edge Runtimes (Wasmtime, Spin by Fermyon)

**Fitness:**  
- **Wasmtime:** Stand‑alone, secure WASI runtime. Executes `.wasm` modules compiled from any language targeting WASI. Ideal for plug‑in systems, serverless functions, or edge workers where you want sandboxed, fast startup (<1ms) and deterministic execution.  
- **Spin:** Framework for building WASM‑based serverless apps (HTTP listeners, databases, key/value stores, etc.) using Wasmtime under the hood. Provides a batteries‑included model (routing, state, outbound HTTP) via `spin new` templates.  

**Dev parity + managed prod:**  
- **Local:** `wasmtime` or `spin` CLI runs instantly on Windows, macOS, Linux.  
- **Managed:** Fermyon Cloud (Spin), Cloudflare Workers WASM, or any WASI‑compatible host (e.g., Netlify Edge, Vercel Edge Functions via wasm‑edge).  

**Maturity:** Wasmtime is a Bytecode Alliance project; used in production by Fastly, Shopify, etc. Spin v2 is stable; v3 (as of 2026) adds native async/await and richer outbound bindings.  
**Learning cost:** Medium. You must learn WASI interfaces and possibly the Spin manifest (`spin.toml`) and component model. However, the model is simpler than learning a full container orchestrator.

**Verdict:** Excellent for workloads that can be expressed as a single WASI module (or a small graph of modules) and require sub‑second startup, strong isolation, and low resource overhead. Not a fit for legacy syscall‑heavy apps or where you need dynamic native linking.

---

## (C) Nix / NixOS / home-manager

**Fitness:**  
- **Nix:** Purely functional package manager; builds packages in isolation, enabling reproducible dev shells (`nix develop`) and declarative deployments.  
- **NixOS:** Linux distribution where the entire OS is declared in `/etc/nixos/configuration.nix`. Rollbacks and atomic upgrades are built‑in.  
- **home-manager:** User‑level dotfiles and CLI tools management using the same Nix language.  

**Dev parity + managed prod:**  
- **Local:** `nix develop .#my-shell` gives you an identical dev environment on any machine (macOS, Linux, WSL2).  
- **Managed:** Deploy the same NixOS configuration to bare metal, VMs, or cloud instances (via `nixos-rebuild` or Terraform/NixOps).  

**Maturity:** Nix is 20+ years old; NixOS has a loyal following. The Flakes experiment (now stabilized) improved reproducibility and composition.  
**Learning cost:** **High.** The Nix language is purely functional and lazy; debugging builds requires understanding of stdenv, builders, and overlays. However, the payoff is true “works on my machine” guarantees.

**Verdict:** Choose Nix when you need bit‑for‑bit reproducible builds and runtime environments across the entire stack (OS, packages, configuration). Overkill if you only need container portability; but invaluable for escaping “works on my machine” hell in heterogeneous teams.

---

## (D) Unikernels / NanoVM‑style Migration

**Fitness:**  
- **Unikernels:** Compile an application with only the necessary OS libraries into a single‑address‑space image that runs directly on a hypervisor (KVM, Xen). Examples: IncludeOS, Rumprun, and the Linux‑based UniKraft.  
- **NanoVMs (Ops):** Packages a traditional Linux ELF binary into a lightweight VM image (using KVM) that boots in ~100 ms and runs with near‑bare‑metal performance. No container layer; the VM *is* the sandbox.  

**Dev parity + managed prod:**  
- **Local:** Build the image with `ops` (NanoVMs) or `unikraft` CLI; run via QEMU/KVM or Hyper‑V on Windows.  
- **Managed:** Cloud providers offering bare metal or dedicated hosts (e.g., Equinix Metal, Hetzner) can run your VM images; some offer “VM‑as‑a‑service” APIs.  

**Maturity:** Unikernels are research‑grade but gaining traction in niche workloads (network functions, security appliances). NanoVMs/Ops is commercial but offers a free tier; used in production for edge functions and legacy app lift‑and‑shift.  
**Learning cost:** Medium‑high. You must learn the tooling (`ops build -t linux -p <binary>`) and understand VM‑specific networking (TAP vs. vhost‑user) and persistent storage (virtio‑blk, 9p).

**Verdict:** Only consider when a container cannot capture the syscall surface or device access you need (e.g., raw NIC, custom kernel modules, or legacy init systems). Provides stronger isolation than containers (hardware‑level) while retaining near‑native performance. Overhead: one VM per app (~10–50 MB RAM).

---

## (E) Fly.io Machines / Fly launch

**Fitness:**  
- **Fly Machines:** Low‑level API to launch and manage Firecracker VMs (or lightweight containers) on Fly’s global hardware. You define a Machine via `fly machines launch` or a `fly.toml` with `[[]]` sections. Machines can run any OCI image *or* a raw kernel/initrd.  
- **Fly launch:** CLI tool that builds a Dockerfile, pushes to Fly’s registry, and creates a Machine (or Apps v2 service) in one command.  

**Dev parity + managed prod:**  
- **Local:** `flyctl` runs on Windows/macOS/Linux; you can test locally with `flyctl ssh console` or run a Machine in `--local-mode` (experimental).  
- **Managed:** Fly’s platform handles global load‑balancing, automatic snapshots, and regional placement.  

**Maturity:** Fly.io has been serving production workloads since 2019; Machines launched in 2022 as the next‑gen evolution beyond Heroku‑style slugs.  
**Learning cost:** Low‑medium if you already know Docker and basic networking. The Fly CLI abstracts much of the VM/placement complexity.

**Verdict:** Excellent choice if you want a managed global platform that runs containers *or* VMs with near‑zero config drift between local `fly launch` and production. Ideal for teams that value simplicity over multi‑cloud portability.

---

## Recommendation & Escape Hatch

**Default substrate:** `podman+quadlet` remains the pragmatic baseline for OCI container workloads (dev and prod match via identical quadlet files or systemd units).  

**One escape hatch to standardize:** **WASI + Spin (Fermyon)**  

### Why WASI/Spin as the single escape hatch?
1. **True portability:** A single `.wasm` module compiled to WASI runs unchanged on Linux, Windows, macOS, and inside any WASI‑compatible host (Cloudflare Workers, Fermyon Cloud, Netlify Edge, Wasmtime‑based serverless platforms).  
2. **Process‑level workloads:** WASI provides sandboxed access to files, sockets, clocks, and randomness—enough for many stateful daemons, sidecars, and CLI‑style utilities without needing a full OS.  
3. **Minimal learning cost:** Compared to learning a full K8s distro or Nix language, the WASI toolchain (`cargo build --target wasm32-wasi`, `spin new`) is approachable for most developers.  
4. **Immutable & reproducible:** The WASM binary is a pure artifact; dependencies are baked in at compile time, eliminating “works on my machine” issues.  
5. **Managed options abound:** You can run the same binary locally with `wasmtime` or deploy to Fermyon Cloud, Cloudflare Workers, or any WASI host with confidence of identical behavior.  

### When to reach for something else?
- **You need the full Kubernetes API** (operators, CRDs, Helm) → use **k0s** or **k3s** inside WSL2.  
- **You require bit‑for‑bit OS reproducibility** → adopt **Nix**/`home-manager`.  
- **You cannot express the workload as a WASI module** (needs raw device access, legacy syscalls, or PID 1 semantics) → consider **NanoVMs/Ops** or a **unikernel**.  
- **You want a globally distributed PaaS with built‑in DB/KV** → **Fly.io Machines** is a strong alternative to WASI‑only platforms.

---

## Conclusion
For most workloads that escape the container model but still need strong dev/prod parity and low operational overhead, **standardizing on WASI + Spin** provides the best balance of portability, maturity, and learning efficiency. Treat `podman+quadlet` as the default for containers, and reach for WASI/Spin when you need a lighter, faster, and more portable sandbox than a VM or K8s node.