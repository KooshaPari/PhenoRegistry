# Alternatives, existence and bootstrap decision ledger

Date: 2026-09-29. Source anchors: research passes and SNAPSHOTS.json. **All product-existence decisions remain OPEN.** These are serious candidate stacks, not claims that integrations have been built or that a winner is known.

## Repository absent counterfactuals

**HeliosLite absent:** start with pinned upstream Forgecode for provider-configured terminal/one-shot work; retain repository/workspace state and a separately controlled accepted-task/evidence adapter. Evaluate Codex App Server as the strongest alternate worker interface where its provider/access and native-platform constraints fit. Do not add a generic orchestration framework unless a required durable-effort behavior cannot be provided by a thin adapter plus persistent storage. Needed comparison: retained fork-specific behavior, headless ergonomics, provider history fidelity, performance, platform support, recovery and patch-maintenance burden.

**KCode absent:** start with pinned upstream jcode and its supported client/runtime stack, with explicit artifact/daemon identity and independent task qualification. Challenge it with a Codex App Server based worker and compare OpenHands SDK only where a real framework rather than a harness client is required. Needed comparison: owned fork's actual behavioral fixes, installed-runtime custody, native Windows/macOS behavior, resource efficiency, SDK consumer fit and maintenance cost.

These substitute products are not assumed to have flawless graders, persistence or security. Apply the same negative controls to alternatives and status quo. No baseline is weakened to make the owned fork win. Exact deployment/provider configuration, reproducible artifacts, pricing/authorization and integration cost remain unresolved before declaring a best stack.

## Differentiation ledger

| Claim | Disposition | Reason / falsification test |
|---|---|---|
| Coding CLI, one-shot use, tools, provider setup | Commodity/contested | Upstream Forgecode and jcode already describe core surfaces; prove a distinct accepted fork obligation |
| Client-agent RPC and session loading | Commodity/contested | Codex/ACP provide relevant prior art; capability negotiation and supported semantics must be tested |
| Generic persistence or agent SDK | Commodity/contested | LangGraph/OpenHands are concrete alternatives, but not automatic fits |
| HeliosLite wins on headless efficiency | Unverified differentiation | User preference/historical interpretation, not a matched measurement at current sources |
| KCode wins on memory or intelligence | Unverified differentiation | README superlatives/configuration-sensitive table do not establish a controlled result |
| Generic sessions/tools are uniquely ours | Falsified as a generic uniqueness claim | Direct upstream/protocol evidence contradicts uniqueness; no assertion the user made this claim |
| Faithful native Windows/POSIX behavior with Pine integration | Candidate differentiation | Accepted user pain/home; actual implementation and baseline advantage unproven |
| Independent outcome/identity fidelity across replaceable workers and fork versions | Candidate differentiation | Matches accepted mission; requires real end-to-end evidence, not merely a wrapper |
| Integration with retained shared capabilities at low maintenance burden | Candidate differentiation | SDK source custody, consumers and cost still unresolved |

## Bootstrap decisions — initial pass, not approved implementation ADRs

| Subsystem | Options actively considered | Current disposition | Closure experiment / cost question |
|---|---|---|---|
| Coding worker host | Use upstream; retain minimal fork; alternate Codex host; build custom | EVALUATE use/fork; reject an automatic fourth combined fork | Same task/provider and failure matrix; cost of retained behavioral patch set |
| Client/agent boundary | ACP adapter; native API; custom protocol | Prefer integrate/adapt existing semantics; not final | Capability negotiation, resume/cancel, protocol skew, unsupported methods |
| Tool/context boundary | MCP library versus custom wire layer | Prefer maintained library; explicit security integration still required | Untrusted annotations, denied calls, reconnect, credential scope and failure propagation |
| Durable execution/state | Existing storage; LangGraph/OpenHands primitives; custom state engine | Compare composition before custom engine | Crash before/after effect, replay/deduplication, migration and retention; no external-effect exactly-once claim without proof |
| SDK boundary | Harness client API; existing framework; recovered Agentora capability | Source/custody and semantics first | Consumer E2E and API compatibility; zero-to-N granularity versus total integration burden |
| Outcome grader | Adapt maintained eval tooling; small deterministic subject-specific oracle; generic platform | Preserve independent policy and add minimum task-specific semantics | Empty/skipped/wrong-candidate controls, mutation witnesses, immutable history and policy-change attack |
| Build/runtime provenance | SLSA-compatible metadata plus live-process identity | Integrate rather than invent supply-chain format | Wrong binary/daemon, mutated signature, stale attestation, verifier compromise boundary |
| Native shell compatibility | Existing Pine boundary, native process APIs, library reuse | Investigate as bounded consumer integration; no new repo | Quoting/path/env/PTY/cancel/process-tree parity on supported Windows and POSIX profiles |
| UI/mobile breadth | Existing terminal/app surfaces; thin projections; new UI | Defer breadth until a real spine closes | Installed actor-to-outcome journey, accessibility, actual routing and evidence |

Every row still needs exact selected library versions, source inspection, licensing/project health, failure semantics and measured integration/operating burden. No dates or arbitrary cost estimates are invented.

## Separate post-build pilot

After a defensible stage is built, compare owned product, best validated alternative stack and status quo/product absent using matched task sets and configurations. Measure correctness, human intervention, total time/cost, regressions, false greens, recovery, trace completeness, user burden and maintenance. That later pilot cannot substitute for the pre-build existence/architecture gate.
