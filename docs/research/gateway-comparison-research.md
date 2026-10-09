> Authored by Instinct

# Gateway comparison: Hermes vs OpenClaw vs Codex/JCode forks (Oct 8, 2026)
Research only; nothing installed.

## Verdict
Hermes Agent as the gateway/control plane. Keep Codex, JCode, KCode and Forge as workers it calls. Do not make a coding-agent fork the gateway.

## 1. Hermes: a real gateway, not just a CLI
- One gateway process serves Telegram, Discord, Slack, WhatsApp, Signal, Email and CLI, with cross-platform conversation continuity (README).
- Built-in cron: natural-language or cron schedules, delivery to any chat, and a no-agent script mode. Webhook routes can fire jobs on events like a PR comment. https://hermes-agent.nousresearch.com/docs/user-guide/features/cron
- Memory: curated memory, FTS5 session search, user modeling. Skills follow the agentskills.io standard.
- MCP client, and it can also run as an MCP server exposing its messaging to other agents. One-line preset to wrap Codex: `hermes mcp add codex --preset codex` (runs `codex mcp-server`). Imports Claude Code config (`hermes import-agent claude-code`) and has `hermes claw migrate` for OpenClaw. https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- Model-neutral: any provider, or your own OpenAI-compatible endpoint. 7 terminal backends (local, Docker, SSH, Modal and others). Security covers DM pairing, command approval and container isolation.
- Gaps: Python-heavy and young. Rough edges and churn are likely. "Self-improving skills" are a convenience, not a guarantee.

## 2. OpenClaw: comparable gateway, more channels, more security baggage
- Gateway control plane with 20+ channels including iMessage, Teams and Google Chat. Companion apps for macOS, iOS, Android and Windows. Cron and inbound webhooks (`/hooks/wake`, disabled by default). Plugin SDK plus ClawHub. https://docs.openclaw.ai/automation/cron-jobs/webhooks
- Harness-agnostic by design: the official `codex` plugin runs agent turns through Codex app-server, so Codex owns the session and OpenClaw owns channels, approvals and transcript. https://docs.openclaw.ai/plugins/codex-harness. Strongest harness-agnostic story of the three, and the one real reason to pick OpenClaw.
- Maturity/security: a third-party tracker (unofficial) lists CVE-2026-25253 (one-click RCE, fixed v2026.1.29), a reverse-proxy localhost auth bypass, and a JFrog claim that most publicly reachable instances were vulnerable. Jan-Feb 2026, fixed; the README now stresses pairing and sandboxing, but the history is real. Tools run on host by default unless sandboxed. Node 24+/pnpm. Foundation funding includes OpenAI, good for Codex support.

## 3. Existing forks as the gateway: possible, but you would be building the gateway
- Codex CLI: no channels, no cron, no persistent memory. Has `codex exec` (non-interactive, JSONL, resume), `codex mcp-server`, and `codex app-server` (stdio/WebSocket/Unix socket, bearer auth) for remote and long-lived sessions. Great worker/backend, not a control plane.
- JCode: closest. Shared daemon/server, swarm of agents, embedding-graph memory, MCP config, and "Ambient Mode": an always-on self-scheduling agent that consolidates memory and does background work with email notifications. No chat-channel gateway or webhook intake found (README + ambient doc only; a deeper code check could change that). Ambient is single-agent and self-scheduled, not user cron. One main maintainer.
- ForgeCode: coding agent with MCP support, ZSH plugin, one-shot CLI. No gateway features.
- KCode: the owner's private fork of JCode; inherits the JCode assessment (not independently verified).
- Cost of this path: writing and maintaining channel adapters, scheduler, webhook intake, pairing/auth and routing yourself, which is rebuilding Hermes. Sensible hybrid: JCode ambient as a worker or memory layer behind the gateway.

## 4. Setup path on the 5800X / 64GB / 3090 Ti + 1080 Ti (24/7)
- Hermes as a systemd service (WSL2 or native Linux). Local terminal backend, or Docker for tool isolation. `hermes setup`, `hermes gateway setup`, `hermes gateway start`. Telegram or Slack first, DM pairing on.
- Models: cloud (ChatGPT Pro, existing MiniMax plan, OpenRouter, OmniRoute) as primary. Optionally point Hermes at a local OpenAI-compatible endpoint on the 3090 Ti (24GB, mid-size) for cheap cron jobs. The 1080 Ti is not useful for modern serving.
- Workers: `hermes mcp add codex --preset codex`; wire JCode/KCode/Forge as MCP servers or shell tools via non-interactive CLIs. PhenoRegistry as shared ledger, PRs on branches.
- Safety: keep the gateway off the public internet, Tailscale for remote access, never run with approvals off.
- Fallback: if channel list or Codex-as-harness matters more than Python-based Hermes (iMessage, Teams), OpenClaw is the swap; pin a recent release and sandbox it. `hermes claw migrate` goes the other way, so switching costs little.

## Caveats
- Hermes maturity is judged from README/docs, not source or runtime. Release cadence and Hermes security advisories were not checked; verify before exposing beyond his own chats.
- Repo star and issue counts were dropped because they could not be verified.
