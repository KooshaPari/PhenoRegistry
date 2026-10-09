# Same-day upstream baselines — 2026-09-30

Frozen for the corrected HeliosCLI + KCode pair.

| Upstream | Branch | SHA | Commit time | Role |
|---|---|---|---|---|
| OpenAI Codex | main | `60947e234156ac12bdb7fba2477d3965f166bd34` | 2026-09-30T19:22:34Z | HeliosCLI active upstream/alternative |
| jcode | master | `3272c0372ed66aff49975e24f48107afca46208c` | 2026-09-30T03:35:47Z | KCode active upstream/alternative |

## Immediate Codex delta implication

Modern Codex's workspace now includes first-class agent graph/identity/roles/message-board surfaces, app-server daemon/client/protocol, plugin/extension APIs, state/thread stores, rollout tracing, workload identity, realtime transports, environment selection, richer permissions/sandboxing, connectors, memories, queue extension, worktrees and a TypeScript SDK.

HeliosCLI's frozen active root harness must therefore justify its harness primitives against this current architecture. The excluded vendored Codex tree is not the comparison baseline.

Initial disposition:
- root Helios harness orchestration: RESEARCH/COMPARE, not presumed differentiation;
- generic harness_interfaces: likely SUPERSEDE/REDESIGN unless independent harness research proves otherwise;
- checkpoint/rollback/spec/verification/scaling ideas: retain as obligations/candidates, compare against modern Codex + jcode + workflow/harness SOTA;
- client UX/product behaviors: recover historically, then map to modern Codex/jcode rather than preserving old implementation.

## jcode implication

KCode comparisons from this point use `3272c037...`, not the earlier `76df646...` snapshot. Re-run any existence claim materially sensitive to upstream movement before final disposition.
