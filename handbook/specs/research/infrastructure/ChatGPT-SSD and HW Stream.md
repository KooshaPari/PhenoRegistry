# SSD and HW Stream

**User:** Anonymous  
**Created:** 7/24/2026 23:30:25  
**Updated:** 7/28/2026 18:16:39  
**Exported:** 7/30/2026 20:47:11  
**Link:** [https://chatgpt.com/c/6a645801-3f54-83e8-bb43-6aebc545f0b0](https://chatgpt.com/c/6a645801-3f54-83e8-bb43-6aebc545f0b0)  

## Prompt:
7/24/2026, 11:30:24 PM

:) 

Fake speculative speculative decoding (SSD) \ DSpark \ Jetspec?

E.g.

An algorithm and\or in mem\disk server semantic user caches along with more used to predict response tokens based on next prompt. utilizing seperate HW stream (E.g.) CPU or just somehow GPU more efficiently ot make logical efficiency gains\sense over equivalent SSD config

## Response:
7/24/2026, 11:30:26 PM

I’m framing this as an architecture question: can semantic and user-history caches serve as a CPU/NVMe draft path, and when would that outperform standard speculative decoding?

## Prompt:
7/24/2026, 11:33:18 PM

should be viewed as a way of predicting uncahced tokens based on cached tokens, also research perhaps LLM side (internal arch) too?

## Response:
7/24/2026, 11:33:31 PM

The novel angle is combining cache-only drafting, draft–verify overlap, and inter-turn personalized speculation into a hierarchical path that exploits otherwise unavailable pre-arrival compute.

More precisely, this is conditional cache completion: use cached prefixes and KV/latent state to synthesize uncached prompt tokens, retaining only verified model state.

# Verdict

Yes. The technically useful formulation is:

> **Cache-conditioned speculative synthesis:** use cached token sequences, target-model artifacts, user history, and semantic neighbors as evidence for a cheap proposer that generates **new continuation edges not present in the cache**, then let the target model verify them.

That is materially different from ordinary semantic caching, which returns an old response, and from Prompt Lookup Decoding, which copies an old continuation.

The closest existing systems now cover most of the individual pieces:

| Work | Relevant contribution | Missing from your stronger formulation |
|---|---|---|
| **Cacheback** | Uses an LRU cache of token n-grams to construct speculative token trees without a neural drafter. | It primarily replays observed continuations rather than synthesizing genuinely new ones. ([arXiv](https://arxiv.org/html/2511.21699v1)) |
| **RASD** | Fuses a retrieval-derived tree with a model-generated draft tree. | Retrieval and generation remain separate candidate sources; memory does not deeply condition the drafter. ([arXiv](https://arxiv.org/html/2503.03434)) |
| **RACER** | Combines exact retrieved patterns with target-logit-derived extrapolation, explicitly using retrieval to guide predictions beyond exact matches. This is the closest training-free precedent. | Its retrieval is token-pattern-oriented, not a persistent semantic, user-specific latent memory. ([arXiv](https://arxiv.org/html/2604.14885)) |
| **CARD** | Runs the draft and target asynchronously through a shared candidate cache-almost exactly your separate-hardware-stream concept. | Its cache is populated by the currently running drafter, rather than long-lived user/domain memory. ([arXiv](https://arxiv.org/html/2508.04462v2)) |
| **DSpark** | Semi-autoregressive parallel drafting plus per-position survival confidence and hardware-aware verification scheduling. | No persistent semantic continuation memory. ([arXiv](https://arxiv.org/html/2607.05147)) |
| **JetSpec** | One-pass, branch-causally-conditioned token-tree prediction from target hidden states. | No external or user-specific associative memory. ([arXiv](https://arxiv.org/html/2606.18394v2)) |
| **OSD / TTS** | Continuously adapts a drafter from the target’s verification outputs and observed user-query distribution. | It parameterizes experience into weights instead of retaining a queryable episodic cache. ([Proceedings of Machine Learning Research](https://proceedings.mlr.press/v235/liu24y.html?utm_source=chatgpt.com)) |

So the idea is not blank-space novelty, but the complete combination is still meaningfully differentiated.

I would call it **Semantic Cache-Conditioned Speculative Decoding**, or **SC²D**. Reserve **S²D** for the two-level version that first predicts the next prompt or agent action and then speculatively decodes the predicted response. Avoid `SSD`, since storage and decoding become impossible to distinguish in the design.

---

# The critical distinction: cache-derived versus cache-conditioned

## Cache-derived drafting

A cache contains:

```text
"the target model" → "then verifies the candidate tokens"
```

When the current output ends in `"the target model"`, the system copies the cached continuation.

That is Cacheback, PLD, suffix decoding, or REST territory.

## Cache-conditioned synthesis

The memory instead contains several related fragments:

```text
A: "the target model" → "verifies all proposed tokens"
B: "candidate branches" → "are evaluated in parallel"
C: "verification failure" → "causes the suffix to be discarded"
```

The drafter synthesizes:

```text
"the target model verifies the candidate branches in parallel"
```

even though that complete continuation never appeared in the cache.

The cache has reduced uncertainty without containing the answer verbatim.

Formally, with current prefix $X$, next response tokens $Y$, and retrieved memory $M$:

$$
\Delta H
=
H(Y\mid X)-H(Y\mid X,M)
=
I(Y;M\mid X)
$$

The memory is useful precisely when its conditional mutual information with the continuation is positive. The system-level question is then whether the cost of extracting that information is lower than the target-model work it avoids.

One terminology correction matters here: an “uncached token” is not a useful unit because nearly every vocabulary token will already exist somewhere in the cache. Measure **uncached continuation edges** or **novel n-grams**:

$$
(\text{current suffix}\rightarrow\text{next token})
\notin M
$$

An accepted novel edge proves synthesis rather than replay.

---

# Proposed architecture

```text
                         PERSISTENT MEMORY PLANE
       ┌───────────────────────────────────────────────────────┐
       │ User episodes │ Domain traces │ Code/AST │ Tool paths │
       │ Prior outputs │ Logit sketches│ Hidden/KV projections │
       └───────────────┬───────────────────────────────┬───────┘
                       │                               │
                semantic retrieval             exact suffix lookup
                once per request                every decode round
                       │                               │
                       └──────────────┬────────────────┘
                                      ▼
                         Request-local memory graph
                     ┌────────────────────────────────┐
                     │ exact paths                    │
                     │ semantic continuation evidence │
                     │ structural templates           │
                     │ user/task/style state          │
                     └───────────────┬────────────────┘
                                     │
 Current target hidden state/logits ─┼──────────────┐
                                     ▼              │
                     Cache-conditioned draft head   │
                 ┌───────────────────────────────────┴──────┐
                 │ JetSpec-style causal parallel tree      │
                 │ DSpark-style sequential correction      │
                 │ retrieved-span cross-attention          │
                 │ acceptance/survival confidence          │
                 └──────────────────────┬───────────────────┘
                                        ▼
                        Expected-goodput tree scheduler
                                        ▼
                            Target-model verification
                                        ▼
                accepted tokens + rejected alternatives + logits
                                        │
                         cache update / online distillation
```

The important systems choice is a **two-stage retrieval path**:

1. **Turn-level semantic retrieval** narrows millions of historical memories to perhaps dozens of relevant episodes.
2. **Token-level exact or latent lookup** operates only over that small request-local candidate graph.

Running a full embedding search for every output token would likely erase much of the benefit. Semantic retrieval is coarse request setup; the inner decode loop should be automata, tries, small matrix operations, and cached latent lookups.

---

# Internal LLM architecture

The safest architecture modifies only the **draft path**, not the target path.

That preserves the target model as the authority and keeps stale or misleading memory from directly changing its distribution. Putting external memory inside the target model would become memory-augmented generation rather than pure inference acceleration.

## 1. Memory query head

At one or more target layers, derive a compact retrieval query:

$$
q_t = W_q h_t
$$

where $h_t$ is the current target hidden state. Retrieve memories by a mixture of:

- semantic similarity;
- user/session identity;
- task, repository, file, tool, or schema identity;
- suffix/token alignment;
- historical target acceptance;
- current system load.

Semantic similarity alone is the wrong objective. A semantically relevant memory can be lexically useless for speculative verification. The final retrieval score should predict **accepted target tokens per unit cost**.

## 2. Memory representation

Each memory can have several compiled forms:

```text
Canonical episode:
  prompt / response / tool trace / AST / diff / metadata

Model-specific compilation:
  tokenizer-specific continuation trie
  top-k target logit sketches
  compressed hidden-state sequence
  selected KV projections
  acceptance statistics
```

This supports your heterogeneous model fabric. Text and structural representations remain portable, while token, hidden-state, and KV artifacts are explicitly namespaced by:

```text
model hash × tokenizer hash × quantization × architecture version
```

A kNN-addressable external memory has already been integrated successfully into Transformer attention in Memorizing Transformers, and newer Cache-to-Cache work shows that learned projection and fusion of KV representations is possible across models. Those are architectural precedents, although neither is itself a speculative-decoding system. ([arXiv](https://arxiv.org/abs/2203.08913?utm_source=chatgpt.com))

## 3. Gated memory fusion

Let $R_t$ be retrieved token or latent memories:

$$
m_t
=
\operatorname{CrossAttention}
\left(
W_q h_t,\,
K(R_t),\,
V(R_t)
\right)
$$

$$
z_t
=
h_t+
g_t\odot W_m m_t
$$

The gate should be able to suppress memory entirely. That matters when retrieval is semantically close but continuation-incompatible.

## 4. Causal parallel tree head

Feed $z_t$ to a JetSpec-like draft head that generates an entire candidate tree in one pass while preserving causal conditioning between branch ancestors. JetSpec’s core result is that one-pass drafting need not sacrifice branch-wise causal consistency. ([arXiv](https://arxiv.org/html/2606.18394v2))

## 5. Lightweight sequential correction

Add a DSpark-style low-rank Markov or recurrent correction:

$$
\ell_i'
=
\ell_i^{\text{parallel}}
+
B(y_{i-1},s_{i-1})
$$

This handles the problem where parallel positions independently choose plausible but mutually inconsistent tokens. DSpark uses precisely this heavy-parallel/light-serial split to reduce suffix acceptance decay. ([arXiv](https://arxiv.org/html/2607.05147))

## 6. Acceptance-confidence head

For every candidate position:

$$
c_i
=
P_\phi
\left(
y_i\text{ accepted}
\mid
y_{<i}\text{ accepted},X,M
\right)
$$

The survival probability of a prefix is approximately:

$$
P_{\text{survive}}(1{:}j)
=
\prod_{i=1}^{j}c_i
$$

This supports dynamic pruning based on both candidate quality and current target-GPU load.

## 7. Online user adaptation

Every target verification already produces supervision:

- target logits;
- accepted/rejected tokens;
- accepted prefix length;
- memory provenance;
- actual latency and verification cost.

Use that to train only:

- the memory retriever;
- a small user/domain adapter;
- the draft head;
- the confidence head.

Online Speculative Decoding demonstrated that adapting drafters to observed query distributions can materially improve acceptance, while Test-Time Speculation uses each verification round directly as an online distillation sample. ([Proceedings of Machine Learning Research](https://proceedings.mlr.press/v235/liu24y.html?utm_source=chatgpt.com))

A suitable objective is:

$$
\mathcal L
=
\lambda_{\mathrm{KL}}
D_{\mathrm{KL}}(p_\theta\Vert q_\phi)
+
\lambda_{\mathrm{accept}}
\operatorname{BCE}(c,\hat c)
+
\lambda_{\mathrm{retrieval}}
\mathcal L_{\mathrm{rank}}
+
\lambda_{\mathrm{cost}}
\mathbb E[\text{wasted verification tokens}]
$$

The retriever should be trained on **acceptance gain**, not generic embedding relevance.

---

# Heterogeneous execution on your hardware

## Recommended placement

| Resource | Role |
|---|---|
| **Ryzen 5800X + 64 GB RAM** | Hot continuation automata, semantic index, candidate union, pruning, confidence bookkeeping, cache updates. |
| **980 Pro / other NVMe** | Persistent cold episodes, compressed token graphs, latent artifacts, snapshots and replay logs. Not the per-token critical path. |
| **RTX 3090 Ti** | Target model, tree verification, and preferably the hidden-state-conditioned draft head. |
| **GTX 1080 Ti** | Optional asynchronous microdrafter or branch explorer that continuously fills candidate queues. Do not make the target wait for it. |
| **Same-GPU secondary CUDA stream** | Potentially useful for tiny draft heads, but only when profiling proves that concurrent kernels exploit otherwise idle resources instead of contending with verification. |

The strongest initial design is:

```text
CPU/RAM cache proposer
        │ token IDs + compact scores
        ▼
3090 Ti target verifier
```

This has no second model, no second KV cache, and almost no GPU-memory overhead. Production measurements have found CPU-resident n-gram drafting to have effectively zero additional GPU-memory footprint, but they also show that target verification-not drafting-is generally the dominant speculative-decoding cost. ([arXiv](https://arxiv.org/html/2601.11580v1))

The 1080 Ti becomes useful later under a CARD-like asynchronous model:

```text
1080 Ti:
  continuously advances several likely draft branches
  writes token trees into shared pinned memory

3090 Ti:
  consumes whichever branch still agrees with verified output
  sends occasional correction/pruning messages
```

Only token IDs, scores, and branch metadata should cross between the GPUs. Sending large target hidden states across the mixed-GPU boundary every speculative round would probably destroy the intended gain.

CARD validates the broader “draft continuously into a shared cache while target query-and-correct runs concurrently” architecture, and WANSpec shows that even remote or older draft hardware can be useful when drafting is explicitly latency-tolerant and never allowed to stall the target. ([arXiv](https://arxiv.org/html/2508.04462v2))

---

# Break-even condition

For ordinary serial speculative decoding:

$$
T_{\text{round}}
=
T_{\text{draft}}
+
T_{\text{verify}}
+
T_{\text{system}}
$$

For your overlapped cache-conditioned form:

$$
T_{\text{draft,eff}}
=
\max
\left(
0,\,
T_{\text{retrieve}}
+
T_{\text{synthesize}}
+
T_{\text{transfer}}
-
T_{\text{available overlap}}
\right)
$$

$$
S
\approx
\frac{
\mathbb E[C]\;T_{\mathrm{AR}}
}{
T_{\text{verify}}
+
T_{\text{draft,eff}}
+
T_{\text{sync}}
}
$$

where:

- $C$ is the number of committed tokens per round;
- $T_{\mathrm{AR}}$ is ordinary target decode time per token;
- $T_{\text{verify}}$ includes rejected candidates;
- $T_{\text{draft,eff}}$ is only the non-overlapped proposal cost.

A candidate node $i$ should be admitted only when:

$$
P_{\text{survive}}(i)\cdot
\Delta T_{\text{target saved}}
>
\Delta T_{\text{verification}}
+
\Delta T_{\text{draft,eff}}
+
\lambda_{\text{load}}
$$

This is the generalization of DSpark’s hardware-aware prefix scheduler: the left side is expected benefit; the right side includes both direct cost and the opportunity cost of consuming batch capacity.

## The blunt concurrency issue

Your expected 100-512-agent regimes are the danger zone.

Speculative decoding helps most when target decoding is memory-bound and there is underutilized arithmetic capacity. As batch size rises, target verification becomes increasingly expensive relative to ordinary continuous batching. One production-oriented study found EAGLE’s relative speedup on an 8B workload falling from $1.73\times$ at batch size 1 to $1.21\times$ at batch size 128, and explicitly identifies verification as the dominant bottleneck. ([arXiv](https://arxiv.org/html/2601.11580v1))

Therefore, your scheduler needs a real **depth-zero state**:

```text
Low load / interactive:
  semantic cache + neural tree; wider and deeper speculation

Moderate load:
  exact cache + shallow neural branches

High load:
  exact high-confidence cache proposals only

Saturated:
  speculation disabled; ordinary continuous batching
```

Current SGLang work is moving in exactly this direction: runtime selection among speculative depths, including depth zero, based on acceptance length, batch size, sequence lengths, and expected throughput. ([GitHub](https://github.com/sgl-project/sglang/issues/23705))

---

# Two-level “speculative speculative decoding”

Your initial wording becomes exact when prediction begins **before the next prompt is known**.

```text
Conversation / agent state
          │
          ▼
Predict likely next prompt, intent, tool call, or work package
          │
       top-k branches
          │
          ▼
For each likely branch:
  prefill probable prompt prefix
  retrieve branch-specific memories
  generate response draft trees
  optionally execute reversible tools
          │
          ▼
Actual next prompt arrives
          │
  ┌───────┴──────────────────────────────────┐
  │ exact branch/prefix match                │ semantic-only match
  ▼                                          ▼
reuse target KV and drafts             use response only as drafts
```

There are two distinct commit rules:

### Exact-token branch match

If the actual prompt shares the exact predicted token prefix, its precomputed target KV state is reusable up to the divergence point.

### Semantic branch match

A semantically similar prompt does **not** have the same KV state. You cannot safely substitute the precomputed KV cache. Its predicted response can still be used as a token-tree proposal and verified normally.

This outer speculation is most likely to pay in:

- agent-to-agent protocols;
- tool loops;
- code-edit/test/fix cycles;
- structured harness workflows;
- your RLVR-AF predicted session trajectories;
- recurring manager/worker prompts.

It is much less reliable for unconstrained human prompts. SPORK provides recent evidence for the agentic version: a running model can often reveal its future tool call early, and even failed speculative probes can contain reusable verified prefixes. ([arXiv](https://arxiv.org/html/2607.03333v1))

Your asymptote/session-path predictor therefore has a direct systems use:

```text
Predicted future session graph
             ↓
 speculative prompt branches
             ↓
 speculative response/token/tool caches
             ↓
 verified consumption as real session unfolds
```

That converts a planning artifact into actual latency and compute reduction.

---

# The implementation I would build

## Phase A - training-free SC²D

Use a custom proposer behind either vLLM or SGLang:

```text
1. Persist target-generated tokens and request metadata.
2. Build per-session and per-user suffix automata / AC automata.
3. Perform one semantic search at request admission.
4. Compile retrieved episodes into a request-local token graph.
5. During decoding:
     a. exact suffix continuation lookup;
     b. RACER-style cached-logit expansion for missing edges;
     c. tree union;
     d. cost/confidence pruning;
     e. target verification.
6. Record accepted and rejected novel edges.
```

vLLM currently supports n-gram, suffix, EAGLE, MTP, dynamic speculation, and an experimental custom proposer backend. SGLang’s n-gram work already identifies external-corpus loading as a missing capability, which is precisely where your cache server would extend it. ([vLLM](https://docs.vllm.ai/en/stable/features/speculative_decoding/))

For your existing SGLang stack, I would define a runtime-neutral proposer interface:

```rust
pub trait SpeculativeProposer {
    fn begin_request(&self, context: RequestContext) -> RequestMemory;
    fn propose(
        &self,
        prefix: &[TokenId],
        artifacts: &TargetArtifacts,
        load: &EngineLoad,
    ) -> CandidateTree;
    fn observe(&self, result: VerificationResult);
}
```

Implementations:

```text
NgramProposer
SuffixProposer
RacerProposer
SemanticCacheProposer
NeuralCacheProposer
CompositeProposer
```

That permits controlled comparisons rather than baking the research idea directly into one engine.

## Phase B - cache-conditioned neural drafter

Train a small memory-conditioned JetSpec/DSpark head:

```text
target hidden state
+ retrieved memory latents
+ current target logit sketch
+ user/domain adapter
→ causal parallel draft tree
→ sequential transition correction
→ survival confidence
```

DeepSeek’s DeepSpec repository now provides an open training/evaluation path for DSpark-style and EAGLE-style draft models, making it a reasonable substrate for this stage. ([GitHub](https://github.com/deepseek-ai/DeepSpec))

## Phase C - asynchronous 1080 Ti worker

Run a compact drafter ahead CARD-style. It should receive only:

```text
verified token prefix updates
request-local retrieved memory IDs
branch-pruning messages
```

It returns:

```text
token trees
proposal probabilities
confidence estimates
```

The 3090 Ti must always be able to continue without it.

## Phase D - outer S²D

Connect your full-turn/session predictor:

```text
predicted next work package
→ speculative prompt branches
→ speculative prefill/draft/tool work
→ exact or draft-only reuse
```

This should be separately gated by idle-power budget and branch entropy.

---

# How to prove it is more than caching

Use these metrics in addition to ordinary throughput:

$$
\text{Novel Edge Acceptance Rate}
=
\frac{
\text{accepted speculative edges absent from retrieved memory}
}{
\text{all accepted speculative edges}
}
$$

$$
\text{Cache-Conditioning Synergy}
=
G_{\text{hybrid}}
-
\max
\left(
G_{\text{cache-only}},
G_{\text{drafter-only}}
\right)
$$

$$
\text{Useful Memory Yield}
=
\frac{
\text{target decode time avoided}
}{
\text{bytes retrieved}+
\text{memory-processing cost}
}
$$

$$
\text{Waste Ratio}
=
\frac{
\text{drafted and verified tokens rejected}
}{
\text{all speculative tokens}
}
$$

Benchmark at minimum:

| Variable | Required comparisons |
|---|---|
| Workload | code editing, tool JSON, repo agent work, chat, long reasoning |
| Memory | none, current prompt, current session, user history, global domain |
| Proposal | exact cache, RACER, neural head, hybrid |
| Hardware | CPU only, same GPU, 1080 Ti async |
| Load | 1, 8, 32, 128, and saturation |
| Storage | RAM-hot, NVMe-cold with request prefetch |
| Adaptation | fixed, OSD-style batch updates, per-request TTS |
| Sampling | greedy first; then properly corrected stochastic sampling |

The essential falsification tests are:

1. **Exact retrieval alone wins.** Then the neural memory path is unnecessary.
2. **JetSpec/DSpark alone wins.** Then semantic memory is noise or too expensive.
3. **Hybrid acceptance rises but throughput falls.** Then verification or synchronization dominates.
4. **All accepted tokens are copied cache edges.** Then this is merely retrieval-based decoding.
5. **Gain disappears above modest concurrency.** Then it remains an interactive-latency optimization, not your high-width agent throughput solution.
6. **Online adaptation beats explicit memory.** Then experience should be distilled into a per-user drafter rather than retrieved on every request.

---

# Final design judgment

The best system is not one new speculative algorithm. It is a **hierarchical proposer fabric**:

```text
Cacheback / suffix lookup
    for nearly free exact repetition

RACER-style logit bridging
    for training-free uncached continuation edges

Memory-conditioned JetSpec head
    for compositional causal tree synthesis

DSpark confidence scheduler
    for load-aware verification allocation

CARD-style asynchronous worker
    for spare CPU / secondary-GPU utilization

OSD / TTS adaptation
    for continuously learning the user's actual distribution

Outer session-path predictor
    for true S²D across prompts, tools, and turns
```

The genuinely new research center is:

> **Retrieve semantically or structurally related cached trajectories, encode them as draft-only latent memory, synthesize novel token-tree continuations, and schedule verification according to expected accepted target work per unit of heterogeneous compute.**

That is logically sound. It can outperform ordinary DSpark or JetSpec where your workloads contain persistent user-, repository-, agent-role-, schema-, or workflow-level regularity. It will not automatically improve saturated 100-512-agent serving; there, the acceptance-aware scheduler and the ability to shut speculation off are as important as the drafter itself.

---

**Sources:**

- [https://arxiv.org/html/2511.21699v1](https://arxiv.org/html/2511.21699v1)
- [Online Speculative Decoding](https://proceedings.mlr.press/v235/liu24y.html?utm_source=chatgpt.com)
- [[Roadmap] Adaptive Speculative Decoding Roadmap · Issue #23705 · sgl-project/sglang · GitHub](https://github.com/sgl-project/sglang/issues/23705)
- [Speculative Decoding - vLLM](https://docs.vllm.ai/en/stable/features/speculative_decoding/)

## Prompt:
7/25/2026, 12:05:20 AM

why not multi layer? e.g. if SSD\Jetspec\Dspark other methods integrated then the speculator couldbe integrated

## Response:
7/25/2026, 12:05:23 AM

Yes—the stronger design is internally integrated and multi-layered across transformer depths, speculation timescales, and proposer methods, provided exactness remains intact and wall-clock cost actually falls.

SSD supplies the execution schedule, JetSpec the tree topology, and DSpark draft quality and verification control; these largely orthogonal components can share one speculative trunk.

> **Explaining multi-layer architecture**
>
> The user is asking about multi-layer integration in speculative subsystems. I'll explain why previous suggestions were conservative and propose a multi-layer solution, considering current papers and architecture options.
>
> **Explained multi-layer architecture**
>
> 
>
> **Searching for 2026 papers on multi-layer speculative decoding**
>
> [JetSpec: Breaking the Scaling Ceiling of Speculative Decoding with ...](https://arxiv.org/abs/2606.18394)
> [DeepSeek](https://chat.deepseek.com/)
> [JetSpec: Breaking the Scaling Ceiling of Speculative Decoding with ...](https://huggingface.co/papers/2606.18394)
> [Enabling Early Exit Inference and Self-Speculative Decoding](https://ai.meta.com/research/publications/layerskip-enabling-early-exit-inference-and-self-speculative-decoding/)
> [DeepSeek](https://www.deepseek.com/en/)
> [JetSpec: Breaking the Scaling Ceiling of Speculative Decoding with ...](https://haoailab.com/blogs/parallel-tree-decoding/)
> [DSpark: Confidence-Scheduled Speculative Decoding with Semi ...](https://www.alphaxiv.org/overview/2607.05147)
> [Enabling Early Exit Inference and Self-Speculative Decoding](https://aclanthology.org/2024.acl-long.681.pdf)
> [DeepSeek Platform](https://platform.deepseek.com/)
> [hao-ai-lab/JetSpec - Parallel Tree Drafting - GitHub](https://github.com/hao-ai-lab/JetSpec)
> [DSpark: Speculative decoding accelerates LLM inference [pdf]](https://news.ycombinator.com/item?id=48696585)
> [LayerSkip: faster LLM Inference with Early Exit and Self ...](https://medium.com/%40techsachin/layerskip-faster-llm-inference-with-early-exit-and-self-speculative-decoding-3110cb93c94e)
> [DeepSeek](https://en.wikipedia.org/wiki/DeepSeek)
> [Deepseek's dspark accelerates deep learning generation - Facebook](https://www.facebook.com/groups/DeepNetGroup/posts/2857302787995918/)
> [Enabling Early Exit Inference and Self-Speculative Decoding](https://www.researchgate.net/publication/384219438_LayerSkip_Enabling_Early_Exit_Inference_and_Self-Speculative_Decoding)
> [[Research] JetSpec: Speculative Decoding with Parallel Tree ...](https://www.reddit.com/r/ResearchML/comments/1ufnuyq/research_jetspec_speculative_decoding_with/)
> [AI-Powered Paper Summarization about the arXiv paper ...](https://summarizepaper.com/en/arxiv-id/2607.05147v1/)
> [LayerSkip: Enabling Early Exit Inference and Self-Speculative ...](https://www.youtube.com/watch?v=fda_wMpRP7U)
> [DeepSeek - AI Assistant - Apps on Google Play](https://play.google.com/store/apps/details?hl=en_US&id=com.deepseek.chat)
> [JetSpec: Breaking the Scaling Ceiling of Speculative Decoding with…](https://www.opentrain.ai/papers/jetspec-breaking-the-scaling-ceiling-of-speculative-decoding-with-parallel-tree--arxiv-2606.18394/)
> [DSpark: Speculative Decoding - Emergent Mind](https://www.emergentmind.com/topics/dspark)
> [SWIFT: On-the-Fly Self-Speculative Decoding for LLM ...](https://openreview.net/forum?id=EKJhH5D5wA&noteId=kn7YXzjX0u)
> [JETSPEC and Parallel Tree Speculative Decoding - Apple Podcasts](https://podcasts.apple.com/ru/podcast/jetspec-and-parallel-tree-speculative-decoding/id1835878324?i=1000774611359&l=uk)
> [[PDF] DSpark: Confidence-Scheduled Speculative Decoding with ...](https://www.semanticscholar.org/paper/42c6db4a9fde6cc229f70ecd6f704529ea8c1871)
> [M2R2: Mixture of Multi-Rate Residuals for Efficient ...](https://machinelearning.apple.com/research/multi-rate-residuals-transformers)
>
> **Searched 25 websites**
>
> 
>
> **Clarifying multi-layer integration**
>
> The user’s asking why speculative subsystems aren’t integrated into model layers. I’ll explain how multi-layer integration is possible and propose a speculative hierarchy, with each layer refining predictions.
>
> **Clarified multi-layer integration**
>
> 
>
> **Exploring multi-layer speculation**
>
> I’m exploring how to integrate speculation across layers without modifying the target model. This includes using a read-only multi-layer sidecar, leveraging various speculative methods like memory, correction, and tree heads.
>
> **Explored multi-layer speculation**
>
> 
>
> **Discussing multi-layer speculation**
>
> I’m explaining multi-layer speculation and verifying its viability. Multi-layer approaches can improve performance, but they need careful design to avoid redundant computations. I’ll suggest the most efficient methods for the user’s project.
>
> **Discussed multi-layer speculation**
>
> 
>
> **Discussing architecture options and verifying relevant papers**
>
> [EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty](https://arxiv.org/abs/2401.15077)
> [Computation and Language 2025](https://www.arxiv.org/list/cs.CL/2025?show=1000&skip=575)
>
> **Searched 2 websites**
>
> 
>
> Worked for 7m 57s

# Yes. Multi-layer is the stronger architecture.

My previous answer described the **lowest-risk retrofit**: freeze the target model and attach one cache-conditioned drafter. That is not the natural endpoint.

The better endpoint is a **speculation lattice** in which speculative state exists across:

1. **Model depth** - shallow, middle, and deep transformer layers.
2. **Token horizon** - $t+1,t+2,\ldots,t+K$.
3. **Candidate branches** - alternative tokens and verification outcomes.
4. **Decode rounds** - current verification and SSD-precomputed next-round continuations.
5. **Memory sources** - exact token cache, semantic user memory, hidden states, KV cache, tool/session traces.

The “speculator” then stops being a separate little model. It becomes an **auxiliary state plane integrated throughout the target architecture**.

JetSpec is already partially this: its Qwen3-8B implementation extracts hidden states from target layers $\{1,9,17,25,33\}$, fuses them, and feeds them into a five-layer causal-parallel draft head. EAGLE-3 likewise improved substantially by fusing low-, middle-, and high-level target features. LayerSkip and Kangaroo go further by using shallow parts of the target itself as the self-drafter. FastEagle assigns separate cascaded layers to different future-token positions. So the pieces of a multi-layer integrated design already exist, just not yet as one complete architecture. ([arXiv](https://arxiv.org/html/2606.18394v2))

---

## The methods operate on different axes

They should not be viewed as mutually exclusive alternatives:

| Method | What it actually solves | Integrated role |
|---|---|---|
| **Semantic/cache proposer** | Supplies prior continuation information | Memory-conditioned initialization |
| **JetSpec** | Efficient, causally consistent token-tree generation | Main parallel branch generator |
| **DSpark** | Repairs parallel-token inconsistency and schedules verification | Residual dependency head and confidence scheduler |
| **SSD/Saguaro** | Overlaps the next drafting round with current verification | Temporal pre-execution |
| **LayerSkip/Kangaroo** | Shares target layers with the drafter | Depth integration and early exits |
| **HSD** | Improves hierarchical verification while preserving the target distribution | Final lossless correction/resampling |
| **PipeSpec-like hierarchy** | Runs multiple prediction/verification levels asynchronously | Hardware and stage pipeline |

SSD explicitly says it can be combined with EAGLE-style hidden-state drafters and token-tree methods: rather than pre-speculating one chain for each probable verification outcome, the integrated version pre-speculates an entire token tree for each outcome. ([arXiv](https://arxiv.org/html/2603.03251v3))

The only important overlap is **JetSpec versus DSpark’s sequential correction**:

- JetSpec already conditions every branch node on its concrete ancestors through tree-causal attention.
- DSpark’s Markov/sequential head exists mainly because an otherwise parallel block predicts mutually inconsistent token marginals.

Therefore, the clean combination is initially:

```text
JetSpec causal tree generator
          +
DSpark confidence head and hardware-aware scheduler
          +
optional tiny DSpark residual transition head
```

Do not blindly stack the full DSpark sequential module after JetSpec without an ablation. It may duplicate dependency modeling rather than improve it. DSpark’s scheduler, however, remains directly useful because it decides which portion of the JetSpec forest is worth sending through the expensive target layers. ([arXiv](https://arxiv.org/html/2606.18394v2))

---

# The architecture I would use

Illustrative target with $L$ transformer layers:

```text
                         TOKEN HORIZON →
                  t+1          t+2          t+3 ... t+K
                ┌─────────────────────────────────────────┐
External cache  │ exact edges · semantic episodes · KV   │
and user memory │ latent traces · accepted/rejected paths│
                └───────────────────┬─────────────────────┘
                                    │
Target layers 1-8                   ▼
┌────────────────────┐   wide cache-conditioned candidate forest
│ shallow semantics  │───────────────► 64 cheap branches
└──────────┬─────────┘
           ▼
Target layers 9-17
┌────────────────────┐   JetSpec causal-parallel refinement
│ syntax / structure │───────────────► 24 coherent branches
└──────────┬─────────┘
           ▼
Target layers 18-25
┌────────────────────┐   latent correction + outcome prediction
│ task / reasoning   │───────────────► 8 likely branches
└──────────┬─────────┘
           ▼
Target layers 26-33
┌────────────────────┐   confidence / survival / proxy verification
│ final semantics    │───────────────► 2-4 surviving branches
└──────────┬─────────┘
           ▼
Target layers 34-L
┌────────────────────┐
│ authoritative pass │───────────────► exact verification and correction
└────────────────────┘

Meanwhile:
deep verification of round r
        ║
        ╚══ shallow/mid speculation for probable outcomes of round r+1
```

The branch counts are examples, not fixed recommendations. The important property is:

> **The speculative forest becomes narrower as it becomes deeper and more expensive.**

A single-head design drafts a tree and then sends substantially the whole tree through the target. A multi-layer design can eliminate weak branches **before they consume the deepest transformer layers**.

Let the stage depths be:

$$
d_1 < d_2 < \cdots < d_m=L
$$

and let $\mathcal B_j$ be the surviving speculative branches at stage $j$. Approximate branch-processing cost becomes:

$$
\mathbb E[C]
=
C_{d_1}\lvert\mathcal B_1\rvert
+
\sum_{j=1}^{m-1}
\left(C_{d_{j+1}}-C_{d_j}\right)
\mathbb E[\lvert\mathcal B_{j+1}\rvert]
$$

Instead of:

$$
C_L\lvert\mathcal B_1\rvert
$$

for sending every original candidate through full depth.

The scheduler should promote branch $b$ only when:

$$
P_{\text{survive}}(b)
\cdot
\Delta T_{\text{saved}}(b)
>
C_{\text{continue}}(b)
+
C_{\text{opportunity}}(b)
$$

That is DSpark’s load-aware scheduling idea generalized from **token-prefix length** to **layer depth × token horizon × branch width**.

---

# The stronger idea: layer-wavefront SSD

Ordinary SSD works at round granularity:

```text
verify round r
      ║
      ╚══ predict outcomes and draft round r+1
```

Your multi-layer version can work at **sub-round depth granularity**:

```text
Target reaches layer 8  → expose shallow states
                       → begin wide next-round speculation

Target reaches layer 17 → replace predicted mid-level states
                       → refine next-round branches

Target reaches layer 25 → update outcome probabilities
                       → prune speculative work

Final layer resolves    → select the already-prepared branch
                       → immediately begin verification
```

This is a diagonal wavefront across transformer depth and future-token time:

```text
                  future token / round
depth        r,t       r,t+1       r,t+2       r+1,t
  8          ● ───────── ○ ───────── ○ ───────── ○
              ╲           ╲           ╲
 17            ● ───────── ● ───────── ○ ───────── ○
                ╲           ╲
 25              ● ───────── ● ───────── ○
                  ╲
  L                ● verified
```

- `●` = progressively grounded by actual target computation.
- `○` = still predicted/speculative.

This would let the speculator continuously **rebase predicted hidden states onto increasingly authoritative target states**, rather than waiting for the entire target pass to finish.

That matters because SSD combined with hidden-state drafting has a known problem: next-round drafting begins before the current round’s target activations exist, forcing the drafter to self-condition on predicted activations for a longer interval. The SSD paper notes that an SSD-EAGLE-3 combination can require up to $2K$ self-generated positions and therefore suffer reduced acceptance. Separate 2026 work also finds that hidden-state drafters exhibit persistent long-range decay because recursively generated states drift and because a single hidden state compresses away context that later speculative positions may need. ([arXiv](https://arxiv.org/html/2603.03251v3))

A multi-layer wavefront does not eliminate that problem, but it gives us a correction mechanism:

$$
\tilde h_{j,b}
=
g_{j,b}\,h^{\text{actual}}_{j,b}
+
(1-g_{j,b})\,h^{\text{predicted}}_{j,b}
$$

As actual stage-$j$ states arrive, the corresponding speculative branches are updated or discarded.

---

# Where the semantic cache enters

The cache should not merely return token strings. At each selected target depth $d_j$, it provides a depth-specific memory representation:

$$
m_j
=
\operatorname{CrossAttention}
\left(
W_j^q h_{d_j},
K_j(M),
V_j(M)
\right)
$$

Then:

$$
z_j
=
h_{d_j}
+
g_j\odot W_j^m m_j
$$

and the speculative branch distribution is:

$$
q_j
=
D_j
\left(
z_j,\,
q_{j-1},\,
\mathcal B_{j-1}
\right)
$$

Different depths should use the cache differently:

| Depth | Cache use |
|---|---|
| Shallow | Broad semantic retrieval, user style, likely task and response class |
| Middle | Repository/schema/tool structure, recurring reasoning patterns |
| Deep | Exact continuation edges, target-logit sketches, accepted hidden/KV traces |
| Final | No unverified cache authority; target model remains authoritative |

This is exactly your intended concept:

> Cached sequences and states reduce uncertainty over new, previously uncached continuation edges.

The cache is not the response. It becomes **evidence injected into a multi-stage future-state predictor**.

---

# Architecturally integrated does not mean serially colocated

There are two separate questions:

### 1. Is the speculator part of the model?

Yes. Its heads, memory adapters, confidence predictors, and future-state lanes can be trained and saved with the target checkpoint.

### 2. Must it execute serially on the same GPU?

No-and for SSD, usually it should not.

If every speculative module runs serially after the target layers, the architecture is integrated but the temporal overlap disappears. SSD’s benefit specifically comes from performing pre-speculation while verification is still in progress. Saguaro therefore uses separate hardware for the speculator and verifier. PipeSpec similarly demonstrates hierarchical asynchronous model stages rather than a strictly alternating draft-then-verify schedule. ([arXiv](https://arxiv.org/html/2603.03251v3))

For your local system, the likely split is:

```text
RTX 3090 Ti:
  target trunk
  multi-layer feature taps
  JetSpec head
  final verification kernels

GTX 1080 Ti or CPU:
  semantic-cache retrieval
  SSD verification-outcome branches
  cheap token/latent continuation expansion
  low-rank confidence estimation

Communication:
  branch IDs
  token IDs
  compressed feature projections
  acceptance/outcome messages
```

Full hidden tensors should not repeatedly cross the device boundary. Project each selected target state to a compact speculative interface-perhaps tens or hundreds of dimensions-then quantize it. The richer JetSpec head should generally remain beside the target; the other device handles the outer SSD forest.

---

# Native training objective

For a genuinely integrated model, train the final language model and all speculative stages jointly:

$$
\mathcal L
=
\mathcal L_{\mathrm{AR}}^{(L)}
+
\sum_j
\lambda_j
D_{\mathrm{KL}}
\left(
p_L\;\|\;q_j
\right)
+
\mu\mathcal L_{\mathrm{outcome}}
+
\nu\mathcal L_{\mathrm{survival}}
+
\rho\mathcal L_{\mathrm{latent}}
+
\xi\mathcal L_{\mathrm{retrieval}}
+
\omega\mathbb E[C]
$$

Where:

- $\mathcal L_{\mathrm{AR}}^{(L)}$: normal final-layer language modeling.
- $D_{\mathrm{KL}}(p_L\|q_j)$: intermediate draft heads imitate the final target distribution.
- $\mathcal L_{\mathrm{outcome}}$: predict SSD verification outcomes.
- $\mathcal L_{\mathrm{survival}}$: predict branch acceptance.
- $\mathcal L_{\mathrm{latent}}$: predict future target hidden/KV states.
- $\mathcal L_{\mathrm{retrieval}}$: select memories that improve accepted tokens, not merely semantic similarity.
- $\mathbb E[C]$: penalize unnecessary branch and layer computation.

For an existing checkpoint, initially stop gradients into the target trunk and train only the attached speculation plane. For a new Pheno-native model, jointly train the trunk so that intermediate representations are deliberately useful for future-token speculation.

---

# Exactness constraint

A multi-layer architecture remains lossless relative to the original target when:

1. Intermediate stages only **propose, score, or reject speculative work**.
2. Final accepted output still goes through the target’s exact verification/correction rule.
3. Any pruned probability mass is handled by a correct residual-resampling path.

HSD demonstrates that hierarchical verification can be constructed to preserve the complete target distribution and can integrate with EAGLE-3. ([arXiv](https://arxiv.org/html/2601.05724v2))

If intermediate layers directly commit tokens without final correction, or memory-conditioned states are written into the authoritative target trunk, then the system is no longer lossless relative to the original checkpoint. That is acceptable for a newly trained architecture, but it is a **new target model**, not merely an inference accelerator for the old one.

---

## Bottom line

The correct end-state is not:

```text
target model + external speculator
```

It is:

```text
target model
+ distributed speculative state across selected layers
+ cache-conditioned future-token lanes
+ causal token-tree construction
+ confidence-driven progressive pruning
+ next-round SSD pre-execution
+ hierarchical exact verification
```

Or more compactly:

> **A two-dimensional transformer over model depth and speculative future time, carrying a dynamically pruned forest of cache-conditioned future states.**

That is a more coherent architecture than treating SSD, JetSpec, DSpark, semantic caching, and self-speculative decoding as separate plugins. The main research contribution would be the **layer-wavefront schedule and progressively rebased speculative state**, not merely attaching several existing heads.

---

**Sources:**

- [JetSpec: Breaking the Scaling Ceiling of Speculative Decoding with Parallel Tree Drafting](https://arxiv.org/html/2606.18394v2)

## Prompt:
7/25/2026, 2:59:29 PM

It looks like my message was lost. Please, um, tell me otherwise. Create an ASCII diagram. Um, as necessary, you'll want to do other things too. This ASCII diagram will show us the current state of a average LLM request. The average LLM request for GLM 5.2 based on OpenCode Go, if I remember correctly, is anywhere from 50,000 to 100,000 tokens in, at a 50 to 95% cache rate, and anywhere from 500 to 2,000 tokens out. Um, I strongly recommend you research further, find other request combinations, um, not for them, but perhaps also session-long or other multi-requests, you know, cumulative counts, um, and other similar values, so you have something to work with. My goal here is that when we analyze our usage, and my RAMemorys will confirm this for you, is almost all of our usage sits in the input tokens, whether cached or uncached. Output is also an issue, but that is more of an issue in terms of speed than it really is cost, even though it is also a massive cost hole. Um, for all of these, cached or uncached, our goal is to either maximize the cache, and output cache does not exist. We need to create such a cache. Um, cached and prediction, of course. Along with this, we also need to expand this further to effectively for every form of token have a fast path of some sort to make it cheaper and cheaper and cheaper, with a verification system that models off speculative decoding or speculative encoding, if you want to call it that, um, and other forms such that we can effectively bring our token cost down as much as possible in terms of the per-token cost, and/or actual compression that lowers the amount of tokens on each end without these strong methods of, for example, retrieval engines, context engines, or a token compression that goes into the current known methods, for example, semantic pruning, caveman LLM lingua. These are all things that are known and things that can be easily added in, but they have many, many risks. We need other ways of smartly and properly lowering tokens and other methods.

## Response:
7/25/2026, 2:59:40 PM

I see the message. I’ll ground the diagram in your actual workload profile, verify GLM/OpenCode assumptions, then map every token class to a cheaper fast path and an exactness/verification gate.

The first correction is important: current OpenCode Go telemetry is even more input-dominated than your recalled envelope—GLM-5.2’s observed “typical request” is about **52,000 cached + 700 new input + 150 output**, while the average completed session is **4.9 million tokens** with an **83% input-cache ratio**.

> **Personalizing**
>
>
> **Personalized and clarified LLM usage and token concerns**
>
> 
>
> **Evaluating costs**
>
> I’m calculating request costs based on token types and cache percentages for GLM-5.2, factoring in both inputs and outputs. I’ll use a web calculator to confirm prices but may compute manually.
>
> **Evaluated costs**
>
> 
>
> **Planning response with diagram**
>
> I’m preparing an answer to include both explanations and an ASCII diagram. This will clearly define the design principles and architectural proposals, ensuring explanations are backed by citations when needed.
>
> **Planned response with diagram**
>
> 
>
> Worked for 2m 19s

## Prompt:
7/25/2026, 3:01:52 PM

Opencode go itself shows many different request profiles per model.

Other companies have the same now too along with iirc proper market research externally.

Would be highly useful to take a look at. Ur diagram. Should just be 1 part of your report or a supporting visual

## Response:
7/25/2026, 3:02:32 PM

You’re right: OpenCode’s per-model profiles are the useful baseline, not one GLM profile. The model spread is already large—roughly **52k–86k cached input and 125–305 output tokens per call** among the listed mainstream models, before long-tail sessions and 200k-class agent calls.

# Universal Token Fast-Path Report

Your correction is right: **GLM-5.2 is one workload profile, not the workload profile**. OpenCode Go now publishes substantially different per-request shapes by model, while OpenRouter, Requesty, Vercel, and recent coding-agent traces provide broader market and session-level evidence.

The central finding survives the broader research:

> Coding-agent inference is overwhelmingly a problem of repeatedly moving, reading, and reprocessing input state-not merely generating output.

But “reduce tokens” conflates several different problems. We need a fast path for each token class, with explicit guarantees about whether it reduces:

1. Billed logical tokens.
2. Model computation.
3. KV/state movement.
4. Wall-clock latency.
5. None of the above, despite appearing efficient.

---

## 1. Observed request profiles

### Workload ladder

| Workload level | Representative shape |
|---|---|
| General LLM traffic | More than **6,000 input / 400 output** tokens per call on average. Programming prompts routinely exceed 20,000 tokens. |
| OpenCode Go ongoing call | Across its listed models: **300-1,100 fresh input**, **52,000-86,000 cached input**, and **125-305 output** tokens. |
| Real coding-agent step | Median: **119,000 cached-prefix**, **875 appended**, and **214 output** tokens. |
| Real coding-agent user request | Average **8.8 LLM calls and 10.8 tool invocations** per request. |
| OpenCode model session | Sampled model averages range from **3.1M to 8.0M total tokens per completed session**, with **83-97% input cache ratios**. |
| Long-tail agent task | Token use can vary by as much as **30× for the same task**, and spending more tokens does not reliably improve success. |

OpenRouter’s 100-trillion-token study found average prompts had grown from roughly 1,500 to more than 6,000 tokens, while average completions grew from about 150 to 400; programming was the main driver of the input growth. ([OpenRouter](https://openrouter.ai/state-of-ai))

OpenCode Go’s official profiles currently span:

| Model | Fresh input | Cached input | Output |
|---|---:|---:|---:|
| Grok 4.5 | 1,100 | 71,500 | 220 |
| GLM-5.2 / 5.1 | 700 | 52,000 | 150 |
| Kimi K3 | 1,050 | 76,500 | 300 |
| Kimi K2.7 / K2.6 | 870 | 55,000 | 200 |
| DeepSeek V4 Pro | 750 | 82,000 | 290 |
| DeepSeek V4 Flash | 790 | 68,000 | 280 |
| MiniMax M3 | 510 | 56,000 | 190 |
| MiniMax M2.7 | 300 | 55,000 | 125 |
| MiMo V2.5 | 830 | 71,500 | 295 |
| MiMo V2.5 Pro | 790 | 86,000 | 305 |
| Qwen3.7 Max | 420 | 66,000 | 200 |
| Qwen3.7 Plus | 500 | 57,000 | 190 |
| Qwen3.6 Plus | 500 | 57,000 | 190 |
| Hy3 | 830 | 71,500 | 295 |

The median of these profiles is approximately:

```text
67,000 cached input
   770 fresh input
   210 output
```

That means about **99% of input tokens in a typical ongoing Go call are cached**. However, this is not the same as the session-wide cache ratio: session starts, eviction, compaction, model changes, and idle periods pull the aggregate down. ([opencode.ai](https://opencode.ai/docs/go/))

OpenCode’s session telemetry shows this variation clearly:

```text
Kimi K3:           3.1M tokens/session, 93% cache
GLM-5.2:           4.9M tokens/session, 83% cache
MiMo V2.5:         5.2M tokens/session, 95% cache
DeepSeek V4 Pro:   6.9M tokens/session, 97% cache
MiniMax M3:        7.5M tokens/session, 94% cache
DeepSeek V4 Flash: 8.0M tokens/session, 96% cache
```

([OpenCode](https://opencode.ai/data/zhipuai/glm-5.2))

A separate twelve-month gateway study covering nine coding agents reports average input sizes ranging from 16,000 for Aider to 95,000 for OpenCode, with cache-hit rates ranging from 46% for Kilo Code to 92% for Claude Code. It also reports a sharp increase in average context size over the year. This is vendor telemetry rather than a controlled academic sample, but it supports the same broad pattern. ([Requesty](https://www.requesty.ai/coding-agent-economy))

---

## 2. What actually dominates cost

Using OpenCode Go’s published request shapes and listed prices, I calculate that **all input-cached plus fresh-accounts for approximately 71-96% of per-call list-price cost across the listed profiles**, with a median near **91%**. ([opencode.ai](https://opencode.ai/docs/go/))

For GLM-5.2 specifically:

```text
700 fresh input  × $1.40/M = $0.00098
52k cached input × $0.26/M = $0.01352
150 output       × $4.40/M = $0.00066
                                  --------
Total                             $0.01516
```

Approximate shares:

```text
Cached input:  89.2%
Fresh input:    6.5%
Output:         4.4%
```

So, for this profile, **output is not currently the massive dollar hole**. It is primarily the latency and serial-execution hole.

For DeepSeek V4 Pro, MiMo V2.5 Pro, and similarly extreme cheap-cache models, output rises toward 20-29% of request cost because cached reads are almost free. Output optimization therefore matters differently by model.

Recent real-world trace analysis reinforces the input result: the median coding-agent invocation contained roughly **119K prefix tokens, 875 appended tokens, and only 214 output tokens**. The researchers also found cached-prefix reads could dominate API cost despite their discounted rate because the entire accumulated context is reread at every step. ([arXiv](https://arxiv.org/html/2606.30560v1))

---

# 3. Current average coding-agent request

This uses the TraceLab median step and average user-request loop, with the OpenCode range shown as a secondary envelope.

```text
 USER REQUEST
 "Implement / debug / inspect / continue this task"
        |
        v
+-----------------------------------------------------------------------+
| AGENT REQUEST LOOP                                                    |
|                                                                       |
|  Average: 8.8 LLM invocations + 10.8 tool calls per user request      |
|                                                                       |
|  +----------------------- LLM STEP -------------------------------+    |
|  |                                                               |    |
|  |  EXISTING SESSION PREFIX                                      |    |
|  |  ~119,000 tokens median                                       |    |
|  |                                                               |    |
|  |  system prompt                                                |    |
|  |  tool definitions                                             |    |
|  |  repository instructions                                      |    |
|  |  previous user messages                                       |    |
|  |  previous model outputs                                       |    |
|  |  prior tool results                                           |    |
|  |                                                               |    |
|  |        prefix-cache lookup                                    |    |
|  |           /         \                                         |    |
|  |       CACHE HIT      CACHE MISS                               |    |
|  |       read KV        recompute some/all 119K tokens            |    |
|  |           \         /                                         |    |
|  |            v       v                                          |    |
|  |  FRESH APPEND: ~875 tokens                                    |    |
|  |  user delta, tool result, file contents, command output        |    |
|  |                 |                                             |    |
|  |                 v                                             |    |
|  |       FULL-LAYER PREFILL OF FRESH TOKENS                       |    |
|  |                 |                                             |    |
|  |                 v                                             |    |
|  |       AUTOREGRESSIVE OUTPUT: ~214 tokens                       |    |
|  |       one token / target decode iteration                      |    |
|  |                 |                                             |    |
|  |                 v                                             |    |
|  |       tool call or final answer                               |    |
|  +-----------------+---------------------------------------------+    |
|                    |                                                  |
|                    v                                                  |
|             TOOL EXECUTION                                            |
|             Bash / Read / Edit / tests / search                       |
|                    |                                                  |
|                    v                                                  |
|             append result and repeat                                  |
+-----------------------------------------------------------------------+

 Approximate median-shaped user request-not a measured aggregate median:

   cached-prefix traffic: 119K × 8.8 ≈ 1.05M token-reads
   fresh append traffic:     875 × 8.8 ≈ 7.7K tokens
   generated output:         214 × 8.8 ≈ 1.9K tokens

 OpenCode Go ongoing-call envelope:

   52K-86K cached + 300-1,100 fresh → 125-305 output
```

The multiplication is only a shape estimate: medians cannot be combined into a statistically valid median request. It nevertheless illustrates the scale mismatch.

TraceLab’s prefix hit rate was 95.7%, but only 19% of appended tokens were actually fresh. The rest were largely re-prefilled state caused by eviction or accounting behavior. Overall, the serving systems performed **5.3× as much append prefill as an ideal persistent cache would require**. ([arXiv](https://arxiv.org/html/2606.30560v1))

---

# 4. “Output cache does not exist” needs qualification

There are four different meanings of output cache.

## A. Exact response cache

```text
same complete request state → return same stored answer
```

This already exists in generic exact and semantic caching systems. It is safe only for completely identical deterministic state or workloads where stale answers are acceptable.

## B. Output KV promotion

During generation, the model creates K/V states for every output token. Those states can be retained and used as part of the next request’s prefix.

This **does exist**, but is not consistently implemented. TraceLab observed both:

```text
OUTPUT-CACHED
previous output KV → directly becomes next-step prefix KV

OUTPUT-RESENT
previous output text → resent and re-prefilled as fresh append
```

Some disaggregated systems discard decode-generated KV because moving it back into shared storage complicates the architecture. ([arXiv](https://arxiv.org/html/2606.30560v1))

Output-to-prefix KV promotion should therefore be one of our first changes.

## C. Continuation cache

```text
cached output patterns
        ↓
propose likely future output tokens
        ↓
target verifies candidates
```

REST, Prompt Lookup Decoding, Cacheback, and RACER are early forms of this. REST retrieves draft continuations from a datastore, while Cacheback uses cached n-grams rather than a neural draft model. ([arXiv](https://arxiv.org/abs/2311.08252))

## D. Latent trajectory cache

This is the stronger version we have been discussing:

```text
cached output tokens
+ target logits
+ hidden states
+ layerwise KV
+ tool trajectories
+ user/repository/task state
        ↓
synthesize previously unseen continuation branches
        ↓
progressive target verification
```

That is not yet a standard serving primitive.

---

# 5. Four separate efficiency ledgers

A method can look excellent on one ledger while doing nothing on another.

| Ledger | Question |
|---|---|
| **Logical-token ledger** | How many tokens are billed or exposed to the model? |
| **Compute ledger** | How many target FLOPs and memory reads occur? |
| **State-movement ledger** | How much KV, hidden state, and text crosses HBM, RAM, NVMe, or network? |
| **Critical-path ledger** | How long until first token, final answer, or successful task completion? |

Examples:

- Prompt caching reduces compute price and often TTFT, but not the logical token count.
- KV quantization reduces memory and transfer cost, but not token count.
- Speculative decoding reduces target decode iterations, but not accepted output tokens.
- Predicting the next request during idle time may reduce latency without reducing total computation.
- Semantic compression reduces logical tokens but can silently destroy necessary information.
- A provider may still bill every token even when your client-side system performs clever speculation.

That last point matters: **the complete fabric only produces physical-cost savings when we control the inference engine**. Against a third-party API, we only reduce the bill when we send fewer billed tokens, make fewer calls, receive fewer outputs, or improve the provider’s own cache reuse.

---

# 6. Fast path for every token class

## Verification levels

```text
V0  Exact identity
    Same model, tokenizer, token IDs, position, and preceding state.

V1  Algebraically exact
    Computation is reorganized but produces the same attention result.

V2  Target-verified speculation
    Candidate may be wrong; target verification preserves the target distribution.

V3  Bounded approximation
    Quality is empirically gated but not mathematically identical.

V4  New trained architecture
    The model itself uses compressed or latent representations.
```

## Token-fate table

| Token/state class | Proposed fast path | Verification | Actual token reduction? |
|---|---|---:|---:|
| Stable system prompt | Persistent content-addressed KV plus radix prefix reuse | V0 | No |
| Shared tool definitions | Shared-prefix attention across requests | V1 | No |
| Repository instructions | Versioned model-specific KV artifact | V0 | No |
| Existing session history | Persistent GPU/RAM/NVMe KV hierarchy | V0 | No |
| Previous generated output | Promote decode KV into next-step prefix | V0 | No |
| Identical file/chunk | Token-block and KV-block reference | V0 where position/context match | Network only |
| Reused non-prefix chunk | Selective recomputation or architecture-aware chunk cache | V1-V3 | Usually no |
| User text delta | Exact edit/delta against canonical session state | V0 | Transport reduction |
| Tool output delta | Content-addressed artifact plus exact diff | V0 | Potentially |
| Predicted tool result | Precompute branches while tool runs; keep exact matching prefix | V0/V2 | No, but hides latency |
| Novel input tokens | Ordinary prefill, or approximate/retrained compression | V3/V4 | Possibly |
| Repeated output span | Prompt lookup, suffix cache, REST, Cacheback | V2 | No |
| Novel output span | JetSpec/DSpark/cache-conditioned drafter | V2 | No |
| Identical deterministic answer | Exact full-response cache | V0 | Yes |
| Reasoning trace | Cached reasoning DAG used as speculative draft | V2 | Compute only |
| Agent-to-agent state | Shared object graph and event references instead of prose | V4/interface change | Yes |
| Frequent reasoning scaffolds | Learned reversible supertokens/macros | V4 | Yes |
| Predicted next turn | SSD-style pre-arrival branch computation | V0/V2 | Usually no |

Hydragen demonstrates that shared-prefix attention can be reorganized exactly, while ChunkAttention uses prefix-aware KV sharing and specialized kernels. Stateful serving systems such as Pensieve retain conversational state across GPU and CPU tiers. ([arXiv](https://arxiv.org/abs/2402.05099))

---

# 7. Speculative encoding is not symmetric with speculative decoding

This is the hardest constraint.

For output decoding:

```text
drafter proposes tokens
target evaluates the whole proposed block in parallel
rejection/acceptance preserves the target distribution
```

The target would otherwise perform sequential decode passes, so parallel verification can save time.

For novel input prefill:

```text
actual input tokens are already known
target must construct the correct hidden/KV state for every layer
```

Suppose a cheap encoder predicts the target’s KV states. To **verify them exactly**, the target generally has to recompute those same states. At that point, the supposed saving disappears.

Therefore exact speculative encoding has only three credible forms:

### 1. Reuse

The token sequence and required state were computed previously.

```text
known input → provenance check → reuse exact state
```

### 2. Algebraic restructuring

Compute the same result more efficiently through shared prefixes, better kernels, block sharing, or factorized attention.

```text
same computation → better schedule
```

### 3. Pre-arrival execution

Predict future input and perform its computation during otherwise idle time.

```text
predicted tool/user branch → prefill early
actual branch arrives       → retain only matching prefix
```

This reduces critical-path latency and may use otherwise idle hardware, but does not necessarily reduce total FLOPs.

Anything that actually skips target computation for **genuinely novel input** is either:

- approximate;
- dependent on certified architectural bounds that current transformers do not generally offer; or
- a newly trained model architecture.

SpecPrefill, for example, uses a smaller model to select prompt tokens that the target processes. It can greatly improve TTFT, but it works by dropping tokens and is therefore an approximate context-compression lane, not the exact speculative-decoding analogue we want as the foundation. ([arXiv](https://arxiv.org/abs/2502.02789))

---

# 8. Proposed universal fast-path fabric

```text
                      CANONICAL AGENT STATE GRAPH
     +----------------------------------------------------------------+
     | system:v42 | tools:v19 | repo:a81f | files:{hashes}            |
     | session:S9 | prior-output:O72 | tool-state:T18 | delta:D73     |
     +------------------------------+---------------------------------+
                                    |
                                    v
                       CONTEXT / STATE COMPILER
     +----------------------------------------------------------------+
     | canonical ordering                                              |
     | tokenize once                                                   |
     | content-address every stable block                              |
     | produce model-specific token/KV/latent artifacts                |
     +------------------------------+---------------------------------+
                                    |
                                    v
                       TOKEN FAST-PATH ROUTER
     +----------------------------------------------------------------+
     |                                                                |
     |  exact prefix? --------> radix/persistent KV ----------------+  |
     |  prior output? --------> decode-KV promotion ---------------+  |
     |  exact block? ----------> content-addressed token/KV block --+  |
     |  non-prefix reuse? -----> selective recompute / chunk path --+  |
     |  predicted future? -----> speculative prefill branches ------+  |
     |  genuinely novel? ------> target prefill ---------------------+  |
     |                                                                |
     +--------------------------------+-------------------------------+
                                      |
                                      v
                 MULTI-LAYER SPECULATION AND VERIFICATION
     +----------------------------------------------------------------+
     |                                                                |
     | shallow layers: broad cached candidates                         |
     | middle layers: syntax/tool/repository refinement                |
     | deep layers: causal JetSpec tree + DSpark confidence            |
     | temporal plane: SSD next-round / next-tool speculation          |
     | final target: authoritative verification                        |
     |                                                                |
     +--------------------------------+-------------------------------+
                                      |
                         +------------+------------+
                         |                         |
                         v                         v
              VERIFIED OUTPUT STREAM       TOOL / STATE ACTION
                         |                         |
                         +------------+------------+
                                      |
                                      v
                        OUTPUT TRAJECTORY STORE
     +----------------------------------------------------------------+
     | text tokens | decode KV | hidden projections | target logits   |
     | accepted/rejected trees | tool traces | state transitions      |
     +----------------------------------------------------------------+
                                      |
                    feeds future input and output speculation
```

This creates a closed loop:

```text
cached input
    predicts new input state
        predicts output candidates
            verified output becomes cached input
                predicts the next request
```

---

# 9. Mechanisms beyond ordinary semantic pruning

## A. Context object protocol

Stop treating the complete prompt as the protocol.

Instead of:

```json
{
  "messages": ["119,000 tokens of prior state", "875 new tokens"]
}
```

use:

```text
model_state = S109
apply:
  append tool-result hash:abc
  patch file:def from version 18 to 19
  append user-message:ghi
```

The inference server reconstructs the exact token sequence and attaches the proper KV blocks.

This does not alter what the model sees. It changes how state is addressed and transported.

## B. Exact context deltas

Most coding-agent state changes are operations:

```text
file A changed lines 30-42
test B produced a new failure
command C appended 70 log lines
model generated 214 new tokens
```

Do not resend the unchanged object. Keep a canonical state and transmit the edit script.

This is analogous to a version-control object database rather than prompt compression.

## C. Decode-to-prefill continuity

Every generated token should be born with a persistent identity:

```text
token IDs
position
model/tokenizer/version
KV block location
hidden-state projection
provenance hash
```

The next invocation should extend this state directly. There should be no decode → text → retokenize → prefill round trip.

## D. Semantic retrieval only as a proposer

Semantic similarity must never itself authorize state reuse.

```text
semantic match
      ↓
find likely exact token/state candidates
      ↓
exact alignment or target verification
```

This avoids the main semantic-cache failure: returning a plausible but wrong old answer.

## E. Predictive tool-result prefill

Tool operations are unusually predictable:

```text
Read(path)        → likely file content
git diff          → deterministic output
test command      → output distribution based on prior failures
compiler          → structured diagnostic grammar
apply_patch       → predictable updated file state
```

While the tool executes, the speculator can prepare several likely result branches. When the actual bytes arrive, retain the longest exactly matching token prefix and discard the rest.

This exploits otherwise idle CPU, 1080 Ti, or secondary streams without risking model correctness.

## F. Output continuation trees

Store not just final outputs but continuation graphs:

```text
prefix → candidate token → subsequent candidates
                    ↘ target acceptance statistics
                    ↘ task/repository/user conditions
```

A semantic query identifies relevant trees; exact suffix alignment and the integrated drafter synthesize novel branches; target verification keeps the result lossless.

## G. Model-native reversible macros

Frequent structural sequences could become single learned tokens:

```text
<TOOL_CALL_OPEN>
<TEST_FAILURE_BLOCK>
<BEGIN_PATCH>
<VERIFY_ASSUMPTIONS>
```

Recent supertoken work shortened reasoning traces by about 8% without a statistically significant benchmark loss in its experiments. That is modest but confirms the general mechanism. It requires training or fine-tuning and is not equivalent to optimizing an unchanged checkpoint. ([arXiv](https://arxiv.org/abs/2604.26355))

The stronger version is a reversible hierarchical tokenizer:

```text
logical supertoken
    ↕
canonical ordinary-token expansion
```

The model reasons over the supertoken internally but can expand it when full text is required.

---

# 10. Highest-ROI build order

## Phase 0 - Instrument token fate

Record for every block:

```text
origin
model/tokenizer/version
first computation
subsequent reads
cache tier
eviction reason
prefill cost
decode cost
whether it was already available elsewhere
```

A plain provider token count is insufficient.

## Phase 1 - Exact state continuity

Build first:

1. Persistent session KV.
2. Output-KV promotion.
3. Content-addressed token/KV blocks.
4. Canonical prompt ordering.
5. Model/version-aware cache invalidation.
6. RAM/NVMe tiering and predictive prefetch.

This is the lowest-risk and probably highest immediate return.

TraceLab estimated that eliminating user-thinking-induced cache misses could reduce observed append prefill by 45.9% and total priced cost by 12.8% in its trace. ([arXiv](https://arxiv.org/html/2606.30560v1))

## Phase 2 - Output continuation cache

Add:

```text
prompt lookup
suffix decoding
REST/Cacheback-style retrieval
target-logit bridges
tree verification
```

Then measure acceptance on your actual code-edit, tool-use, and harness workloads.

## Phase 3 - Predictive branch prefill

Use the RLVR-AF session-path predictor to speculate:

```text
next tool
next tool result
next user correction
next work package
next model response
```

Compute during human/tool idle gaps.

## Phase 4 - Integrated multi-layer speculator

Combine:

```text
cache-conditioned memory
+ JetSpec causal tree
+ DSpark confidence/scheduling
+ SSD temporal overlap
+ layer-wavefront rebasing
```

This is where the prior multi-layer architecture belongs.

## Phase 5 - New model architecture

Only after the exact fabric is measured:

```text
reversible supertokens
latent memory blocks
hierarchical input units
agent-state object attention
shared reasoning DAGs
```

This is higher upside, but it stops being an inference-only optimization.

---

# 11. Metrics that matter

Cache rate alone is misleading. A 99% hit rate can still be expensive if the same 100K-token prefix is read thousands of times.

Track:

$$
\text{Freshness Ratio}
=
\frac{\text{truly new context tokens}}
{\text{all logical input tokens}}
$$

$$
\text{Prefill Amplification}
=
\frac{\text{tokens actually prefilled}}
{\text{irreducibly fresh tokens}}
$$

$$
\text{Cache Read Amplification}
=
\frac{\text{cached tokens repeatedly read}}
{\text{fresh tokens}}
$$

$$
\text{Output Promotion Rate}
=
\frac{\text{previous output tokens reused as KV}}
{\text{previous output tokens needed next turn}}
$$

$$
\text{Speculative Goodput}
=
\frac{\text{accepted target tokens}}
{\text{draft compute + verification compute}}
$$

$$
\text{State-Transition Efficiency}
=
\frac{\text{successful useful state changes}}
{\text{total token-equivalent cost}}
$$

The final metric should be task-grounded:

```text
cost / accepted patch
cost / passing test
cost / resolved issue
cost / validated work package
```

not merely tokens per session.

---

# Bottom line

Your broader premise is correct, but the architecture needs one hard division:

```text
EXACT FAST PATHS
  reuse state
  preserve output KV
  share prefixes
  transmit deltas
  algebraically reorganize attention
  target-verify output speculation

SPECULATIVE CRITICAL-PATH PATHS
  predict next tool result
  predict next request
  prefill branches during idle time
  progressively rebase layer states

APPROXIMATE / NEW-MODEL PATHS
  token dropping
  semantic compression
  latent summaries
  supertokens
  memory-token architectures
```

The biggest near-term opportunity is not better LLMLingua-style compression. It is eliminating the absurdity that a session with only hundreds of truly new tokens repeatedly reads or prefills tens or hundreds of thousands of old tokens.

The target architecture is therefore:

> **A stateful, content-addressed LLM runtime where every token or latent block has provenance, reuse eligibility, a specialized fast path, and an exact or explicitly bounded verification policy.**

That runtime then becomes the substrate under the integrated SSD-JetSpec-DSpark multi-layer speculator, rather than treating speculation as an output-only bolt-on.

I can monitor new prompt-cache, speculative-prefill, stateful-serving, and decoding research and deliver a monthly architecture delta.

---

**Sources:**

- [https://openrouter.ai/state-of-ai](https://openrouter.ai/state-of-ai)
- [https://opencode.ai/data/zhipuai/glm-5.2](https://opencode.ai/data/zhipuai/glm-5.2)
- [https://www.requesty.ai/coding-agent-economy](https://www.requesty.ai/coding-agent-economy)
- [https://arxiv.org/html/2606.30560v1](https://arxiv.org/html/2606.30560v1)

## Prompt:
7/25/2026, 3:11:22 PM

Find such then Give me a pdf report plz strong and with many supporting viz and or gfx. Build in html and or docx and or latex whatever allows for most richness and precompile as pdf b4 handing to me

## Response:
7/25/2026, 3:11:44 PM

I’ll build a research-backed systems report covering workload evidence, fast paths, integrated speculation, falsification tests, and quantitative visuals.

## Prompt:
7/25/2026, 3:15:42 PM

Resume

## Response:
7/25/2026, 3:15:44 PM

I’m resuming this as a research-backed systems report, verifying workload evidence and related systems before compiling, preflighting, and visually inspecting the finished PDF.

## Prompt:
7/25/2026, 3:23:39 PM

Resume

## Response:
7/25/2026, 3:23:43 PM

I’m resuming this as a full research artifact: verifying workload evidence, building the taxonomy and architecture, then compiling and inspecting a visually rich PDF before delivery.

The evidence reveals two bottlenecks: cached input dominates volume, state traffic, and often price, while effective KV reuse can leave serial decoding dominating GPU time.

Evidence now spans API, agent-step, and session scales: GLM-5.2 averages 52K cached, 700 fresh, 150 output per call; only 19% of observed append tokens were truly fresh.

The 37-page report includes 20 original visuals and clearly labels evidence versus proposals. Preflight found two clipped captions; I’m fixing them and rerendering the PDF.

The quantitative core now shows 67K cached, 770 fresh, and 210 output tokens, with input driving median 91% of cost. Separate ledgers track billing, compute, movement, and latency.

> **Inspecting PDF skill and files**
>
>
> **Inspected PDF skills and read create/convert tasks**
>
> 
>
> **Looking up sources**
>
> I’m gathering primary sources for July 2026 research, focusing on technical details from Open Code, AI models, and GitHub. I'll ensure to include URLs and citations in the final report as needed.
>
> **Looked up sources**
>
> 
>
> **Searching for OpenCode Go model data and stats**
>
> [AI Model Usage Rankings | OpenCode Data](https://opencode.ai/data/)
> [Opencode tokens per request : r/opencodeCLI](https://www.reddit.com/r/opencodeCLI/comments/1sz4j80/opencode_tokens_per_request/)
> [OpenCode Token Usage: How It Works and How to ...](https://www.truefoundry.com/blog/opencode-token-usage-how-it-works-and-how-to-optimize-it)
> [Ridiculously big usage of input tokens for simple tasks #254](https://github.com/anomalyco/opencode/issues/254)
> [pi-opencode-go-cache · Packages](https://pi.dev/packages/pi-opencode-go-cache)
>
> **Searched 5 websites**
>
> 
>
> **Searching for API pricing and AI telemetry data**
>
> [More than 1 million children lost access to food benefits after Trump bill passed](https://www.theguardian.com/us-news/2026/jul/25/food-stamps-children-trump)
> [2026](https://en.wikipedia.org/wiki/2026)
> [State of AI Engineering](https://www.datadoghq.com/state-of-ai-engineering/)
> [How to track LLM token usage (2026): Prompt, completion ...](https://www.braintrust.dev/articles/how-to-track-llm-token-usage-2026)
> [Custom Reporting](https://vercel.com/docs/ai-gateway/observability-and-spend/custom-reporting)
> [Cost](https://docs.datadoghq.com/llm_observability/monitoring/cost/)
> [Minimizing token usage and caching tool schemas with ...](https://community.vercel.com/t/minimizing-token-usage-and-caching-tool-schemas-with-vercel-ai/27518)
> [The 2026 CrossFit Games: Day 3](https://www.youtube.com/watch?v=HeyM_2fyD04)
> [Year 2026 Calendar – United States](https://www.timeanddate.com/calendar/?country=1)
> [President Trump Delivers Remarks, Jul. 24, 2026 – The White ...](https://www.whitehouse.gov/videos/president-trump-delivers-remarks-jul-24-2026/)
> [US Federal Holidays 2026 | Complete Holiday Calendar](https://www.bluesunhotels.com/en/content/usa-federal-holidays-2026)
> [Week numbers for 2026](https://www.epochconverter.com/weeks/2026)
>
> **Searched 12 websites**
>
> 
>
> **Preparing the report**
>
> I’m structuring a PDF report with visuals, covering areas like workload analysis, caching, techniques mapping, and proposed architecture. I’ll include charts and diagrams (SVG/Python) and necessary citations.
>
> **Prepared the report**
>
> 
>
> **Searching the web**
>
> [TraceLab: Characterizing Coding Agent Workloads for LLM Serving](https://arxiv.org/html/2606.30560v1)
> [The Coding Agent Economy | Requesty](https://www.requesty.ai/coding-agent-economy)
> [State of AI 2025: 100T Token LLM Usage Study | OpenRouter](https://openrouter.ai/state-of-ai)
> [www.datadoghq.com](https://www.datadoghq.com/state-of-ai-engineering/)
>
> **Searched 4 websites**
>
> 
>
> **Fetching OpenCode model session data**
>
>
> **Fetched OpenCode model session data**
>
> 
>
> **Searching for session cache ratio across models**
>
> [DeepSeek V4 Flash Usage, Cost & Rank](https://opencode.ai/data/deepseek/deepseek-v4-flash)
> [DeepSeek V4 Pro Usage, Cost & Rank | OpenCode Data](https://stats.opencode.ai/data/deepseek/deepseek-v4-pro)
>
> **Searched 2 websites**
>
> 
>
> **Searching for research on input caching and stateful serving**
>
>
> **Searched 20 websites**
>
> 
>
> **Researching compression techniques**
>
> I’m gathering info on new compression methods like dynamic pruning and cache economics, and proposing new approaches. The report needs profiling across various models and cost analysis for each.
>
> **Researched compression techniques**
>
> 
>
> **Searching the web**
>
> [Go | OpenCode](https://opencode.ai/docs/go/)
>
> **Searched 1 website**
>
> 
>
> **Resuming report progress**
>
> I’m continuing to build the PDF with a focus on LLM/token profiles, output caching, and speculative decoding. I’ll integrate visuals, including an ASCII diagram, and keep the user updated.
>
> **Resumed report progress**
>
> 
>
> **Reading PDF skill**
>
>
> **Read PDF skill and create/convert tasks**
>
> 
>
> **Searching for primary research sources and papers**
>
>
> **Searched 16 websites**
>
> 
>
> **Proceeding with report development**
>
> I’m continuing to build the PDF report with visuals based on research and inputs. The focus is on LLM request profiles, cache efficiency, and speculative architecture, while inspecting the document for accuracy.
>
> **Reading PDF skill file**
>
>
> **Read PDF skill file and instructions**
>
> 
>
> **Searching technical papers and official documentation sources**
>
>
> **Finishing report visuals**
>
> I’m finalizing the PDF report by correcting SVG clipping issues on pages 16 and 21. Once that's complete, I’ll ensure the report is polished, including source HTML and CSVs for optional access.
>
> **Searched 21 websites**
>
> 
>
> **Downloading and converting PDF content**
>
>
> **Downloaded and converted PDF content to text**
>
> 
>
> **Searching for exact paper titles and sources**
>
> [Rest® | Best Cooling Bedding for Hot Sleepers](https://rest.com/)
> [Cacheback: Speculative Decoding With Nothing But Cache](https://arxiv.org/html/2511.21699v1)
> [SGLang is a high-performance serving framework for large ...](https://github.com/sgl-project/sglang)
> [RESTful](https://en.wikipedia.org/wiki/REST)
> [Welcome to SGLang - SGLang Documentation](https://docs.sglang.ai/)
> [REST Definition & Meaning](https://www.merriam-webster.com/dictionary/rest)
> [Cacheback: Speculative Decoding With Nothing But Cache](https://aclanthology.org/2025.emnlp-main.1581/)
> [Seven types of rest to help restore your body's energy](https://www.apa.org/topics/mental-health/seven-rest-types)
> [Cascade Speculative Drafting for up to 72 percent ...](https://www.reddit.com/r/LocalLLaMA/comments/18lwfdl/cascade_speculative_drafting_for_up_to_72_percent/)
> [RACER: Retrieval-Augmented Contextual Rapid ...](https://openreview.net/forum?id=i8SjqQQOVt)
> [ReST Smart Bed Technology- The World's First Smart Mattress](https://restperformance.com/)
> [Efficient Speculative Decoding for AI PCs via Hierarchical ...](https://dl.acm.org/doi/pdf/10.1145/3737902.3768352)
> [SGLang](https://www.linkedin.com/company/sgl-project)
> [Rest (@rest) • Instagram photos and videos](https://www.instagram.com/rest/)
> [SGLang: Fast Serving Framework for Large Language and ...](https://rocm.blogs.amd.com/artificial-intelligence/sglang/README.html)
> [Rest](https://open.spotify.com/artist/6lGbUVZzujCnRJWgPZkkxk)
> [SGLang](https://sky.cs.berkeley.edu/project/sglang/)
> [REST | definition in the Cambridge English Dictionary](https://dictionary.cambridge.org/us/dictionary/english/rest)
> [Retrieval-Augmented Contextual Rapid Speculative ...](https://www.themoonlight.io/en/review/racer-retrieval-augmented-contextual-rapid-speculative-decoding)
> [Accelerating LLM Inference with Speculative Decoding for ...](https://www.zenml.io/llmops-database/accelerating-llm-inference-with-speculative-decoding-for-ai-agent-applications)
> [RACER: Retrieval-Augmented Speculative Decoding](https://www.emergentmind.com/papers/2604.14885)
>
> **Searched 21 websites**
>
> 
>
> **Inspecting current files in directory**
>
>
> **Inspected current files in directory**
>
> 
>
> **Searching documentation for speculative decoding and related papers**
>
> [Speculative Decoding](https://docs.vllm.ai/en/latest/features/speculative_decoding/)
> [HiCache System Design and Optimization - SGLang](https://docs.sglang.ai/advanced_features/hicache_design.html)
> [LayerSkip: Enabling Early Exit Inference and Self-Speculative Decoding](https://arxiv.org/abs/2404.16710)
> [Eagle](https://en.wikipedia.org/wiki/Eagle)
> [Bald Eagle | Audubon Field Guide](https://www.audubon.org/field-guide/bird/bald-eagle)
> [LayerSkip: faster LLM Inference with Early Exit and Self ...](https://medium.com/%40techsachin/layerskip-faster-llm-inference-with-early-exit-and-self-speculative-decoding-3110cb93c94e)
> [CLaSp: In-Context Layer Skip for Self-Speculative Decoding](https://aclanthology.org/2025.acl-long.1525.pdf)
> [LayerSkip: Enabling Early Exit Inference and Self-Speculative ...](https://www.youtube.com/watch?v=fda_wMpRP7U)
> [Enabling Early Exit Inference and Self-Speculative Decoding](https://huggingface.co/papers/2404.16710)
> [Eagle Management | U.S. Fish & Wildlife Service](https://www.fws.gov/program/eagle-management)
> [Enabling Early Exit Inference and Self-Speculative Decoding](https://ai.meta.com/research/publications/layerskip-enabling-early-exit-inference-and-self-speculative-decoding/)
> [DEL: Context-Aware Dynamic Exit Layer for Efficient Self- ...](https://openreview.net/forum?id=cAFxSuXQvT)
> [Fascinating Eagle FAQ](https://www.nationaleaglecenter.org/learn/faq/)
> [American Eagle Foundation | Protecting and Caring for Bald ...](https://eagles.org/)
> [Bald Eagle](https://www.allaboutbirds.org/guide/Bald_Eagle/overview)
> [List of Eagle Species](https://www.birdlife.org/list-of-eagle-species/)
>
> **Searched 16 websites**
>
> 
>
> **Generating data and chart scripts**
>
>
> **Generated data and chart scripts**
>
> 
>
> **Creating report generation script**
>
>
> **Created report generation script and processed PDF with images**
>
> 
>
> Worked for 33m 17s

# Universal Token Fast Paths

Completed and precompiled as a **33-page PDF report**. It has been rendered page-by-page and checked for clipping, overflow, broken glyphs, malformed pages, and missing chart content.

The report includes:

- OpenCode Go request profiles across the currently listed models
- Session-level and multi-request coding-agent workload evidence
- Cost decomposition across cached input, fresh input, and output
- The requested ASCII diagram of the current coding-agent request loop
- Separate logical-token, compute, state-movement, and latency ledgers
- A fast-path taxonomy for every major token and state class
- Five distinct forms of output caching
- Analysis of why speculative encoding is not symmetrical with speculative decoding
- Existing cache, KV, agent-serving, and speculative-decoding systems
- The proposed **Universal Token Fast-Path Fabric**
- Integrated **JetSpec + DSpark + SSD** multi-layer speculation lattice
- A layer-wavefront architecture for continuously corrected speculation
- Cache-conditioned prediction of genuinely uncached continuation edges
- Mapping to the RTX 3090 Ti, GTX 1080 Ti, Ryzen 5800X, RAM, and NVMe
- Dynamic speculation policy for 1–512 concurrent requests
- Quantitative prefill-reduction scenarios
- API-provider economics versus self-hosted physical inference savings
- A phased implementation roadmap, ablation matrix, falsification criteria, and metrics
- 34 primary papers and official runtime/product references

## Deliverables

[Download the completed PDF report](sandbox:/mnt/data/Universal_Token_Fast_Paths_Report.pdf)

[Download the retained HTML, vector graphics, and calculated-data source bundle](sandbox:/mnt/data/Universal_Token_Fast_Paths_Source.zip)

## Response:
7/25/2026, 3:56:37 PM

# Report complete

I finished and precompiled the **46-page TokenFabric report**. The final PDF was rendered and inspected page by page for broken layouts, clipped diagrams, orphan pages, unreadable charts, and missing glyphs.

It includes:

- OpenCode Go’s per-model request profiles and session-level telemetry.
- Broader coding-agent and market workload evidence.
- Your own Claude Code and OmniRoute token telemetry.
- Per-request, per-turn, per-user-request, per-session, and long-horizon workload models.
- **13 quantitative charts**, multiple architecture graphics, and the requested ASCII request diagram.
- Separate accounting for logical tokens, model compute, KV/state movement, and critical-path latency.
- A four-part definition of “output caching.”
- Fast paths for cached input, uncached input, prior output, novel output, tool results, agent state, and predicted future turns.
- The exactness boundary for speculative encoding/prefill.
- The integrated **SSD + JetSpec + DSpark + cache-conditioned multi-layer speculator**.
- Layer-wavefront execution, heterogeneous hardware mapping, scheduling policy, API design, implementation order, risk register, and falsification benchmarks.
- 25 primary papers, vendor documents, and telemetry sources.

[Download the TokenFabric Universal Token Fast-Path Report](sandbox:/mnt/data/tokenfastpath_deliverable/TokenFabric_Universal_Token_Fast_Path_Report.pdf)

## Prompt:
7/25/2026, 4:30:53 PM

what is tracelab.

## Response:
7/25/2026, 4:30:56 PM

I’m verifying which specific paper or system “TraceLab” refers to, since several unrelated projects use that name.

> **Searching for TraceLab coding agents on arXiv**
>
>
> **Searched 9 websites**
>
> 
>
> Worked for 2m 7s

## TraceLab, in this report

**TraceLab is a University of Washington research project for measuring real coding-agent workloads from an LLM-serving perspective.** It is unrelated to your **Tracera**, `trace`, or AGSLAG work.

I should have defined it explicitly on first use rather than dropping the name into the report.

TraceLab refers to three connected things:

| Component | What it is |
|---|---|
| **Research paper** | *TraceLab: Characterizing Coding Agent Workloads for LLM Serving*, released in June 2026 |
| **Dataset** | Sanitized traces from day-to-day Claude Code and Codex usage |
| **Tooling** | Open-source collection, normalization, sanitization, analysis, visualization, and workload-replay pipeline |

It is **not primarily a coding-quality benchmark** like SWE-bench. It does not ask, “Did the agent solve the issue?” Its main question is:

> What does real coding-agent traffic look like to an inference server?

That includes context growth, repeated prefix reads, fresh appended tokens, generated output, tool calls, human pauses, KV-cache eviction, and request arrival patterns. ([SyFI Lab](https://syfi.cs.washington.edu/blog/2026-06-25-tracelab/))

## What its dataset contains

The current paper reports:

- **4,265 sessions**
- **357,161 LLM invocations**
- **432,510 tool calls**
- **43 developers**
- **23 model versions**
- Claude Code and Codex activity collected from roughly **September/October 2025 through June 2026**
- **54.90 billion input tokens**
- **186.9 million output tokens**, including reported reasoning tokens where available ([arXiv](https://arxiv.org/html/2606.30560v2))

That last pair is the source of the striking workload shape:

$$
\frac{54.90B\ input}{186.9M\ output}\approx294:1
$$

So across its trace, there were roughly **294 input tokens for every output token**. That does **not** mean each individual request has exactly that ratio; it is the aggregate across long, repeatedly replayed sessions.

## Why it mattered to our report

TraceLab offers unusually relevant evidence for your claim that coding-agent usage is dominated by repeatedly processed input state.

Its principal findings include:

- One user request triggers an average of **8.8 LLM calls** and **10.8 tool calls** before the agent returns control.
- **88% of LLM rounds** respond to tool results rather than directly to humans.
- Aggregate prefix-cache hit rate is **95.7%**, but user-triggered rounds perform worse because human pauses often outlive cache-retention windows.
- Of approximately **2.34 billion append tokens**, only **19% represented genuinely new context**. The remaining **81% represented repeated prefill work** caused by lost, shifted, or unavailable cached state.
- Their interpretation is that each genuinely new token was effectively prefilled around **five times on average**. ([SyFI Lab](https://syfi.cs.washington.edu/blog/2026-06-25-tracelab/))

That is why I used it to support this architecture argument:

```text
Logical session state
        |
        |  only a small delta is genuinely new
        v
+------------------------+
| Huge existing prefix   |----> ideally persistent KV reuse
+------------------------+
| Small appended delta   |----> actual required prefill
+------------------------+
| Short output           |----> decode / speculation problem
+------------------------+

Observed serving failure:

existing prefix or portions of it
        |
        +----> evicted / shifted / not promoted / not portable
        |
        v
re-prefill already-known state
```

In other words, a nominal “95.7% cache hit rate” can still conceal substantial waste. **Hit rate alone does not tell us how often the remaining miss causes tens or hundreds of thousands of old tokens to be recomputed.**

## Important limitation

TraceLab is strong systems evidence, but it is **not universal market telemetry**. Its traces came from 43 developers associated with research and systems-building workflows, using Claude Code and Codex. The authors explicitly acknowledge that their projects and habits may bias the distribution, which is why they released the collection pipeline and encouraged others to contribute traces. ([SyFI Lab](https://syfi.cs.washington.edu/blog/2026-06-25-tracelab/))

So the correct use in our report is:

> **A large, unusually detailed real-world coding-agent trace that provides one strong workload sample-not a definitive estimate of all OpenCode, Cursor, Factory, Claude Code, or global agent traffic.**

OpenCode Go’s provider telemetry, Requesty-style gateway observations, your own Claude/OmniRoute history, and other production traces should remain separate evidence layers rather than being blended into a fictional single “average request.”

---

**Sources:**

- [TraceLab: Characterizing Coding Agent Workloads for LLM Serving | SyFI Lab](https://syfi.cs.washington.edu/blog/2026-06-25-tracelab/)
- [TraceLab: Characterizing Coding Agent Workloads for LLM Serving](https://arxiv.org/html/2606.30560v2)



---
Powered by [ChatGPT Exporter](https://www.chatgptexporter.com)