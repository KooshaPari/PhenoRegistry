# Capability lineage and mature destination matrix — pass 1

| Capability | Historical donor | Current stronger candidate | Mature destination hypothesis | Status |
|---|---|---|---|---|
| Interactive coding TUI/UX | HeliosCLI/Codex lineage | modern Codex; jcode also strong | client-specific Codex/jcode adapters; preserve best UX | compare |
| Fast native/light headless | Forgecode/HeliosLite | jcode; Codex exec | client mode/adapter; standalone Forgecode only if measured niche survives | likely sunset |
| Multi-provider subscriptions/models | KCode/jcode | current jcode | jcode adapter + provider port | likely upstream |
| App/IDE/GUI protocol | modern Codex app-server | current Codex | Codex adapter informs EventProjection/ClientAdapter; do not copy wholesale | research |
| Server-owned sessions/multi-client | jcode | current jcode | SessionPort/client projection adapter | research |
| Generic agent lifecycle | Agentora intent | OpenAI Agents SDK/MS Agent Framework + recovered Agentora | shared Agent Kernel | design |
| Durable effort/workflow | historical Agentora/checkpoint ideas | Temporal/Durable Task/MS AF patterns | DurableExecutionPort + canonical DurableEffort schema | design |
| External-effect recovery | KCode/HeliosLite recovery research | shared contract | shared harness effect ledger/reconciler | accepted contract |
| Resource scheduling | old harness_scaling/queue ideas | Ray/K8s/custom schedulers | SchedulerPort; external substrate | research |
| Queue/cache | Helios root harness | Tokio/runtime/cache libs | commodity dependency; retire custom unless benchmarked need | likely replace |
| Process execution | Helios runner; Codex exec-server; jcode tools | Codex exec-server/jcode/Pine/runtime adapters | Workspace/ToolRuntime port | compare |
| Sandbox | Codex/KCode/Helios root | current Codex + platform substrate | Workspace/Policy adapters | compare |
| Approval/policy | Codex UX; KCode permissions; Agentora intent | modern Codex/jcode + policy stack | shared Policy/Approval contract, client presentation separate | design |
| Memory/context/compaction | KCode/jcode; Agentora intent | current jcode + research frameworks | Session/Context ports | research |
| Multi-agent/swarm | KCode/jcode; Agentora; old RootManager | current jcode + research frameworks | WorkGraph/Agent Kernel; scheduler separate | research |
| MCP tools | all modern lineages | MCP standard/current clients | ToolCapability adapter | integrate |
| A2A task interoperability | none historical primary | A2A | optional adapter, Artifact/Task mapping | integrate candidate |
| Evidence/grading | harness_verify/Tracera/MACE intent | shared recovery doctrine | independent Evidence/Grader plane | canonical |
| Tracing/replay | Agentora intent; providers | OpenAI Agents tracing + OTEL ecosystems | TracePort/Evidence links | integrate |
| GUI workbench | HeliosLab | modern Codex app + CMux/Herder lessons | HeliosLab ClientAdapter | product-specific |
| Windows POSIX compatibility | Pine intent + KCode/Helios needs | research/current substrates | Workspace/runtime adapter | separate substrate |
| Release/runtime identity | KCode recovery | shared evidence contract | client/runtime adapter invariant | canonical |

A hypothesis is not a disposition. Final rows require source/SOTA/experiment evidence.
