> Authored by Instinct

# Stack review: Paperclip and the other tools (Oct 8, 2026)
Research only. No tool integration was tested hands-on; docs and repo review only. Star and issue counts are left out on purpose (search-index snapshots disagreed).

## Decision lines (his rulings, Oct 8)
- Gateway: Hermes Agent. OpenClaw is rejected on his preference (not a fallback). He is comfortable owning or custom-writing adapters into Hermes where gaps exist; iMessage is the known gap.
- Paperclip = paperclipai/paperclip (confirmed by him).
- Preferred layout (updated 10:52 PM): Hermes is the top, the CEO / living device assistant gateway he talks to. Paperclip is the management view (org chart, goals, budgets; the Agslag direction), not above Hermes in the command chain. JCode and Codex are subagents and his parent chat surfaces.
- OmniRoute is REJECTED (too buggy). Routing layer: cliproxyapi-plusplus (his fork) or another, else hand routing.
- Model map: OpenCode Go = Step 5 free / MiMo 2.6; MiniMax plan = M3; default tiers: normal = GPT 6 Luna med, high = GPT 6.1 Sol med.

## 1. Paperclip (paperclipai/paperclip)
Open-source (MIT) orchestration for teams of AI agents. Node.js server plus React UI with org charts, goals, tasks, budgets and governance. Tagline: "If OpenClaw is an employee, Paperclip is the company." Created 2026-03-02; recent release v2026.1005.0. Sources: https://github.com/paperclipai/paperclip , https://paperclip.ing
Fit: management view beside Hermes (org chart, goals, budgets), not in the command chain. Adapters: built-in `hermes_local` plus Claude Code, Codex, Cursor, OpenCode, Gemini CLI (https://docs.paperclip.ing/reference/adapters/overview/).
Caveat: the `hermes_local` adapter is the rough edge. Open issues #4009 (heartbeat failures on WSL2) and #3833 (AGENTS.md not injected) point to rough handling. Two control planes can conflict, so keep a clear split: Paperclip owns goals, tasks and budgets; Hermes owns channels, cron and webhooks.

## 2. Other tools and their role
- Hermes Agent (MIT, v0.21.6 cut Oct 8, fast-moving, expect churn): MCP client, ACP server, `delegate_task` subagents, bundled skills that delegate coding to Claude Code and Codex via CLI. `hermes mcp serve` exposes messaging conversations as MCP tools, not coding or orchestration. Role: comms and cron gateway. https://github.com/NousResearch/hermes-agent
- Claude Code (ships near-daily, v2.1.295 Oct 8): worker via CLI or headless from Hermes. https://code.claude.com/docs/en/changelog
- Codex CLI (Rust, frequent releases, 0.161.0 Oct 7): worker via CLI. https://github.com/openai/codex/releases
- Cursor: headless CLI (`-p`, `--force`) and MCP. Worker via CLI if wanted; the IDE stays standalone. https://cursor.com/docs/cli/headless
- JCode (1jehuang/jcode): Rust coding-agent harness, MIT, v0.91.0 Oct 6, one main maintainer. Worker or standalone; no verified Hermes integration. https://github.com/1jehuang/jcode
- KCode (https://github.com/KooshaPari/KCode): his PUBLIC fork of JCode, 137 commits ahead and about 2.5k behind upstream; adds swarm TUI, manager/researcher modes and more. Still no chat gateway. See the KCode divergence report (PR #617).
- ForgeCode (Apache-2.0, 300+ models, ZSH plugin; he has a fork): optional worker via CLI; overlaps the other coding agents. https://github.com/tailcallhq/forgecode
- OmniRoute (REJECTED by him as too buggy; do not use): KooshaPari/OmniRoute is a fork of diegosouzapw/OmniRoute; he publishes @kooshapari/omniroute on npm and has merged upstream PRs. He also maintains a cliproxyapi-plusplus fork. Replace with cliproxyapi-plusplus (his fork) or another proxy, else hand routing. https://github.com/KooshaPari/OmniRoute , https://github.com/diegosouzapw/OmniRoute , https://www.npmjs.com/package/@kooshapari/omniroute

## 3. Overlaps and caveats
- Control plane: Paperclip (org level) above Hermes (comms and cron). Keep the split explicit.
- Model routing: OmniRoute is out. Hermes calls cliproxyapi-plusplus or another proxy, or routes by hand.
- Worker redundancy: Claude Code, Codex, Cursor, JCode/KCode and ForgeCode fill the same slot.
- Hermes and Paperclip are both months to a year old, fast-moving, with large issue backlogs. Hermes CLI delegation is PTY-driven; expect permission-prompt and session quirks.

## Layering and infra decisions (added Oct 8, 2026)
Decision lines from him, applied after the first draft. Fuller write-ups are in PR #618 (docs/research/).
- Workflow orchestration is a MUST and sits under the workers in the Hermes (top) / Paperclip (management view) layout. It is an open candidate slot: Temporal OSS primary, Hatchet alt, Kestra et al. compared in workflow-orchestrator-comparison.md.
- Infra: one Postgres anchor, NATS (JetStream) as the agent event bus, MinIO for artifacts, Neo4j rejected for now.
- Network: tailnet = machine-to-machine fabric; Cloudflare Access/Tunnel = identity edge for browser-reached clients; cloudflared runs inside the tailnet. Desktop first, laptop second.
- Workers run containerized on both devices: one shared base image, per-task instances, destroyed on completion. Bare metal stays his end-user environment.
- Shared base reference: his own "Research Agent Business Stack" analysis (shared-base-agent-corp.md).
