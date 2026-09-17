# RL and GPT Fine-Tuning

**User:**   
**Created:** 4/2/2026 23:39:28  
**Updated:** 4/3/2026 23:35:05  
**Exported:** 4/20/2026 17:32:48  
**Link:** [https://chatgpt.com/c/69cf6073-5f88-8326-8ad1-013d113e3d72](https://chatgpt.com/c/69cf6073-5f88-8326-8ad1-013d113e3d72)  

## Prompt:
4/2/2026, 11:39:27 PM

Reinforcement learning  and recursive + diffusiive lm tie  we can add over black box api like gpt ( theg zipper fine tune but exp so no local only yes but no train both pre and during runtime to continuously improve coding agents

## Response:
4/2/2026, 11:39:28 PM

I’m checking what’s actually feasible with black-box APIs versus what only works when you control weights, then I’ll map that onto coding agents specifically.

There is a hard line here: you can continuously improve the _agent system_ over a black-box GPT API, but you cannot continuously improve the base model itself unless the provider exposes fine-tuning or RL-style training endpoints. I’m pulling in the current provider-side options so I can separate the two cleanly.

> **Searching for up-to-date papers on RL and APIs**
>
> [Reinforcement fine-tuning | OpenAI API](https://developers.openai.com/api/docs/guides/reinforcement-fine-tuning/)
> [Recursive Language Models](https://alexzhang13.github.io/blog/2025/rlm/)
> [Diffusion Large Language Models for Black-Box Optimization](https://arxiv.org/abs/2601.14446)
> [NeurIPS 2025 Papers](https://neurips.cc/virtual/2025/papers.html)
> [Finetuning GPT for Personal Document Editing](https://community.openai.com/t/finetuning-gpt-for-personal-document-editing/932128)
> [Accepted Papers](https://2025.naacl.org/program/accepted_papers/)
> [New tools for building agents](https://openai.com/index/new-tools-for-building-agents/)
> [Recursive Language Models (MIT SAIL, December 2025)](https://www.facebook.com/groups/3670562573177653/posts/4435124633388106/)
> [Diffusion Large Language Models for Black-Box Optimization](https://openreview.net/forum?id=Q27VrQodL3)
> [LLM Research Papers: The 2025 List (July to December)](https://magazine.sebastianraschka.com/p/llm-research-papers-2025-part2)
> [Downloads 2025](https://iclr.cc/Downloads/2025)
> [Recursive Language Models (Dec 2025)](https://www.youtube.com/watch?v=djEDs-c7eVM)
>
> **Searching for OpenAI API evals, distillation, and research**
>
> [Working with evals | OpenAI API](https://developers.openai.com/api/docs/guides/evals/)
> [Model Distillation in the API](https://openai.com/index/api-model-distillation/)
> [Inference-Aware Prompt Optimization for Aligning Black-Box Large Language Models](https://arxiv.org/abs/2508.10030)
> [Self-Evolving Code Agents via Reliable Self-Verification](https://openreview.net/forum?id=q56ZI1Co43)
> [Black-Box Prompt Optimization: Aligning Large Language ...](https://aclanthology.org/2024.acl-long.176/)
> [Working hard to undersanding working of api ...](https://community.openai.com/t/working-hard-to-undersanding-working-of-api-openai-blocks-your-access/1324380)
> [Collaborative Discrete-Continuous Black-Box Prompt ...](https://iclr.cc/virtual/2025/poster/28111)
> [Black-Box Prompt Optimization: Aligning Large Language ...](https://www.researchgate.net/publication/384214618_Black-Box_Prompt_Optimization_Aligning_Large_Language_Models_without_Model_Training)
> [weitianxin/Awesome-Agentic-Reasoning: A curated list of ...](https://github.com/weitianxin/Awesome-Agentic-Reasoning)
> [Black-Box Test-Time Prompt Tuning for Vision-Language ...](https://ojs.aaai.org/index.php/AAAI/article/view/32652)
> [DynamicRAG: Leveraging Outputs of Large Language ...](https://neurips.cc/virtual/2025/poster/118330)
>
> Thought for 19s

Yes, but mostly at the **agent/control-plane layer**, not the base GPT itself.

What you can add over a black-box API:

1.  **Outer-loop reinforcement learning for the agent**  
    Treat the whole coding agent as the policy:
    *   state = repo slice, task, prior failures, tool outputs
    *   action = prompt template, tool choice, decomposition strategy, verifier choice, retry depth, model selection
    *   reward = tests pass, lint/security pass, patch size, latency, token cost, human acceptance, post-merge regressions
    This is the most practical route for black-box models because you do not need gradients or weights. You optimize the **wrapper policy** around the model instead. Black-box prompt optimization and inference-aware prompt optimization both support this general direction. [ACL Anthology+1](https://aclanthology.org/2024.acl-long.176/?utm_source=chatgpt.com)
2.  **Online learning during runtime**  
    You can continuously improve:
    *   routing
    *   prompt selection
    *   scaffold selection
    *   retry policy
    *   tool-use policy
    *   verifier/reranker thresholds
    *   memory retrieval policy
    *   bug-localization heuristics
    The clean implementation is contextual bandits first, then heavier RL only where delayed reward matters. For coding agents, this usually beats trying to do “full RL everywhere.”
3.  **Recursive inference / recursive LM style orchestration**  
    Recursive Language Models are basically an inference pattern where the model decomposes a long problem, recursively calls itself on subproblems, and interacts with external context/program state. That maps very well onto coding agents handling large repos, long traces, and repair loops. You can implement the _pattern_ over a black-box API even if you do not own the model. [arXiv+1](https://arxiv.org/abs/2512.24601?utm_source=chatgpt.com)
4.  **Diffusive / iterative refinement layer**  
    “Diffusion LM” ideas are less directly usable as a drop-in over GPT APIs for coding agents. But the useful transferable part is **iterative denoising/refinement**:
    *   generate rough patch / plan
    *   mask weak spans
    *   regenerate only weak spans
    *   re-score with tests/verifiers
    *   repeat until budget exhausted
    So the architecture can be diffusion-like even if the underlying model is still autoregressive. The diffusion-paper result you’d borrow is the iterative refinement mindset, not the exact model class. [arXiv+1](https://arxiv.org/abs/2601.14446?utm_source=chatgpt.com)

What you cannot really do over a pure black-box API:

*   true weight updates on every runtime interaction
*   low-level RL on hidden states / logits
*   genuine continual pretraining
*   parameter-efficient tricks like LoRA unless the provider exposes training

That requires provider-side fine-tuning or your own model weights. OpenAI does expose fine-tuning and reinforcement fine-tuning in the API, where a grader scores outputs and training updates the model weights, but that is still a provider-managed training path, not arbitrary local/runtime weight hacking. [OpenAI Developers+1](https://developers.openai.com/api/docs/guides/reinforcement-fine-tuning/?utm_source=chatgpt.com)

So the real split is:

*   **black-box only** → improve the **agent**
*   **fine-tune access** → improve the **model**
*   **own weights** → improve both aggressively

For your coding-agent goal, the best stack is:

**Layer 1: runtime online improvement**

*   contextual bandit for model/router choice
*   bandit for prompt family selection
*   bandit for decomposition strategy
*   adaptive budgets for retries / self-repair
*   per-repo memory and retrieval optimization

**Layer 2: recursive execution**

*   planner → subtask tree
*   local file-context summarizers
*   recursive patching on file/function/module scopes
*   verifier-guided branch pruning

**Layer 3: verifier-driven self-improvement**

*   compile/tests/lint/security/mutation/static-analysis as reward
*   patch critic + bug-localizer + ranker
*   store successful trajectories and failed trajectories
*   learn which trajectories are worth retrying

This verifier-heavy direction is well aligned with recent work on self-verifying code agents and verifier scaling. [OpenReview+1](https://openreview.net/forum?id=q56ZI1Co43&utm_source=chatgpt.com)

**Layer 4: offline periodic training**  
Use runtime traces to periodically create:

*   eval sets
*   preference pairs
*   successful patch traces
*   decomposition exemplars
*   failure archetypes

Then either:

*   fine-tune the provider-hosted model when available, or
*   distill stronger-model traces into a cheaper model where allowed and supported by the platform. OpenAI’s evals and distillation tooling are meant for this kind of app-level improvement loop. [OpenAI+4OpenAI Developers+4OpenAI Developers+4](https://developers.openai.com/api/docs/guides/evals/?utm_source=chatgpt.com)

The blunt answer:

*   **RL tie-in:** yes, strongly, but mostly as agent-policy RL/bandits
*   **recursive tie-in:** yes, probably very useful for repo-scale coding
*   **diffusive tie-in:** yes, but as iterative refinement, not literal diffusion training
*   **continuous improvement with only black-box GPT APIs:** yes for the system, no for raw model weights
*   **pre + during runtime training of the model itself:** only if the API exposes fine-tuning/RFT; otherwise no

What I’d actually build:

1.  **Trajectory store**  
    Save every coding episode:  
    task, repo hash, retrieved files, prompts, tool calls, outputs, diffs, verifier scores, final outcome.
2.  **Reward model / scorer**  
    Weighted score:  
    `pass_rate + static_quality + regression_safety - latency - tokens - retries - patch_bloat`
3.  **Bandit controller**  
    Choose among:
    *   prompt template
    *   model
    *   context packing strategy
    *   repair loop depth
    *   verifier sequence
4.  **Recursive task engine**  
    Split tasks into:
    *   localization
    *   hypothesis
    *   patch
    *   verify
    *   reduce
    *   finalize
5.  **Patch refiner**  
    Diffusion-style iterative loop:
    *   write rough patch
    *   identify suspicious hunks
    *   regenerate only those hunks
    *   stop on reward plateau
6.  **Periodic distillation/fine-tuning**  
    Weekly or nightly:
    *   synthesize best traces
    *   run evals
    *   fine-tune cheaper coding specialist if allowed

If you try to jump straight to “continuous RL training of GPT itself” through a pure black-box endpoint, that is the wrong mental model. The winning move is to make the **agent shell self-improving**, and only later add provider-side fine-tuning on top.

If you want, I’ll turn this into a concrete architecture for your existing Bifrost / thegent / router stack.

---

**Sources:**

- [Black-Box Prompt Optimization: Aligning Large Language ...](https://aclanthology.org/2024.acl-long.176/?utm_source=chatgpt.com)
- [[2512.24601] Recursive Language Models](https://arxiv.org/abs/2512.24601?utm_source=chatgpt.com)
- [Reinforcement fine-tuning | OpenAI API](https://developers.openai.com/api/docs/guides/reinforcement-fine-tuning/?utm_source=chatgpt.com)
- [Self-Evolving Code Agents via Reliable Self-Verification](https://openreview.net/forum?id=q56ZI1Co43&utm_source=chatgpt.com)

## Prompt:
4/3/2026, 12:15:11 AM

White box gemma 4 qwen<35b w latent Mas spec decode tidar reap if moe and flash attention and other tweaks?

## Response:
4/3/2026, 12:15:11 AM

I’m checking which of those pieces are real, current, and compatible together, because some belong at model architecture level while others are inference-time overlays.

> **Searching for latest Gemma, Qwen, and REAP specs**
>
> [Gemma releases | Google AI for Developers](https://ai.google.dev/gemma/docs/releases)
> [Qwen/Qwen3.5-35B-A3B](https://huggingface.co/Qwen/Qwen3.5-35B-A3B)
> [The Latent Space: Foundation, Evolution, Mechanism ...](https://arxiv.org/html/2604.02029v1)
> [Qwen3.5: Towards Native Multimodal Agents](https://qwen.ai/blog?id=qwen3.5)
>
> **Considering what's needed for model stack evaluation**
>
> The user asks about a complex model stack with various components and tweaks. I'll focus on whether this setup, which might involve "TIDAL" (a possible typo), is viable. I'll search for details on "TIDAR model inference" to get more info and clarify the viability of this stack.
>
> **Searching viability of TIDAR model with optimizations**
>
> [TiDAR: Think in Diffusion, Talk in Autoregression](https://arxiv.org/html/2511.08923v1)
> [togethercomputer/flash-attention-3: Fast and memory ...](https://github.com/togethercomputer/flash-attention-3)
>
> Thought for 20s

Yes, but not as one neat universal stack. Some of those are **drop-in inference upgrades**, some are **training-time architecture choices**, and some only make sense for **homogeneous white-box model families**.

The clean breakdown:

What actually composes well
---------------------------

### Best fit under your constraints

For **white-box open coding agents under ~35B total params**, the strongest practical lane is:

*   **Qwen3.5-35B-A3B** or a REAP derivative as the main model [Hugging Face+1](https://huggingface.co/Qwen/Qwen3.5-35B-A3B?utm_source=chatgpt.com)
*   **speculative decoding** with a smaller draft model from the same family
*   **FlashAttention** / modern paged-attention inference stack
*   **MoE-aware quantization / pruning**
*   **latent-MAS only if the participating agents are same-family or you build cache-translation machinery**
*   **TiDAR is not a bolt-on tweak; it is a model architecture/training choice** [arXiv+1](https://arxiv.org/abs/2511.08923?utm_source=chatgpt.com)

That is the blunt answer.

* * *

Piece by piece
--------------

### 1) Gemma 4

Gemma 4 is real now, with released sizes including E2B, E4B, 31B, and 26B A4B variants. Google positions Gemma 4 as open-weight and deployable/tunable. [Google AI for Developers+2Google AI for Developers+2](https://ai.google.dev/gemma/docs/releases?utm_source=chatgpt.com)

My take:

*   **Gemma 4 is viable** as a white-box base if you want cleaner licensing/Google ecosystem support.
*   But for **coding-agent heavy work**, **Qwen-family open coder variants are still the more natural playground** right now because of ecosystem momentum, variants, and easier MoE/compression experimentation. That is partly inference ecosystem reality, not just raw benchmark worship. [Hugging Face+2Qwen+2](https://huggingface.co/Qwen/Qwen3.5-35B-A3B?utm_source=chatgpt.com)

### 2) Qwen under 35B

Yes. This is the sweet spot.

Relevant current anchor:

*   **Qwen3.5-35B-A3B** exists and is compatible with Transformers, vLLM, SGLang, KTransformers, etc. [Hugging Face](https://huggingface.co/Qwen/Qwen3.5-35B-A3B?utm_source=chatgpt.com)

That matters because it gives you:

*   a strong open-weight base
*   MoE-ish activated-parameter efficiency
*   mature serving options
*   room for speculative decoding and router experiments

If your real constraint is “<35B total” rather than “<35B activated,” this is still one of the most interesting choices because the active footprint is much smaller than the headline parameter count.

### 3) REAP

Yes, **if the model is MoE or MoE-like enough for expert pruning to matter**.

REAP = Router-weighted Expert Activation Pruning. It is not just generic compression. It is specifically useful for MoE families because it prunes redundant experts while trying to preserve routing quality. The Qwen REAP examples and Cerebras REAP models are exactly this story. [Hugging Face+1](https://huggingface.co/cerebras/Qwen3-Coder-REAP-25B-A3B?utm_source=chatgpt.com)

My take:

*   For **Qwen3.5-35B-A3B**, REAP-style variants are very plausible and attractive.
*   For **Gemma 4**, whether REAP is appropriate depends on the exact architecture variant. Not every model family benefits the same way.

So:

*   **Qwen + REAP:** yes, strong fit
*   **Gemma + REAP:** maybe, architecture-dependent

### 4) Speculative decoding

Yes. This is one of the most practical upgrades.

For coding agents, spec decode is useful when:

*   acceptance rate is decent
*   draft model is cheap enough
*   verifier is strong enough
*   your workloads are not dominated by giant-context KV bandwidth bottlenecks

The best practical setup is usually:

*   same-family smaller drafter
*   same tokenizer
*   similar style distribution
*   code-specialized drafter if the verifier is code-specialized

So for example:

*   drafter: smaller Qwen-family code model
*   verifier: Qwen3.5-35B-A3B or REAP-coded variant

That is much more realistic than trying to force cross-family weirdness.

### 5) Latent MAS

Yes, but with an asterisk the size of a building.

LatentMAS-style systems rely on passing latent state such as KV cache or hidden-state-derived structures instead of plain text. Recent work explicitly frames LatentMAS around KV-cache latent reasoning, and related work notes that cross-model latent transfer is much easier in homogeneous settings or with translation modules. [arXiv+2arXiv+2](https://arxiv.org/pdf/2602.03695?utm_source=chatgpt.com)

That means:

*   **same family, same architecture, same tokenizer, same hidden shapes**  
    best case
*   **same family, different size**  
    possible but trickier
*   **Gemma ↔ Qwen latent handoff**  
    ugly unless you build explicit cache/latent translators

So if you want latent MAS:

*   do it **within one family first**
*   ideally within one serving stack
*   probably **Qwen-family to Qwen-family**
*   maybe **Gemma-to-Gemma**
*   not “random mixed open models all throwing KV at each other”

### 6) TiDAR

This is the one people will overread.

**TiDAR is not a serving trick you slap on top of an existing AR model.**  
It is a **hybrid architecture** that combines diffusion-style drafting with autoregressive talking in one model design. The paper reports large throughput gains and exact KV cache support, but that is because the model was built/trained that way. [arXiv](https://arxiv.org/abs/2511.08923?utm_source=chatgpt.com)

So:

*   **Can you add TiDAR to existing Qwen/Gemma?** No, not in the real sense.
*   **Can you imitate the spirit of TiDAR with a diffusion drafter + AR verifier?** Yes, partially.
*   **Can you productionize that today for coding agents?** Maybe experimentally, but it is materially higher risk than standard speculative decoding. DFlash/DEER-type work shows this area is active, but still not the boring/default choice. [arXiv+2arXiv+2](https://arxiv.org/html/2602.06036v1?utm_source=chatgpt.com)

### 7) FlashAttention

Yes, obviously, where supported.

This is table-stakes for white-box efficient serving. FlashAttention remains a core memory/speed improvement path, and newer FA lines are especially relevant on Hopper-class hardware. [GitHub+2GitHub+2](https://github.com/togethercomputer/flash-attention-3?utm_source=chatgpt.com)

Practical reality:

*   **H100/Hopper**: great
*   **consumer GPUs**: still useful, but exact FA version support and wins vary by stack
*   **Mac/MLX**: different story, don’t assume the same FA path

* * *

What I would actually recommend
-------------------------------

Best practical stack right now
------------------------------

### Option A: Most sane

**Qwen3.5-35B-A3B main model**

*   add **speculative decoding**
*   add **REAP variant if stable**
*   run with **FlashAttention / vLLM / SGLang-class serving**
*   latent-MAS only among same-family workers

Why:

*   best overall composability
*   most room for compression and serving tricks
*   strong coding-agent fit
*   less architectural weirdness than trying to make diffusion hybrids your core path

### Option B: Conservative alternative

**Gemma 4 31B or 26B A4B**

*   standard efficient serving
*   spec decode if you can source/train a good same-family drafter
*   latent-MAS only inside Gemma-family experiments
*   skip TiDAR fantasies unless you are doing real model R&D

Why:

*   cleaner family and supported release line
*   likely easier if you want a tighter single-vendor-ish ecosystem
*   less obvious for aggressive MoE pruning tricks than Qwen A3B lane

* * *

What not to do
--------------

Do **not** assume this stack all snaps together:

*   Gemma 4
*   Qwen under 35B
*   latent MAS
*   TiDAR
*   REAP
*   speculative decoding
*   FlashAttention

That is mixing:

*   architecture choices
*   training-time compression
*   inference-time acceleration
*   multi-agent communication protocol design

It is not one feature bundle. It is 4 different layers.

* * *

My actual verdict
-----------------

For **white-box coding agents**, I would rank the paths like this:

1.  **Qwen3.5-35B-A3B + FlashAttention + spec decode + optional REAP**
2.  **Gemma 4 31B + FlashAttention + standard verifier loops**
3.  **latent-MAS inside one family only**
4.  **TiDAR-style hybrid experiments only after the above works**

So the answer is:

*   **Qwen <35B:** yes, strong
*   **Gemma 4:** yes, but less obviously the best coding-agent playground
*   **latent MAS:** yes, but mostly same-family
*   **spec decode:** yes, very worthwhile
*   **REAP:** yes for MoE-style Qwen variants
*   **TiDAR:** not a drop-in; treat as a research branch
*   **FlashAttention:** yes, mandatory where supported

If you want, I’ll turn that into a concrete build matrix for your hardware tiers: **3090 Ti**, **M1 Pro**, and **rented 48 GB GPU**, with which combos are actually worth running.

---

**Sources:**

- [Qwen/Qwen3.5-35B-A3B](https://huggingface.co/Qwen/Qwen3.5-35B-A3B?utm_source=chatgpt.com)
- [TiDAR: Think in Diffusion, Talk in Autoregression](https://arxiv.org/abs/2511.08923?utm_source=chatgpt.com)
- [Gemma releases | Google AI for Developers](https://ai.google.dev/gemma/docs/releases?utm_source=chatgpt.com)
- [togethercomputer/flash-attention-3: Fast and memory ...](https://github.com/togethercomputer/flash-attention-3?utm_source=chatgpt.com)

## Prompt:
4/3/2026, 12:16:53 AM

Think  Claude code agents and their swarms
Research other sota items and experiments as of 20 26 50 of fhem

## Response:
4/3/2026, 12:17:00 AM

I’m pulling together current agentic coding and swarm-style systems, then I’ll compress them into a practical list instead of a pile of hype.

I’ve got the main product-side players and a few benchmark anchors. Next I’m filling the list with the more interesting research directions instead of repeating “another IDE agent.”

> **Searching for 2026 research on coding agents and swarms**
>
> [Cursor Launches a New AI Agent Experience to Take On Claude Code and Codex](https://www.wired.com/story/cusor-launches-coding-agent-openai-anthropic)
> [Anthropic leaked 500,000 lines of its own source code](https://www.axios.com/2026/03/31/anthropic-leaked-source-code-ai)
> [Claude's code: Anthropic leaks source code for AI software engineering tool](https://www.theguardian.com/technology/2026/apr/01/anthropic-claudes-code-leaks-ai)
> [At this AI startup, the engineers became the bosses, and agents do the coding](https://www.businessinsider.com/wayfound-ai-ceo-transforms-engineers-into-ai-managers-2026-3)
> [Anthropic scrambles to contain self-inflicted leak of valuable AI code](https://nypost.com/2026/04/01/business/anthropic-scrambles-to-contain-self-inflicted-leak-of-valuable-ai-code/)
> [What is OpenClaw? Agentic AI that can automate any task](https://www.techradar.com/pro/what-is-openclaw)
> [2026 Agentic Coding Trends Report](https://resources.anthropic.com/hubfs/2026%20Agentic%20Coding%20Trends%20Report.pdf)
> [We Tested 15 AI Coding Agents (2026). Only 3 Changed How ...](https://morphllm.com/ai-coding-agent)
> [Claude Code Swarms: How Multi-Agent Teams Change ...](https://medium.com/coding-nexus/claude-code-swarms-how-multi-agent-teams-change-the-way-we-build-software-bd3d7d89bf09)
> [SWE-bench Leaderboards](https://www.swebench.com/)
> [Best AI Coding Agents in 2026: Ranked and Compared](https://codegen.com/blog/best-ai-coding-agents/)
> [15 Best Claude Code Alternatives: AI Coding Tools (2026)](https://www.taskade.com/blog/claude-code-alternatives)
> [Best LLMs for Coding in 2026: Top 15 Models Compared ...](https://www.edenai.co/post/best-llms-for-coding)
> [Claude Code Alternatives (2026): 11 Tested, 3 That Beat It for ...](https://www.morphllm.com/comparisons/claude-code-alternatives)
> [FeatureBench: Benchmarking Agentic Coding for Complex Feature Development](https://arxiv.org/abs/2602.10975)
> [State of AI Agents 2026: Autonomy is Here](https://www.prosus.com/news-insights/2026/state-of-ai-agents-2026-autonomy-is-here)
>
> **Collecting info for Claude code swarms**
>
> I need 50 items, maybe starting with research, benchmarks, and product tools. I'll focus on experiments related to Claude code swarms. I'll organize these into categories like agent tools, multi-agent frameworks, benchmarks, runtime techniques, and experiments. Reliable sources are crucial, so I'll target product docs, official pages, and academic papers for a thorough search.
>
> **Searching for Claude code multi-agent tools and experiments**
>
> [2026 Agentic Coding Trends Report](https://resources.anthropic.com/hubfs/2026%20Agentic%20Coding%20Trends%20Report.pdf)
> [Introducing Codex](https://openai.com/index/introducing-codex/)
> [Best practices for coding with agents](https://cursor.com/blog/agent-best-practices)
> [SWE-agent takes a GitHub issue and tries ...](https://github.com/swe-agent/swe-agent)
> [Claude Code | Anthropic's agentic coding system](https://www.anthropic.com/product/claude-code)
> [Cursor CLI (Jan 16, 2026): CLI Agent Modes and Cloud ...](https://forum.cursor.com/t/cursor-cli-jan-16-2026-cli-agent-modes-and-cloud-handoff/149171)
> [Tips and Tricks for using Codex](https://community.openai.com/t/tips-and-tricks-for-using-codex/1373143)
>
> **Searching for benchmark papers on agentic coding**
>
> [FeatureBench: Benchmarking Agentic Coding for Complex Feature Development](https://arxiv.org/abs/2602.10975)
> [Multiagent Systems Feb 2026](https://www.arxiv.org/list/cs.MA/2026-02?show=50&skip=150)
>
> **Gathering 50 relevant items on AI tools**
>
> I need about 50 items, likely from product docs, papers, and benchmarks. I'll look into recent news on tools like Cursor, Claude, Codex, plus possibly Gemini CLI and Devin. Official pages will be helpful for accurate, up-to-date info. Time to focus on searching specific products and related sources.
>
> **Searching for recent product and benchmark updates**
>
> [Developer's Guide to Building ADK Agents with Skills](https://developers.googleblog.com/developers-guide-to-building-adk-agents-with-skills/)
> [Devin can now Manage Devins](https://cognition.ai/blog/devin-can-now-manage-devins)
> [aider is AI pair programming in your terminal](https://github.com/aider-ai/aider)
> [Cline - AI Coding, Open Source and Uncompromised](https://cline.bot/)
>
> **Considering additional relevant tools for search**
>
> I’m thinking about possibly including MetaGPT, OpenHands, and OpenDevin in my search. These might fit well with the other tools I’m looking into. I’ll need to check for recent updates or news on these to make sure they’re part of the context I’m gathering.
>
> **Searching GitHub for MetaGPT, OpenHands, OpenDevin**
>
> [OpenHands: AI-Driven Development](https://github.com/OpenHands/OpenHands)
>
> **Gathering 50 items with benchmarks and research**
>
> I need to gather 50 relevant items, possibly including benchmarks like CodeClash, SWE-bench mutated, Code Review Agent Benchmark, and others. I also need to look into current models, not just systems. I’ll focus on benchmarks and research experiments to ensure a wide range of relevant and up-to-date information.
>
> **Searching benchmarks and research experiments for software models**
>
> [SWE-bench Leaderboards](https://www.swebench.com/)
> [SWE-bench/SWE-smith: [NeurIPS 2025 D&B Spotlight] ...](https://github.com/SWE-bench/SWE-smith)
> [Huxley-Gödel Machine: Human-Level Coding Agent ...](https://arxiv.org/abs/2510.21614)
>
> **Organizing 50 relevant items with sources**
>
> I’ll gather 50 top items and experiments, including systems, benchmarks, and research techniques. I plan to categorize these with concise notes for each. I'll use citations for all factual claims, preferably from official pages and arXiv. I'll organize them into product/systems, benchmarks, and research sections, ensuring accuracy and support for claims. I'll reference sources like Anthropic and OpenAI pages, Cursor, Gemini CLI, and others for the most reliable data. I might use a numbered list to keep it clear.
>
> **Compiling benchmarks and research**
>
> I’ll include several benchmarks like SWE-bench, CodeClash, and others, while keeping evaluations such as Task-Level Performance Prediction in mind. I might mention SWE-rebench V2, but only if I have a direct source. For research, I’ll focus on topics like agent primitives, LatentMem, speculative decoding RL, and other advanced techniques, searching for relevant, up-to-date sources.
>
> **Compiling products, benchmarks, research, and citations**
>
> [[2504.15228] A Self-Improving Coding Agent](https://arxiv.org/abs/2504.15228)
> [A Self-Improving Coding Agent (Apr 2025)](https://www.youtube.com/watch?v=n-MrHiY8ga4)
> [Toward Training Superintelligent Software Agents through ...](https://alphaxiv.org/overview/2512.18552v1)
> [Self-Improving Coding Agent (SICA)](https://www.emergentmind.com/topics/self-improving-coding-agent-sica)
> [Toward Training Superintelligent Software Agents through ...](https://www.facebook.com/groups/DeepNetGroup/posts/2686724418387090/)
> [Better Ways to Build Self-Improving AI Agents](https://yoheinakajima.com/better-ways-to-build-self-improving-ai-agents/)
>
> **Exploring agentic systems and experiments**
>
> I think I should search for terms like "AlphaEvolve," "ADAS," and "Agentless" to cover more ground. The user asked for SOTA items and experiments as of 2026, so I’ll focus not only on coding agents but also related agentic systems. I’ll look up additional sources to make sure I’m thorough.
>
> **Searching for AlphaEvolve, ADAS, and agentic systems**
>
> [AlphaEvolve: A coding agent for scientific and algorithmic ...](https://arxiv.org/abs/2506.13131)
>
> **Organizing the 50 items with citations**
>
> I’m planning to put together a list of 50 relevant items, grouped by categories. It’ll have concise one-liners with citations after each bullet. To make it manageable, I'll prioritize the top 10 most relevant items, starting with “For Claude, Code swarms specifically.” I’ll ensure all sources are accurate, including specific dates when available. The goal is to make it dense but useful.
>
> Thought for 1m 56s

Here’s the **50-item research + build list** I’d actually review for **Claude Code–style coding agents and swarms** as of **April 3, 2026**.

I’m biasing toward things that are either:

*   directly useful for **multi-agent coding/swarm orchestration**,
*   strong **benchmarks / training data** for SWE agents,
*   or real **research directions** that can change how you build the stack.

The 10 I’d read first
---------------------

1.  **Anthropic – Claude Code**: baseline reference point for terminal-first agentic coding. [Anthropic](https://www.anthropic.com/product/claude-code?utm_source=chatgpt.com)
2.  **Anthropic – 2026 Agentic Coding Trends Report**: especially the “single agents evolve into coordinated teams” framing. [Anthropic Resources+1](https://resources.anthropic.com/2026-agentic-coding-trends-report?utm_source=chatgpt.com)
3.  **Anthropic – Building a C compiler with a team of parallel Claudes**: concrete large-scope swarm case study; 16 agents, ~2,000 sessions, real cost/scale data. [Anthropic](https://www.anthropic.com/engineering/building-c-compiler?utm_source=chatgpt.com)
4.  **OpenAI – Codex app / coordinated teams of agents**: one of the cleanest product signals that supervised swarms are mainstream now. [OpenAI](https://openai.com/index/introducing-the-codex-app/?utm_source=chatgpt.com)
5.  **Cursor – Scaling long-running autonomous coding**: useful if you care about week-long runs, cloud handoff, and repo-scale operation. [Cursor+1](https://cursor.com/product?utm_source=chatgpt.com)
6.  **Cognition – Devin can now Manage Devins**: explicit manager-worker swarm model with isolated VMs. [Cognition](https://cognition.ai/blog/devin-can-now-manage-devins?utm_source=chatgpt.com)
7.  **FeatureBench**: great reality check because agents that score well on SWE-bench can still crater on feature-level work. [arXiv](https://arxiv.org/abs/2602.10975?utm_source=chatgpt.com)
8.  **SlopCodeBench**: probably the most important “don’t get fooled by pass-rate” benchmark this year. [arXiv](https://arxiv.org/abs/2603.24755?utm_source=chatgpt.com)
9.  **SWE-smith**: strongest current direction for scalable SWE-agent data generation/training. [GitHub](https://github.com/SWE-bench/SWE-smith?utm_source=chatgpt.com)
10.  **Self-Play SWE-RL**: the clearest “continuous improvement without human issue labels” paper in the SWE-agent lane. [arXiv](https://arxiv.org/abs/2512.18552?utm_source=chatgpt.com)

50 items worth studying
-----------------------

### A. Product systems and swarm-capable coding agents

1.  **Claude Code** — Anthropic’s core agentic coding system. [Anthropic](https://www.anthropic.com/product/claude-code?utm_source=chatgpt.com)
2.  **Anthropic 2026 Agentic Coding Trends Report** — coordinated teams, changing roles, and enterprise adoption patterns. [Anthropic Resources+1](https://resources.anthropic.com/2026-agentic-coding-trends-report?utm_source=chatgpt.com)
3.  **Parallel Claudes C compiler experiment** — the most concrete published Claude-code swarm case study. [Anthropic](https://www.anthropic.com/engineering/building-c-compiler?utm_source=chatgpt.com)
4.  **Long-running Claude for scientific computing** — persistent-memory and multi-day workflow patterns that transfer well to coding agents. [Anthropic](https://www.anthropic.com/research/long-running-Claude?utm_source=chatgpt.com)
5.  **Codex (OpenAI)** — cloud SWE agent with many tasks in parallel. [OpenAI](https://openai.com/index/introducing-codex/?utm_source=chatgpt.com)
6.  **Codex app** — OpenAI’s “supervising coordinated teams of agents” framing. [OpenAI](https://openai.com/index/introducing-the-codex-app/?utm_source=chatgpt.com)
7.  **Codex harness / App Server** — useful if you care about embedding a coding-agent runtime cleanly. [OpenAI](https://openai.com/index/unlocking-the-codex-harness/?utm_source=chatgpt.com)
8.  **Cursor Agent** — current mainstream IDE-native agent competitor. [Cursor](https://cursor.com/?utm_source=chatgpt.com)
9.  **Cursor research: scaling long-running autonomous coding** — relevant for long-lived workers and shared indexing. [Cursor](https://cursor.com/product?utm_source=chatgpt.com)
10.  **Cursor Automations** — always-on agents triggered by events or schedules. [Cursor](https://cursor.com/blog/automations?utm_source=chatgpt.com)
11.  **Cursor CLI agent modes + cloud handoff** — useful terminal/cloud split pattern. [Cursor - Community Forum](https://forum.cursor.com/t/cursor-cli-jan-16-2026-cli-agent-modes-and-cloud-handoff/149171?utm_source=chatgpt.com)
12.  **Devin** — still one of the main “AI teammate” cloud agent products. [Cognition+1](https://cognition.ai/blog/how-cognition-uses-devin-to-build-devin?utm_source=chatgpt.com)
13.  **Devin can now Manage Devins** — explicit manager/subagent hierarchy. [Cognition](https://cognition.ai/blog/devin-can-now-manage-devins?utm_source=chatgpt.com)
14.  **Devin can now Schedule Devins** — useful for recurring backlog / maintenance swarms. [Cognition](https://cognition.ai/blog/devin-can-now-schedule-devins?utm_source=chatgpt.com)
15.  **How Cognition Uses Devin to Build Devin** — operational patterns, task sizing, and usage model. [Cognition](https://cognition.ai/blog/how-cognition-uses-devin-to-build-devin?utm_source=chatgpt.com)
16.  **Gemini CLI Plan Mode** — read-only planning phase before action; good for safer decomposition. [Google Developers Blog](https://developers.googleblog.com/plan-mode-now-available-in-gemini-cli/?utm_source=chatgpt.com)
17.  **Gemini CLI Conductor** — context-driven development/orchestration layer. [Google Developers Blog](https://developers.googleblog.com/conductor-introducing-context-driven-development-for-gemini-cli/?utm_source=chatgpt.com)
18.  **Gemini CLI Hooks** — interceptors around the agent loop for policy/control. [Google Developers Blog](https://developers.googleblog.com/tailor-gemini-cli-to-your-workflow-with-hooks/?utm_source=chatgpt.com)
19.  **Cline** — strong open-source coding agent with Plan/Act modes and MCP emphasis. [Cline](https://cline.bot/?utm_source=chatgpt.com)
20.  **Cline Kanban** — explicit multi-agent orchestration product for parallel coding work. [Cline](https://cline.bot/blog/announcing-kanban?utm_source=chatgpt.com)
21.  **Aider** — still the cleanest terminal-first local-repo pair programmer baseline. [GitHub](https://github.com/aider-ai/aider?utm_source=chatgpt.com)
22.  **OpenHands** — open development-agent platform; SDK claims local and cloud scaling to large agent counts. [GitHub+1](https://github.com/OpenHands/OpenHands?utm_source=chatgpt.com)
23.  **MetaGPT / MGX** — “AI software company” workflow pattern; still relevant as a role-based multi-agent reference. [GitHub](https://github.com/geekan/MetaGPT/blob/main/README.md?utm_source=chatgpt.com)
24.  **SWE-agent** — foundational open framework for issue-solving agents. [GitHub](https://github.com/swe-agent/swe-agent?utm_source=chatgpt.com)
25.  **mini-SWE-agent** — important because it shows how far simple scaffolding can go. [GitHub+1](https://github.com/SWE-agent/mini-swe-agent?spm=a2c6h.13046898.publish-article.6.14286ffa9ItVbO&utm_source=chatgpt.com)
26.  **Codeflash** — not a general swarm framework, but highly relevant for automated performance-improvement loops in Python-heavy repos. [GitHub](https://github.com/codeflash-ai/codeflash?utm_source=chatgpt.com)

### B. Benchmarks, datasets, and training/eval infrastructure

27.  **SWE-bench** — still the canonical repo-issue benchmark. [GitHub](https://github.com/swe-bench/SWE-bench?utm_source=chatgpt.com)
28.  **SWE-bench leaderboard** — useful for tracking what agent scaffolds are actually landing. [SWE-bench](https://www.swebench.com/?utm_source=chatgpt.com)
29.  **FeatureBench** — evaluates end-to-end feature development rather than one-shot patching. [arXiv](https://arxiv.org/abs/2602.10975?utm_source=chatgpt.com)
30.  **SlopCodeBench** — measures long-horizon degradation, verbosity, and structural erosion. [arXiv](https://arxiv.org/abs/2603.24755?utm_source=chatgpt.com)
31.  **CodeClash** — goal-oriented SWE benchmark rather than narrowly task-oriented eval. [GitHub+1](https://github.com/codeclash-ai/codeclash?utm_source=chatgpt.com)
32.  **SWE-smith** — toolkit for generating training data / SWE gyms from repos. [GitHub](https://github.com/SWE-bench/SWE-smith?utm_source=chatgpt.com)
33.  **SWE-smith JavaScript expansion** — important signal that the ecosystem is moving beyond Python-only training. [SWE-bench](https://www.swebench.com/post-260113-swesmith-javascript.html?utm_source=chatgpt.com)
34.  **SWE-Factory** — automated factory for issue-resolution training data and benchmarks. [GitHub](https://github.com/deepsoftwareanalytics/swe-factory?utm_source=chatgpt.com)
35.  **SWE-Playground** — fully automated synthetic task and unit-test generation for coding-agent training. [GitHub](https://github.com/neulab/SWE-Playground?utm_source=chatgpt.com)
36.  **SWE-Bench-Mutated** — benchmark mutation approach to reduce contamination / overfitting artifacts. [GitHub](https://github.com/microsoft/SWE-Bench-Mutated-CAIN26?utm_source=chatgpt.com)
37.  **Code Review Agent Benchmark** — code-writing is not enough; review/QA needs its own eval. [arXiv+1](https://arxiv.org/abs/2603.23448?utm_source=chatgpt.com)
38.  **OmniCode** — broader benchmark for software engineering agents. [arXiv](https://arxiv.org/abs/2602.02262?utm_source=chatgpt.com)
39.  **SWE-CI** — benchmarking agents in CI maintenance/settings. [arXiv](https://arxiv.org/html/2603.03823v4?utm_source=chatgpt.com)
40.  **SWE-Next** — scalable real-world SWE tasks for agents. [arXiv](https://arxiv.org/abs/2603.20691?utm_source=chatgpt.com)
41.  **SWE-Universe** — scalable verifiable environments built from GitHub PRs. [arXiv](https://arxiv.org/pdf/2602.02361?utm_source=chatgpt.com)
42.  **daVinci-Env** — open SWE environment synthesis at scale. [arXiv](https://arxiv.org/html/2603.13023v2?utm_source=chatgpt.com)
43.  **Scale-SWE-Data / Immersion in the GitHub Universe** — 100k verified real-world instances is a serious data point. [arXiv](https://arxiv.org/html/2602.09892v4?utm_source=chatgpt.com)
44.  **Task-Level Performance Prediction in Agentic Coding** — worth watching if you want adaptive routing / early-stop / budget control. [arXiv](https://arxiv.org/html/2604.00594v1?utm_source=chatgpt.com)

### C. Research directions and experiments that could matter a lot

45.  **SICA — A Self-Improving Coding Agent** — direct self-modification of the agent codebase. [arXiv+1](https://arxiv.org/abs/2504.15228?utm_source=chatgpt.com)
46.  **Self-Play SWE-RL** — autonomous bug injection + repair for RL training without human-labeled issues/tests. [arXiv+1](https://arxiv.org/abs/2512.18552?utm_source=chatgpt.com)
47.  **SWE-World** — software agents trained/evaluated with simulated execution rather than full physical execution. [arXiv+1](https://arxiv.org/abs/2602.03419?utm_source=chatgpt.com)
48.  **SGAgent** — suggestion-guided multi-agent repository-level software repair. [arXiv](https://arxiv.org/abs/2602.23647?utm_source=chatgpt.com)
49.  **Agent Primitives** — reusable latent building blocks for multi-agent systems; relevant to latent-MAS ideas. [arXiv+1](https://arxiv.org/abs/2602.03695?utm_source=chatgpt.com)
50.  **LatentMem** — customizable latent memory for MAS; relevant if you want agents communicating through compressed internal state rather than pure text. [arXiv](https://arxiv.org/abs/2602.03036?utm_source=chatgpt.com)

Five more that narrowly missed the 50 but are worth it
------------------------------------------------------

These are not filler; they just barely lost the cut:

*   **Vision Wormhole** — latent-space communication across heterogeneous agents; useful if you want cross-model latent handoff instead of same-family-only latent MAS. [arXiv](https://arxiv.org/abs/2602.15382?utm_source=chatgpt.com)
*   **ACE (Agentic Context Engineering)** — one of the most practical “self-improvement without weight updates” directions. [arXiv+1](https://arxiv.org/abs/2510.04618?utm_source=chatgpt.com)
*   **AlphaEvolve** — evolutionary coding agent for scientific/algorithmic work; less directly “PR agent,” but very relevant to autonomous code improvement. [arXiv](https://arxiv.org/abs/2506.13131?utm_source=chatgpt.com)
*   **CodeEvolve** — open-source evolutionary coding framework inspired by that lane. [arXiv+1](https://arxiv.org/abs/2510.14150?utm_source=chatgpt.com)
*   **ADAS** — automated design of agentic systems; useful if you want the swarm architecture itself to be searched/generated. [arXiv+1](https://arxiv.org/abs/2408.08435?utm_source=chatgpt.com)

What I think actually matters for your use case
-----------------------------------------------

If your target is **Claude Code agents and swarms for real repo work**, the biggest ideas right now are:

*   **Manager-worker swarms** are no longer speculative; Anthropic, OpenAI, Cognition, Cursor, and Cline are all converging on coordinated parallel agents in different forms. [Cline+4OpenAI+4Anthropic+4](https://openai.com/index/introducing-the-codex-app/?utm_source=chatgpt.com)
*   **Benchmark inflation is real**. A system can look great on SWE-bench and still fall apart on feature development or long iterative extension. FeatureBench and SlopCodeBench are the cleanest proof of that. [arXiv+1](https://arxiv.org/abs/2602.10975?utm_source=chatgpt.com)
*   **The next real moat is not the base model alone**. It is data generation, evaluator quality, long-horizon orchestration, and online improvement loops. SWE-smith, SWE-Factory, SWE-Playground, Self-Play SWE-RL, and ACE all point in that direction. [arXiv+4GitHub+4GitHub+4](https://github.com/SWE-bench/SWE-smith?utm_source=chatgpt.com)
*   **Latent communication is promising but not yet boring infrastructure**. Agent Primitives, LatentMem, and related work are interesting, but today’s practical wins still mostly come from better decomposition, memory, verifiers, and orchestration. [arXiv+2arXiv+2](https://arxiv.org/abs/2602.03695?utm_source=chatgpt.com)

Recent product/news context around the category is also moving fast, including Cursor’s newer agent push and public scrutiny around Claude Code after Anthropic’s source leak. [WIRED+2Axios+2](https://www.wired.com/story/cusor-launches-coding-agent-openai-anthropic?utm_source=chatgpt.com)

[

![Cursor Launches a New AI Agent Experience to Take On Claude Code and Codex](https://images.openai.com/static-rsc-1/tnSHf3QeZnsQDZfpZp-I3-SCoIVzr1vZcRUMFj-Y3Gz0AEZLHc8Zp4YWNesnlG0aZmF4hn5I2fJ51w6W7N7jOFTLfCz9VfKWCimATE-ZcMyzc81jS3DpKfo2iYNPEC6tG0h9ccsRhxPIS8w-31mY2EliYqpVgMNitohVuedWNL_ivCFUGx9HcB_rswrRCMhcGt6XweMQM7CYkW9AD9fUbl3hHCLeMr1Z2d-8sbM7Jcc)

![](https://www.google.com/s2/favicons?domain=https://www.wired.com&sz=32)

WIRED

Cursor Launches a New AI Agent Experience to Take On Claude Code and Codex

18 days ago

](https://www.wired.com/story/cusor-launches-coding-agent-openai-anthropic?utm_source=chatgpt.com)

[

![Anthropic leaked 500,000 lines of its own source code](https://images.openai.com/static-rsc-1/q2A-zCGxyHv3wNIJQf6M4RY3UnhWrzXqpOl3XD-hlq3mlO_ynt_kxna4iODtqaEpci_7rjsGfXTQN1WSNskqcf8frZ3PvvTlQ7KasDe-UiksVUZFE7QmRvBmbmL_g4ydlA5NWc5dgd9HlYif3N2QCdpNsO86k_c8R5F9i_MGD7s)

![](https://www.google.com/s2/favicons?domain=https://www.axios.com&sz=32)

Axios

Anthropic leaked 500,000 lines of its own source code

20 days ago

](https://www.axios.com/2026/03/31/anthropic-leaked-source-code-ai?utm_source=chatgpt.com)

[

![At this AI startup, the engineers became the bosses, and agents do the coding](https://images.openai.com/static-rsc-1/dUvAafrWXXZvfDQvu2o8Qo8_D9pu_hEPf59Y1-1ALhsMUXcjtu0xH_VTCj5-3b1WHyWZL3GjrAsDaFSrgEAUur07SsLD5uFJw6DGMnE8DUHWIuz_Y3E9TFf5bs8WK4Jx)

![](https://www.google.com/s2/favicons?domain=https://www.businessinsider.com&sz=32)

Business Insider

At this AI startup, the engineers became the bosses, and agents do the coding

24 days ago

](https://www.businessinsider.com/wayfound-ai-ceo-transforms-engineers-into-ai-managers-2026-3?utm_source=chatgpt.com)

The blunt takeaway: if you want to build a serious swarm stack in 2026, don’t copy just one tool. Steal from **Claude Code / Codex / Cursor / Devin** for orchestration patterns, then ground your eval and training loop in **FeatureBench / SlopCodeBench / SWE-smith / Self-Play SWE-RL**.

---

**Sources:**

- [Claude Code | Anthropic's agentic coding system](https://www.anthropic.com/product/claude-code?utm_source=chatgpt.com)
- [2026 Agentic Coding Trends Report](https://resources.anthropic.com/2026-agentic-coding-trends-report?utm_source=chatgpt.com)
- [Introducing the Codex app](https://openai.com/index/introducing-the-codex-app/?utm_source=chatgpt.com)
- [Cursor · Agent](https://cursor.com/product?utm_source=chatgpt.com)
- [Devin can now Manage Devins](https://cognition.ai/blog/devin-can-now-manage-devins?utm_source=chatgpt.com)
- [FeatureBench: Benchmarking Agentic Coding for Complex Feature Development](https://arxiv.org/abs/2602.10975?utm_source=chatgpt.com)
- [SWE-bench/SWE-smith: [NeurIPS 2025 D&B Spotlight] ...](https://github.com/SWE-bench/SWE-smith?utm_source=chatgpt.com)
- [Cursor CLI (Jan 16, 2026): CLI Agent Modes and Cloud ...](https://forum.cursor.com/t/cursor-cli-jan-16-2026-cli-agent-modes-and-cloud-handoff/149171?utm_source=chatgpt.com)
- [Plan mode is now available in Gemini CLI](https://developers.googleblog.com/plan-mode-now-available-in-gemini-cli/?utm_source=chatgpt.com)
- [Cline - AI Coding, Open Source and Uncompromised](https://cline.bot/?utm_source=chatgpt.com)
- [SWE-bench Leaderboards](https://www.swebench.com/?utm_source=chatgpt.com)
- [Cursor Launches a New AI Agent Experience to Take On Claude Code and Codex](https://www.wired.com/story/cusor-launches-coding-agent-openai-anthropic?utm_source=chatgpt.com)

## Prompt:
4/3/2026, 3:25:33 AM

Items like reap, eoq, sft, flash attn and tidar + latentmas and spec decode I meant

## Response:
4/3/2026, 3:25:36 AM

I’m checking the exact 2026 meaning of each item, especially EOQ, so I don’t mash together unrelated model, training, and serving concepts.

> **Browsing for 2026 research on Claude agents and techniques**
>
> ['A high-speed digital cheat sheet': Google unveils TurboQuant AI-compression algorithm, which it claims can hugely reduce LLM memory usage](https://www.techradar.com/pro/a-high-speed-digital-cheat-sheet-google-unveils-turboquant-ai-compression-algorithm-which-it-claims-can-hugely-reduce-llm-memory-usage)
> [REAP: Router-weighted Expert Activation Pruning for ...](https://github.com/CerebrasResearch/reap)
> [TiDAR: Think in Diffusion, Talk in Autoregression](https://arxiv.org/html/2511.08923v1)
> [README.md · 0xSero/Qwen-3.5-28B-A3B-REAP at main](https://huggingface.co/0xSero/Qwen-3.5-28B-A3B-REAP/blob/main/README.md)
> [Start of 2026 what's the best open coding model?](https://www.reddit.com/r/LocalLLaMA/comments/1q82ae8/start_of_2026_whats_the_best_open_coding_model/)
> [Live MoE Expert Pruning in vLLM - DGX Spark / GB10](https://forums.developer.nvidia.com/t/why-you-should-reap-it-yourself-live-moe-expert-pruning-in-vllm/364098)
> [Google TurboQuant: 2026 LLM Compression Guide - O-mega.ai](https://o-mega.ai/articles/google-turboquant-the-2026-llm-compression-guide)
> [Breaking Free from Text: How LatentMAS Enables Multi- ...](https://medium.com/towardsdev/breaking-free-from-text-how-latentmas-enables-multi-agent-ai-systems-to-think-purely-in-a7b9fa58bbe5)
> [Optimizing LLMs for Performance and Accuracy with Post- ...](https://developer.nvidia.com/blog/optimizing-llms-for-performance-and-accuracy-with-post-training-quantization/)
> [(PDF) Latent Collaboration in Multi-Agent Systems](https://www.researchgate.net/publication/397983060_Latent_Collaboration_in_Multi-Agent_Systems)
> [REAP: One-Shot Pruning for Trillion-Parameter Mixture-of- ...](https://www.cerebras.ai/blog/reap)
> [Quantization of LLM Models: Model Compression ...](https://www.linkedin.com/pulse/quantization-llm-models-model-compression-strategies-reducing-matani-6x3ff)
> [The Invisible AI Threat: Latent Collaboration's Efficiency ...](https://kenhuangus.substack.com/p/latentmas-ai-agents-collaborate-at)
> [Codebook Lossless LLM Compression: 10–25%+ RAM ...](https://bigattichouse.medium.com/codebook-lossless-llm-compression-10-25-ram-reduction-with-bitwise-generic-packing-of-indexed-c35ba49fc2b8)
> [Model Compression Is Unlocking On-Premises AI Agents](https://ibl.ai/blog/model-compression-on-premises-ai-agents-2026)
>
> **Searching for EOQ and LLM model references**
>
> [Mastering Demand Forecasting in 2026](https://www.impactanalytics.ai/blog/demand-forecasting)
> [Extending the EOQ Model: A Mathematical Framework for ...](https://eajournals.org/ijmss/vol13-issue-1-2025/extending-the-eoq-model-a-mathematical-framework-for-incorporating-real-world-constraints/)
> [StreamingThinker: Large Language Models Can Think ...](https://arxiv.org/html/2510.17238v1)
> [Challenges of Inventory Management​ in 2026- USA Guide](https://www.hakunamatatatech.com/our-resources/blog/top-7-inventory-management-challenges-solutions)
> [A Comparison Between GPT-4, LlaMA-2 and Gemini](https://www.ijimai.org/index.php/ijimai/article/download/858/917/4898)
> [How I Built Supply Chain Optimization Using AI Agents](https://medium.com/%40learn-simplified/how-i-built-supply-chain-optimization-using-ai-agents-84339654938c)
> [(PDF) Book Chapter AN OVERVIEW OF EOQ INVENTORY ...](https://www.researchgate.net/publication/403038430_Book_Chapter_AN_OVERVIEW_OF_EOQ_INVENTORY_MODEL_FOR_GOODS_WITH_DEMAND_FORECASTING_APPROACH)
> [Quantization-Aware Training for Domain Generalization](https://icml.cc/virtual/2025/poster/45444)
> [LARGE LANGUAGE MODELS CAN THINK WHILE READING](https://openreview.net/pdf?id=10Iiew095e)
> [Order quantity optimization model for perishable products ...](https://www.sciencedirect.com/science/article/pii/S0305048325001185)
> [Enabling Conversational Interaction with Mobile UI using ...](https://dl.acm.org/doi/10.1145/3544548.3580895)
> [Mathematics, Volume 12, Issue 23 (December-1 2024)](https://www.mdpi.com/2227-7390/12/23)
> [Inventory Optimization Beyond EOQ: A Mathematical ...](https://www.linkedin.com/posts/knaidu1_inventoryoptimization-supplychainanalytics-activity-7409496980424581120-UYix)
> [EOQ model for deteriorating items with exponential ...](https://fs.unm.edu/nss8/index.php/111/article/view/7340)
> [caiovicentino1/Qwen3.5-27B-PolarQuant-Q5](https://huggingface.co/caiovicentino1/Qwen3.5-27B-PolarQuant-Q5)
> [Leveraging large language models for human-AI collaborative ...](https://link.springer.com/article/10.1007/s44443-025-00458-9)
> [Re-examining optimal ordering policies in a two-warehouse ...](https://academic.oup.com/imaman/advance-article-abstract/doi/10.1093/imaman/dpag004/8471180)
> [Large Language Models Can Think While Reading](https://www.alphaxiv.org/overview/2510.17238v1)
> [Integrating EOQ and ARIMA for Data-Driven Learning](https://edutech-journals.org/index.php/j-hytel/article/view/218)
>
> **Clarifying technical terms and sources**
>
> I’m trying to figure out what exactly the user meant with “EOQ." It might be about quantization, or something specific to collection. If possible, I should avoid asking unnecessary questions but offer possible expansions. I'll mention SFT and Flash Attention, and maybe refer to official documentation or papers on these, possibly searching for methods related to runtime, training techniques, and efficiency. I'll also clarify any mention of latentMAS and speculative decoding.
>
> **Searching for sources on FlashAttention and decoding techniques**
>
> [Dao-AILab/flash-attention: Fast and memory-efficient ...](https://github.com/dao-ailab/flash-attention)
> [An Introduction to Speculative Decoding for Reducing ...](https://developer.nvidia.com/blog/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference/)
> [Supervised fine-tuning | OpenAI API](https://developers.openai.com/api/docs/guides/supervised-fine-tuning/)
> [Speculative Decoding - vLLM](https://docs.vllm.ai/en/latest/features/speculative_decoding/)
> [Speculative speculative decoding - DGX Spark / GB10](https://forums.developer.nvidia.com/t/speculative-speculative-decoding/362599)
> [Speculative Decoding: Achieving 2-3x LLM Inference Speedup](https://introl.com/blog/speculative-decoding-llm-inference-speedup-guide-2025)
> [LLM Fine-Tuning: The Complete Guide to Customizing ...](https://beltsys.com/en/blog/llm-fine-tuning-complete-guide/)
> [LLM Performance and AI Hardware: 2023–2025 ...](https://medium.com/%40olku/llm-performance-and-ai-hardware-2023-2025-breakthroughs-fa3a1f8dc505)
> [vLLM Production Deployment: Complete 2026 Guide](https://www.sitepoint.com/vllm-production-deployment-guide-2026/)
> [Accelerating LLM Inference on NVIDIA GPUs with ReDrafter](https://machinelearning.apple.com/research/redrafter-nvidia-tensorrt-llm)
>
> Thought for 26s

Got it — you meant **technique-level knobs**, not product names.

For **Claude Code–style coding agents and swarms**, I’d bucket the meaningful 2026 knobs like this:

1\. Strongly practical right now
--------------------------------

**FlashAttention**  
This is still table-stakes for efficient white-box transformer serving. The official repo remains the reference implementation for FlashAttention / FlashAttention-2, and newer FA4 prereleases are active in 2026. [GitHub+1](https://github.com/dao-ailab/flash-attention?utm_source=chatgpt.com)

**Speculative decoding**  
This is one of the most practical latency reducers for code agents. vLLM documents it as useful for reducing inter-token latency on medium-to-low QPS, memory-bound workloads, and its speculators docs describe roughly 2–3× faster token generation in good cases. NVIDIA likewise frames it as parallel draft-and-verify acceleration rather than a quality change. [vLLM+2vLLM+2](https://docs.vllm.ai/en/latest/features/speculative_decoding/?utm_source=chatgpt.com)

**SFT**  
Supervised fine-tuning is still the boring, reliable customization tool when you want a coding model to better match patch style, tool-call formatting, repo conventions, or decomposition patterns. OpenAI’s docs describe SFT as training on example inputs and known-good outputs to improve reliability and efficiency for a task. [OpenAI Developers+2OpenAI Developers+2](https://developers.openai.com/api/docs/guides/supervised-fine-tuning/?utm_source=chatgpt.com)

**REAP**  
REAP is real and relevant if you are in the **MoE lane**. Cerebras describes it as Router-weighted Expert Activation Pruning, and recent public REAP-compressed Qwen-family coder checkpoints show it being used to prune experts while preserving much of coding ability. [Hugging Face+3GitHub+3Cerebras+3](https://github.com/CerebrasResearch/reap?utm_source=chatgpt.com)

2\. Real, promising, but not “boring infrastructure” yet
--------------------------------------------------------

**LatentMAS**  
LatentMAS is a training-free framework for multi-agent collaboration in latent space instead of text, with a shared latent working memory and last-layer hidden-state exchange. It is very relevant to swarm design, but it is still researchy, and the cleanest use case is same-family or closely compatible models. [arXiv+2arXiv+2](https://arxiv.org/abs/2511.20639?utm_source=chatgpt.com)

**TiDAR**  
TiDAR is not just a serving trick. The paper presents it as a hybrid model that “thinks in diffusion, talks in autoregression,” with parallel drafting plus exact KV-cache support, and reports higher throughput than speculative decoding in its evaluated settings. That makes it interesting, but it is an **architecture/training path**, not something you cleanly bolt onto an existing Qwen/Gemma checkpoint. [arXiv](https://arxiv.org/html/2511.08923v1?utm_source=chatgpt.com)

3\. Adjacent knobs that matter a lot for coding swarms
------------------------------------------------------

**KV-cache compression / quantization**  
Google’s TurboQuant is the current noteworthy item here: it targets KV cache memory directly, can work without retraining, and aims to reduce cache memory substantially while preserving attention quality. That matters a lot for long-context coding agents and multi-agent concurrency. [TechRadar+1](https://www.techradar.com/pro/a-high-speed-digital-cheat-sheet-google-unveils-turboquant-ai-compression-algorithm-which-it-claims-can-hugely-reduce-llm-memory-usage?utm_source=chatgpt.com)

**Post-training quantization generally**  
NVIDIA’s post-training quantization writeup reflects the current reality: quantization is still one of the biggest levers for latency, throughput, and memory efficiency without retraining. This is not glamorous, but for swarm density it matters more than hype papers. [NVIDIA Developer](https://developer.nvidia.com/blog/optimizing-llms-for-performance-and-accuracy-with-post-training-quantization/?utm_source=chatgpt.com)

**Draft-model training ecosystems for speculation**  
vLLM’s speculative stack is not just “turn it on”; the project also points to dedicated draft-model training and integration via its speculators work, with active 2026 roadmap work around online data generation and newer speculative algorithms. [vLLM+1](https://docs.vllm.ai/en/latest/features/speculative_decoding/speculators/?utm_source=chatgpt.com)

4\. The one unclear item: “EOQ”
-------------------------------

I could not verify **EOQ** as a standard 2026 LLM/coding-agent optimization term from authoritative sources. The only things that turned up were unrelated meanings, plus one Hugging Face collection description using “EOQ quantized large models,” which is not enough to treat EOQ as an established technique term. [Hugging Face](https://huggingface.co/caiovicentino1/Qwen3.5-27B-PolarQuant-Q5?utm_source=chatgpt.com)

So on EOQ, the honest answer is:

*   it is **not** a widely established technique label like REAP, SFT, FlashAttention, TiDAR, LatentMAS, or speculative decoding, based on what I found; [vLLM+5GitHub+5OpenAI Developers+5](https://github.com/CerebrasResearch/reap?utm_source=chatgpt.com)
*   you may have meant a niche repo/model tag, or a different acronym.

What I’d rank highest for actual Claude-Code-style swarms
---------------------------------------------------------

For a practical coding-agent swarm stack, my priority order would be:

**Tier 1**

*   FlashAttention
*   speculative decoding
*   quantization / KV-cache compression
*   SFT for formatting, tool use, repo style

These are the easiest to cash into real speed/cost wins. [OpenAI Developers+4GitHub+4vLLM+4](https://github.com/dao-ailab/flash-attention?utm_source=chatgpt.com)

**Tier 2**

*   REAP, if you are using MoE models and want more concurrent workers per box
*   latent-space memory/communication ideas, if you are building a serious swarm research stack

These can matter a lot, but they are more architecture-dependent. [Cerebras+2Hugging Face+2](https://www.cerebras.ai/blog/reap?utm_source=chatgpt.com)

**Tier 3**

*   TiDAR-style hybrid generation paths

Interesting, but this is more of a dedicated model-R&D branch than a default deployment knob. [arXiv](https://arxiv.org/html/2511.08923v1?utm_source=chatgpt.com)

The blunt version
-----------------

If your goal is **better coding swarms in 2026**, the stuff that actually moves the needle fastest is:

*   **spec decode**
*   **FlashAttention**
*   **good quantization / KV compression**
*   **SFT**
*   **REAP if MoE**

Then, once that works:

*   **LatentMAS-style communication**
*   **TiDAR-like hybrid generation research**

That is the order I’d spend money and engineering time in.

If you want, I can turn this into a **ranked list of 30–50 adjacent technique families/experiments** in this exact vein, not product names.

---

**Sources:**

- [Dao-AILab/flash-attention: Fast and memory-efficient ...](https://github.com/dao-ailab/flash-attention?utm_source=chatgpt.com)
- [Speculative Decoding - vLLM](https://docs.vllm.ai/en/latest/features/speculative_decoding/?utm_source=chatgpt.com)
- [Supervised fine-tuning | OpenAI API](https://developers.openai.com/api/docs/guides/supervised-fine-tuning/?utm_source=chatgpt.com)
- [[2511.20639] Latent Collaboration in Multi-Agent Systems](https://arxiv.org/abs/2511.20639?utm_source=chatgpt.com)
- ['A high-speed digital cheat sheet': Google unveils TurboQuant AI-compression algorithm, which it claims can hugely reduce LLM memory usage](https://www.techradar.com/pro/a-high-speed-digital-cheat-sheet-google-unveils-turboquant-ai-compression-algorithm-which-it-claims-can-hugely-reduce-llm-memory-usage?utm_source=chatgpt.com)
- [Optimizing LLMs for Performance and Accuracy with Post- ...](https://developer.nvidia.com/blog/optimizing-llms-for-performance-and-accuracy-with-post-training-quantization/?utm_source=chatgpt.com)
- [caiovicentino1/Qwen3.5-27B-PolarQuant-Q5](https://huggingface.co/caiovicentino1/Qwen3.5-27B-PolarQuant-Q5?utm_source=chatgpt.com)
- [REAP: One-Shot Pruning for Trillion-Parameter Mixture-of- ...](https://www.cerebras.ai/blog/reap?utm_source=chatgpt.com)

## Prompt:
4/3/2026, 7:48:15 PM

Find 25 to 50 more items + 25 addtl papers

## Response:
4/3/2026, 7:48:19 PM

I’m expanding this into technique-level items only, then separating out 25 additional papers so the list isn’t polluted with duplicate ideas wearing different names.

> **Searching for swarm coding techniques and recent papers**
>
> [LLM Inference Optimization Techniques](https://redwerk.com/blog/llm-inference-optimization-techniques/)
> [A Self-Improving Coding Agent](https://arxiv.org/html/2504.15228v1)
> [(PDF) A Self-Improving Coding Agent](https://www.researchgate.net/publication/390991089_A_Self-Improving_Coding_Agent)
> [Artificial Intelligence 2025](https://www.arxiv.org/list/cs.AI/2025?show=1000&skip=14925)
> [xlite-dev/Awesome-LLM-Inference: 📚A curated list of ...](https://github.com/xlite-dev/Awesome-LLM-Inference)
> [A Self-Improving Coding Agent (University of Bristol, April ...](https://www.facebook.com/groups/cto.founder/posts/2425343071165572/)
> [LLM Inference Optimization Techniques: Batching ...](https://www.linkedin.com/posts/samin-chandeepa_llm-inference-optimization-techniques-activity-7393222700976103424-eLnw)
> [LLM Inference Optimization](https://medium.com/%40harshit.sinha0910/llm-inference-optimization-f720e71f5da0)
> [Rethinking the High-Throughput LLM Inference](https://openreview.net/forum?id=59OJOgKLzN)
>
> **Looking into more specific searches**
>
> I think I need to refine my searches and focus on more specific topics. Things like surveys for decoding, key-value compression, agent memory, and verifiers might yield more relevant information for what I'm trying to understand. Just got to be a bit more focused with the queries!
>
> **Searching for specific papers on LLM decoding and more**
>
> [KV Cache Optimization Strategies for Scalable and ...](https://arxiv.org/html/2603.20397v1)
>
> **Refining the search for techniques and methods**
>
> I think I need about 25 more items, potentially grouped by technique families. An ideal list might include 30 items with brief notes on each, plus 25 relevant papers. I’ll also need to specifically look up methods like EAGLE, Medusa, DoLa, MTP, and others, making sure to include citations.
>
> **Searching for papers on LLM techniques and methods**
>
> [Optimizing Large Batched LLM Inference with Global Prefix ...](https://arxiv.org/html/2412.03594v1)
> [Speculative Decoding with a Speculative Vocabulary](https://www.arxiv.org/pdf/2602.13836)
>
> **Exploring MoE, memory, and tool use**
>
> I think I need to gather more information on MoE (Mixture of Experts), memory, routing, verifiers, and tool use. It's important to dive deeper into these areas to cover the different techniques and methods involved. I want to make sure I’m thorough in my search!
>
> **Searching recent papers on MoE, memory, routing, and more**
>
> [Advancing Expert Specialization for Better MoE](https://arxiv.org/html/2505.22323v5)
>
> **Refining the list and adding citations**
>
> I think I need to create a new list with 25-50 items, plus 25 additional papers. I’ll aim for concise labels and one-liners, keeping the details minimal. I’ll also have to cite every statement sourced from the web. I can group related bullets for efficiency, adding citations in bigger chunks. I'll focus on crafting a solid list!
>
> Thought for 41s

Here are **30 more technique-level items** and **25 additional papers**, aimed at the exact lane you meant: **coding agents / swarms / white-box serving / training / runtime optimization**, not product names.

I’m excluding the obvious ones you already named where possible, and I’m biasing toward things that can actually change throughput, concurrency, verifier quality, or multi-agent behavior.

30 more items
-------------

### Decoding and inference acceleration

1.  **PagedAttention** — KV paging to make long-context serving less wasteful.
2.  **Continuous batching** — iteration-level scheduling of mixed requests instead of naive batch boundaries.
3.  **Chunked / split prefill** — prevents long prefills from stalling decodes.
4.  **Disaggregated prefill-decode** — separates prompt ingestion from token generation to improve scheduler efficiency.
5.  **Global prefix caching** — reuse shared prompt prefixes across requests.
6.  **Prefix-aware batching** — batch requests based on shared prefixes, not just arrival time.
7.  **Prompt cache reuse** — especially useful for swarms with repeated system/tool scaffolds.
8.  **Multi-token prediction (MTP)** — predict several future tokens at once.
9.  **Training-free MTP** — probe frozen models for multi-token parallelism without retraining.
10.  **Self-distilled MTP** — improve MTP head acceptance rates with better joint training.
11.  **Medusa-style multi-head decoding** — auxiliary decoding heads for faster token acceptance.
12.  **EAGLE-3** — stronger speculative pipeline with direct token prediction and multi-layer fusion.
13.  **P-EAGLE** — parallel-drafting EAGLE with scalable training and vLLM integration.
14.  **Adaptive speculative decoding with RL** — tune speculation depth/behavior online.
15.  **Pattern-aware speculative execution for agents** — speculation adapted to LLM-tool loop structure.
16.  **Dual-level speculation** — combine agent-level speculation with token-level speculation.
17.  **Speculative vocabularies** — constrain verification to smarter candidate subsets.
18.  **Contrastive decoding** — quality gains via expert-vs-amateur style comparisons.
19.  **DoLa** — layer-contrastive decoding using the same model with early exits.
20.  **LayerCake** — token-aware contrastive decoding inside one model.
21.  **Temporal guidance decoding** — internal self-contrastive guidance to stabilize decoding.
22.  **Early-exit decoding** — stop parts of the model early when confidence is high.
23.  **Speculative early exiting** — combine early exit with speculation.
24.  **Prompt-conditioned decoding policies** — adapt decoding settings to task/repo type.
25.  **Function-call parallel decoding** — reduce latency for tool-call emission itself.
26.  **Parallel tool calling** — widen the work done per reasoning step rather than only per token.
27.  **BatchLLM/global-prefix preprocessing** — throughput-oriented large-batch optimization.
28.  **PackInfer-style kernel balancing** — attention kernels optimized for heterogeneous request lengths.
29.  **Prefill-only engines** — valuable for verifier/scorer/ranker workers that only need one-token or short-output passes.
30.  **Shared decode execution across related models** — reuse parts of decoding across model family variants. [arXiv+9arXiv+9arXiv+9](https://arxiv.org/html/2412.03594v1?utm_source=chatgpt.com)

### KV-cache, memory, and long-context efficiency

31.  **KV eviction policies** — choose what to drop instead of assuming all past tokens matter equally.
32.  **KV quantization** — compress cache values numerically.
33.  **Low-rank KV compression** — compress along representation dimension.
34.  **Sequence-length KV merging** — merge similar KV states instead of just dropping them.
35.  **On-demand reversible KV compression** — switch between compressed and standard cache modes.
36.  **Adaptive KV compression** — tune compression without a fixed hand-set budget.
37.  **Zero-shot KV compression** — deploy compression without retraining.
38.  **Vector-quantized KV compression** — higher-ratio cache compression while preserving fidelity.
39.  **Compression-as-distillation for KV** — treat compressed cache formation as a learned distillation problem.
40.  **Head-aware KV compression** — compress selectively across attention heads.
41.  **Hybrid memory tiers for KV** — GPU + host memory strategies for higher concurrency.
42.  **Prefix memory hierarchies** — store and reuse recurrent prefix blocks efficiently.
43.  **Latent factual memory** — encode recoverable memory in latent representations instead of plain-text notes.
44.  **Episodic agent memory** — preserve multi-step interaction history with less destructive preprocessing.
45.  **Action-conditioned memory retrieval** — memory selected based on the action to be taken, not only semantic similarity.
46.  **Memory governance / stability controls** — separate “what memory becomes” from “how it is allowed to evolve.”
47.  **RL-optimized memory operations** — learn extraction, update, and retrieval policies.
48.  **Interdependent multi-agent memory benchmarks** — evaluate memory under real cooperative task dependencies. [arXiv+11arXiv+11arXiv+11](https://arxiv.org/html/2603.20397v1?utm_source=chatgpt.com)

### MoE, schedulers, swarm control, and verifier loops

49.  **Dense-to-MoE conversion** — convert dense checkpoints into sparse expert-routed models.
50.  **Dense-model inherent-MoE extraction** — find latent expert structure without full retraining.
51.  **Expert specialization analysis** — measure whether experts actually specialize by domain/task.
52.  **Expert pruning over expert merging** — especially for generative tasks where routing control matters.
53.  **Redundancy-reduced MoE variants** — trim expert overlap to improve memory efficiency.
54.  **Router-aware expert compression** — compress while respecting routing behavior.
55.  **Fair scheduling for task-parallel agents** — memory-centric rather than compute-centric scheduling.
56.  **Failure-pattern-aware swarm control** — use historical failure traces to route retries/escalations.
57.  **Task-level performance prediction** — estimate likely success before spending full agent budget.
58.  **Agentic verifiers** — multi-turn execution-based verification rather than static judging.
59.  **Rubric-based deep verifiers** — structured verification with explicit dimensions of success/failure.
60.  **Reward-hack detection for code agents** — detect when the agent gamed the benchmark or tests.
61.  **Self-improving coding agents** — agent edits its own scaffolding/tooling/policies.
62.  **Synthetic-data-to-verifiable-reward RL loops** — generate tasks, solve them, verify them, then reinforce.
63.  **Self-play SWE RL** — autonomous bug injection / repair / verifier cycles.
64.  **Parallel reasoning + parallel tool work** — widen both thought and action bandwidth in swarms.
65.  **Function-call latency as first-class optimization target** — matters for real-time game or UI agents.
66.  **Agent-memory benchmarks with environment interaction** — not just “does it remember text,” but “does memory help it act.” [arXiv+11arXiv+11arXiv+11](https://arxiv.org/html/2602.15521v1?utm_source=chatgpt.com)

25 additional papers
--------------------

These are **additional papers**, mostly not the same ones I named earlier.

1.  **Speculative Speculative Decoding** — recursive/stacked speculative acceleration. [arXiv](https://arxiv.org/pdf/2603.03251?utm_source=chatgpt.com)
2.  **Adaptive Speculative Decoding with Reinforcement Learning** — RL-tuned speculation policy. [arXiv](https://arxiv.org/html/2603.01639v1?utm_source=chatgpt.com)
3.  **Accelerating LLM Agents via Pattern-Aware Speculative Execution** — speculation adapted to agent loops. [arXiv](https://arxiv.org/pdf/2603.18897?utm_source=chatgpt.com)
4.  **DualSpec: Accelerating Deep Research Agents via Dual Speculation** — combines coarser and finer speculation. [arXiv](https://arxiv.org/html/2603.07416v1?utm_source=chatgpt.com)
5.  **P-EAGLE: Parallel-Drafting EAGLE with Scalable Training** — practical scaled speculative drafting. [arXiv](https://arxiv.org/pdf/2602.01469?utm_source=chatgpt.com)
6.  **EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test** — strong current EAGLE reference. [arXiv](https://arxiv.org/html/2503.01840v1?utm_source=chatgpt.com)
7.  **SpecForge** — open-source production-oriented framework for training speculative models. [arXiv](https://arxiv.org/html/2603.18567v1?utm_source=chatgpt.com)
8.  **Speculative Decoding with a Speculative Vocabulary** — tighter candidate-space verification. [arXiv](https://www.arxiv.org/pdf/2602.13836?utm_source=chatgpt.com)
9.  **Efficient Training-Free Multi-Token Prediction via On-the-Fly Mask Tokens** — frozen-model MTP. [arXiv](https://arxiv.org/html/2603.17942v1?utm_source=chatgpt.com)
10.  **Self-Distillation for Multi-Token Prediction** — stronger MTP head training. [arXiv](https://arxiv.org/html/2603.23911v1?utm_source=chatgpt.com)
11.  **DoLa: Decoding by Contrasting Layers Improves Factuality in Large Language Models** — classic layer-contrastive decoding reference. [arXiv](https://arxiv.org/html/2309.03883v2?utm_source=chatgpt.com)
12.  **LayerCake: Token-Aware Contrastive Decoding within a Single Model** — newer internal contrastive decoding variant. [arXiv](https://arxiv.org/html/2507.04404v1?utm_source=chatgpt.com)
13.  **Temporal Guidance for Large Language Models** — self-contrastive guidance without external amateur model. [arXiv](https://arxiv.org/html/2601.21744v1?utm_source=chatgpt.com)
14.  **KV Cache Optimization Strategies for Scalable and Efficient LLM Inference** — useful 2026 survey. [arXiv](https://arxiv.org/html/2603.20397v1?utm_source=chatgpt.com)
15.  **EchoKV: Efficient KV Cache Compression via Similarity-Based On-Demand Transitions** — reversible compression path. [arXiv](https://arxiv.org/html/2603.22910v1?utm_source=chatgpt.com)
16.  **VQKV: High-Fidelity and High-Ratio Cache Compression** — vector-quantized KV compression. [arXiv](https://arxiv.org/html/2603.16435v1?utm_source=chatgpt.com)
17.  **KVSculpt: KV Cache Compression as Distillation** — treats cache compression as learned distillation. [arXiv](https://arxiv.org/html/2603.27819v1?utm_source=chatgpt.com)
18.  **Adaptive KV-Cache Compression without Manually Setting Compression Ratios** — dynamic KV budgeting. [arXiv](https://arxiv.org/pdf/2509.03136?utm_source=chatgpt.com)
19.  **ZSMerge: Zero-Shot KV Cache Compression for Memory-Efficient Long-Context LLMs** — zero-shot compression lane. [arXiv](https://www.arxiv.org/list/cs.AI/2025?show=1000&skip=14925&utm_source=chatgpt.com)
20.  **ToMoE: Converting Dense Large Language Models to Mixture-of-Experts** — dense-to-MoE conversion. [arXiv](https://arxiv.org/html/2501.15316v2?utm_source=chatgpt.com)
21.  **ExpertWeaver: Unlocking the Inherent MoE in Dense LLMs** — training-free dense-to-sparse conversion. [arXiv](https://arxiv.org/html/2602.15521v1?utm_source=chatgpt.com)
22.  **REAP the Experts: Why Pruning Prevails for One-Shot MoE Compression** — pruning vs merging for generative MoEs. [arXiv](https://arxiv.org/html/2510.13999v2?utm_source=chatgpt.com)
23.  **Justitia: Fair and Efficient Scheduling of Task-Parallel LLM Agents** — memory-aware swarm scheduler. [arXiv](https://arxiv.org/html/2510.17015v2?utm_source=chatgpt.com)
24.  **EAGER: Efficient Failure Management for Multi-Agent Systems** — failure-history-aware MAS control. [arXiv](https://arxiv.org/html/2603.21522v1?utm_source=chatgpt.com)
25.  **Unified Inference & Training Framework for Agent Memory** — RL-flavored memory operation infrastructure. [arXiv](https://arxiv.org/html/2603.29493v3?utm_source=chatgpt.com)

What I would prioritize for your stack
--------------------------------------

If the goal is **coding swarms that continuously get faster/cheaper without wrecking quality**, the highest-value next areas are:

*   **speculation family**: EAGLE-3, P-EAGLE, adaptive speculative decoding, pattern-aware agent speculation, and MTP variants. These directly attack token latency and serial agent loops. [arXiv+4arXiv+4arXiv+4](https://arxiv.org/pdf/2602.01469?utm_source=chatgpt.com)
*   **KV/cache family**: EchoKV, VQKV, KVSculpt, adaptive KV compression, and zero-shot merge/compression methods. For multi-agent concurrency, memory is often the real bottleneck. [arXiv+4arXiv+4arXiv+4](https://arxiv.org/html/2603.20397v1?utm_source=chatgpt.com)
*   **MoE density family**: dense-to-MoE conversion, REAP-style pruning, expert specialization analysis, and redundancy reduction. This is the lane that can buy you more workers per box. [arXiv+3arXiv+3arXiv+3](https://arxiv.org/html/2501.15316v2?utm_source=chatgpt.com)
*   **verifier/scheduler/memory family**: agentic verifiers, DeepVerifier-style rubric systems, Justitia scheduling, EAGER failure management, and RL-optimized memory ops. That is where swarm quality and cost control start to become operational rather than academic. [arXiv+4arXiv+4arXiv+4](https://arxiv.org/html/2602.04254v1?utm_source=chatgpt.com)

The blunt version: after **FlashAttention + quantization + basic spec decode**, the next serious wins are probably **KV-cache engineering**, **MoE compression/conversion**, and **better verifier/scheduler loops**. TiDAR and latent-space agent communication are interesting, but they are still a more experimental branch than these. [arXiv+3arXiv+3arXiv+3](https://arxiv.org/html/2603.20397v1?utm_source=chatgpt.com)

If you want, I can turn this into a **ranked matrix** with columns like **“drop-in today,” “needs own weights,” “needs retraining,” “best for 3090 Ti,” “best for 48 GB rental,” and “best for coding swarms specifically.”**

---

**Sources:**

- [Optimizing Large Batched LLM Inference with Global Prefix ...](https://arxiv.org/html/2412.03594v1?utm_source=chatgpt.com)

## Prompt:
4/3/2026, 7:57:58 PM

Exl3 and other item.s?

## Response:
4/3/2026, 7:58:00 PM

I’m checking EXL3 specifically and then grouping the adjacent techniques that actually belong in the same decision set, instead of mixing quantizers, kernels, and model architectures.

> **Browsing for EXL3 quantization information and updates**
>
> [turboderp-org/exllamav3](https://github.com/turboderp-org/exllamav3)
> [ArtusDev/requests-exl](https://huggingface.co/ArtusDev/requests-exl)
> [Introducing ExLlamaV3: A Modular Framework for Llama ...](https://www.linkedin.com/posts/nir-diamant-ai_exllamav3-is-an-exciting-early-preview-activity-7315396170984423424-Ed5t)
> [EXL3 early preview has been released! exl3 4.0 bpw ...](https://www.reddit.com/r/LocalLLaMA/comments/1jt08di/exl3_early_preview_has_been_released_exl3_40bpw/)
> [Run Llama 3.3 70B on Your GPU with ExLlamaV3](https://kaitchup.substack.com/p/run-llama-33-70b-on-your-gpu-with)
>
> Thought for 6s

Yes — **EXL3 is a real 2025–2026 item**, and it belongs in the same bucket as **quantization / consumer-GPU inference formats**, not in the same bucket as TiDAR or LatentMAS.

**What EXL3 is:**  
EXL3 is the new quantization format used by **ExLlamaV3**. The ExLlamaV3 repo describes it as a new format based on **QTIP**, with different regularization and tensor packing, aimed at fast local inference on modern consumer GPUs. [GitHub+1](https://github.com/turboderp-org/exllamav3?utm_source=chatgpt.com)

**What it is good for:**  
Use EXL3 when your goal is **fit bigger models into less VRAM** and still keep decent quality/speed on a single consumer GPU. Public EXL3 model cards emphasize mixed-precision bit allocation and note that some layers get more bits than others because attention layers tend to be more quality-sensitive than expert FFNs. [Hugging Face+1](https://huggingface.co/mratsim/GLM-4.7-EXL3?utm_source=chatgpt.com)

**What it is not:**  
It is **not** a general distributed-serving standard right now. As of March 2026, at least one Qwen3.5 EXL3 model card says **ExLlamaV3 + TabbyAPI is the only supported inference stack**, while vLLM support was still being requested rather than treated as mainstream support. [Hugging Face+1](https://huggingface.co/ykarout/Qwen3.5-27B-exl3-3.0bpw?utm_source=chatgpt.com)

**Practical downside:**  
EXL3 looks strongest for **local / small-batch / consumer-GPU** use, but not automatically the best choice for broader serving stacks. There are also current reports that the Ampere path is not yet ideal, with an open optimization issue noting weaker saturation on Ampere GPUs like the 3090 than competing implementations. [Kaitchup+1](https://kaitchup.substack.com/p/serving-exllamav3-with-tabbyapi-accuracy?utm_source=chatgpt.com)

So the blunt version is:

*   **EXL3** = strong **local quant format** for consumer GPUs
*   **GGUF / AWQ / GPTQ / Marlin-family paths** = broader “portable-ish inference ecosystem” territory
*   **REAP** = MoE pruning/compression
*   **FlashAttention** = attention kernel acceleration
*   **Spec decode / EAGLE / Medusa / MTP** = decoding acceleration
*   **TiDAR** = hybrid model architecture
*   **LatentMAS** = multi-agent communication/memory method

If you want **other items in the EXL3 neighborhood**, these are the ones that actually belong in the same decision set:

**Quantization / weight-format side**

*   **EXL2** — older ExLlama quant family predecessor to EXL3.
*   **QTIP** — important because EXL3 is explicitly described as based on it. [GitHub](https://github.com/turboderp-org/exllamav3/blob/master/doc/exl3.md?utm_source=chatgpt.com)
*   **GGUF** — major local-inference format ecosystem.
*   **AWQ**
*   **GPTQ**
*   **Marlin kernels / Marlin-style GEMM**
*   **mixed-precision layerwise quantization**
*   **lm\_head higher-bit retention** — EXL3 model cards commonly keep the output head at a higher bit width such as 6 bits. [Hugging Face+1](https://huggingface.co/ykarout/Qwen3.5-27B-exl3-3.0bpw?utm_source=chatgpt.com)
*   **Hadamard-transform-based quantization** — explicitly mentioned in some EXL3 quant releases. [Hugging Face](https://huggingface.co/mratsim/GLM-4.7-EXL3?utm_source=chatgpt.com)

**Cache / memory side**

*   **cache quantization** — even ExLlama ecosystem chatter calls out EXL3 cache quantization as a distinct improvement area. [Reddit](https://www.reddit.com/r/Oobabooga/comments/1k8ujnj/release_v31_speculative_decoding_3090_speed/?utm_source=chatgpt.com)
*   **KV-cache compression**
*   **TurboQuant-style KV compression**
*   **prefix caching**
*   **paged KV / paged attention**

**Decoding side**

*   **speculative decoding**
*   **EAGLE / EAGLE-3 / P-EAGLE**
*   **Medusa**
*   **multi-token prediction**
*   **early exit**
*   **contrastive decoding / DoLa**

**MoE / model-structure side**

*   **REAP**
*   **expert pruning**
*   **expert merging**
*   **dense-to-MoE conversion**

**Swarm / coding-agent side**

*   **LatentMAS**
*   **latent memory**
*   **agentic verifiers**
*   **task-level performance prediction**
*   **failure-aware schedulers**

My actual recommendation for your kind of stack:

*   On a **3090 Ti / consumer box**, **EXL3 is very worth considering** for local coding workers when your top concern is squeezing model quality into limited VRAM. [GitHub+1](https://github.com/turboderp-org/exllamav3?utm_source=chatgpt.com)
*   For a **larger multi-tenant serving stack**, I would be more cautious, because EXL3 portability/support still looks narrower than the mainstream server stacks. [GitHub+1](https://github.com/vllm-project/vllm/issues/19896?utm_source=chatgpt.com)
*   For **coding swarms**, EXL3 is a **capacity enabler**, not the whole story. The next layer is still **spec decode + cache optimization + verifier quality + scheduler quality**.

If you want, I can build you a **clean taxonomy of 50–75 items** split into:  
**quantization formats, kernels, cache tricks, decoding tricks, MoE tricks, and swarm-control tricks**.

---

**Sources:**

- [turboderp-org/exllamav3](https://github.com/turboderp-org/exllamav3?utm_source=chatgpt.com)
- [mratsim/GLM-4.7-EXL3](https://huggingface.co/mratsim/GLM-4.7-EXL3?utm_source=chatgpt.com)
- [Serving ExLlamaV3 with tabbyAPI: Accuracy, Speed, and ...](https://kaitchup.substack.com/p/serving-exllamav3-with-tabbyapi-accuracy?utm_source=chatgpt.com)
- [Release v3.1: Speculative decoding (+30-90% speed!) ...](https://www.reddit.com/r/Oobabooga/comments/1k8ujnj/release_v31_speculative_decoding_3090_speed/?utm_source=chatgpt.com)

## Prompt:
4/3/2026, 8:11:54 PM

25 to 50 unique items and papers not ye covered especially with new techniques

## Response:
4/3/2026, 8:12:00 PM

I’m expanding into techniques that are genuinely distinct from the earlier buckets, especially newer training/inference ideas rather than just more quantizers with different names.

> **Searching for 2025-2026 LLM inference techniques**
>
> [ExpertFlow: Efficient Mixture-of-Experts Inference via ...](https://arxiv.org/html/2410.17954v2)
>
> **Searching for recent techniques in language models**
>
> [A Unified Decoding Framework for Large Language Models](https://arxiv.org/abs/2601.07525)
>
> Thought for 16s

Yes. Here are **25 more technique-level items** that are mostly **new relative to the earlier lists**, plus **25 additional papers** to read. I’m focusing on things that are meaningfully distinct, not just renamed versions of “quantization” or “spec decode.”

25 additional unique technique items
------------------------------------

1.  **Prefix-aware attention kernels** — exploit hierarchical shared prefixes across requests instead of treating every decode stream independently. PAT is a current example. [arXiv](https://arxiv.org/html/2511.22333v3?utm_source=chatgpt.com)
2.  **Route-path prediction for MoE inference** — predict expert usage ahead of time so the system can schedule and preload experts before the real forward pass. ExpertFlow is a clean example. [arXiv+1](https://arxiv.org/html/2410.17954v2?utm_source=chatgpt.com)
3.  **Predictive expert caching** — cache only the experts likely to be needed next rather than full expert sets. [arXiv](https://arxiv.org/html/2410.17954v2?utm_source=chatgpt.com)
4.  **Sequence-level expert routing** — choose experts at the sequence level rather than per token, reducing routing overhead and instability. [arXiv](https://arxiv.org/html/2511.06494v2?utm_source=chatgpt.com)
5.  **Routing-free MoE** — remove centralized TopK/Softmax routing and let experts determine activation behavior directly. [arXiv](https://arxiv.org/html/2604.00801v1?utm_source=chatgpt.com)
6.  **Speculation-assisted MoE memory management** — use speculative decoding not just for speed, but to look ahead and manage expert loading. [arXiv](https://arxiv.org/html/2603.09983v1?utm_source=chatgpt.com)
7.  **Expert prefetching from internal representations** — predict near-future expert selection from internal signals during inference, without retraining the base MoE. [arXiv](https://arxiv.org/html/2603.19289?utm_source=chatgpt.com)
8.  **Low-batch MoE chiplet parallelism** — new parallelization schemes aimed specifically at low-batch MoE inference, which matters for agentic workloads. [arXiv](https://arxiv.org/html/2603.27624v1?utm_source=chatgpt.com)
9.  **Disaggregated prefill/decode storage paths** — move beyond prefill-centric storage loading and use decode-side storage bandwidth too. DualPath is in this lane. [arXiv](https://arxiv.org/html/2602.21548v2?utm_source=chatgpt.com)
10.  **CXL-backed disaggregated KV memory** — offload KV cache to remote memory fabrics and prefetch/speculate against that tier. [arXiv](https://arxiv.org/html/2512.11920v1?utm_source=chatgpt.com)
11.  **Persistent low-bit KV caches for multi-agent systems** — keep compressed agent KV state around instead of constantly rebuilding after eviction. [arXiv](https://arxiv.org/pdf/2603.04428?utm_source=chatgpt.com)
12.  **Multi-LoRA KV cache sharing** — share cache efficiently across many LoRA-specialized agents rather than treating each adapter as a full separate cache domain. [arXiv](https://arxiv.org/html/2602.01053v1?utm_source=chatgpt.com)
13.  **Flash-LoRA attention kernels** — reorder attention computation so LoRA contributions can be reconstructed without fully materializing expanded low-rank caches. [arXiv](https://arxiv.org/html/2602.01053v1?utm_source=chatgpt.com)
14.  **Model-driven KV cache management** — learn or estimate which KV blocks matter for long-horizon agent workloads instead of using static heuristics. SideQuest is in this direction. [arXiv](https://arxiv.org/html/2602.22603v1?utm_source=chatgpt.com)
15.  **Similarity-triggered reversible KV compression** — compress and later restore KV state on demand when similarity conditions allow it. EchoKV is a current example. [arXiv](https://arxiv.org/html/2603.22910v1?utm_source=chatgpt.com)
16.  **Position-aware decoding-aligned KV compression** — compress KV in ways that are explicitly aligned to downstream decoding behavior, not only token importance scores. [arXiv](https://arxiv.org/html/2603.11564?utm_source=chatgpt.com)
17.  **Learned latent-head attention variants beyond MLA** — Multi-Head Low-Rank Attention is an example of pushing the latent-attention idea further. [arXiv](https://arxiv.org/html/2603.02188v1?utm_source=chatgpt.com)
18.  **Unified constrained-decoding frameworks** — systems that separate “thinking” from “constraining,” rather than bolting constraints onto standard greedy/sampling loops. [arXiv](https://arxiv.org/abs/2601.07525?utm_source=chatgpt.com)
19.  **Future-aware speculative drafting** — improve the drafter by explicitly modeling farther-future token implications rather than only next-token fidelity. [arXiv](https://arxiv.org/html/2603.08899v1?utm_source=chatgpt.com)
20.  **Adaptive parallel decoding for diffusion LMs** — divide-and-conquer style decoding for diffusion-based language models rather than plain AR speculation. [arXiv](https://arxiv.org/abs/2602.23792?utm_source=chatgpt.com)
21.  **Generalized agent-planning foundation models** — models trained specifically for planning in agent settings, instead of raw next-token modeling plus scaffolding. MagicAgent fits here. [arXiv](https://arxiv.org/html/2602.19000v1?utm_source=chatgpt.com)
22.  **Trajectory-informed memory synthesis** — create reusable memory objects from execution traces so agents improve from prior runs. [arXiv](https://arxiv.org/html/2603.10600?utm_source=chatgpt.com)
23.  **Coordinated multi-agent memory cycles** — jointly optimize memory writing, retrieval, and use across multiple agents instead of treating them as separate components. MemMA is in this lane. [arXiv](https://arxiv.org/html/2603.18718v1?utm_source=chatgpt.com)
24.  **Memory governance / anti-drift controls** — explicit mechanisms for keeping long-term agent memory stable, privacy-safe, and resistant to semantic drift. [arXiv+1](https://arxiv.org/html/2603.11768v1?utm_source=chatgpt.com)
25.  **Fair schedulers for task-parallel agents** — scheduling policies that account for agent memory cost and long-lived context, not just request count or FLOPs. Justitia is a notable example. [arXiv](https://arxiv.org/html/2510.17015v2?utm_source=chatgpt.com)

25 additional papers to read
----------------------------

These are mostly distinct from the prior papers I already named earlier.

1.  **PAT: Accelerating LLM Decoding via Prefix-Aware Attention**. [arXiv](https://arxiv.org/html/2511.22333v3?utm_source=chatgpt.com)
2.  **ExpertFlow: Efficient Mixture-of-Experts Inference via Routing Path Prediction, Token Scheduling, and Predictive Expert Cache**. [arXiv+1](https://arxiv.org/html/2410.17954v2?utm_source=chatgpt.com)
3.  **MoE-SpAc: Efficient MoE Inference Based on Speculative Decoding as Memory Lookahead**. [arXiv](https://arxiv.org/html/2603.09983v1?utm_source=chatgpt.com)
4.  **Speculating Experts Accelerates Inference for Mixture-of-Experts Models**. [arXiv](https://arxiv.org/html/2603.19289?utm_source=chatgpt.com)
5.  **Route Expert by Sequence, Not by Token**. [arXiv](https://arxiv.org/html/2511.06494v2?utm_source=chatgpt.com)
6.  **Routing-Free Mixture-of-Experts**. [arXiv](https://arxiv.org/html/2604.00801v1?utm_source=chatgpt.com)
7.  **Accelerating Low-Batch MoE Inference via Multi-Chiplet Fully Sharded Expert Data Parallelism**. [arXiv](https://arxiv.org/html/2603.27624v1?utm_source=chatgpt.com)
8.  **DualPath: Breaking the Storage Bandwidth Bottleneck in Agentic LLM Inference**. [arXiv](https://arxiv.org/html/2602.21548v2?utm_source=chatgpt.com)
9.  **CXL-SpecKV: A Disaggregated FPGA Speculative KV-Cache Architecture**. [arXiv](https://arxiv.org/html/2512.11920v1?utm_source=chatgpt.com)
10.  **Persistent Q4 KV Cache for Multi-Agent LLM Inference on Edge Devices**. [arXiv](https://arxiv.org/pdf/2603.04428?utm_source=chatgpt.com)
11.  **Efficient KV Cache Sharing for Multi-LoRA LLM Agents**. [arXiv](https://arxiv.org/html/2602.01053v1?utm_source=chatgpt.com)
12.  **SideQuest: Model-Driven KV Cache Management for Long-Horizon Agentic Workloads**. [arXiv](https://arxiv.org/html/2602.22603v1?utm_source=chatgpt.com)
13.  **EchoKV: Efficient KV Cache Compression via Similarity-Based On-Demand Transitions**. [arXiv](https://arxiv.org/html/2603.22910v1?utm_source=chatgpt.com)
14.  **Decoding-aligned KV Cache Compression via Position-Aware Methods**. [arXiv](https://arxiv.org/html/2603.11564?utm_source=chatgpt.com)
15.  **Multi-Head Low-Rank Attention**. [arXiv](https://arxiv.org/html/2603.02188v1?utm_source=chatgpt.com)
16.  **Thinking Before Constraining: A Unified Decoding Framework for Large Language Models**. [arXiv](https://arxiv.org/abs/2601.07525?utm_source=chatgpt.com)
17.  **Contemplate the Future for Better Speculative Sampling**. [arXiv](https://arxiv.org/html/2603.08899v1?utm_source=chatgpt.com)
18.  **Divide and Conquer: Accelerating Diffusion-Based Large Language Models via Adaptive Parallel Decoding**. [arXiv](https://arxiv.org/abs/2602.23792?utm_source=chatgpt.com)
19.  **MagicAgent: Towards Generalized Agent Planning**. [arXiv](https://arxiv.org/html/2602.19000v1?utm_source=chatgpt.com)
20.  **Trajectory-Informed Memory Generation for Self-Improving Agents**. [arXiv](https://arxiv.org/html/2603.10600?utm_source=chatgpt.com)
21.  **MemMA: Coordinating the Memory Cycle through Multi-Agent Memory Augmentation**. [arXiv](https://arxiv.org/html/2603.18718v1?utm_source=chatgpt.com)
22.  **Memory for Autonomous LLM Agents: Mechanisms, Taxonomy, and Engineering Realities**. [arXiv+1](https://arxiv.org/html/2603.07670v1?utm_source=chatgpt.com)
23.  **Governing Evolving Memory in LLM Agents**. [arXiv](https://arxiv.org/html/2603.11768v1?utm_source=chatgpt.com)
24.  **Justitia: Fair and Efficient Scheduling of Task-Parallel LLM Agents**. [arXiv](https://arxiv.org/html/2510.17015v2?utm_source=chatgpt.com)
25.  **Agentic Verification of Software Systems**. [arXiv](https://arxiv.org/html/2511.17330v2?utm_source=chatgpt.com)

The ones I’d prioritize for your use case
-----------------------------------------

If your target is **coding-agent swarms**, the most interesting newer areas here are:

*   **MoE inference control**: ExpertFlow, sequence-level routing, routing-free MoE, and expert-prefetch work are directly relevant if you want more swarm density per box. [arXiv+3arXiv+3arXiv+3](https://arxiv.org/html/2410.17954v2?utm_source=chatgpt.com)
*   **KV/cache engineering for long-lived agents**: SideQuest, EchoKV, persistent Q4 KV, Multi-LoRA KV sharing, and DualPath are very aligned with long-running repo agents. [arXiv+4arXiv+4arXiv+4](https://arxiv.org/html/2602.22603v1?utm_source=chatgpt.com)
*   **Memory as a first-class agent system**: trajectory-informed memory, MemMA, and memory governance papers matter if you want agents that improve over repeated repo interactions instead of stateless benchmark runs. [arXiv+2arXiv+2](https://arxiv.org/html/2603.10600?utm_source=chatgpt.com)
*   **Agent-specific infrastructure**: Justitia and Agentic Verification are more practically valuable than a lot of flashy decoding work if your real bottleneck is reliable multi-agent software execution. [arXiv+1](https://arxiv.org/html/2510.17015v2?utm_source=chatgpt.com)

The blunt version: after the already-covered basics like FlashAttention, standard quantization, and vanilla spec decode, the next serious frontier is **memory hierarchy, KV persistence/compression, MoE routing control, and agent scheduler/verifier design**. That is where the newer technique surface is getting more interesting. [arXiv+3arXiv+3arXiv+3](https://arxiv.org/html/2603.11768v1?utm_source=chatgpt.com)

If you want, I can turn all of the techniques across the whole conversation into one **deduplicated master spreadsheet-style matrix** with columns for **drop-in today / needs own weights / needs retraining / best for coding swarms / best for 3090 Ti / best for 48 GB rental**.

---

**Sources:**

- [PAT: Accelerating LLM Decoding via Prefix-Aware ...](https://arxiv.org/html/2511.22333v3?utm_source=chatgpt.com)

## Prompt:
4/3/2026, 8:13:18 PM

Using qwen3.5 and gemma4 and their derivatives on hf as your foundation now plan heavy overhauls in full

## Response:
4/3/2026, 8:13:20 PM

I’m grounding this in what actually exists on Hugging Face and what those families support today, then I’ll turn it into a concrete overhaul plan rather than a vague wishlist.

I’ve confirmed the foundations exist in the forms that matter: base/instruct weights, consumer-GPU quant builds, and mainstream serving compatibility. Now I’m turning that into an end-to-end overhaul plan instead of just enumerating model files.

> **Searching HF models, Qwen3.5, Gemma4, inference stacks**
>
> [Qwen/Qwen3.5-35B-A3B](https://huggingface.co/Qwen/Qwen3.5-35B-A3B)
> [turboderp-org/exllamav3](https://github.com/turboderp-org/exllamav3)
> [Speculative Decoding - vLLM](https://docs.vllm.ai/en/latest/features/speculative_decoding/)
> [exllamav3 QWEN3.5 support (and more updates)](https://www.reddit.com/r/LocalLLaMA/comments/1rlsloy/exllamav3_qwen35_support_and_more_updates/)
> [Speculative Decoding with vLLM](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/vLLM/README.html)
> [Speculative decoding — Tutorials for AI developers 12.0](https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/notebooks/inference/speculative_decoding_deep_dive.html)
>
> **Searching for Gemma 4 31B and derivatives**
>
> [google/gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)
> [Qwen3.5 MLX vs GGUF Performance on Mac Studio M3 ...](https://www.reddit.com/r/LocalLLaMA/comments/1rwaq47/qwen35_mlx_vs_gguf_performance_on_mac_studio_m3/)
> [Fine-Tune Gemma using Hugging Face Transformers and ...](https://ai.google.dev/gemma/docs/core/huggingface_text_finetune_qlora)
> [Bringing AI Closer to the Edge and On-Device with Gemma 4](https://developer.nvidia.com/blog/bringing-ai-closer-to-the-edge-and-on-device-with-gemma-4/)
> [gemma-4-31b-it Model by Google | NVIDIA NIM](https://build.nvidia.com/google/gemma-4-31b-it/modelcard)
>
> Thought for 19s

Yes. If you are standardizing on **Qwen3.5 + Gemma 4 and their Hugging Face derivatives**, I would do a **full-stack overhaul**, not a few isolated tweaks.

The foundations are now broad enough to justify that. Qwen3.5 has official Hugging Face releases with compatibility called out for Transformers, vLLM, SGLang, and KTransformers, while Gemma 4 just landed on Hugging Face with open-weight releases, 256K context, multimodal support, and explicit support messaging around agents, inference engines, and fine-tuning libraries. The derivative ecosystem is already there too: GGUF, MLX conversions, EXL3 quants for Qwen3.5, and NVFP4-style Gemma 4 variants. [Hugging Face+7Hugging Face+7Hugging Face+7](https://huggingface.co/Qwen/Qwen3.5-35B-A3B?utm_source=chatgpt.com)

My blunt recommendation is:

*   **Qwen3.5 becomes your text-first coding family**
*   **Gemma 4 becomes your multimodal / long-context / judge / UI-review family**
*   **derivatives are deployment forms, not strategy**
*   **you optimize the serving layer, swarm layer, verifier layer, and training layer around those two families**

1\. The target architecture
---------------------------

Build a **two-family model platform** instead of a pile of random checkpoints.

Use **Qwen3.5** for:

*   code generation
*   repo-local edits
*   tool use
*   repair loops
*   draft-model roles for speculative decoding
*   cheap worker specialization via fine-tunes or LoRA derivatives

Use **Gemma 4** for:

*   multimodal review
*   screenshot / GIF / UI / desktop / mobile verification
*   long-context repo understanding and summarization
*   higher-context manager or planner roles
*   judge / verifier roles where text + image grounding matters

That split is grounded by what the families expose today: Qwen3.5 is already positioned with mainstream inference stack compatibility, while Gemma 4 is released as a multimodal family with long context and agent/fine-tune ecosystem support. [Hugging Face+4Hugging Face+4Hugging Face+4](https://huggingface.co/Qwen/Qwen3.5-35B-A3B?utm_source=chatgpt.com)

2\. Stop thinking in “one model”; think in role tiers
-----------------------------------------------------

I would define six runtime tiers.

**Tier A: orchestrator / planner**  
Primary: Gemma 4 31B IT or 26B A4B IT  
Purpose: task decomposition, multimodal planning, long-context routing, synthesis. Gemma 4’s 256K context and multimodal support make it a better home for “manager” roles than a pure text coder. [Hugging Face+2Hugging Face+2](https://huggingface.co/google/gemma-4-31B-it?utm_source=chatgpt.com)

**Tier B: main code worker**  
Primary: Qwen3.5-35B-A3B or a strong derivative  
Purpose: core code writing, patch generation, repair loops, tool calling. Qwen’s official card explicitly calls out mainstream inference compatibility, which matters for turning it into the backbone of a real platform. [Hugging Face](https://huggingface.co/Qwen/Qwen3.5-35B-A3B?utm_source=chatgpt.com)

**Tier C: cheap parallel code workers**  
Primary: Qwen3.5 9B / smaller derivatives / GGUF / EXL3 local quants  
Purpose: search-space widening, patch candidates, tests, summarization, file-local transforms. Qwen3.5 EXL3 and GGUF derivatives already exist broadly on Hugging Face. [Hugging Face+2ROCm Documentation+2](https://huggingface.co/turboderp/Qwen3.5-9B-exl3?utm_source=chatgpt.com)

**Tier D: multimodal verifier**  
Primary: Gemma 4 31B IT or 26B A4B IT / quantized derivative  
Purpose: judge screenshots, VHS clips, Playwright GIFs, app walkthroughs, “did the PR visually do what it claimed?” Gemma 4 is explicitly multimodal on release. [Hugging Face+2Hugging Face+2](https://huggingface.co/google/gemma-4-E2B?utm_source=chatgpt.com)

**Tier E: draft model for speculative decoding**  
Primary: same-family Qwen3.5 smaller coder or distilled derivative  
Purpose: reduce latency on the main Qwen worker. vLLM’s current docs still frame speculative decoding as one of the main paths to lower inter-token latency, and they point to draft-model training/integration. [vLLM+2vLLM+2](https://docs.vllm.ai/en/latest/features/speculative_decoding/?utm_source=chatgpt.com)

**Tier F: memory / summarizer / retrieval workers**  
Primary: small Qwen3.5 derivatives or Gemma E2B/E4B  
Purpose: cheap context folding, retrieval summaries, commit/thread compression. Gemma 4 small-family variants are already available, including deployment-oriented forms. [Hugging Face+2Hugging Face+2](https://huggingface.co/google/gemma-4-E2B?utm_source=chatgpt.com)

3\. Overhaul the model portfolio itself
---------------------------------------

Do not treat every Hugging Face derivative as equally strategic.

Use four buckets:

**Bucket 1: canonical base families**

*   official Qwen3.5 base + instruct
*   official Gemma 4 base + instruct  
    These are your truth source for training and eval baselines. [Hugging Face+3Hugging Face+3Hugging Face+3](https://huggingface.co/Qwen/Qwen3.5-35B-A3B?utm_source=chatgpt.com)

**Bucket 2: production deployment forms**

*   GGUF for CPU / llama.cpp / portable local setups
*   MLX for Apple Silicon
*   NVFP4 / vendor quant builds for NVIDIA-friendly deployment  
    These are not separate “models” in strategy terms; they are runtime packaging choices. The Hugging Face ecosystem already shows all three for these families. [Hugging Face+4Hugging Face+4Hugging Face+4](https://huggingface.co/mlx-community/Qwen3.5-35B-A3B-4bit?utm_source=chatgpt.com)

**Bucket 3: local performance quants**

*   EXL3 for Qwen3.5 on consumer GPUs  
    EXL3 is currently compelling for local Qwen3.5 use, but support is narrower; one model card explicitly says ExLlamaV3 + TabbyAPI is the only supported stack as of March 2026. That means use it where it wins locally, not as your whole serving standard. [GitHub+2Hugging Face+2](https://github.com/turboderp-org/exllamav3?utm_source=chatgpt.com)

**Bucket 4: derivatives worth adopting only after eval**

*   task-distilled coders
*   repo-style SFTs
*   reasoning-distilled variants
*   special domain fine-tunes  
    Some exist on Hugging Face already, but many will be noisy, overfit, or poorly documented. Treat third-party derivatives as candidates, not truth. [Hugging Face+1](https://huggingface.co/blockblockblock/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-6bpw-exl3?utm_source=chatgpt.com)

4\. Overhaul serving around three runtimes, not one
---------------------------------------------------

Use **three serving planes**.

**Plane 1: datacenter / serious serving**

*   vLLM first
*   SGLang second where useful
*   Triton/vLLM for productionized nodes if needed

Reason: Qwen3.5 official compatibility is already called out, and vLLM is where your speculative-decoding and serious serving work is most straightforward. [Hugging Face+2vLLM+2](https://huggingface.co/Qwen/Qwen3.5-35B-A3B?utm_source=chatgpt.com)

**Plane 2: Apple Silicon / travel / laptop**

*   MLX-native derivatives of Qwen3.5 and Gemma 4  
    Those conversions already exist on Hugging Face for both families. [Hugging Face+2Hugging Face+2](https://huggingface.co/mlx-community/Qwen3.5-35B-A3B-4bit?utm_source=chatgpt.com)

**Plane 3: high-efficiency local GPU lane**

*   ExLlamaV3 + EXL3 for Qwen3.5 worker pools on consumer GPUs  
    This is your “pack more decent workers into one box” path, but not your main standard because ecosystem portability is still limited. [GitHub+2Hugging Face+2](https://github.com/turboderp-org/exllamav3?utm_source=chatgpt.com)

5\. Overhaul inference with a strict priority order
---------------------------------------------------

Do these in this order:

### A. Speculative decoding first

If you are running Qwen3.5 as the main coder, add speculation before chasing exotic research branches. vLLM explicitly positions speculative decoding as a latency reducer for memory-bound workloads, and it now documents n-gram speculation plus draft-model training routes; its P-EAGLE note also shows the field is still actively improving. [vLLM+2vLLM+2](https://docs.vllm.ai/en/latest/features/speculative_decoding/?utm_source=chatgpt.com)

### B. Quantization second

For each role, maintain:

*   BF16 / high-fidelity baseline
*   server quant
*   local quant  
    Gemma 4 already has NVFP4 variants and MLX quantized derivatives; Qwen3.5 already has GGUF and EXL3 ecosystems. [ROCm Documentation+4Hugging Face+4Hugging Face+4](https://huggingface.co/nvidia/Gemma-4-31B-IT-NVFP4?utm_source=chatgpt.com)

### C. Prefix / cache engineering third

Once speculation works, move to:

*   prefix caching
*   chunked prefill
*   shared system-prompt scaffolds
*   agent-session reuse  
    This matters because coding swarms repeat enormous amounts of scaffolding.

### D. MoE-aware compression fourth

This is mainly a Qwen lane. If you are using Qwen3.5 A3B-family models, REAP-style and related MoE compression work is worth serious study later, but not before speculation and serving are stable.

6\. Overhaul the swarm architecture itself
------------------------------------------

Do not let every agent talk in free-form text all day.

Use this structure:

**Manager**

*   Gemma 4 31B or 26B A4B
*   sees task, PRD/ADR/plan, screenshots, failing UI artifacts
*   outputs DAG, acceptance criteria, stop conditions

**Implementers**

*   Qwen3.5-35B-A3B main workers
*   each owns a narrow branch/file/module task
*   tool calls allowed, but bounded

**Cheap scouts**

*   Qwen3.5 9B or quantized variants
*   grep/search, test synthesis, file summarization, small patch exploration

**Verifiers**

*   Gemma 4 multimodal verifiers for UI and recorded runs
*   Qwen3.5 verifier for static code review and trace consistency

**Reducer**

*   one model merges branch outputs and resolves conflicts, ideally same-family as main worker for style consistency

This is where your real gains come from: not “one magical model,” but role isolation and cheap parallelism.

7\. Overhaul training into family-specific lanes
------------------------------------------------

You should train **Qwen** and **Gemma** differently.

### Qwen lane

Focus on:

*   code-edit SFT
*   tool-call formatting SFT
*   repo-style adaptation
*   repair-loop preference data
*   draft-model distillation for speculation

Qwen is your text-coding workhorse, so its customizations should stay brutally practical.

### Gemma lane

Focus on:

*   multimodal verifier SFT
*   screenshot / GIF / UI-state judgment
*   planner / manager exemplars
*   long-context summarization
*   issue triage with artifacts

Gemma 4 is explicitly released into the multimodal/agent space, and Google’s own fine-tuning docs already point to HF Transformers + TRL + QLoRA workflows. NVIDIA is also already messaging day-0 Gemma 4 SFT/LoRA from Hugging Face checkpoints. [Google AI for Developers+1](https://ai.google.dev/gemma/docs/core/huggingface_text_finetune_qlora?utm_source=chatgpt.com)

8\. Overhaul data generation
----------------------------

Build five data streams.

**Stream 1: patch traces**  
Prompt, retrieved files, reasoning summary, diff, tests, outcome.

**Stream 2: verifier traces**  
What the agent claimed, what tests showed, what screenshots/GIFs showed, final verdict.

**Stream 3: decomposition traces**  
Task → plan DAG → subtask sequence → outcomes.

**Stream 4: failure traces**  
Hallucinated API use, wrong-file edits, partial refactors, fake passes, weak test gaming.

**Stream 5: multimodal PR evidence**  
Before/after screenshots, terminal recordings, Playwright captures, mobile/desktop clips.

That gives you the raw material for:

*   SFT
*   DPO / preference-style training
*   reward modeling
*   task difficulty prediction
*   draft model training
*   manager-agent improvement

9\. Overhaul evals so derivatives stop fooling you
--------------------------------------------------

Every candidate model or derivative needs the same gauntlet.

**Code quality**

*   repo issue resolution
*   feature implementation
*   refactor robustness
*   test-writing quality

**Agent behavior**

*   tool-call correctness
*   retrieval discipline
*   retry efficiency
*   stop-condition honesty

**Multimodal QA**

*   “does the UI match the PR claims?”
*   “did the GIF actually show the expected flow?”
*   “did desktop/mobile behavior regress?”

**Operational metrics**

*   TTFT
*   TPS
*   time to green
*   verifier false-pass rate
*   cost per accepted patch
*   context memory footprint

This is the only way to compare:

*   official base
*   instruct
*   GGUF
*   EXL3
*   MLX
*   custom fine-tunes
*   reasoning-distilled forks

on one field.

10\. Overhaul deployment by hardware class
------------------------------------------

### Your 3090 Ti / consumer GPU lane

Best use:

*   Qwen3.5 EXL3 or compact quants
*   cheap parallel workers
*   local dev and rapid iteration
*   possibly one stronger worker plus several scouts

Do not make this your primary Gemma 4 multimodal high-context lane unless the actual quant/runtime combo proves good enough.

### Apple Silicon lane

Best use:

*   MLX-converted Qwen/Gemma derivatives
*   travel mode
*   offline planning / summarization / light coding
*   fallback manager or verifier roles

### 48 GB rental / larger GPU lane

Best use:

*   full Qwen3.5-35B-A3B main workers
*   Gemma 4 31B or 26B A4B manager/verifier roles
*   speculative decoding experiments
*   heavy batch evals
*   fine-tuning runs

This gives you a clean split:

*   laptop = continuity
*   home GPU = cheap worker density
*   rented larger GPU = serious evals and stronger runtime roles

11\. Overhaul memory and context handling
-----------------------------------------

Do not let long-context become a dumb token dump.

Use:

*   strict repository maps
*   file-role summaries
*   branch-aware memory
*   replayable agent state
*   compressed task traces
*   artifact-linked memory for screenshots/test runs

Gemma 4’s long context is useful, but long context is not memory architecture by itself. Treat it as a capacity ceiling, not the whole solution. [Hugging Face+1](https://huggingface.co/google/gemma-4-E2B?utm_source=chatgpt.com)

12\. Overhaul safety and governance in a practical way
------------------------------------------------------

Because you are standardizing on open-weight families and third-party derivatives, enforce:

*   signed allowlist of approved model repos
*   separate trust tiers for official vs community derivatives
*   reproducible eval before promotion
*   no uncited community “uncensored” or mystery-distilled checkpoints in production by default
*   isolated sandboxes for experimental derivatives
*   audit logs for model/version per patch

That matters because Hugging Face already has plenty of derivative churn, and not all of it is production-worthy. [Hugging Face+1](https://huggingface.co/huihui-ai/Huihui-Qwen3.5-35B-A3B-abliterated?utm_source=chatgpt.com)

13\. The concrete phased plan
-----------------------------

### Phase 1: normalize foundations

Pick and freeze:

*   official Qwen3.5 main coder baseline
*   official Gemma 4 main manager/verifier baseline
*   one MLX fallback per family
*   one local quant per family
*   one EXL3 Qwen lane for consumer-GPU experiments

Success condition:

*   all models load through one registry and role-routing layer.

### Phase 2: serving overhaul

Stand up:

*   vLLM main serving plane
*   MLX laptop plane
*   ExLlamaV3 local-worker plane

Success condition:

*   same API schema, same tracing, same metrics across planes.

### Phase 3: role routing

Implement:

*   planner
*   worker
*   scout
*   verifier
*   reducer

Success condition:

*   tasks route by role instead of by one default model.

### Phase 4: eval harness

Run:

*   code tasks
*   UI review tasks
*   GIF/screenshot judgments
*   cost/latency sweeps
*   derivative comparison matrix

Success condition:

*   you have a promotion policy backed by numbers.

### Phase 5: speculation and quant optimization

Add:

*   speculative decoding to Qwen main workers
*   quant tiers for Gemma and Qwen
*   cost/perf routing

Success condition:

*   lower latency and lower cost without meaningful quality loss.

### Phase 6: family-specific fine-tuning

Train:

*   Qwen code-edit/tool-use SFTs
*   Gemma verifier/planner SFTs

Success condition:

*   measurable lift on your internal evals, not just vibes.

### Phase 7: self-improving loops

Add:

*   trace collection
*   verifier preference data
*   failure replay
*   task difficulty prediction
*   automatic model-role reassignment

Success condition:

*   the system gets better from operation, not only from manual tuning.

14\. The final shape I would aim for
------------------------------------

End state:

*   **Gemma 4 manager**
*   **Qwen3.5 primary code worker**
*   **Qwen3.5 smaller derivatives as scouts/drafters**
*   **Gemma 4 multimodal verifier**
*   **vLLM as core serving**
*   **MLX for Apple fallback**
*   **EXL3 only where local density wins enough to justify stack fragmentation**
*   **spec decode on core Qwen workers**
*   **internal eval gate before any derivative promotion**
*   **family-specific SFT instead of random model collecting**

That is the heavy overhaul.

The main mistake to avoid is treating Hugging Face as a buffet and trying to build a platform out of twenty unrelated derivatives. Use **Qwen3.5 and Gemma 4 as the two canonical families**, treat derivatives as deployment artifacts or narrowly scoped candidates, and rebuild the rest of the stack around **roles, serving, evals, and training data**. [Hugging Face+5Hugging Face+5Hugging Face+5](https://huggingface.co/Qwen/Qwen3.5-35B-A3B?utm_source=chatgpt.com)

If you want the next step, I’ll turn this into a **repo-grade implementation plan** with exact folders, services, APIs, model registry schema, routing policy, and evaluation pipeline.

---

**Sources:**

- [Qwen/Qwen3.5-35B-A3B](https://huggingface.co/Qwen/Qwen3.5-35B-A3B?utm_source=chatgpt.com)
- [Speculative Decoding - vLLM](https://docs.vllm.ai/en/latest/features/speculative_decoding/?utm_source=chatgpt.com)
- [turboderp-org/exllamav3](https://github.com/turboderp-org/exllamav3?utm_source=chatgpt.com)
- [Fine-Tune Gemma using Hugging Face Transformers and ...](https://ai.google.dev/gemma/docs/core/huggingface_text_finetune_qlora?utm_source=chatgpt.com)

## Prompt:
4/3/2026, 11:33:12 PM

Yes

## Response:
4/3/2026, 11:33:15 PM

I’m converting the architecture into an implementation blueprint: repo layout, services, APIs, routing policy, model registry, and eval pipeline.

> **Searching for official documentation and citations on models**
>
> [Qwen/Qwen3.5-35B-A3B](https://huggingface.co/Qwen/Qwen3.5-35B-A3B)
> [Speculative Decoding - vLLM](https://docs.vllm.ai/en/latest/features/speculative_decoding/)
> [turboderp-org/exllamav3](https://github.com/turboderp-org/exllamav3)
>
> Thought for 9s

Below is a repo-grade implementation plan for a **Qwen3.5 + Gemma 4** platform, built around what those families and runtimes actually support today: Qwen3.5 official Hugging Face releases explicitly call out compatibility with Transformers, vLLM, SGLang, and KTransformers; Gemma 4 official releases are open-weight, multimodal, and up to 256K context; vLLM supports multiple speculative-decoding methods including draft models, EAGLE, and MTP; and ExLlamaV3’s EXL3 is a QTIP-based quantization format with dynamic batching, speculative decoding, cache quantization, and TabbyAPI support. [GitHub+4Hugging Face+4Hugging Face+4](https://huggingface.co/Qwen/Qwen3.5-35B-A3B?utm_source=chatgpt.com)

1\. What you are building
-------------------------

A **model platform**, not just a router.

The platform has six layers:

1.  **registry** — every approved model, quant, adapter, and runtime form
2.  **serving** — vLLM, MLX, ExLlamaV3/Tabby lanes
3.  **routing** — role-based assignment of tasks to model families
4.  **swarm orchestration** — planner, workers, verifiers, reducer
5.  **evaluation** — automated promotion gates
6.  **training** — SFT / preference / draft-model / verifier tuning

The hard stance:

*   **Qwen3.5** is your primary **text/code family**
*   **Gemma 4** is your primary **multimodal / long-context / judge family**
*   derivatives are deployment artifacts or candidates, not your architecture

2\. The repository layout
-------------------------

Use a mono-repo for the platform itself.

```
llm-platform/
├─ README.md
├─ pyproject.toml
├─ uv.lock
├─ .env.example
├─ docker-compose.yml
├─ Makefile
├─ configs/
│  ├─ environments/
│  │  ├─ local.yaml
│  │  ├─ homebox.yaml
│  │  ├─ rental-48g.yaml
│  │  └─ laptop-mlx.yaml
│  ├─ routing/
│  │  ├─ roles.yaml
│  │  ├─ budgets.yaml
│  │  ├─ fallback_policy.yaml
│  │  └─ promotion_policy.yaml
│  ├─ serving/
│  │  ├─ vllm.yaml
│  │  ├─ exllama.yaml
│  │  ├─ mlx.yaml
│  │  └─ tabbyapi.yaml
│  └─ evals/
│     ├─ code.yaml
│     ├─ multimodal.yaml
│     ├─ latency.yaml
│     └─ regression.yaml
├─ registry/
│  ├─ models/
│  │  ├─ qwen/
│  │  │  ├─ qwen35-35b-a3b.yaml
│  │  │  ├─ qwen35-9b.yaml
│  │  │  ├─ qwen35-exl3-local.yaml
│  │  │  └─ qwen35-mlx.yaml
│  │  ├─ gemma/
│  │  │  ├─ gemma4-31b-it.yaml
│  │  │  ├─ gemma4-26b-a4b-it.yaml
│  │  │  ├─ gemma4-nvfp4.yaml
│  │  │  └─ gemma4-mlx.yaml
│  │  └─ candidates/
│  │     ├─ community/
│  │     └─ experimental/
│  ├─ adapters/
│  ├─ prompts/
│  └─ capabilities/
├─ services/
│  ├─ gateway/
│  │  ├─ app/
│  │  ├─ routers/
│  │  ├─ policies/
│  │  ├─ schemas/
│  │  └─ main.py
│  ├─ scheduler/
│  │  ├─ app/
│  │  └─ main.py
│  ├─ swarm/
│  │  ├─ planner/
│  │  ├─ worker/
│  │  ├─ verifier/
│  │  ├─ reducer/
│  │  └─ memory/
│  ├─ evals/
│  │  ├─ runners/
│  │  ├─ judges/
│  │  ├─ datasets/
│  │  └─ reports/
│  ├─ trainer/
│  │  ├─ sft/
│  │  ├─ dpo/
│  │  ├─ draft_model/
│  │  └─ verifier/
│  └─ ingest/
│     ├─ traces/
│     ├─ artifacts/
│     └─ repo_events/
├─ runtimes/
│  ├─ vllm/
│  ├─ exllama/
│  ├─ mlx/
│  └─ sandboxes/
├─ sdk/
│  ├─ python/
│  ├─ go/
│  └─ ts/
├─ datasets/
│  ├─ internal/
│  ├─ generated/
│  ├─ verified/
│  └─ multimodal/
├─ docs/
│  ├─ architecture/
│  ├─ ops/
│  ├─ evals/
│  ├─ training/
│  └─ governance/
└─ scripts/
   ├─ bootstrap/
   ├─ deploy/
   ├─ bench/
   └─ promote/
```

3\. The minimum service graph
-----------------------------

### `gateway`

Single OpenAI-compatible front door.

Responsibilities:

*   auth
*   request normalization
*   role selection
*   budget enforcement
*   trace IDs
*   prompt scaffold insertion
*   capability negotiation

### `scheduler`

Decides:

*   which runtime lane
*   which model
*   whether to spawn a swarm
*   whether to speculate
*   whether to escalate to multimodal verification

### `swarm`

Runs structured agent roles:

*   planner
*   worker(s)
*   verifier(s)
*   reducer

### `evals`

Runs promotion tests on:

*   code tasks
*   benchmark tasks
*   UI artifact tasks
*   latency/cost regressions

### `trainer`

Periodically trains:

*   code-edit SFTs
*   verifier SFTs
*   draft models for speculation
*   preference models or ranking heads

### `ingest`

Consumes:

*   traces
*   screenshots
*   test logs
*   repo metadata
*   PR feedback
*   failure signatures

4\. The role model
------------------

Your routing policy should be role-first, not model-first.

### Planner

Default:

*   **Gemma 4 31B IT**
*   fallback: Gemma 4 26B A4B IT

Use for:

*   task decomposition
*   multimodal understanding
*   long-context synthesis
*   acceptance criteria generation

Gemma 4 official releases are multimodal and support up to 256K context, which is why it fits manager/planner roles better than a pure code-specialist lane. [Hugging Face](https://huggingface.co/google/gemma-4-31B-it?utm_source=chatgpt.com)

### Main code worker

Default:

*   **Qwen3.5-35B-A3B**
*   fallback: Qwen3.5 9B tuned derivative when budget constrained

Use for:

*   core file edits
*   repair loops
*   tool use
*   patch generation

Qwen3.5’s official Hugging Face release explicitly lists compatibility with the main serving stacks you’d want in production. [Hugging Face](https://huggingface.co/Qwen/Qwen3.5-35B-A3B?utm_source=chatgpt.com)

### Draft worker

Default:

*   smaller same-family **Qwen3.5** derivative

Use for:

*   speculative decoding
*   cheap first-pass patch proposals
*   branch-local exploration

vLLM’s current docs support draft-model speculative decoding and list EAGLE, MTP, and draft-model paths as the stronger latency-reduction options. [vLLM+2vLLM+2](https://docs.vllm.ai/en/latest/features/speculative_decoding/?utm_source=chatgpt.com)

### Multimodal verifier

Default:

*   **Gemma 4 31B IT**
*   fallback: Gemma 4 26B A4B or NVFP4 deployment form

Use for:

*   screenshot review
*   GIF/recording judgment
*   “does the UI match the PR/issue claim?”

NVIDIA’s Gemma 4 NVFP4 release also explicitly frames Gemma 4 as useful for reasoning, coding, multimodal understanding, and consumer-GPU/workstation deployment. [Hugging Face+1](https://huggingface.co/nvidia/Gemma-4-31B-IT-NVFP4?utm_source=chatgpt.com)

### Cheap scout

Default:

*   Qwen3.5 0.8B–9B derivatives
*   local quant builds where needed

Use for:

*   grep/search summaries
*   file-map construction
*   low-cost branch exploration
*   test candidate drafting

### Reducer

Default:

*   same-family as the main code worker unless multimodal arbitration is needed

Use for:

*   merge candidate outputs
*   style normalization
*   conflict resolution

5\. The model registry schema
-----------------------------

Use a real registry, not hardcoded model names.

Example YAML:

```
id: qwen35_35b_a3b_main
family: qwen35
vendor: qwen
source: huggingface
hf_repo: Qwen/Qwen3.5-35B-A3B
runtime_forms:
  - type: vllm
    enabled: true
  - type: sglang
    enabled: true
  - type: exllama
    enabled: false
  - type: mlx
    enabled: false
role_affinity:
  planner: 0.35
  coder_main: 0.98
  coder_draft: 0.20
  verifier_text: 0.82
  verifier_mm: 0.05
capabilities:
  text: true
  image_input: false
  tool_calling: true
  code_editing: true
  long_context: medium
cost_profile:
  local_gpu: medium
  rental_gpu: medium
latency_profile:
  prefill: medium
  decode: medium
promotion_status: production
trust_tier: official
eval_requirements:
  - code_passrate_min: 0.72
  - regression_fail_max: 0.03
  - verifier_hallucination_max: 0.05
```

Gemma example:

```
id: gemma4_31b_it_mm_manager
family: gemma4
vendor: google
source: huggingface
hf_repo: google/gemma-4-31B-it
runtime_forms:
  - type: vllm
    enabled: true
  - type: mlx
    enabled: true
  - type: nvfp4
    enabled: true
role_affinity:
  planner: 0.97
  coder_main: 0.68
  coder_draft: 0.10
  verifier_text: 0.88
  verifier_mm: 0.99
capabilities:
  text: true
  image_input: true
  multimodal: true
  long_context: high
promotion_status: production
trust_tier: official
```

6\. The routing policy
----------------------

Use a scorecard, not ad hoc heuristics.

### Inputs

*   task type
*   repo size
*   file count touched
*   multimodal artifacts present
*   latency budget
*   token budget
*   hardware availability
*   historical failure patterns
*   required confidence

### Score components

*   role affinity
*   capability match
*   eval score
*   runtime availability
*   cost
*   expected latency
*   recent regression rate
*   context fit

### Hard rules

*   if image/video artifact exists, planner or verifier must be multimodal-capable
*   if task is code patching, primary worker must be from Qwen family unless explicit override
*   community derivatives cannot be selected for production paths without promotion status
*   EXL3 lane is only eligible on designated local-GPU targets

7\. The API surface
-------------------

### `POST /v1/tasks/run`

Single entry point for work requests.

Request:

```
{
  "task_type": "code_patch",
  "repo": {
    "url": "git@example.com/org/repo.git",
    "ref": "main"
  },
  "goal": "Fix broken auth callback in desktop app",
  "artifacts": [
    {"type": "image", "uri": "s3://.../before.png"},
    {"type": "gif", "uri": "s3://.../repro.gif"}
  ],
  "constraints": {
    "max_cost_usd": 1.50,
    "max_minutes": 12,
    "require_multimodal_verification": true
  }
}
```

Response:

```
{
  "run_id": "run_123",
  "route": {
    "planner": "gemma4_31b_it_mm_manager",
    "workers": ["qwen35_35b_a3b_main", "qwen35_9b_scout"],
    "verifiers": ["gemma4_31b_it_mm_manager"]
  }
}
```

### `POST /v1/evals/run`

Runs a model, runtime, or derivative through gated evaluations.

### `POST /v1/models/promote`

Requires eval report IDs and signed approval policy.

### `GET /v1/traces/{run_id}`

Returns structured trace, artifact links, timing, model usage, pass/fail.

8\. The swarm execution protocol
--------------------------------

### Step 1: planning

Planner emits:

*   task DAG
*   acceptance criteria
*   required artifacts
*   file hypotheses
*   stop conditions

### Step 2: worker fanout

Workers receive:

*   bounded subtask
*   allowed files/modules
*   token budget
*   tool budget
*   required evidence

### Step 3: verification

Verifiers check:

*   tests
*   lint/type/security
*   diff scope
*   screenshot/GIF/terminal evidence if present
*   mismatch between claimed fix and observed behavior

### Step 4: reduction

Reducer decides:

*   accept worker A patch
*   merge worker A+B
*   request repair round
*   escalate to different runtime/model

### Step 5: trace capture

Everything is logged:

*   prompts
*   tools
*   diffs
*   artifacts
*   timings
*   scores
*   failure reasons

9\. Serving lanes
-----------------

### Lane A: vLLM

Primary production lane.

Use for:

*   Qwen3.5 main workers
*   Gemma 4 manager/verifier
*   speculative decoding experiments
*   batch evals

Why:

*   Qwen official compatibility
*   speculation support
*   draft models and MTP/EAGLE support in docs

[vLLM+3Hugging Face+3vLLM+3](https://huggingface.co/Qwen/Qwen3.5-35B-A3B?utm_source=chatgpt.com)

### Lane B: MLX

Travel / Mac / fallback lane.

Use for:

*   local planning
*   lightweight verification
*   degraded offline mode

### Lane C: ExLlamaV3 / TabbyAPI

Consumer-GPU density lane.

Use for:

*   local cheap Qwen workers
*   EXL3 experiments
*   high worker count per limited VRAM

ExLlamaV3’s official repo explicitly describes EXL3 as QTIP-based and lists dynamic batching, speculative decoding, cache quantization, and TabbyAPI support. [GitHub+1](https://github.com/turboderp-org/exllamav3?utm_source=chatgpt.com)

10\. Speculative decoding plan
------------------------------

Do not make speculation universal at first.

### Phase 1

Enable speculation only for:

*   Qwen main worker on repetitive code-edit tasks
*   fixed prompt scaffolds
*   same-family draft model

### Phase 2

Experiment with:

*   draft model
*   MTP
*   EAGLE

vLLM says model-based methods like EAGLE, MTP, and draft models give the best latency reduction, while simpler methods like n-gram and suffix speculation offer more modest gains. [vLLM+1](https://docs.vllm.ai/en/latest/features/speculative_decoding/?utm_source=chatgpt.com)

### Phase 3

Adaptive speculation  
Select speculation mode by:

*   prompt length
*   concurrency
*   recent acceptance rate
*   task type

11\. Evaluation pipeline
------------------------

Every model/runtime/quant candidate must pass four gates.

### Gate A: code correctness

*   unit/integration pass rate
*   regression rate
*   patch acceptance rate
*   over-edit rate

### Gate B: agent behavior

*   tool misuse rate
*   wrong-file-edit rate
*   retry waste
*   fake-completion rate

### Gate C: multimodal truthfulness

*   screenshot alignment
*   GIF / terminal sequence correctness
*   claim-to-artifact consistency

### Gate D: ops

*   TTFT
*   decode TPS
*   time to green
*   tokens per accepted patch
*   cost per accepted patch
*   GPU memory footprint

Promotion rule example:

*   official model: can enter staging after passing all four
*   community derivative: must beat baseline on at least one primary metric and not regress more than threshold on any safety metric

12\. Training plan
------------------

### Qwen training lane

Focus on:

*   code-edit SFT
*   repair-loop exemplars
*   repo-style adaptation
*   tool-call format consistency
*   draft-model distillation

### Gemma training lane

Focus on:

*   screenshot/GIF verifier SFT
*   planner exemplars
*   issue triage from multimodal artifacts
*   long-context summarization

### Shared data lake

Store:

*   repo snapshot
*   problem statement
*   selected files
*   prompts
*   tool traces
*   output diffs
*   tests
*   screenshots/GIFs
*   final verdict

13\. Hardware mapping
---------------------

### 3090 Ti / local box

Best use:

*   Qwen cheap workers
*   EXL3 experiments
*   scout and draft roles
*   local dev evals

### M1 Pro / Apple Silicon

Best use:

*   MLX fallback
*   planner-lite
*   summarizer
*   degraded offline mode

### 48 GB rental

Best use:

*   main Qwen worker
*   Gemma 4 manager/verifier
*   batch evals
*   training/fine-tune runs
*   speculative decoding experiments

14\. Governance
---------------

You need trust tiers.

### Tier 1: official

*   vendor-authored official repos
*   production eligible after eval pass

### Tier 2: sanctioned derivative

*   internal fine-tune / quant / adapter
*   production eligible after stronger eval

### Tier 3: community candidate

*   isolated sandbox only
*   cannot auto-promote
*   full provenance required

### Tier 4: experimental

*   no production path
*   eval and research only

15\. The first 30 days
----------------------

### Week 1

*   stand up registry
*   stand up gateway
*   register official Qwen3.5 + Gemma 4 baselines
*   add vLLM lane

### Week 2

*   add swarm roles
*   add basic task router
*   add trace capture
*   add evaluation harness skeleton

### Week 3

*   add multimodal verification
*   add MLX fallback
*   add EXL3 local lane for Qwen
*   run baseline eval matrix

### Week 4

*   enable speculative decoding on one Qwen path
*   collect trace data
*   define promotion thresholds
*   freeze first production roster

16\. The first production roster
--------------------------------

Start with just this:

*   `gemma4_31b_it_mm_manager`
*   `gemma4_26b_a4b_it_mm_fallback`
*   `qwen35_35b_a3b_main`
*   `qwen35_9b_scout`
*   `qwen35_9b_draft`
*   `qwen35_exl3_local_scout`
*   `gemma4_nvfp4_mm_verifier`

Everything else stays candidate-only until it passes evals.

17\. What not to do
-------------------

Do not:

*   let every task pick from dozens of HF repos
*   mix community derivatives into production routing by default
*   make EXL3 your universal serving standard
*   let multimodal QA be optional for UI-heavy work
*   add 10 speculation modes before you measure one
*   let long context substitute for memory design

18\. End state
--------------

You want:

*   one gateway
*   one registry
*   three serving lanes
*   two canonical model families
*   role-based routing
*   multimodal verification
*   trace-driven training
*   eval-gated promotion

That is the full overhaul in implementation form.

If you want the next step, I can write the actual starter files: `roles.yaml`, model-registry YAMLs, FastAPI schemas, and the routing policy pseudocode.

---

**Sources:**

- [Qwen/Qwen3.5-35B-A3B](https://huggingface.co/Qwen/Qwen3.5-35B-A3B?utm_source=chatgpt.com)
- [Speculative Decoding - vLLM](https://docs.vllm.ai/en/latest/features/speculative_decoding/?utm_source=chatgpt.com)
- [turboderp-org/exllamav3](https://github.com/turboderp-org/exllamav3?utm_source=chatgpt.com)



---
Powered by [ChatGPT Exporter](https://www.chatgptexporter.com)