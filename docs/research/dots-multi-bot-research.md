> Authored by Instinct

# Multi-bot expansion research (Oct 8, 2026)
Sources through Oct 7, 2026. Moderate depth: OpenAI help pages fetched live; reviews/news partly as search excerpts.

## Headlines
1. Custom GPTs are being retired. OpenAI help: "New GPT creation and publishing are not available on personal ChatGPT accounts (Free, Go, Plus, Pro)." Plugins replace them; Enterprise retirement Dec 11, 2026, other plans "expected to follow." "An assistant like Instinct on ChatGPT" = a Dot (plus Projects/Plugins), not a GPT.
   - https://help.openai.com/en/articles/8554397-creating-and-editing-gpts
   - https://www.toolbit.ai/blog/custom-gpts-retirement-move-to-chatgpt-projects
   - https://triedaitools.com/chatgpt-apps-gpts-skills-explained/
2. Dots exist and are the right surface, but are 9 days old and rough.
3. Google replacing Gems with "skills" (Sep 30). Anthropic merged Cowork into Claude (Sep 16). Every vendor shipped/announced an always-on agent in Sep 2026: OpenAI Dots (Sep 29), Meta Muse (Sep 8), Grok Bot (xAI).

## Custom GPTs (legacy, mostly moot)
- Limits: 10 knowledge files per GPT; Projects 25 (Plus) / 40 (Pro). https://help.openai.com/en/articles/8555545-uploading-files-and-audio-to-chatgpt
- Fiascos: knowledge files and system instructions extractable by prompt injection, repeatedly shown:
  - https://aclanthology.org/2025.acl-long.936.pdf
  - https://arxiv.org/html/2311.11538V2
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC13274269/
  - https://wraith.sh/learn/how-to-pentest-custom-gpt
  - Lesson: never put secrets or private data in any GPT/Project/Gem knowledge or instructions.
- Cannot: run in background, act unprompted, hold its own computer. That is what Dots add.

## Dots
What: always-on agent on GPT-6 Astra, own cloud computer + browser, starts from ChatGPT memory, Codex + plugins (4,000+ apps claimed), reachable in ChatGPT + Slack (Teams invite alpha, US-only text beta). Pro 18+, outside EEA/UK/CH; first dot included.
- https://openai.com/index/introducing-dots/
- https://chatgpt.com/features/dots/
Approval model, 4 layers: (a) plugin permissions (shared across dots/ChatGPT/Work/Codex); (b) Custom Rules (allow/require-approval/block; cannot override built-ins); (c) Auto-review screens account-affecting/info-sharing actions; (d) Activity View + kill/redirect. Proactive background research is read-only.
- https://help.openai.com/en/articles/20001529-dots-privacy-security-and-safety-faqs
Early flaws (treat as early/anecdotal):
- Confirmation friction: shuttle booking took 3 yeses; eesel scored 3/5. https://www.eesel.ai/blog/openai-dots-review
- Custom Rules checker rejects broad authorizations; won't fetch 2FA codes; local-computer tasks die silently when laptop sleeps; one connected computer at a time; setup desktop only. https://platform-monkey.com/reviews/openai-dots-always-on-agents
- The Register (Oct 7): task failures, connectivity issues, disappearing dots, refusals. https://www.theregister.com/ai-and-ml/2026/10/07/openai-dots-inspire-open-source-imitators-amid-technical-difficulties/5301734
- Hands-on: blocked shopping site, rough output, but a proactive failed-payment alert was a real win. https://www.ai.joaoqueiros.com/blog/chatgpt-dots-honest-review-pat-simmons-real-tasks
Privacy: dot memory shared with ChatGPT memory; cannot view/edit/delete individual dot memories (only delete whole dot); disconnecting a plugin does not delete ingested data; on personal plans "Improve the model for everyone" governs training on dot work (turn off); credentials/screenshots not retained in dot context. Browser egress via OpenAI TLS-inspection proxy claimed (single secondary source, unverified).
Cost: Pro 200 allowance cut from Oct 30 (20x to 10x Plus in Work/Codex; GPT-6 Pro chat 200 to 100/wk); extended "deeper work" allowance lasts first month only; dot-started Codex/Work tasks count against limits (secondary source).

## Claude and Gemini equivalents
- Claude: Projects (redesigned Sep 17 beta); Skills (open standard) vs MCP connectors vs Projects; custom remote-MCP connectors on all plans; Cowork merged into Claude Sep 16 (keeps working after laptop closes); chat/Cowork memory merged Aug 25.
  - https://claude.com/resources/articles/projects-redesigned
  - https://www.rabinarayanpatra.com/blogs/claude-skills-vs-mcp-vs-projects
  - https://support.claude.com/en/articles/11817273
  - https://claude.com/resources/articles/cowork-is-now-claude
- Gemini: Gems being replaced by "skills" (slash-invoked prompts + reference files).
  - https://blog.google/products-and-platforms/products/gemini/automate-tasks-with-skills/
  - https://workspaceupdates.googleblog.com/2026/09/skills-gemini-app-workspace.html

## Grok and Meta (distrust justified by record)
- Grok: Aug 2025 share-link indexing exposed hundreds of thousands of chats (BBC/TechCrunch). 2026: Canada OPC findings on deepfakes; UK ICO formal investigation; lawsuit alleging training on CSAM (allegation only). Grok 4.6 Aug 12; Grok Bot = always-on agents.
  - https://www.bbc.com/news/articles/cdrkmk00jy0o
  - https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/02/ico-announces-investigation-into-grok/
- Meta: Jun 2025 Discover feed accidentally public chats; since Dec 16, 2025 Meta AI chats feed ad personalization; Mar 2026 smart-glasses class action. Muse (Sep 8) ties to FB/IG. https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/
- Recommendation: keep both out of anything holding job, identity or repo data.

## Where each wins (consensus, low rigor)
Claude: instruction-following, long-form, coding agents. GPT: structured output, tool use. Gemini: multimodal, biggest context. Grok: real-time X data. Pattern: route by task, don't pick one.

## Proposal: his dot config (for his review; he must create it)
- Role: "agent-stack ops" dot. Read-mostly watcher of KooshaPari GitHub (PRs, CI, failed Actions), CF and Vercel deploy/usage dashboards, CLI agents' output; summarizes and flags. Can start Codex tasks for bounded coding jobs.
- Custom Rules, strict first: block sending email/messages as him; block payments; block merges/pushes to main outside job-cockpit; block deletes; require approval for deploys and form submits; allow read/notes/drafts/open PRs with "[Dot]" prefix. Narrow enumerable rules (checker rejects broad ones).
- Don't give it: passwords/vault, personal identifiers, job-platform logins. Turn off "Improve the model for everyone".
- Job pipeline: dot as second opinion on cover letters and read-only cockpit auditor, not the applier.
- Pilot read-only 1-2 weeks, then widen (dots are flaky now).

## New capability ideas he hasn't asked for
a. Quota/cost sentinel: track usage across ChatGPT/Claude/Gemini, warn before limits (Oct 30 Pro allowance cut makes this real).
b. Model-router policy doc in phenoregistry: writing/long-form -> Claude, structured tool tasks -> GPT, multimodal/huge context -> Gemini; re-test periodically.
c. Prompt-injection hygiene: site allowlist per agent + quarterly red-team of his own Projects/skills (Wraith checklist).
d. Memory hygiene/portability: canonical memory in his repo (phenoregistry), vendor memory as disposable cache; periodic exports.
e. Skills as the portable layer: write core procedures once as skills (job rules, drafting voice, deploy checklist) - Claude Skills are an open standard, Gemini has skills, ChatGPT has skills in plugins.

## Open points / unverified
- His specific Pro tier + US region dots access not confirmed.
- Non-Enterprise custom-GPT retirement dates not stated.
- Gemini agent capability and Grok Bot/Muse privacy specifics not from primary sources.
- Several review sites are low-authority; numbers indicative.
