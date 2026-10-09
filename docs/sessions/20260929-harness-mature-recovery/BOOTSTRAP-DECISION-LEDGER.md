# Bootstrap decision ledger — generic harness pass 1

| Primitive | Candidate prior art | Current disposition | Why not custom yet? | Custom trigger |
|---|---|---|---|---|
| Multi-client coding harness projection | modern Codex core + App Server | LEARN / potentially EXTEND | already powers multiple clients with bidirectional typed-ish event protocol | missing generic/non-Codex semantics or unacceptable coupling |
| Durable execution | Temporal; Microsoft Durable Task | EVALUATE / INTEGRATE backend | mature crash recovery, event history/checkpointing, workers, HITL, scaling | measured latency/footprint/semantic/provenance/ops gap |
| Agent runtime local/distributed | AutoGen Core | LEARN / EVALUATE | common APIs across standalone/distributed runtime, identity/lifecycle/message routing | coding/durability/QoS semantics cannot fit without distortion |
| Agent programming core | OpenAI Agents SDK; Microsoft Agent Framework; OpenHands SDK | LEARN / ADAPT | established agent/tool/handoff/session/workflow abstractions | generic contract needs stronger evidence/authority/runtime semantics |
| Coding ACI | Codex; jcode; SWE-agent/OpenHands | COMPOSE / EXPERIMENT | ACI strongly affects outcomes; existing mature tools | unique required interaction unsupported |
| Sandbox/workspace | Codex/jcode/OpenHands/Google Agent Runtime and OS primitives | COMPOSE | substantial isolation/runtime work exists | unsupported local/native/latency semantics |
| Provider routing | jcode external provider architecture + existing SDKs | EXTEND/ADAPT | active upstream and adapters | capability model cannot express required providers |
| Client UI | HeliosLab + modern Codex app-server lessons | BUILD PRODUCT CLIENT | GUI-native UX is actual product differentiation | N/A; reuse protocol/components where sensible |
| Evidence/MACE | evaluation frameworks + tracing systems | CUSTOM CONTRACT, reuse collectors | product-specific authority/evidence identity not supplied end-to-end by one framework | already triggered by recovery requirements |
| Scheduler/QoS/fleet | Temporal task queues, Durable Task, AutoGen distributed, existing infra schedulers | EVALUATE/COMPOSE | avoid bespoke distributed scheduler before measurements | extreme concurrency/local packing requirements exceed candidates |
| Generic plugin/capability system | MCP, provider/tool plugin ecosystems | ADAPT/COMPOSE | interoperability exists | need typed semantics/versioning absent externally |
| Shared harness implementation | Agentora/PhenoShared descendants | AUDIT BEFORE BUILD | may already contain intended obligations | audit proves absent/inadequate |

Disposition is provisional until licensing, health, performance, semantic fidelity and integration cost are recorded.