# Networking, identity and routing evidence

## Four route classes — proposed policy

| Class | Intended consumer | Candidate path | Required authorization evidence |
|---|---|---|---|
| Private-tailnet | Operators and approved internal agents | Tailnet-private service path | Allowed node/user policy plus application role checks where needed |
| Authenticated-public-hostname | Users needing a custom public hostname but restricted access | Named tunnel plus separately configured Access/application policy | Visitor identity, audience/role behavior, denied identity and origin-bypass tests |
| Anonymous-public | Portfolio/demo content deliberately public | Qualified public HTTP path | Explicit public-data scope; no accidental admin or state endpoint exposure |
| Authenticated-machine | CI events, webhooks, service callers | Private route or authenticated public endpoint | Caller-supported service identity or validated webhook signature and replay handling |

The recovered user feedback names `*.pheno.studio`, `*.phenotype.space` and `projects.kooshapari.com`, and says private services should be inaccessible outside the tailnet. This is attributed intent in a compaction frame, not a verified DNS/zone inventory or authorization to change it. Private owned-domain names should use a qualified private DNS/TLS/origin path; custom spelling does not require public ingress. The authenticated-public-hostname row is an optional separately approved route class, not the default for this local stack. [E006; S032; S049]

Funnel reachability is public. Do not read a permission to create a Funnel as visitor authentication. The reviewed product restricts its names/ports and bandwidth configuration; that is a fit constraint, not a blanket claim that no production use is valid. Switching an existing private port to Funnel can change exposure. [S022]

A custom hostname with an Access policy can still be a private application in the ordinary sense of restricted users; “public hostname” describes reachability, not anonymous access. Conversely, deliberately anonymous pages should not inherit a browser-login requirement simply because private administration uses one. [S024; design distinction]

## Streaming path qualification

Quick Tunnel’s documented lack of SSE support is an explicit disqualifier when SSE is required. Its 200 in-flight request limit is also a limit, not a throughput benchmark. Do not carry these restrictions over indiscriminately to named tunnels. [S023]

For the selected path record every hop: client → local/network edge → tunnel/reverse proxy → application → upstream provider. Test event framing, immediate flushing, heartbeats, long gaps, first useful output, client disconnect, upstream cancellation and explicit failure termination at the **client**, not just at localhost. Specify buffering/timeouts, identity forwarding and maximum concurrent streams for the actual versions and plan. Leave unsupported settings as unknown rather than copying settings from a different proxy.

SSE bytes can include non-text events. A valid tool invocation, structured result or protocol-defined refusal must not be classified as an empty failure merely because text is absent. Define semantic completion per protocol and application. Conversely, an empty terminal marker or an upstream error hidden inside a successful HTTP envelope must not count as useful output.

## What the attached logs do and do not establish

The reproducible counts are in `evidence/log-metrics.json`; `tools/analyze_logs.py` regenerates them without repairing or replacing the original file. The input is a Markdown-escaped terminal excerpt, not a clean authoritative JSONL export. Pattern extraction is intentionally narrow and keeps original line references.

One explicit event reports success after **83,173 ms and 32 fallbacks** at original line 1777. It is a concrete reason to investigate latency and candidate traversal. It is not a measured user-end-to-end percentile. The repeated terminal `decisions` field requires a code definition; it could count policy events or traversal decisions rather than upstream calls. [S001:1777]

The file also shows warnings about empty completion and errors before useful content. It shows repeated zero-model sync reports despite explicit configured CPA routes. Zero discovered models need not mean no manually configured route exists. No complete correlation proves these observations share a cause. [S001:501,520,593,831,1053,1191,1764–1908]

**Do not calculate an error rate from six warning lines divided by the terminal-trace count.** The selected views lack a complete request denominator, request-start records and shared correlation on all warning messages. Do not infer that Cloudflare caused these loopback/provider-routing observations.

## Proposed observability contract

Per request: request ID, caller/tenant scope, requested protocol, resolved combo/policy generation, accepted context budget, deadline and semantic outcome. Per attempt: attempt ID, parent request, provider/model/config identity, start/end, transport status, error class, reason for selection/fallback, emitted event/byte/tool counts and cancellation status. Separate **queue time**, **upstream wait**, **first useful event**, **total attempt time** and **total request time**.

A decision event includes its type so the terminal summary can separately report `decisions_count`, `attempts_count` and `fallbacks_count`. A counter’s name is not its definition; link its source implementation and test. Keep payload bodies and prompts out of routine telemetry unless explicitly necessary and authorized.

## Bounded failover and replay safety

Define maximum attempts, total deadline, provider backoff/cooldown and terminal reason per workload. Respect quota/rate-limit signals rather than retrying every candidate until something happens. Missing quotas are unknown, not infinite capacity. These are control-plane design requirements, not a request to change provider accounts or subscription terms.

Failover before any irreversible effect can be permitted under policy, but it may still consume quota or incur cost. After content is emitted or a tool-side effect might have occurred, silent replay is unsafe unless the protocol supports it and the application has an explicit replay/idempotency contract. Propagate cancellation to the underlying work; disconnecting the client must not leave an uncontrolled cascade running.

## Investigation order

First obtain the active source/config generation and raw correlated traces. Then resolve what `decisions` means in code and whether context limits are enforced per upstream rather than merely declared on the combo. Reproduce the empty/error cases against a deterministic fixture. Finally test the actual external streaming path. This order avoids redesigning infrastructure to repair an unproven network diagnosis.
