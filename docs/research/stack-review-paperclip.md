> Authored by Instinct

# Stack review: Paperclip and the other tools (Oct 8, 2026)
Research only. No tool integration was tested hands-on; docs and repo review only. Star and issue counts are left out on purpose (search-index snapshots disagreed).

## Decision lines (his rulings, Oct 8)
- Gateway: Hermes Agent. OpenClaw is rejected on his preference (not a fallback). He is comfortable owning or custom-writing adapters into Hermes where gaps exist; iMessage is the known gap.
- Paperclip = paperclipai/paperclip (confirmed by him).
- Preferred layout: Paperclip as the org-level cockpit (goals, tasks, budgets; the Agslag direction), Hermes as the comms and cron gateway below it, coding agents as workers.

## 1. Paperclip (paperclipai/paperclip)
Open-source (MIT) orchestration for teams of AI agents. Node.js server plus React UI with org charts, goals, tasks, budgets and governance. Tagline: "If OpenClaw is an employee, Paperclip is the company." Created 2026-03-02; recent release v2026.1005.0. Sources: https://github.com/paperclipai/paperclip , https://paperclip.ing
Fit in the layered layout: org-level cockpit above Hermes. Adapters: built-in `hermes_local` plus Claude Code, Codex, Cursor, OpenCode, Gemini CLI (https://docs.paperclip.ing/reference/adapters/overview/).
Caveat: the `hermes_local` adapter is the rough edge. Open issues #4009 (heartbeat failures on WSL2) and #3833 (AGENTS.md not injected) point to rough handling. Two control planes can conflict, so keep a clear split: Paperclip owns goals, tasks and budgets; Hermes owns channels, cron and webhooks.

## 2. Other tools and their role
- Hermes Agent (MIT, v0.21.6 cut Oct 8, fast-moving, expect churn): MCP client, ACP server, `delegate_task` subagents, bundled skills that delegate coding to Claude Code and Codex via CLI. `hermes mcp serve` exposes messaging conversations as MCP tools, not coding or orchestration. Role: comms and cron gateway. https://github.com/NousResearch/hermes-agent
- Claude Code (ships near-daily, v2.1.295 Oct 8): worker via CLI or headless from Hermes. https://code.claude.com/docs/en/changelog
- Codex CLI (Rust, frequent releases, 0.161.0 Oct 7): worker via CLI. https://github.com/openai/codex/releases
- Cursor: headless CLI (`-p`, `--force`) and MCP. Worker via CLI if wanted; the IDE stays standalone. https://cursor.com/docs/cli/headless
- JCode (1jehuang/jcode): Rust coding-agent harness, MIT, v0.91.0 Oct 6, one main maintainer. Worker or standalone; no verified Hermes integration. https://github.com/1jehuang/jcode
- KCode (https://github.com/KooshaPari/KCode): his PUBLIC fork of JCode, 137 commits ahead and about 2.5k behind upstream; adds swarm TUI, manager/researcher modes and more. Still no chat gateway. See the KCode divergence report (PR #617).
- ForgeCode (Apache-2.0, 300+ models, ZSH plugin; he has a fork): optional worker via CLI; overlaps the other coding agents. https://github.com/tailcallhq/forgecode
- OmniRoute: KooshaPari/OmniRoute is a fork of diegosouzapw/OmniRoute; he publishes @kooshapari/omniroute on npm and has merged upstream PRs. He also maintains a cliproxyapi-plusplus fork. Role: standalone model-routing layer; point Hermes at it as a single OpenAI-compatible endpoint. https://github.com/KooshaPari/OmniRoute , https://github.com/diegosouzapw/OmniRoute , https://www.npmjs.com/package/@kooshapari/omniroute

## 3. Overlaps and caveats
- Control plane: Paperclip (org level) above Hermes (comms and cron). Keep the split explicit.
- Model routing: Hermes vs OmniRoute vs cliproxyapi. Cleanest: Hermes calls OmniRoute.
- Worker redundancy: Claude Code, Codex, Cursor, JCode/KCode and ForgeCode fill the same slot.
- Hermes and Paperclip are both months to a year old, fast-moving, with large issue backlogs. Hermes CLI delegation is PTY-driven; expect permission-prompt and session quirks.
