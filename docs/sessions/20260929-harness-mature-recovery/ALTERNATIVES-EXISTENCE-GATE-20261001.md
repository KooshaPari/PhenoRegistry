# Alternatives / existence gate — HeliosCLI + KCode family

Date: 2026-10-01. No winner presumed.

## Alternative A — Modern Codex as primary client/runtime adapter
Baseline: openai/codex@60947e234156ac12bdb7fba2477d3965f166bd34.

Strengths to validate:
- active upstream/contribution path;
- typed app-server protocol shared by TUI/exec/external clients;
- in-process and external transport paths;
- separate exec-server for filesystem/process environment work;
- broad modern Codex UX/tool/security ecosystem.

Risks:
- OpenAI-specific product/provider assumptions;
- protocol breadth may exceed generic harness needs;
- shared harness authority must not become Codex app-server authority by accident;
- upstream evolution/carry cost and contribution acceptance.

Default strategy: CONTRIBUTE / ADAPT / THIN OVERLAY before hard fork.

## Alternative B — Modern jcode as primary client/runtime adapter
Baseline: 1jehuang/jcode@5f1c091cf7682cbce781d08444cc19ffb7ec01d8.

Strengths to validate:
- user preference for jcode in most CLI cases;
- active upstream and existing contributor relationship;
- native server/client model with server-owned sessions;
- multi-provider, memory, swarm/tool/runtime capabilities;
- lightweight/native TUI performance focus.

Risks:
- current KCode fork divergence/carry cost;
- protocol/daemon identity and effect/recovery semantics need hardening;
- proposed multi-session architecture must be distinguished from shipped behavior;
- generic harness extraction may require upstream extension points.

Default strategy: CONTRIBUTE / EXTERNAL ADAPTER / THIN PATCH before deep fork.

## Alternative C — Segmented Codex + jcode clients over one shared harness
Codex-lineage client specializes where modern Codex UX/app-server/ecosystem is advantageous; jcode-lineage client specializes in fast native multi-provider/headless/server use. Both consume shared product-neutral harness ports.

Survival gate:
- roles produce materially different user/operational value;
- shared semantics prevent duplicate harness implementations;
- maintenance cost of two clients is justified by measured use;
- no role can be cleanly expressed as mode/config/plugin of the other.

## Alternative D — Converged/superset single client
Choose the stronger base or build a thin new client over shared harness, port only surviving UX/runtime advantages from both.

Survival gate:
- no material role requires independent release/runtime;
- upstream contribution/adapter paths preserve useful capabilities;
- migration cost lower than indefinite dual-client carry.

## Alternative E — Status quo old forks
HeliosCLI root harness + deep KCode fork maintained independently.

Current disposition: REJECT AS DEFAULT. It duplicates semantics, carries stale upstream state and encourages client-owned harness behavior. It survives only if experiments falsify A-D.

## HeliosLite / Forgecode
Sunset donor. Candidate niche: extremely light ephemeral/headless chat. Before retaining any standalone product, compare modern jcode/Codex/shared-harness startup latency, memory, binary footprint and headless ergonomics. If the niche is reproducible as a mode, adapter or stripped build, retire standalone HeliosLite.

## Shared harness alternative stack
Do not build every substrate:
- small agent kernel inspired by minimal SDK designs;
- active client/runtime adapters to Codex/jcode;
- pluggable durable execution (local backend + optional Temporal/Durable Task-class adapter);
- scheduler port capable of local queue through Ray/K8s/custom fleet substrate;
- MCP/A2A adapters;
- independent evidence/grader plane;
- client-neutral event projection.

## Decision evidence required
Matched tasks and non-coding workload; startup/memory/latency; concurrency; recovery; effect safety; provider/tool breadth; client UX; protocol stability; upstream carry cost; contribution feasibility; security; cross-client semantic conformance.

No weighted score may average away safety/evidence failures.
