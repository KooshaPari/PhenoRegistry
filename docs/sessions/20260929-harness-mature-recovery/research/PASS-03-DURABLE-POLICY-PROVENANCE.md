# SOTA pass 3 — durable execution, policy, protocol evolution and provenance

Retrieved 2026-09-29. This pass narrows the architecture question for the two active products; it does not approve adoption.

## 2026 protocol evolution

MCP 2026-07-28 moved to a stateless protocol core and moved long-running work into the `io.modelcontextprotocol/tasks` extension. A server may return a durable task handle from `tools/call`; clients then use `tasks/get`, `tasks/update`, and `tasks/cancel`. The earlier experimental task lifecycle from 2025-11-25 was deliberately redesigned after production feedback. Consequence: do not embed durable development-effort identity into a transport connection or recreate a session-heavy task wire protocol merely because older MCP designs did so.

The Tasks extension's endpoint identity and resumable durable handle are relevant prior art for machine interfaces, but they do not replace our product-level durable effort, evidence, authorization, or side-effect reconciliation. A task handle can survive disconnects while still being the wrong abstraction for accepted product truth.

## Durable execution

Temporal is serious prior art for failure-resilient durable workflows: workflow state and progress can survive process/network/server failures. This is a COMPOSE/EVALUATE option when our durable development effort becomes a real multi-step workflow service. It is not a justification for adding Temporal to either CLI today.

Architecture consequence: distinguish replayable internal orchestration from external effects. A durable engine can retry work; exact external-effect semantics still require idempotency/deduplication/uncertainty handling at the adapter boundary. The first vertical-slice oracle therefore keeps effect identity and ambiguous-effect recovery explicit rather than asserting magical exactly-once behavior.

## Policy authority and grader hardening

OPA decision logs contain decision identifiers, policy input and bundle revision for audit; signed policy bundles can cryptographically bind policy contents to an independently configured trust key. This is strong prior art for our requirement that worker-writeable implementation code must not silently weaken its own grader.

Candidate bootstrap: LEARN/ADAPT the policy-bundle + decision-receipt pattern before inventing a generalized policy engine. A small deterministic grader can remain local if its accepted policy/version is independently controlled and receipts bind policy identity. OPA becomes useful when cross-repo/organization authorization and policy distribution justify the operational cost.

## Artifact provenance

SLSA v1.2 is approved and defines artifact/source provenance concepts. Use SLSA-compatible provenance for source/build custody where possible; do not redefine that vocabulary. Extend evidence identity separately with live-runtime subject information that SLSA build provenance does not prove—for KCode, the daemon that actually answered; for HeliosLite, the exact executable/configuration/verifier run.

## Consequences for the two products

**HeliosLite:** the custom benchmark should stay small and task-specific, but its terminal/evidence policy must fail closed. Do not turn benchmark orchestration into a new generic workflow platform. If long-running eval execution later needs durable handles, MCP Tasks or an external durable engine is preferable to bespoke connection-bound sessions.

**KCode:** its existing single-server architecture, reconnect/reload state and persisted sessions are already substantial. The immediate custom work justified by evidence is only the missing responder identity in the lightweight handshake. Durable development-effort orchestration should not be forced into the daemon merely because sessions live there.

## Bootstrap ledger updates

| Need | Prior art | Disposition |
|---|---|---|
| Long-running machine request | MCP Tasks 2026-07-28 | INTEGRATE/ADAPT when needed; no custom task protocol now |
| Crash-resilient multi-step orchestration | Temporal durable workflows | EVALUATE only if workflow-service complexity is justified |
| Grader/policy authority | OPA signed bundles + decision logs | LEARN/ADAPT; start smaller, preserve independent policy identity |
| Build/source provenance | SLSA v1.2 | USE vocabulary/attestations rather than custom supply-chain format |
| Product behavioral acceptance | none of the above by itself | BUILD task-specific oracles and bind them to provenance |

Remaining work: exact library/package versions and licenses for any selected integration; performance/operational cost; failure injection; migration/exit strategy; matched pilot against the existing simpler implementation.
