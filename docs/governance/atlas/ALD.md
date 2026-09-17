> **v1.4 clarification:** capability/behavior composition is primary; peer UI embedding is optional. Canonical design, multi-channel product bridges and scope-bound numerical grading are specified in [proof/README.md](proof/README.md). Historical anti-score statements no longer prohibit defensible grades; critical gates and evidence limits remain.

> **v1.2 dispatch precedence:** [one existing chat per current repository](prompts/ONE-CHAT-PER-REPOSITORY.md) replaces historical ten-seat/pair staffing. Technical assurance/reuse obligations remain; historical counts and observations are not a current heartbeat.

# Abstraction-layer design

ALD here means **Abstraction-Layer Design**, explicitly chosen for this package rather than claimed as an official AgilePlus acronym.

## Layer 0 — source facts

Git objects, filesystem captures, manifests, compiler indexes, native coverage/test reports, runtime observations, build artifacts and authenticated engine receipts. Preserve each producer's limits and exact identity. No global code graph is presumed complete from regex or grep output.

## Layer 1 — normalized observations

Adapters map source facts to portable records with source anchors, timestamps, tool versions, actor/visibility and failure states. Normalization does not discard original units, scopes, missing data or native error categories. Unicode/text normalization and redaction create separate derived objects with source links.

## Layer 2 — semantic entities and relationships

Repository, product, applet, package, source unit, interface, state object, capability, obligation, test, run, artifact, installation, claim and decision. Each relationship has provenance and applicability. A static reference, dynamic observation and inferred dependency remain distinguishable. A source entity can map to several product capabilities; one capability can span several repositories.

## Layer 3 — obligations and analysis

Apply accepted predicates: reachable required feature; public behavior documented; actual consumer source resolves; negative test produces failure; covered denominator meets floor; state survives migration; private evidence not published. Produce dissatisfaction and research hypotheses with uncertainty. LLM semantic interpretation proposes explanations; it does not override deterministic facts or accept its own authority.

## Layer 4 — bounded work

Convert accepted dissatisfaction into a task with parent outcome, required inputs, allowed changes, relevant oracles, affected consumers and rollback. The work graph is not the product model. Work can complete and disappear from active scheduling while the persistent capability remains.

## Layer 5 — human and agent projections

Render concise context packets, nested maps, comparison tables, specs, task views, CI verdicts and release notes from the same IDs. Scaled graph navigation expands only a bounded neighborhood or aggregate, with source-linked drilldown. A command-line query must expose the same semantics as the GUI without requiring a graphical session.

## Recursive composition

An applet combines domain logic, ports, adapters, state/permissions, lifecycle, surfaces and children. A composite applet can expose a smaller public boundary upward. Composition does not imply copying child state or dissolving trust boundaries. Direct function calls are preferable for qualified same-process paths; network/process/Wasm adapters require explicit overhead and isolation justification. Avoid automatic protocol promotion at every recursive level.

## Revision 1.1 — ecosystem-wide consumer impact

[Continuous ecosystem-first evolution](architecture/ECOSYSTEM-FIRST-EVOLUTION.md) applies to design, implementation, verification and delivery. External and owned reuse are both considered before handrolling. Current and committed consumers determine compatible behavior; plausible future consumers guide inexpensive seams, not speculative mandatory dependencies. Capability owners, adapters, consumer versions, cross-repo rollout and aggregate maintenance effects belong in each material change record. The repository write boundary does not narrow reasoning or expand authority. The proposed impact shape is `schemas/ecosystem-impact.schema.json`; it is structural evidence, not an approval or proof of parity.

## Revision 1.3 — reciprocal application composition

[The federation amendment](federation/README.md) extends recursive applets into independently useful, automatically discoverable, host-relative applications. Installation, binding, service instance, UI perspective and data authority are separate. App Center is optional; no implicit permission/data/source merge is allowed. Native/host-specific lowering and qualified lifecycle replace a universal embedding promise. New proposed requirements are FED-01-01 through FED-07-08, linked through SPEC-12, ADR-014 and WP-FED-01 through WP-FED-12. Actual product evidence remains absent until executed by the authorized owners.
