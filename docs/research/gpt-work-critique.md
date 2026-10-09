> Authored by Instinct

# GPT Work critique of the agent stack architecture (Oct 8, 2026)
**This is input and critique, not adopted decisions.** It is ChatGPT Work's (GPT-6.1 Sol) answer to the full stack picture and the questions: what is missing, what breaks first, weakest/contradicting decisions, build sequence. Chat: https://chatgpt.com/c/6ac8868e-22b8-83e9-9ec8-b1a9cfbfa07b

Copied in full below with its own uncertainty notes intact (it says these are architectural predictions, not measured findings, and that it did not inspect his forks, HERDR, worker profiles, provider entitlements or deployed config). The model's inline source citations were rendered as bare labels (Learn Temporal, SPIFFE, Docker Docs, gVisor, Cloudflare One docs, postgresql.org, GitHub) without URLs in the page text, so those labels were dropped; check any external claim before relying on it.

---

Worked for 2m 41s
Your largest gap is authority, not agent orchestration. You have several components capable of scheduling work, changing state, and reporting budgets—but no complete specification for which component owns each decision.
My predicted first failure is duplicate or stale execution after a timeout, followed by resource contention and provider throttling. The most consequential failure is an agent reaching an external effect through a path that bypasses approval.
These are architectural predictions, not measured findings. Unsure: I have not inspected your forks, HERDR implementation, actual worker profiles, provider entitlements, or deployed configuration. The listed model routes are treated as your intended configuration, not verified availability.
1. Missing pieces
Some are mentioned in your picture but lack the machinery that makes them enforceable.
| Missing contract or service | What it must do | Failure without it |
|---|---|---|
| Authority map | Assign one writer/decision owner for task admission, execution, approvals, spend, artifacts, and organizational state | Hermes, Paperclip, Temporal, and JetStream disagree about what should run |
| Task/run/attempt identity | Separate persistent agent identity, logical task, workflow, execution attempt, and container slot | A retry inherits stale permissions or appears to be a new authorized action |
| Host execution supervisor | Launch, reconcile, fence, cancel, and clean up processes independently of the AI worker | Temporal retries while the original container continues working |
| Effect executor | Hold final-effect credentials and execute only validated, approved action envelopes | Approval is recorded, but nothing actually prevents bypass |
| Admission controller | Atomically reserve resources, budget, provider quota, and delegation allowance before dispatch | Hundreds of logical agents become hundreds of runnable processes |
| Credential broker and egress enforcement | Issue task-scoped capabilities; prevent direct provider/service access outside approved routes | A worker bypasses budgets, exports data, or uses cached credentials |
| Reconciliation service | Compare desired state against containers, workflow state, artifacts, and external effects | Orphan containers and ambiguous writes accumulate |
| Independent verification | Test acceptance criteria against immutable artifacts with separately controlled verification | Workers mark their own plausible output “done” |
| Memory governance | Preserve provenance, access scope, freshness, and distinctions between evidence and inference | Prompt injection becomes persistent organizational “knowledge” |
| Recovery specification | Define restore order, reconciliation, key recovery, RPO/RTO, and approval invalidation | A successful database restore re-enables previously consumed approvals |

Your approval broker needs an executor beside it
Hashing the artifact is necessary but insufficient. Approval should bind a canonical action envelope, including:
Task and logical effect IDs.
Exact artifact digest and dependency/input digests where relevant.
Operation, destination, account, environment, and relevant parameters.
Preconditions: expected commit, resource version, current state.
Maximum spend or other bounded effects.
Expiry, one-time nonce, policy version, and authenticated owner.
Execution receipt and resulting external resource identifier.
Approve “deploy this digest to this environment,” not “approve this file.”
The executor must fetch and verify the immutable artifact itself. It must never trust a worker’s statement that the bytes still match.
The hard case: the external service accepts the write, then your executor crashes before recording success. Neither an approval hash nor durable workflow replay solves this. Use receiver-supported idempotency, queryable reconciliation, or an explicit OUTCOME_UNKNOWN state that blocks automatic retry. Temporal’s own guidance pairs at-least-once Activity execution with application/receiver idempotency. 
For each effect class, specify which of those three strategies applies. Some browser actions will remain reconciliation-dependent.
Identity and secrets need two separate layers
“Agent identity lives in git” is organizational identity. It does not authenticate a running process.
Use:
Persistent identity: agent role and ownership.
Execution identity: task, attempt, host, image digest, expiration.
Capabilities: narrowly scoped permission to request a particular operation.
Provider credentials: retained outside worker containers wherever possible.
Start with supervisor-issued, audience-bound, short-lived credentials and online authorization checks for sensitive actions. SPIFFE/SPIRE is a later implementation option; SPIFFE explicitly models short-lived workload identity documents. Short lifetime alone does not provide immediate revocation. 
A secrets vault cannot fix unrestricted network access or broadly privileged credentials.
Budget enforcement must precede spending
Paperclip reports governance and budget hard-stops, but those features do not establish enforcement over every route in your proposed system. 
Your model gateway should:
Reserve worst-case allowed request cost atomically.
Enforce input/output limits, model allowlists, and concurrent request limits.
Settle actual usage and release unused reservation.
Charge retries and delegated work to the originating budget.
Reject bypass routes.
Include limits for money, tokens, wall time, retries, child tasks, tools, and external effects. A subscription route still needs a capacity budget.
Unsure: whether each CLI and subscription route supports this gateway model without credential forwarding or incompatible authentication. Verify each adapter independently. If a route cannot be mediated, label its spend limit as soft and restrict its blast radius.
2. What breaks first
The ordering changes with workload. API-heavy workers hit provider limits; build-heavy workers hit RAM, CPU, and disk; approval-heavy workers hit you.
| Likely failure | Concrete trigger | Required response |
|---|---|---|
| Duplicate execution | Worker heartbeat times out while its container remains alive | Fence old attempts; supervisor reconciles before relaunch |
| Provider throttling / retry amplification | Many agents wake together; retries synchronize | Per-provider admission, jittered backoff, circuit breakers, bounded retry budgets |
| Laptop memory pressure | CLI sessions overlap with builds, browsers, and the container VM | Measure workload classes; admit by resource envelope |
| Desktop CPU and disk contention | Multiple compilers, tests, installs, and artifact uploads overlap | Separate LLM-wait slots from build/browser slots |
| Human approval backlog | Small actions generate individual approval requests | Bound pending approvals; expire stale requests; batch only explicit bounded actions |
| Control-plane starvation | Workers consume resources needed by Postgres and orchestration | Reserve control-plane resources and shed worker load |
| State divergence | DB commit succeeds but event publication fails | Transactional outbox, consumer inbox/deduplication, reconciliation |
| Storage exhaustion | Workspaces, logs, images, and artifacts grow without retention | Quotas, retention, garbage collection, low-space admission stop |

Ten to twenty laptop containers is not a defensible active-worker target yet. It may work for mostly idle shells. It is a different claim for twenty agents compiling or running browsers.
Illustrative arithmetic—not a benchmark: reserving 6 GiB of a 16 GiB laptop leaves about 10 GiB. Ten tasks averaging 1 GiB exhaust that allocation before accounting for bursts; twenty averaging 0.5 GiB do the same. Docker Desktop also runs its engine inside a Linux VM. 
Start with 2 laptop and 4 desktop active tasks, then raise limits from measured mixed-workload results. These are conservative starting settings, not hardware capacity estimates.
Docker containers have no resource constraints by default. Explicit memory, CPU, PID, workspace, and log limits are part of your worker contract. 
Hundreds of logical agents are plausible here. Hundreds of simultaneously active tool-heavy workers are an unproven and probably poor target. Waiting agents should consume durable state, not a container.
3. Weakest decisions and contradictions
Hermes as CEO must not imply executive authority
Keep the firm decision. Define “CEO” as planner and conversational gateway.
Hermes may propose tasks, priorities, and organizational changes. It must not grant credentials, raise budgets, approve its own effects, modify enforcement policy, or bypass admission. Treat its messages and memory as potentially compromised inputs.
Hermes already provides cron and memory facilities. That creates overlap with your workflow scheduler unless cron is restricted to submitting deduplicated workflow requests. 
Paperclip as cockpit requires disabling competing execution paths
Paperclip advertises scheduling, adapters, governance, and agent control; it is not inherently just a passive view. 
Your intended placement needs an adapter that turns cockpit commands into canonical task requests. Do not let Paperclip separately launch CLI workers while Temporal also owns them.
Recommended authority split:
| Component | Owns |
|---|---|
| Hermes | Intent capture and proposals |
| Paperclip | Organizational view and user commands |
| Temporal | Durable execution progression |
| Admission service | Resource, quota, and budget permission |
| Host supervisor | Actual process/container lifecycle |
| Approval broker | Owner authorization records |
| Effect executor | Approved external writes |
| Postgres application schemas | Transactional business records |
| PhenoRegistry | Versioned specifications, policies, evidence manifests |
| JetStream | Event distribution and replay for consumers |

“One Postgres anchor” can mean one instance, not shared table ownership. Give Temporal, Paperclip, and your application separate databases/schemas and roles as their supported configurations require.
Temporal plus JetStream is acceptable only with a boundary
Temporal should own execution dependencies, timers, retries, and approval waits. JetStream should carry notifications and projections. Do not implement a second workflow engine through event consumers.
JetStream provides deduplication and acknowledgment mechanisms, but these do not atomically commit an unrelated database update or external API write. 
Use an application DB outbox for application events. Where Temporal transitions feed application state, use idempotent Activities and reconciliation; there is no implied transaction spanning all three systems.
Temporal is the leading choice—but scope its promise correctly
Postgres-backed Visibility is supported, so Elasticsearch is not inherently required for your initial deployment. 
Keep workflow code deterministic. LLM calls, CLI launches, database access, and external operations belong in Activities. 
Do not place an entire multi-hour CLI session inside an unstructured Activity and assume you gained reliable execution. Give it bounded stages, heartbeats, cancellation, artifact checkpoints, and reconciliation.
Unsure: which Hatchet issue your gate refers to and its current fix status. Public reports include durable reconnect and ambiguous acknowledgment failures; they justify testing those paths, not claiming Hatchet universally fails. 
Run the same failure harness against Temporal and any serious alternative. Stop comparing dashboards once one passes your execution requirements.
“gVisor/Kata only for untrusted code” leaves the classification undefined
Agent-generated code, repository scripts, dependencies, and fetched content should be considered untrusted execution unless you have a concrete reason otherwise. Owning the repository does not establish that every command an injected agent runs is trusted.
gVisor explicitly targets untrusted workloads, including LLM-generated code, while warning that sandboxing does not replace secure architecture. 
Unsure: performance and compatibility for your exact toolchains and both hosts. Benchmark isolation modes. Keep approval services and privileged credentials outside worker-accessible execution environments.
A shared image should mean a shared specification
Your hosts have different architectures. Build pinned amd64 and arm64 variants, with per-CLI layers and adapter qualification. A single mutable image containing six evolving tools creates a large failure surface.
Warm slots must be pristine. Never recycle a used task container into another task; recycle by destroying and recreating it.
HERDR is privileged even when its facade is read-only
The host-side component performing docker exec is an execution surface. The facade should read sanitized output through a separate API, not expose a terminal transport with input disabled in the UI.
Test WebSocket input, resize/control messages, alternate endpoints, terminal escape handling, and secret leakage. Viewing a log is also reading untrusted content.
Cloudflare provides connector-side Access JWT validation options. Explicitly prevent alternate LAN/tailnet origin paths from bypassing application authorization. 
PhenoRegistry cannot be the live transaction ledger
Use git for specifications, policy versions, agent definitions, and evidence manifests. Use transactional storage for reservations, leases, approval consumption, and effect receipts.
Agents must not be able to make a policy authoritative merely by committing it. Policy deployment is a privileged operation.
“Independent approvals” needs a threat boundary
Separate credentials protect against compromised workers. They do not establish independence from a compromised host administrator.
For the initial build, explicitly promise worker-compromise resistance, not full host-compromise resistance. If the latter becomes required, move signing/authorization trust to a separate device or hardware-backed boundary.
4. Build sequence and exit tests
Build one complete vertical slice before adding more worker brands or organizational complexity.
| Phase | Build | Exit tests |
|---|---|---|
| 0. Authority and contracts | Ownership map; typed task/action schemas; state transitions; threat model; canonical IDs | Every privileged transition has one owner. Agent requests cannot alter policy or raise budgets. Conflicting scheduler submissions produce one logical task |
| 1. One bounded worker | One CLI adapter, pinned image, immutable inputs, hard limits, structured result, supervisor | Kill supervisor and worker independently. Reconcile orphans. Deny host files, Docker socket, sibling workspaces, and forbidden egress. Cancellation removes the entire process tree |
| 2. Approved effects | Broker, owner authentication, immutable artifacts, executor, idempotency/reconciliation | Your Pilot F: changed artifact rejected; duplicate approval consumed once; revoked grant denied; crash after write causes reconciliation or OUTCOME_UNKNOWN, never blind repeat |
| 3. Durable workflow | Temporal task lifecycle, approval waits without containers, bounded retries, checkpoint references | Restart service and workers at each transition. Replay old histories after code updates. Lost heartbeat does not create two authorized active attempts. Duplicate signals do not duplicate effects |
| 4. Budget and admission | Model gateway, atomic reservations, provider quotas, resource classes, delegation caps | Concurrent requests cannot exceed reserved budget. Direct provider bypass fails. Inject 429s, outages, and stuck streams; retry traffic stays bounded and control plane remains responsive |
| 5. Audit and recovery | Correlated traces, append-only audit path, metrics, backup/restore, artifact retention | Reconstruct a task from intent through receipt. Restore on a clean environment. Old approvals do not resurrect. Missing artifacts and ambiguous external effects are detected |
| 6. Hermes and Paperclip integration | Intent/cockpit adapters, deduplicated schedules, projections | Repeated cron and cockpit submissions yield one workflow. Compromised Hermes cannot grant itself authority. Stale Paperclip views cannot override canonical execution state |
| 7. Verification and memory | Independent acceptance checks, task-class evals, provenance-aware memory promotion | Seed false “done” reports and malicious documents. Verifier catches seeded defects. Untrusted memory cannot become policy or cross access boundaries |
| 8. Two-host scheduling | Host capabilities, architecture-aware placement, fencing, checkpoints | Disconnect/sleep laptop mid-task. Old attempt cannot publish accepted results after reassignment. Resume from durable artifact references rather than assumed live CLI state |
| 9. Scale and Fabric | Measured expansion, then PhenoFabric/ShareCLI integration | Run 100 logical agents under bounded active concurrency for a mixed-workload soak. No unauthorized effects, duplicate logical effects, unbounded retries, starvation, or budget violations |

For Phase 5, proposed starting recovery targets are RPO ≤15 minutes and RTO ≤2 hours, subject to what you can actually demonstrate. Postgres point-in-time recovery requires base backups plus an adequate WAL archive; ordinary SQL dumps do not provide that continuous recovery mechanism. Back up artifacts and recovery keys separately from the desktop’s failure domain. 
Observability should expose queue age, blocked reason, active attempts, resource pressure, reservation versus actual spend, approval age, ambiguous effects, verifier failures, and completed usable outcomes. Panes show activity; they do not establish correctness.
My build recommendation: keep Hermes and Paperclip in their chosen positions, choose Temporal provisionally, and implement one CLI → one supervisor → one workflow → one immutable artifact → one independent approval → one effect receipt. Delay broad worker support, JetStream-dependent coordination, and Fabric until that path survives Pilot F.
The decisive milestone is not “100 agents running.” It is 100 logical agents producing useful work while concurrency, authority, spending, and recovery remain bounded—even when workers lie, crash, retry, or get injected.

