# Pass 3C — ShareCLI mediation reach and BytePort implementation-fiction map

Date: 2026-09-29.

## ShareCLI: observation and mediation are architecturally separate

Direct inspection of `crates/harness-native/Cargo.toml` and `src/dispatcher.rs` resolves an important ambiguity.

The native dispatcher binary is named **`helios-shield`**, feature-gated as a Unix dispatcher. Its own source says proxy mode is invoked through symlinks such as `proxy/ruff -> helios-shield`. It resolves the real binary, determines whether the caller is an agent, and only then applies configured strategies such as coalesce/queue/retry. Human and passthrough paths exec the real binary.

Therefore:
- FR-006 process scanning can satisfy **observation without vendor-binary replacement**.
- Hypervisor/harness optimization of an arbitrary vendor command is **not automatically reached merely because the agent process was detected**.
- The recovered optimization path can require explicit proxy/symlink interception or another caller that invokes Hypervisor.
- “No wrapping as the primary detection path” and “some optimization paths use a proxy dispatcher” are compatible statements.

This materially narrows the mature architecture question. ShareCLI needs an explicit capability matrix:
`observed | supervised | mediated | filesystem-intercepted | optimization-eligible`
per workload/tool/platform. It must not show an observed process as mediated or safely coalesced.

It also increases the attractiveness of adapter-based optimization: a proxy for a known tool can select a tool-specific equivalence adapter; unrelated observed agents can remain monitor/control-only.

## BytePort: documented journeys contain implementation fiction

Search of the frozen tree for the J3 portfolio implementation named in `USER_JOURNEYS.md` found no `frontend/web/src/routes/p/[slug]/+page.svelte`, no `backend/byteport/lib/llm.go`, and no concrete portfolio-template generator symbol. Portfolio terms survive primarily in governance/spec/security/history and settings integration surfaces.

Likewise the journey says the backend validates `odin.nvms` and a local `backend/nvms` performs Git/AWS deployment, while the currently mounted handler translates the request directly to a NanoVMS SandboxConfig with `alpine:latest`.

Classification:
- J1/J3 journey text = **accepted/supporting intended journey candidate**, not current implementation fact.
- named missing paths = **historical/proposal/implementation-fiction until source/history proves otherwise**.
- current wire-contract tests = **provider protocol tests**, not J1 selected-application acceptance.

This is exactly why current implementation mapping follows mature contract recovery rather than deriving requirements from route/test names.
