> Authored by Instinct

# Bot alternatives + self-hosting research (Oct 8, 2026)
Research only; no accounts, installs, repo edits. Full source list at end.

## Recommendation
Self-host the control plane, memory and execution first, not the largest model. Keep existing CLI agents and GitHub ledger; add ONE model-neutral persistent gateway (trial Hermes Agent vs OpenClaw, pick one) and one cheap API route. Trial a local 27B/30B model on hardware already owned. Do NOT buy GPUs merely to save tokens until measured volume and privacy requirements justify it. Additional consumer subscriptions mostly duplicate the current stack.

## Hosted options
1. Mistral Vibe (formerly Le Chat): strongest inexpensive hosted alternative to trial. Long-horizon work, 100+ connectors, triggered/recurring workflows, async coding PRs. Pro $14.99/mo; verified student $5.99/mo. Large API $0.50/M in, $1.50/M out. Privacy caveat: paid Vibe/API not trained on by default per current docs, but Sep 3 help says Vibe defaults into training + API has separate opt-out - disable BOTH; avoid Labs models (training exception overrides opt-out). API retention 30 rolling days; Agents API retains until account termination. ZDR only on supported stateless endpoints.
2. Perplexity: research/search tool, not another coding bot. Pro includes Computer, premium sources, file/app creation; Education Pro $10/mo with verification. Pricing page shows annual-billed equivalents ($17/mo Pro, $167/mo Max) - not month-to-month. Consumer tiers default into training: switch off AI data retention first; opt-out is prospective only.
3. DeepSeek: cheap inference route, not a home for personal inbox. Current API: V4.1-Flash and V4-Pro-0813 (1M context, tool calls; Flash has vision). Flash $0.30/$1.20 peak, $0.15/$0.60 off-peak per 1M in/out; Pro $1.32/$3.96 peak, $0.66/$1.98 off-peak. Consumer policy allows training, stores/processes data in mainland China; Italy processing restriction Jan 2025 (historical regulator action). Use public/non-sensitive context only.
4. Qwen: prefer Alibaba Model Studio API (never trains, but retains call data; no-training != zero-retention). International Qwen3.8-Max $2/M in, $6/M out. Consumer privacy unverified. Local Qwen3.8-27B more interesting than another chat plan.
5. Kimi: K3, K2.7-Code, K2.6; K2.5 retired Aug 31. Mainland RMB tiers (not verified US pricing). Kimi Claw = cloud OpenClaw, ~0.6% of credits daily even idle. Consumer data may train + stored in China; opt-out via support (5-7 days). API says no training on inputs/outputs.
6. Z.ai and MiniMax: API bakeoff candidates, not subscriptions. Z.ai DPA: processed without saving, generally Singapore; Team plan no-training but 2-seat minimum. MiniMax $22/$55/$132 token plans; M3 up to 512k input $0.30/M in, $1.20/M out. MiniMax privacy page unreadable - do not route sensitive material on assumption.

## Self-hostable models + hardware sizing (estimates, NOT measured on his machines)
Candidates: Qwen3.8-27B (general/multimodal), GLM-4.7-Flash 30B/3B-active (lighter coding/tool), Qwen3-Coder-Next 80B/3B-active (when more memory available). None establishes parity with frontier CLI agents - test on his own repo tasks.
4-bit weights ~ params x 0.5 bytes + metadata/buffers/KV cache. Active MoE params cut compute, NOT storage.
- 8B: ~8-12GB VRAM class, modest context, routine triage only.
- 27B/30B: 24GB sensible target, 32GB for context headroom. 16GB card works with aggressive quants/shorter context.
- 70B/80B: 48-64GB aggregate VRAM or ample unified memory.
- Llama 4 Scout 109B: 54.5GB weights; custom license. Not first solo pick.
- GLM5.3-Flash 320B, DeepSeek V4.1-Flash 552B+196B Engram, GLM5 744B: server projects, not consumer GPU. Don't confuse active params with memory footprint.
Community data point: Qwen3.8-27B Q4_K_M = 17.1GB, IQ4_XS = 14.6GB (512-token context test only).

## Harness choices
- Keep existing CLI tooling. OpenCode or Aider easiest model-neutral terminal additions; Aider analytics opt-in, excludes code/chat.
- Cline for editor-first Plan/Act + local Ollama/LM Studio. Telemetry ON by default - disable.
- OpenHands for unattended issue-to-PR workers + separate execution environments. More platform to operate.
- goose: extensible local CLI/desktop + MCP, telemetry off switch.
- smolagents: custom Python experiments; local executor is NOT a security boundary - use Docker/VM + scoped creds.
- Roo Code: sunset/archived 2026 - maintenance trap; pick maintained Cline/OpenCode.

## Always-on options (incl. The Register's imitators)
- CopilotKit OpenDots: real, MIT template, alpha. Repo: https://github.com/CopilotKit/OpenDots . Catch: conversations require CopilotKit Intelligence (hosted, local Docker eval, or LICENSED production self-host). Hosted Intelligence receives messages/tool calls/run events. Useful UI fork experiment, not the all-private production default.
- "Open Dot" Electron app: repo lead unverified (CRAWL_NOT_FOUND). Watchlist only.
- OpenClaw: maintained persistent gateway, memory, cron/webhooks, many chat channels, selectable hosted/local models. MIT; state on his machine; only a default version-check leaves (can disable). Isolate from everyday workstation, start read-only. https://openclaw.ai/
- Hermes Agent (Nous): MIT, terminal + messaging gateway, memory/session search, scheduled tasks, subagents, local/Docker/SSH/cloud execution. $5 VPS control-plane route (NOT $5 local frontier inference). Strong fit for his CLI orientation. https://github.com/nousresearch/hermes-agent
Trial Hermes vs OpenClaw, choose ONE.
- Caution: open-dots.dev is an unrelated unverified crypto-token product - excluded.

## Orchestration
- Windmill Community: code-first durable scheduled Python/TS jobs, queues, UI; free self-hosted unlimited executions; AGPL core.
- n8n Community: connector-heavy visual flows; fair-code Sustainable Use License (not OSI); self-host telemetry defaults on.
- Activepieces: MIT core, free self-hosted unlimited flows/users; Community lacks paid Agents/Chat layer.
Choose one or use existing code. Self-hosted logs/credentials stay in the host; cloud connectors still transmit payloads.

## Economics + hybrid
Illustrative: 20M uncached input + 2M output = $4.20-$8.40 DeepSeek Flash, $34.32 Pro peak, ~$13 Mistral Large page rates, before fees. Always-on 100W system = 72kWh/mo; 300W = 216kWh, x tariff. Existing GPU: privacy/experimentation justifies local. New multi-GPU machine solely to beat single-digit monthly API spend is a poor bet.
Suggested setup: registry remains state-of-record; Hermes OR OpenClaw on isolated existing machine/cheap VM; deterministic jobs in existing code or Windmill; local Qwen/GLM for private classification/summaries/modest edits; cheap hosted API for public bulk; frontier agents for hard planning/debugging/review. Explicit per-task routing, bounded budgets, no automatic secret/inbox upload to all providers. Benchmark 20 representative tasks (pass rate, retries, wall time, cost per accepted result) before any hardware.
Vercel/CF for cockpit/frontends/webhooks, NOT perpetual inference: Vercel Hobby Functions 2GB/300s; Workers Free 10ms CPU; Workers AI 10k neurons/day free but Cloudflare-hosted. Event-fed remote worker is the sensible split.

## Unknowns that would change sizing
His actual GPU/VRAM, RAM, uptime, electricity tariff, monthly task/token volume, required data residency.

## Sources
[1] mistral.ai/pricing, mistral.ai/products/vibe, docs.mistral.ai/admin/monitor-comply/privacy-data-controls, help.mistral.ai/en/articles/455207, legal.mistral.ai/terms/privacy-policy, docs.mistral.ai/admin/monitor-comply/zero-data-retention
[2] perplexity.ai/hub/pricing, perplexity.ai help-center articles/11187416, /11564572
[3] api-docs.deepseek.com/quick_start/pricing, cdn.deepseek.com/policies/en-US/deepseek-privacy-policy.html, garanteprivacy.it/home/docweb/-/docweb-display/docweb/10097450
[4] alibabacloud.com/help/en/model-studio/model-pricing, docs.modelstudio.console.alibabacloud.com/en/model-studio/privacy-notice, qwen.ai/privacypolicy
[5] kimi.com/en/help/membership/membership-pricing, /help/others/data-usage, /help/kimi-api/api-data-security, platform.kimi.ai/docs/pricing/chat-k25, /chat-k3
[6] docs.z.ai/legal-agreement/privacy-policy, docs.z.ai/devpack/teamplan, platform.minimax.io/docs/guides/pricing-token-plan, /docs/pricing/overview
[7] huggingface.co/Qwen/Qwen3.8-27B, /Qwen/Qwen3-Coder-Next, /zai-org/GLM-4.7-Flash, /zai-org/GLM-5.3-Flash, /zai-org/GLM-5, /deepseek-ai/DeepSeek-V4.1-Flash
[8] huggingface.co/docs/transformers/model_doc/llama4
[9] reddit.com/r/LocalLLM/comments/1vr4iqj (community, not independent lab)
[10] openhands.dev/blog/open-source-ai-coding-agents, github.com/openhands/openhands, aider.chat/docs/llms.html, /docs/more/analytics.html, docs.cline.bot/running-models-locally/overview, docs.cline.bot/enterprise-solutions/monitoring/telemetry, block-goose.mintlify.app/api/cli/configure, huggingface.co/docs/smolagents/en/tutorials/secure_code_execution, github.com/RooCodeInc/Roo-Code/commit/b4f2a242bc4d51b65e5e9406f03fd24d1b5f2a2a
[11] copilotkit.ai/opendots, github.com/CopilotKit/OpenDots
[12] theregister.com/ai-and-ml/2026/10/07/openai-dots-inspire-open-source-imitators-amid-technical-difficulties/5301734, news.lavx.hu/article/openai-s-dots-agents-stumble-as-open-source-clones-race-to-fill-gaps
[13] openclaw.ai, docs.openclaw.ai
[14] github.com/nousresearch/hermes-agent
[15] windmill.dev/pricing, /platform/self-host, n8n.io/pricing, docs.n8n.io/privacy-and-security/sustainable-use-license, activepieces.com/pricing, /solutions/open-source-developers
[16] vercel.com/docs/functions/limitations, developers.cloudflare.com/workers/platform/pricing/, /workers-ai/platform/pricing/
