# Family capability-lineage matrix — pass 1

| Capability / concern | HeliosCLI / Codex lineage | KCode / jcode lineage | HeliosLite / Forgecode donor | Shared-harness destination hypothesis | Status |
|---|---|---|---|---|---|
| Rich client/TUI UX | historical Helios preference; modern Codex materially evolved | jcode preferred overall by user | useful but sunset | client-specific projection over shared events | compare current behavior |
| GUI/workbench integration | modern Codex App Server explicitly serves app/IDE/web/TUI | jcode protocol/server/client SDK surfaces | not canonical | versioned event/projection API consumed by HeliosLab | strong Codex prior art |
| Headless/ephemeral light chat | Codex exec/SDK exist | jcode can likely cover; measure | historical Forgecode strength | lightweight client/mode, not separate core | falsification required |
| Provider/model abstraction | current Codex provider semantics | jcode provider runtime/extensibility strong | Forgecode multi-provider donor | provider port + capability negotiation | compare |
| Agent loop | modern Codex core | jcode runtime | Forgecode runtime | Agent Kernel contract; client-independent | compare + SOTA |
| Tool runtime | Codex tools/MCP/apps | jcode tools/provider bridges | Forgecode tools | typed capability/tool runtime | compare + SOTA |
| ACI/coding environment | modern Codex coding harness | jcode coding runtime | donor | coding specialization over workspace/tool runtime | research required |
| Durable effort | old Helios root checkpoint scaffolds insufficient | KCode session durability != effort authority | donor recovery work | backend port; Temporal/Durable Task/custom candidates | architecture open |
| External effect reconciliation | old root not proven | KCode candidate primitive qualified/unmounted | HeliosLite donor primitive qualified/unmounted | durable effort/effect contract | contract mature; backend open |
| Multi-agent orchestration | root RootManager prototype only | jcode capabilities to map | donor | orchestrator layer separate from kernel | SOTA open |
| Scheduling/fleet/QoS | harness_scaling claims to inspect | runtime concurrency to inspect | Forgecode lightness donor | scheduler/control-plane layer | SOTA open |
| Memory/context/compaction | old Codex/vendor not implementation | jcode has substantial memory/compaction surfaces | donor | kernel/context subsystem with provider/client adapters | compare |
| Evidence/grader/MACE | root verify/spec crates to inspect | no automatic acceptance authority | donor | independent grader/evidence subsystem | normative contract defined |
| Approvals/policy | current Codex has client-driven bidirectional approval patterns | jcode policy surfaces to map | donor | shared policy/HITL contract | compare |
| Sandbox/workspace | root helios-sandbox + current Codex alternatives | jcode workspace/runtime | donor | workspace/environment runtime | compare |
| Windows/POSIX Pine | old Helios docs WSL-oriented | KCode candidate integration target | donor | workspace/platform adapter | separate Pine evidence |
| Plugins/extensions | root pheno-plugin/plugin-arch prototypes | external provider adapters | donor | capability/plugin system | SOTA open |
| Observability/replay | root tracing only; no mature OTel | jcode logging/session evidence | donor | event/evidence/trace contract | SOTA + mapping |
| Upstream maintenance | Codex active, contribution possible | jcode active, user contributor | Forgecode sunset | prefer upstream contributions/thin overlays | accepted strategy |
| Client interchange | modern Codex App Server demonstrates model | jcode protocol candidate | donor | mandatory shared projection semantics | mature requirement |
| Generic non-coding use | root interfaces generic but shallow | coding-derived | coding-derived | Freyr/shared harness must pass non-coding falsification | open |

Pass 1 records destination hypotheses only. No row is a final architecture decision until source mapping + SOTA + experiments support it.