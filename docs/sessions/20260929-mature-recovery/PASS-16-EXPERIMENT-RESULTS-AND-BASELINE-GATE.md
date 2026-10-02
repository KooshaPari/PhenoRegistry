# Pass 16 — architecture experiment results + baseline gate

Date 2026-09-30.

The previous turn's bounded architecture packages now have self-contained semantic prototypes, result ledgers and explicit baseline-readiness gates. This is substantially more than prose design, but still not native product validation.

## Portage
Experiment design `027ec1bc...`; prototype `ac9ae36...`; result ledger `be340c05...`; baseline gate `25a1a0af...`.

Static prototype passes compound subject identity change and fail-closed required artifact/criterion semantics without replacing Harbor core. Direct source also shows TrialConfig already carries many subject inputs, making a thin canonical projection plausible.

Native integration remains blocked/unrun. Baseline blockers include Harbor hook experiment, install authority, semantic fork delta, exact envelope/export schema, native oracles and residual source coverage.

## PhenoMLX
Design `ec220a78...`; profile prototype `a0699024...`; result ledger `91d50d83...`; baseline gate `e1a034c9...`.

Current repo already has six engine adapters. Static prototype proves requested-vs-realized fallback, runtime generation and explicit unknown observability can be represented above them. This supports the typed-profile hypothesis without validating real cross-engine value.

Real two-engine run, lifecycle/admission evidence, source-of-truth consumer validation and exact engine/version/license matrix remain blockers.

## PhenoLab
Design `376458be...`; identity prototype `2ba6e3fd...`; result ledger `d2929c2e...`; baseline gate `08a627c9...`.

Static prototype passes candidate identity, assignment epoch, missing-evidence and critical-gate semantics. Existing source independently supplies fail-closed garden gates, human-gated two-window promotion eligibility, risky-action policy and append ledger primitives.

Current workflows triggered for prototype head but remain failure/skipped under the known CI infrastructure problem; no native test receipt claimed.

Vertical runner→Assessment→Decision, malicious false-green, worker replacement, Tracera bridge, evaluator query budget and replicate policy remain blockers.

## Program decision

**No v0.2 baseline is promoted yet.**

However, architecture risk has materially decreased:
- Portage likely needs a thin policy/envelope layer, not a runner rewrite.
- PhenoMLX likely needs typed profile/evidence wrapping over existing adapters, not engine replacement.
- PhenoLab likely needs typed durable identities around existing garden primitives, not platform reconstruction.

Next highest-value work should implement the bounded **spec-side vertical prototypes** far enough to exercise cross-object lifecycle semantics, while remaining isolated from production behavior:
1. Portage envelope: DeliveryEvent/regrade/cancel/import lifecycle.
2. PhenoMLX envelope: support/admission/stream/fallback lifecycle across two fake/native adapter identities.
3. PhenoLab envelope: Candidate→Assessment→Decision ledger, worker replacement and malicious grader-change rejection.

Those prototypes can falsify the v0.2 data/state models before production implementation. In parallel, close exact source-coverage blockers that do not require runtime infrastructure.

No completion percentage is defensible.
