# Pass 14 — consolidated-contract architecture attack

Date 2026-09-30.

All three mature-contract v0.1 candidates were reconciled against current obligations/journeys and attacked with materially different architectures. None is promoted to baseline yet. Each now has v0.2.

## Portage

v0.1 admitted broad fork, plugin, external gateway, schema/library and product-absence alternatives. This is good implementation neutrality. Broad fork is not justified by current evidence.

v0.2 makes package/service/library deployment neutral, explicit criterion aggregation, delivery/retry/cancellation lifecycle and evidence-retention/regrade interaction. Existence requires reusable compound-subject/evidence value beyond simply moving PhenoLab logic.

Review `7a408b0582146d23eef76129e6815c783a9d9586`; v0.2 `494e6a57f3df7e3b3073590f45b99acc54259d9a`.

## PhenoMLX

Alternatives included universal engine, typed adapter/control layer, qualification-only registry, routing-owned profiles, product absence and hardware-registry+engine composition. Universal engine is not preferred; typed composition remains strongest.

The key blocker is source-of-truth duplication. v0.2 now proposes:
- hwledger owns reusable hardware/device capability observations;
- engine adapters own engine-native facts;
- PhenoMLX composes LLM runtime profile/qualification/support truth;
- routing systems consume that truth rather than silently redefining it;
- Portage can evaluate profiles but does not own profile support truth.

This boundary is a candidate architecture and must be validated against actual consumers/registry decisions.

Review `dc70edf8a3549bca8f0097416ed5fe90ecb7d75d`; v0.2 `6c47d3fd7c5662f810474f943e24ea7001e74dcc`.

## PhenoLab / PhenoLM

Alternatives included monolith, typed control plane, Tracera-owned canonical product state, CI/GitHub as ledger, generic platform+GEPA/no product and event-sourced library.

v0.2 adopts a cleaner candidate boundary consistent with prior ecosystem architecture: PhenoLab/PhenoLM owns **experimental truth**; Tracera remains canonical product/system truth where the target is Tracera-managed. PromotionRecord bridges authorized experiment evidence/Decision to accepted product state rather than duplicating it. Self-contained non-Tracera targets can apply decisions directly with explicit authority.

Existing garden/risky-action/gate primitives are explicitly reused.

Review `62372ac10be3ad8858b02843ec4a8e2c3427e5be`; v0.2 `b2d6565b7c01146c999a366286255c68fb05805d`.

## Baseline gate

No v0.2 is accepted yet.

Next highest-value work is **architecture experiments**, not another prose-only revision:
1. Portage — prove stock Harbor + thin extension/gateway can or cannot carry compound subject + fail-closed evidence/export semantics.
2. PhenoMLX — two-engine typed-profile experiment with matched evidence and explicit unsupported/not-observable fields.
3. PhenoLab — one vertical typed Candidate→runner→existing gates→Assessment→Decision→durable record composition, including malicious false-green and worker replacement.

In parallel, reconcile v0.2 against source coverage and expand semantic obligations only when experiment findings require it.

No implementation program beyond bounded architecture experiments is authorized by these drafts.
