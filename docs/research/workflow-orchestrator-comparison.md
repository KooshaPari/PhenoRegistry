> Authored by Instinct

# Workflow orchestrator comparison (Oct 8, 2026)
Research only; nothing installed. Sources are official docs and live issue trackers; no invented stats.

## His ruling
A workflow-orchestration layer is a MUST. Candidates he named: Temporal, Prefect, Hatchet, "others". Shared-base analysis ("Research Agent Business Stack") also listed Kestra OSS, Activepieces, Windmill, n8n. It rejected Temporal for needing code; for him that does not apply. This slot sits under the workers in the Hermes/Paperclip layout.

## Verdict
PRIMARY: Temporal OSS (Python workers, PostgreSQL-only). ALT: Hatchet OSS (Lite + PostgreSQL), gated on crash/replay tests (open issue #4235). Temporal's earlier rejection for needing code does not apply to Koosha. Prioritize the durable control-plane foundation over no-code UI convenience. Single-node Temporal does NOT require Redis, RabbitMQ, Elasticsearch or Kubernetes.

## Candidates
- Temporal: persisted event history + deterministic replay; durable signals/timers; CLI runs in Activities with retries, heartbeats, cancellation. Server + PostgreSQL (primary + visibility DBs) + UI + Python worker. MIT. Strongest documented correctness model. You own schema upgrades, auth, approval UI/service. No self-host RBAC/audit out of the box. No built-in CLI process recovery: reconcile/restart Activities safely.
- Hatchet: PostgreSQL transactional state; at-least-once execution; durable parents checkpoint waits/children with deterministic code between checkpoints. Lite bundles the control plane; Postgres required, RabbitMQ optional. Python worker + useful UI + official MCP cookbook. MIT. Approval = event/wait primitive, not independently authenticated owner consent. Open reports: Python SDK v1.33.9 durable replay crash #4235, TS #4785; older #3823 closed with recurrence discussed. These are user reports, not reproduced tests, hence alt and not primary.
- Kestra OSS: real contender. Standalone Java + PostgreSQL + local artifacts; no Redis/Kafka. Vendor minimum 4 GiB / 2 vCPU. Native shell/Python/container tasks, Pause/resume UI, at-least-once failed-worker resubmission. Apache-2.0; RBAC/service accounts are enterprise. Best if UI-authored YAML/shell dominates.
- Prefect: good Python for data/ML; retries, persisted/cached results, typed pause/suspend UI. Single server can use SQLite, Postgres preferable; Redis not strictly required on a single server. Not event-history replay of arbitrary Python. Apache-2.0.
- Windmill: Rust backend, Postgres queue/state, strong UI; workflows-as-code with checkpoint/replay and zombie restart (it is durable). Free approval steps use secret URLs; logged-in approver permissions and disabling self-approval are Cloud/Enterprise. License: source AGPLv3, Community binaries contain proprietary code; free internal use allowed.
- Activepieces: MIT community; Postgres + Redis; durable replay of checkpointed steps is claimed (checkpoints every 15s vs "crash loses at most current step" tension needs testing). CLI workers need a custom piece/HTTP adapter. Better business-integration edge.
- n8n: light single instance; queue mode needs Postgres + Redis + workers. Durable Wait + webhook auth, good execution UI. Execute Command is disabled by default since 2.0 and runs in a container, not on the host. SUL fair-code, not OSI. No evidence of arbitrary running-node crash replay comparable to Temporal; do not claim it.

## Concrete primary setup
1. Official samples-server POSTGRES-ONLY Compose (not the default Compose with Elasticsearch). Pin releases, replace sample creds, named durable Postgres volume, loopback/private binding, test DB backup/restore.
2. Design: Paperclip -> bounded work-order API -> Temporal -> isolated Python Activity invoking a CLI worker through Hermes -> artifact -> owner approval -> separate privileged commit Activity. (Proposed glue, not a verified connector.)
3. Wrap CLI execution: work-order/run ID, timeout, process-group termination, heartbeats, logs, artifact capture. An orchestration timeout does not prove the OS subprocess stopped. Isolated agent workspaces; never mount the host Docker socket into coding workers.
4. Independent approvals: a broker stores a hash of the exact artifact/action/target; owner-authenticated approve/reject; single-use decision + expiry; the privileged executor re-verifies. Agents must NOT hold approval endpoint credentials, workflow-control tokens, or final-effect credentials. Temporal signals and Hatchet events are transport, not proof of human authority; a pause button alone does not meet this.
5. Idempotency/reconciliation on every effect. Nothing makes a CLI agent's git push or API side effect exactly-once. Do not blanket-retry whole sessions without checking artifacts/commits.
6. Acceptance tests before adoption: kill the CLI worker mid-run; kill the orchestrator while waiting for approval; reboot; duplicate approval; change artifact after approval; crash between side effect and ack; restore DB. Assert no unapproved effects, lost work, or untracked duplicates. A single desktop recovers after restart but is unavailable while the host is down.

## Alt setup
Hatchet Lite + Postgres Compose, pinned SDK/engine, persistent volumes, one Python worker. The durable parent only coordinates waits/children; CLI side effects run in ordinary child tasks. Same approval broker. Validate #4235 on the chosen versions before relying on replay. If lower ops burden dominates AND tests pass, Hatchet can become primary.

## Sources
- Temporal: docs.temporal.io/self-hosted-guide/deployment, /production-checklist; github.com/temporalio/samples-server/blob/main/compose/docker-compose-postgres.yml; docs.temporal.io/guides/reliable-document-approvals; github.com/temporalio/temporal
- Hatchet: docs.hatchet.run/self-hosting/hatchet-lite, /docker-compose, /llms/v1/architecture-and-guarantees.md, /v1/durable-tasks, /cookbooks/hatchet-and-mcp; github.com/hatchet-dev/hatchet/issues/4235, /4785, /3823
- Kestra: kestra.io/docs (installation/docker-compose, oss-vs-paid, server-lifecycle, pause-resume, requirements); github.com/kestra-io/kestra
- Prefect: docs.prefect.io/v3 (self-hosted/docker-compose, interactive, results, detect-zombie-flows); github.com/PrefectHQ/prefect
- Windmill: windmill.dev/docs (advanced/self_host, workflows_as_code, flow_approval); github.com/windmill-labs/windmill
- Activepieces: activepieces.com/docs (install/options/docker-compose, architecture/durable-execution, sandboxing); github.com/activepieces/activepieces
- n8n: docs.n8n.io (license-faq, queue-mode, wait, executecommand)
