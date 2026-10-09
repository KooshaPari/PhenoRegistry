> Authored by Instinct

# Shared base: "Research Agent Business Stack" (Oct 8, 2026)
Reference: https://chatgpt.com/share/6ac87fb2-1a50-83e8-9e6e-03eaff13742a

This is Koosha's own authored analysis, written for Mahmoud and tailored to his needs. Per Koosha, the core base (one human running an agent civilization/corp) is the same goal as Phenotype's, so this is the shared-base reference for the architecture docs here.

## Conclusions
- Do not build around Paperclip, OpenClaw, CrewAI or AutoGPT.
- Core = reliable business systems + durable workflow orchestration + bounded AI workers + independently enforced approvals.
- Candidates: Kestra OSS (conditional leader), Activepieces (strong alt), Windmill, n8n (conditional). Temporal rejected there for needing code. Paperclip as an optional management layer only. OpenClaw rejected as core.
- Pilot F: a 4-week failure-first test plan, F01-F10 hard tests (crash after external write, prompt injection, credential revocation, and similar).
- Six case studies A-F. Case B (AI-operated B2B service/trading company) was revised into a multi-vendor B2B marketplace; contenders Spree, Mercur, Bagisto, modeled on Faire.

## How it folds into the architecture PRs
- Orchestration is an open candidate slot under the workers in the Hermes (top) / Paperclip (management view) layout. See workflow-orchestrator-comparison.md: Temporal OSS primary, Hatchet alt, Kestra a real contender.
- Approvals must be enforced independently of agents (hash of exact artifact/action, owner-authenticated, agents hold no approval or final-effect credentials).
- Pilot F tests should gate adoption of any orchestrator.
- Source of truth for the chat is the share link above; this summary is from reading the rendered page.
