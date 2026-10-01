# Harness family capability-lineage matrix — pass 1

Date: 2026-10-01. This is a semantic convergence matrix, not a winner scorecard.

| Capability / concern | HeliosCLI/Codex lineage | KCode/jcode lineage | HeliosLite/Forgecode donor | Mature destination hypothesis | Evidence status / next falsifier |
|---|---|---|---|---|---|
| Interactive coding CLI/TUI | Historical HeliosCLI UX donor; modern Codex is active and substantially evolved; owned vendored Codex is unmounted | jcode is active and user generally prefers it for most use | lighter CLI donor | Client adapter(s), possibly one canonical CLI or segmented Codex/jcode clients | Need matched current Codex/jcode journey comparison |
| Headless/ephemeral light chat | Root HeliosCLI has Ask/Exec but not modern Codex parity | jcode likely capable but heavier role must be measured | strongest historical preference for light/headless use | Thin client profile over shared harness unless Forgecode has irreducible advantage | Benchmark startup/RSS/TTFT/operational complexity |
| Generic agent kernel | Root HeliosCLI harness is prototype/scaffold; not sufficient | KCode/jcode contains richer agent/runtime semantics but client-coupled areas remain | donor ideas only | Shared Agentora/PhenoShared/Freyr-derived kernel | Audit Agentora absorption + external SOTA |
| Durable development effort | Helios root checkpointing is run/file oriented; old architecture intentionally stateless | KCode transcript persistence strong, but effort/effect authority separate | not canonical | Shared durable-effort/orchestration layer | Specify authority/event model; implementation experiment later |
| Worker attempt lifecycle | Prototype agents/tasks in Helios root | richer runtime/session/daemon primitives | donor | Shared harness kernel + scheduler | Complete lifecycle ontology/oracles |
| External-effect reconciliation | HeliosLite donor primitive qualified but unmounted; HeliosCLI not yet mapped | KCode primitive qualified/reachability open | qualified donor primitive | Shared durable-effort policy with client/runtime hooks | Non-code contract mostly defined; real consumer remains implementation blocker |
| Provider/model abstraction | Root Helios AI supports OpenAI-compatible endpoint; modern Codex active | jcode/KCode broad provider/runtime direction; ForgeCode adapter candidate | broad model support donor | Shared provider capability interface + client policy | Research capability negotiation/routing |
| Tool runtime | Root Helios tools/harness need mapping | jcode has registry/tool context and mature surfaces | Forgecode tool executor donor | Shared typed capability/tool runtime | Compare MCP/A2A/tool semantics and failure models |
| MCP/interoperability | README Codex claims cannot count unless root mounts them | jcode has relevant external/provider/tool surfaces | donor | Shared interop adapters | Exact mounted-interface audit |
| Context/compaction/memory | root harness incomplete | KCode has substantive but upstream-overlapping cache/compaction/memory work | donor | Shared context/memory subsystem with client projections | Semantic upstream comparison + research |
| Multi-agent orchestration | RootManager is prototype synthetic success | jcode/KCode not accepted as canonical generic orchestrator | Forgecode donor only | Shared orchestration layer | SOTA workflow/multi-agent research; ontology |
| Scheduling/scaling | Helios has named harness_scaling/queue crates; semantics unverified | jcode runtime concurrency useful donor | lightweight runtime donor | Shared scheduler/fleet runtime | Inspect implementation + benchmark workload |
| Sandbox/workspace | Helios root has helios-sandbox; modern Codex strong active reference | jcode/KCode has runtime/tool workspace semantics | donor | Shared environment runtime with client adapters | Compare security/failure/isolation guarantees |
| Approvals/policy/IAM | Helios Exec has approval enum but generic policy layer unproven | jcode permission system richer; owned permission work overlaps upstream | donor | Shared policy/approval/IAM layer | Research policy engines and exact authority |
| Evidence/grading/MACE | harness_verify/spec names exist but maturity unproven | recovery evidence primitives added; no canonical grader | donor | Shared evidence/grader layer | Complete rubric/version/evidence schema |
| Event streaming/projections | root interface pubsub generic and insufficient | jcode daemon/protocol is strong donor | Forgecode streaming donor | Shared versioned event/projection API | Compare event identity/backpressure/replay |
| Observability/replay | tracing present; OTel/Prometheus not wired per architecture | jcode runtime identity/evidence improvements | donor | Shared observability/evidence substrate | SOTA tracing/replay research |
| GUI-native workbench | not HeliosCLI responsibility | not KCode responsibility | not HeliosLite responsibility | HeliosLab client over shared harness | Define GUI projection contracts, not terminal scraping |
| Windows/POSIX compatibility | old Helios/Codex history relevant | KCode/jcode relevant | Forgecode Windows donor | Pine/shared environment adapter where still needed | Current upstream comparison |
| Release/runtime identity | HeliosCLI release provenance not yet mapped | KCode daemon identity qualified; macOS policy primitive qualified | donor | Per-client release + shared evidence identity contract | Helios release audit; KCode signed-release experiment |
| Plugin/extensibility | Helios root pheno-plugin/plugin-arch present; reachability unknown | jcode external provider architecture promising | donor | Shared extension contract where generic; client plugins where presentation-specific | Audit consumers and compatibility |
| Client-independent API/SDK | historical goal, root interfaces inadequate | jcode daemon/protocol donor | headless donor | Shared SDK/API as first-class surface | Agentora/PhenoShared audit |
| Control plane/fleet | no mature evidence yet | no accepted canonical implementation | none | Separate control-plane layer | Research OpenHands/production factory systems |
| Non-coding agents | current implementations coding-biased | current implementations coding-biased | coding/chat biased | Generic harness must support falsification workloads | Define non-coding case suite before ontology freeze |

## Current topology hypotheses to test

A. **Converged client:** one canonical CLI over shared harness, absorbing best Codex+jcode interaction/runtime semantics.
B. **Segmented clients:** Codex-lineage and jcode-lineage clients survive because stable roles differ, while sharing the same kernel/runtime contracts.
C. **jcode-primary + Codex contribution/reference:** jcode client wins most local roles; Codex remains upstream/contribution/reference and perhaps a distinct OpenAI-native client.
D. **Codex-primary + jcode runtime donors:** inverse of C.
E. **Light third profile without HeliosLite product:** ephemeral/headless profile is configuration/build profile of shared harness/client rather than maintained Forgecode fork.

No hypothesis is accepted yet. HeliosLite surviving as a standalone third primary product is not a default hypothesis.
