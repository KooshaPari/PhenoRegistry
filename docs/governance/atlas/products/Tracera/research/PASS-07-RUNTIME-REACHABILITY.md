# Tracera Research Pass 07 — Runtime Reachability Receipt

**Status:** incomplete; source-backed static reachability review.  
**Tracera commit:** `b8d3095c243e95ee21f3e147d5d7567841ee0492`

## Findings promoted from static review

1. Product query helpers appear unmounted outside their own tests/re-exports. The ignored `ProductQuery.product_id` is therefore a latent contract defect, not currently proven runtime leakage.
2. `AssessmentEngine::assess_product` scopes once, then passes the entire observation slice into capability assessment and derives baseline/count globally.
3. Product and capability identities are conflated in assessment despite `Observation.capability_id` existing separately.
4. Explicit fresh `Unknown`/`Stale` observation results can fall through to `Satisfied` because assessment does not exhaustively match all result variants.
5. Product tables exist in SQLite/Postgres migrations, but static search did not find product-node/edge store CRUD or mounted handlers. `ObservationStore` is in-memory.
6. `PageDecompositionView` implements the historically important Site→Page→Layout→Section→Component→Element projection, but static search finds no live consumer beyond tests. Several named tests are shallow render assertions.

## Interpretation

The current product layer is not "nothing": identity/baseline/observation/assessment/detector/query/traversal primitives, persistence schema, and an experience-decomposition component exist.

It is also not yet evidenced as a closed product journey. The most efficient next architecture move is to verticalize one canonical product-truth path rather than add more disconnected breadth.

## Required next witness

Use two products and two capabilities with deliberately overlapping local names, different baselines, contradictory evidence, and a fixed evaluation time. The selected mounted API/UI path must prove:
- product/capability isolation;
- exact baseline/configuration binding;
- Unknown/Stale/Inconclusive cannot green;
- persistence across restart;
- bounded query;
- UI/machine semantic parity;
- work completion alone does not change product acceptance.

No completion percentage is derived from this receipt.
