# Tracera Pass 10 — Candidate identity and compatibility-certificate checkpoint

**Status:** research architecture evidence; not product verification.

## Executed reference cases

The research-only candidate/certificate model exercised 10 scoped cases; all 10 matched expected decisions.

Negative controls covered:
- certificate operation mismatch;
- criterion revision mismatch;
- untrusted certificate issuer;
- revoked certificate;
- changed dependency lock;
- changed feature flag;
- changed environment.

All seven negative cases deliberately retained the same source commit. A source-commit-only reuse rule would therefore falsely reuse evidence in **7/7 negative seed cases**.

A changed artifact digest was intentionally reusable in one case because the criterion's declared dependency footprint excluded the artifact itself and all relevant dependencies remained identical. This demonstrates the intended principle: candidate equality is criterion-dependent, not universally full-candidate equality.

## Proposed invariants

1. Same Git/source revision is not candidate equivalence.
2. Each criterion declares the candidate/configuration dimensions capable of affecting its result.
3. Evidence may cross a changed dimension only through an admitted compatibility proof scoped to that criterion revision and operation/surface.
4. Compatibility is directional.
5. Compatibility is non-transitive by default.
6. Omitted certificate scope is not wildcard.
7. Untrusted, expired or revoked certificates cannot authorize new reuse.
8. Historical evidence/certificates remain queryable after expiry/revocation.
9. A criterion revision creates a new proof obligation unless explicit compatibility is established.
10. Certificate authority is itself evidence-bearing and cannot be established by the worker merely asserting an issuer name.

## Remaining attacks

The seed model does not yet prove:
- certificate-chain composition;
- operation-set hierarchy;
- certificate revocation fanout;
- dependency-footprint derivation correctness;
- impact-analysis false negatives;
- cryptographic issuer authentication;
- candidate equivalence for generated artifacts/toolchains;
- real Tracera runtime behavior.

## Architecture consequence

The mature evidence key should not be one giant exact candidate tuple for every criterion, nor merely a source commit.

Use:
- exact evaluation/candidate identity for provenance;
- criterion-specific dependency footprint for reuse reasoning;
- scoped compatibility certificates for justified changed dimensions;
- suspect/invalidation propagation when any dependency or certificate changes.

This preserves exact history while allowing safe reuse to be more selective than full configuration equality.

No product completion percentage follows from this checkpoint.
