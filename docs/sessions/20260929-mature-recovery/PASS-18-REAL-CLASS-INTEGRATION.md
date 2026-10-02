# Pass 18 — real-class integration

Date 2026-09-30.

The architecture prototypes now bind to real existing implementation classes/primitives rather than only isolated state models.

## Portage

Integration commit `caf4f9d63981f157882c348c9ee98c84eee2c4a1`; review `bb26d363d4b4d40e9a212e5d2ea636c4318265ec`; contract delta `15fa0bc7b07f1a4bdcd21b80400bfd603ff3372c`.

Prototype imports actual Harbor TrialConfig/AgentConfig/TaskConfig/ArtifactManifest classes. Native skill changes alter subject projection; failed/skipped required artifact blocks acceptance.

New falsification/correction: Harbor intentionally redacts sensitive env serialization, so public subject config identity cannot uniquely identify behaviorally relevant credential/account bindings. Portage contract adds SecretBindingSet as opaque IAM/secrets references/version/scope, never raw secret material.

This is the only new ontology-level correction from real-class integration.

## PhenoMLX

Integration `3d90a41366a340fe62a67b6281d2c599c6212db2`; review `c02aca9031ebc3495ef5df2ba83953a9f7799b92`.

Prototype imports actual LlamaCppBackend and VllmBackend without model load. Their real static capabilities differ (e.g. spec-decode declaration), and requested-vs-realized fallback/unknown engine version can be represented above them.

No new identity needed. Important authority rule: BackendCapabilities are deterministic source declarations, not verified runtime qualification. SupportEnvelope must preserve that evidence/authority state.

## PhenoLab

Integration `feeea2ccc7887f18752e0be8591ea594b2762a7a`; review `d11e33acaeed218e509272ff2471e4219174f0b2`.

Prototype imports actual evaluate_gates and promotion_decision. Missing required safety input is red; red+green cannot promote despite human approval; two green+human approval becomes eligible but non-mutating; no-human remains hold.

This directly validates the v0.3 Assessment→Decision architecture against existing garden policy primitives. Remaining need is typed/provenance-bound inputs and durable records, not gate redesign.

## CI status

Portage integration head triggered fresh workflows; they were queued at query time with policy-gate already failed. PhenoMLX/PhenoLab returned no commit-associated workflow receipts at query time. No native green claimed.

## Baseline decision

Still **NO baseline promotion**.

Real-class integration materially strengthens all three architecture hypotheses, but blockers remain:
- Portage: native integration execution, exact envelope/export/secret-binding schema, existence/fork/package gates.
- PhenoMLX: real two-engine/model qualification, lifecycle/admission evidence, consumer/source-of-truth validation.
- PhenoLab: real runner + typed persistence + candidate provenance + worker replacement + malicious grader attack + Tracera bridge.

Next work should push one level further into **vertical persistence/execution contracts** and close source-coverage/security/release boundaries, not return to broad conceptual research.
