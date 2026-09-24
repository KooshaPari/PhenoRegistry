# Multi-agent operating model

## Core rule

Local repository agents are evidence producers and scoped closure workers. They are not sovereign portfolio architects.

The portfolio fails if 146 agents independently decide:

- what their repo owns;
- which sibling is obsolete;
- which schema is canonical;
- where shared code belongs;
- what “complete” means;
- whether their own tests prove success.

Central adjudication is therefore a control boundary, not bureaucracy.

## Roles

### Human sponsor

Owns irreducible product and portfolio value judgments, destructive approvals, public brand decisions, and risk acceptance.

### Portfolio adjudicator

- Maintains capability/authority graph.
- Approves role/disposition.
- Resolves cross-family conflicts.
- Controls repo births and retirements.
- Accepts target topology.
- Issues scoped decision IDs.

### Registry/evidence service

- Observes GitHub facts.
- Stores stable IDs.
- Validates worker output.
- Generates queues and projections.
- Does not make product-value decisions autonomously.

### Family lead

- Owns a bounded semantic family.
- Runs history/clone/consumer analysis.
- Produces target alternatives.
- Coordinates pilots and migration DAG.
- Requests central decisions.

### Repository closure agent

- Audits and completes a scoped repository/target slice.
- Preserves local intent.
- Produces machine-readable handoff.
- Cannot self-approve cross-repo authority.

### Research/pilot agent

- Builds SOTA inventory.
- Runs controlled comparisons.
- Must disclose target affiliation and tuning.
- Produces raw evidence.

### Migration agent

- Stages history/code/package/data moves.
- Operates only from approved source→target map.
- Preserves rollback and provenance.

### Independent verifier

- Reproduces critical checks.
- Audits negative controls and release inclusion.
- Rejects unsupported completion claims.
- Does not implement the same material slice it certifies.

## Work claim protocol

1. Query current queue.
2. Select a `READY` task whose predecessors and decision IDs are satisfied.
3. Acquire lease with repo/path scope and TTL.
4. Record observed source refs.
5. Create isolated worktree/clone.
6. Execute only assigned mode.
7. Persist checkpoint and evidence continuously.
8. Submit schema-valid handoff.
9. Independent verifier reviews.
10. Portfolio/family state updates only after acceptance.
11. Release/archive/migration requires explicit next authorization.

## Scope locks

A task must declare:

- repositories;
- refs;
- bounded paths;
- allowed generated artifacts;
- external systems;
- migration targets;
- forbidden sibling mutations;
- resource limits.

Two agents may work in one repo when path and contract ownership are disjoint. Shared canonical files require a designated integration owner.

## Context packaging

Do not give each agent the whole ecosystem history.

Every assignment package contains:

- repo/family ID;
- role hypotheses;
- relevant human intent excerpts and provenance;
- central policies;
- current authority map projection;
- related decision IDs;
- source refs;
- prior checkpoint;
- expected outputs/schema;
- explicit non-goals;
- test/resource limits.

The agent can request more evidence by ID.

## Escalation events

A repo agent must stop the affected decision—not all safe work—and escalate when:

- sibling authority conflict appears;
- destructive migration seems required;
- human intent is contradictory;
- license/security boundary changes;
- current source refs changed materially;
- required history is inaccessible;
- pilot reveals product has no distinct value;
- richer SSOT conflicts with central assumptions;
- implementation would rewrite accepted scope;
- a consumer not in migration map is discovered.

## Reconciliation

Worker proposals enter a central queue:

```text
worker finding
→ schema validation
→ evidence verification
→ family reconciliation
→ portfolio decision
→ generated authority projection
→ new closure work
```

A README change cannot itself settle a decision.

## Agent quality controls

- Every material result cites immutable refs/paths.
- Claims use evidence classes.
- Tests have negative controls.
- Exact commands and results retained.
- Unknown and blocked are valid outputs.
- No agent-generated completion percentage without a computed contract.
- No generic docs files added merely for score.
- No source file rewritten solely to match an audit template.
- No cross-repo import path changed without consumer check.
- No archive action without provenance and successor.

## WIP and scheduling

Default maximum:

- One authority family.
- Two forensic families.
- Three closure repos per family.
- One pilot per family.
- Independent verifier queue.

Agents can parallelize evidence collection inside a family, but one family lead integrates the model.

## Closure review rubric

A closure is accepted only when:

- terminal outcome is explicit;
- role/authority is approved or correctly marked proposed;
- required gate evidence exists;
- claims and README are honest;
- consumers/compatibility handled;
- no richer source was lost;
- tests can fail and pass appropriately;
- migration is reversible;
- registry and projections update;
- raw coverage limitations remain visible.

## Prompt routing

Use:

- `MASTER-PORTFOLIO-COORDINATOR-PROMPT.md` for the central program.
- `FAMILY-ADJUDICATOR-PROMPT.md` for a semantic/lineage cluster.
- `PER-REPO-AUDITOR-AND-CLOSURE-PROMPT.md` for one bounded repo.
- `SOTA-PILOT-AGENT-PROMPT.md` for controlled comparison.
- Prior forensic recovery and polyrepo migration prompts as supporting deep modes when explicitly assigned.

## Human-decision efficiency

Batch only genuinely irreducible choices. Present:

- decision question;
- evidence summary;
- two to four serious alternatives;
- recommended option;
- affected products/consumers;
- reversible first step;
- consequence of no decision.

Do not ask the human to choose file layouts the evidence can determine.
