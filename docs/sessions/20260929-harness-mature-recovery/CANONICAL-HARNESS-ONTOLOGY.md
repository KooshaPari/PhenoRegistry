# Canonical harness mature ontology — candidate v0.1

Date: 2026-10-01. Status: REVIEW CANDIDATE, deliberately falsifiable.

This ontology is independent of repository layout. A mature product obligation may project into multiple views.

## Core entities

### Product/client
A user-facing or machine-facing client/application consuming harness contracts. Examples: canonical CLI(s), HeliosLab, SDK/API service. Client identity does not own generic agent semantics.

### Agent definition
Reusable behavioral/configuration definition: instructions/policy defaults/model requirements/tool capability requirements/context strategy. Not a running process.

### Worker attempt
Ephemeral execution of an agent definition under a concrete model/runtime/config/environment. May die/restart without destroying durable effort.

### Durable effort
Persistent development/work objective across attempts: assignment, plan/work packages, dependencies, effect receipts, reviews, grader history and execution receipts.

### Product state
Accepted product/domain truth independent of development machinery.

### Run/turn/step
Nested execution scopes within an attempt. Exact hierarchy may vary by agent strategy; IDs and causality are mandatory where evidence/replay depends on them.

### Capability/tool
Typed operation available to an attempt, with input/output/error/effect classification, policy requirements and reconciliation semantics.

### External effect
Potentially state-changing operation outside the attempt's transactional state. Carries durable identity and known/uncertain/reconciled outcome.

### Workspace/environment
Execution substrate and resource namespace: filesystem/repo/worktree/process/sandbox/browser/VM/container/device/network. Must expose capability and isolation semantics rather than one implementation assumption.

### Context
Model-visible bounded projection assembled from instructions, conversation/events, workspace state, memory/retrieval, tools and durable effort.

### Memory
Information intended to survive beyond immediate context. Distinguish durable facts/records, retrieval indexes, summaries and inferred memory; preserve authority/provenance.

### Provider/model runtime
Model invocation and capability negotiation surface: streaming, tool calls, reasoning controls, multimodality, context limits, caching, cost/rate/resource constraints.

### Policy/authorization
Decision authority for capabilities/effects/secrets/resources. Human approval is one policy actor, not the entire system.

### Event
Immutable or append-only fact/observation about lifecycle/action/state transition with identity, causality, authority/provenance and schema version.

### Projection
Client-specific/read-optimized view derived from events/product state. GUI/TUI/CLI presentation differences live here when possible.

### Evidence
Artifact binding a claim/criterion to exact subject/candidate/config/environment/verifier/run/time/raw provenance.

### Criterion/rubric/grader
Independent acceptance policy and evaluator. Grader output cannot itself redefine accepted contract.

### Scheduler
Maps runnable work/attempts to resources under priority, dependency, concurrency, budget and QoS constraints.

### Control plane
Fleet-wide discovery, policy, scheduling coordination, credentials/resource bindings, observability and administration. Not required in-process for every harness consumer.

### Extension/adapter
Versioned integration implementing a stable contract for providers, tools, environments, clients, policies, storage or interoperability.

## Independent projections

1. Product/client experience.
2. Agent semantics.
3. Durable workflow/effort.
4. Runtime/execution.
5. Environment/workspace.
6. Context/memory.
7. Capability/tool/effect.
8. Provider/model.
9. Policy/security/IAM.
10. Event/projection/API.
11. Evidence/evaluation/MACE.
12. Scheduling/resources/QoS.
13. Persistence/recovery.
14. Observability/replay.
15. Extension/interoperability.
16. Supply chain/release.
17. Operations/control plane.
18. Documentation/developer experience.

Do not flatten these into one tree. Requirements reference whichever projections apply.

## Core invariants

- Worker attempt != durable effort != product state.
- Client presentation cannot be the sole source of agent truth.
- Confidence != authority.
- Missing/skipped/stale/wrong-subject evidence != green.
- External uncertainty cannot be silently converted to failure/success.
- A replacement worker cannot blindly repeat an uncertain effect.
- Runtime-generated identity used for recovery must survive replacement.
- Grader/version/criterion/candidate/config/environment are evidence identity.
- Client adapters may enrich presentation but cannot silently alter accepted lifecycle semantics.
- Provider-specific capabilities are negotiated, not assumed universal.
- Cancellation is a lifecycle event with explicit downstream/effect semantics, not merely dropping a future.
- Durable state transitions require defined atomicity/idempotency/reconciliation boundaries.
- Generic core cannot require a coding repository; coding capabilities are extensions/profiles.
- Product-specific state is not automatically harness state.
- A tool existing in code but not mounted/reachable is not a usable capability.
- Historical implementation is evidence, not current implementation.
- An upstream feature is not owned differentiation merely because an old fork also contains it.

## Falsification workloads before freeze

The ontology must explain without special pleading:
- interactive coding session with tools and approvals;
- 500 parallel headless coding attempts with shared resource limits;
- long-running research agent using browser/files and human clarification;
- email/operations workflow with irreversible external effects;
- data-analysis workflow with notebook/artifact production;
- GUI workbench with multiple live attempts and projections;
- voice/real-time conversational agent;
- scheduled background monitoring agent;
- multi-agent software factory with durable work packages;
- worker crash after side effect before acknowledgement;
- provider switch mid-effort;
- offline/local model runtime;
- remote sandbox/fleet worker;
- non-coding agent with no repository/worktree concept.

Any case requiring a new foundational entity triggers ontology review.
