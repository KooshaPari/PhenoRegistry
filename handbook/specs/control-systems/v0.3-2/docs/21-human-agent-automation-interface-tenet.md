# Human, agent and automation interface tenet

## Global product rule

The user's requirement is stronger than "have an API": **humans, agents and automations are all first-class users**. S052.

The durable rule should be adopted at governance/charter level across products:

> One capability model, one authorization model, one observable state and evidence model; multiple ergonomic clients.

## Surface contract

| Surface | Optimized for | Required properties |
|---|---|---|
| GUI | discovery, comprehension, approvals, visual state | every mutation maps to public typed operations; no hidden state |
| CLI | expert/operator speed | script-safe modes, JSON output, stable exit codes, explicit plans/diffs |
| SDK | composition | typed models, idempotency, retries, pagination, streaming/events |
| agents | reasoning + tools | compact schemas, explainable failures, dry-run, bounded actions, receipts |
| automations | unattended reliability | deterministic identifiers, idempotency keys, event cursors, leases, backoff semantics |

The GUI may aggregate and visualize. It must not possess an unexported deployment capability that agents cannot invoke. Conversely, an agent-only privileged backdoor is not acceptable simply because agents are important.

## Mutation envelope

For meaningful mutations, expose a common lifecycle:

`discover -> plan -> validate -> authorize -> apply -> observe -> reconcile/recover`.

Return machine-readable preconditions, unsupported capabilities, cost/budget impact, exact target and artifact identities, and receipts. Human confirmation can be one authorization policy; automation can use pre-authorized policy scopes. Both operate on the same candidate object.

## Why this matters beyond BytePort

The same rule applies to Tracera evidence, AgilePlus work graphs, review control, assessment dossiers, ResearchLedger and future products. It prevents a recurring failure mode where agent-generated automation becomes a separate unobservable system beside the user-facing application.
