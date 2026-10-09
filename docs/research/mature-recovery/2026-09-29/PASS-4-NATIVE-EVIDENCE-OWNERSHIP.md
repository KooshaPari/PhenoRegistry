# Pass 4 — native evidence and BytePort/NanoVMS ownership split

Date: 2026-09-29. Scope remains ShareCLI + BytePort; NanoVMS is inspected only as a materially depended-on boundary, not a third recovery program.

## BytePort BP-F03 native result

Exact candidate `934b0456de5509b5e89294c3adaa046e632a2767`, Go-test job `109572633061`, executed the adversarial handler test and failed:

- ProjectID: `project-123`
- persisted provider runtime ID: `provider-sandbox-777`
- actual stop target: `project-123`
- expected provider target: `provider-sandbox-777`

Classification: **NATIVE COUNTEREXAMPLE REPRODUCED**.

This upgrades BP-F03 from source finding to exact-candidate runtime evidence. It does not select the remediation architecture.

## ShareCLI SC-F01 native status

The first exact candidate attempt failed before the oracle because Linux tray compilation was unrelatedly broken. The first isolated sharecli-core workflow also failed before test execution because `spawn-core-sys` invokes Zig and the isolated workflow did not provision it.

Both are **INFRASTRUCTURE-BLOCKED / ORACLE NOT EXECUTED**. Neither counts for or against SC-F01.

The branch now contains an oracle workflow with the repository's pinned Zig 0.14.1 setup. A new exact run is pending. This is an environment repair only; product behavior and test semantics are unchanged.

## BytePort ↔ NanoVMS ownership evidence

Registry source `85d7cd00cf59c379c05b740e8130a85b0d5bd31b` provides two useful but authority-qualified boundaries.

### NanoVMS boundary

`docs/boundary/nanovms.md` says its domain is native sandbox/VMM isolation:
- WASM/gVisor/Firecracker tiers;
- sandbox adapters;
- libkrun;
- pure-data SandboxConfig/runtime domain;
- high-level orchestration is out of scope;
- cloud VMM provisioning is out of scope.

Its intent file is largely uncurated and therefore not strong user-intent evidence. The boundary itself comes from a Forge/audit session and must not be treated as direct user intent, but it is consistent with the actual BytePort integration shape inspected so far.

### BytePort boundary

The September BytePort boundary says native sandboxing lives in NanoVMS. However the same document also claims backend healthz/presign routes and other surfaces already contradicted by the mounted current router. It is therefore **supporting/generated boundary evidence, not implementation truth or automatic mature authority**.

The cross-boundary statement that BytePort does not own native sandbox implementation is nevertheless consistent with:
- the mature deployment/productization charter;
- current BytePort calling an external NanoVMS sandbox API;
- NanoVMS's own sandbox-focused boundary.

## Architecture consequence

BytePort should not expect NanoVMS to magically solve SourceSnapshot → ManifestRevision → BuildArtifact unless its actual API proves such a source-build contract. Current evidence instead points to NanoVMS as a **runtime/sandbox provider adapter**.

Therefore BytePort's architecture decision narrows from three equally plausible source-build options:

- A: BytePort owns build orchestration;
- B: BytePort delegates build to an established build/CI engine and consumes immutable artifact identity;
- C: NanoVMS/provider owns source build.

to:

- **A/B remain plausible**;
- **C is currently unsupported by evidence and should be rejected unless direct NanoVMS API/source inspection falsifies this conclusion.**

Given the existence-gate pressure from established build/deployment systems, B is the stronger bootstrap candidate: BytePort owns project/source/manifest/deployment/evidence semantics while composing a build engine and treating NanoVMS as one runtime target.

This is a research recommendation, not an accepted architecture freeze.

## New crash-window probe

BytePort branch now contains an observational native probe that:
1. allows provider deploy to succeed;
2. injects local DB persistence failure;
3. verifies the handler surfaces server error;
4. observes whether a provider stop/compensation occurred.

A PASS of this probe means the unsafe remote-side-effect window was reproduced; it is deliberately not a desired-behavior acceptance test because the final recovery mechanism (journal/reconcile/adopt/compensate) has not yet been selected.

## Gate delta

- BP-F03: NATIVE REPRODUCED.
- BP-F04: native observational probe committed; execution pending.
- BytePort source-build ownership: materially narrowed; provider-owned source build unsupported so far.
- SC-F01: still native UNKNOWN; second infrastructure repair in place, exact rerun pending.
- Architecture freeze: still blocked.
