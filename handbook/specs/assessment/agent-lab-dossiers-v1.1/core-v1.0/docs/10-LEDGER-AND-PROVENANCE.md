# Ledger and provenance contract

## Three revisions

S is the source/tree and artifacts actually evaluated. R is the later commit storing the assessment. L is the registry receipt or commit registering it. The assessment names S; a later receipt can name R and the bundle digest. Do not try to embed a future commit's own hash inside itself. Also record environment, configuration, dependency, evaluator, fixture and profile identities.

The reference assignment is byte-hashed after creation; its assessment and results bind that digest. This catches accidental or unreconciled weight/scope mutation, not an attacker who can rewrite every record and every trust anchor. The package manifest is unsigned integrity metadata, not authenticity proof.

## Event ownership

Use one immutable record per producer event or per run, or per-producer append streams with explicit reconciliation. Do not let every agent rewrite one shared JSONL file. Stable IDs and idempotency keys prevent duplicates. Compare-and-swap/fencing must be enforced by the actual storage or coordinator; putting a token in JSON is not a lock.

Preserve proposals, contradictions and rejected attempts. Canonical means designated owner and correction rules, not that every stored claim is true. Corrections supersede rather than erase. A generated report or dashboard remains a rebuildable projection.

## Delivery

An outbox contains destination label, payload digest, idempotency key, actual authority reference and PENDING/BLOCKED/DELIVERED state. A delivered state requires a receipt reference; the receipt requires independent resolution through the destination adapter. The reference kernel checks shape/state consistency only and does not send or authenticate receipts.

At-least-once delivery is safe only when the destination deduplicates. Store last error and attempt count. Replaying an outbox must not rerun a product repair. Missing central software leaves delivery pending and permits unrelated local work. Never claim a successful remote write because a local file was created.

## Time and retention

Observed time, produced time and recorded time are distinct. Causal links and trusted receipts matter when device clocks disagree. Evidence freshness includes semantic invalidators, not only a TTL. Keep historical results when they expire. Reuse requires a scoped justification and supported verifier; this kernel conservatively requires exact subject binding rather than accepting cross-subject reuse.

Keep raw private evidence in authorized storage; publish only allowed references and redactions. Content hashes can also leak sensitive correlations, so assess their publication risk. Preserve permitted metadata when raw payload retention expires. Hash chains need independently anchored roots to resist a privileged writer rewriting all history [SLSA-PROVENANCE is a provenance reference, not a proof of this implementation].
