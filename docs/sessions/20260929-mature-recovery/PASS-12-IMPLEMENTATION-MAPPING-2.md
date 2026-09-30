# Pass 12 — second implementation mapping

Date 2026-09-30.

Goal: distinguish reusable implementation, clean delegation, unreachable/partial behavior and true semantic gaps.

## PhenoLab correction: materially less greenfield

Direct source mapping found reusable mature-policy primitives outside the RLVR-AF tournament slice:

- `harness/self_improvement/gates.py`: required holdout/regression/safety/budget/reproducibility/serving-stability gates; missing required metric becomes not_evaluated and overall red.
- `promotion.py`: two consecutive green windows + explicit human approval; intentionally non-mutating.
- `scripts/gardener.py`: append-written garden ledger with git/component/model/provider/suite/metrics/gate/rollback fields.
- `retention.py`: non-destructive retention preview.
- `verifier/risky_action.py`: pre-execution command risk/blocklist/secret/path/dry-run/verifier/human approval gate.
- dataset loader: HF revision/source metadata, though omitted revision defaults to mutable main.
- Terminal-Bench manifest: suite/subset/task manifest hashes and explicit scoreable=false / verification_status=not_run.

These are reusable primitives, not completed mature identities. Genuine gaps remain typed subject/candidate/assignment epochs, independent Assessment, evaluator roles/query budgets, environment epochs, replicate statistics, durable authorized Decision/PromotionRecord, observation window and imported authority.

PhenoLab receipt `038e361a6233fa4228c9762bec7d8b8359bfd925`.

## Portage

Current direct evidence still supports a thin-layer hypothesis. Generic task/verifier/artifact/trajectory/regrade mechanisms should be delegated upstream where current Harbor satisfies them.

Likely genuine Portage semantic gaps remain subject identity, strict required-evidence envelope, authority/lifecycle/idempotency/dependency/criterion/import semantics and stable authority-preserving consumer export. But connector search is demonstrably sparse for known Harbor symbols, so these are **mapping gaps, not confirmed absent code** until direct file/tree traversal.

Receipt `f5441b17f6107a432b628636bcded0f38d51a81c`.

## PhenoMLX

Verified current pieces remain launcher/external app integration, web invocation defect, historical/profile benchmark evidence, custom extensions and old capacity concepts. Mature engine internals should be delegated to MLX-LM/oMLX/vLLM/SGLang/TRT-LLM/llama.cpp unless measured deficiency.

Likely genuine product-layer gaps are typed requested/realized profile, runtime generation, topology, cache domain/state-store identity, observability level, support lifecycle, stream terminal semantics, capacity/admission and dynamic operating state. Search limitations prevent treating generic-term absence as code absence.

Receipt `696528934b74461ab4f353959b86a30f8e228ebb`.

## Program consequence

Do not generate implementation WPs yet.

Next:
1. direct file/tree mapping for Portage Harbor job/trial/artifact/regrade/export models;
2. direct file/tree mapping for PhenoMLX backend/cockpit/request lifecycle/evidence schemas;
3. PhenoLab reconcile existing garden primitives into the v1 trace graph and test whether a thin typed identity layer can close CVP rather than a rewrite;
4. only then consolidate obligations v0+v1 into candidate mature contract v0.1 and run another adversarial review.

No CVP is closed and no percentage is assigned.
