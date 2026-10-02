# Pass 19 — vertical persistence/execution contracts

Date 2026-09-30.

The v0.3 architecture models have now crossed another boundary: typed records survive serialization/restart in spec-side prototypes, and PhenoLab directly exercises grader-policy mutation as a separate epoch.

## Portage
Prototype `4d74bb773bf485e155cd72ba6b72ba382e245b55`; review `e19d74587a150edebb8cec3ed33b1369b7d4ab8a`.

Roundtrip preserves Assessment/trial/subject/reverification and opaque secret-binding refs. Retention expiry does not rewrite historical pass. Remaining store requirement: immutable/append-supersede semantics and concurrent-write safety.

Fresh workflows queued; policy-gate already failed independently. No native green claimed.

## PhenoMLX
Prototype `47bacef0e1533c606bcfe062a2f5e7edda099aa4`; review `75a1880d221495db8d803022ad8df4d3c10290cb`.

Profile generation and unknown observability survive persistence; support withdrawal is a separate versioned relation. Remaining store requirement: preserve historical profile/support relations rather than mutable latest row.

No workflow receipt returned at query time.

## PhenoLab
Prototype `dadd1c8c1e7c09bdb480637a711d40626d02fc11`; review `7753430d5d6dc872b27bf4532a63a80d680c2789`.

Candidate/Assessment survive worker replacement from append log. A weakened grader policy creates a new policy epoch; the old red Assessment remains red. Decision persists Assessment IDs and is non-mutating. Duplicate IDs are detectable.

Remaining store requirements: enforce idempotent unique append, authority/provenance on epochs, schema/hash/causal links and transactional/idempotent Decision application to target product.

Fresh workflows queued; no native green yet.

## Architecture conclusion

No state-model contradiction emerged. The candidate contracts are stabilizing under increasingly concrete prototypes.

However, baseline promotion still requires at least:
- native test execution receipts or a qualified local-equivalent execution path;
- Portage actual Harbor integration hooks/existence gate;
- PhenoMLX real two-engine/model qualification;
- PhenoLab real runner evidence + target/Tracera bridge.

Next work should now split:
A. poll/inspect the fresh CI jobs and fix only spec-branch/test-infrastructure issues that block observing these prototypes, without production semantic repair;
B. deepen the remaining real integration gates (Portage Harbor envelope over TrialResult; PhenoMLX actual availability/version/profile capture; PhenoLab real runner manifest→gate→Assessment conversion);
C. prepare a candidate-baseline review packet if native/static evidence remains consistent.

No completion percentage.
