# Synthetic, non-production examples

The Podman and WSLC capability examples are deliberately **unqualified**. Their null versions and empty evidence do not describe observed user hosts and cannot authorize placement. JSON Schema only validates record shape, not the truth of capability claims.

`plan-request.unqualified.json` is a synthetic data-shape example for the proposed control API. Its zero/example hashes and placeholder revisions are not valid deployable provenance. Passing the schema is not a promotion decision.

`schedule-two-commits.json` is synthetic input to the pure scheduling reference. Its `target_qualified` flag is a test assumption, not a host observation. The result remains `authorizes_deployment: false` and cannot advance a watermark.

Reconcile these schemas with the existing specification/type authorities before implementation. No runtime credentials, approval tokens, installation commands or live endpoints are supplied.
