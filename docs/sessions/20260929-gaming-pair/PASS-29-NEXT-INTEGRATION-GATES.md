# Pass 29 — next integration gates locked

Date 2026-09-30. Exactly Dino + Civis.

Dino pure GenerationStore implementation candidate is green on candidate e267db309f4ca0cbc3bdef41d93741afa60a48d9, run36715187076:4/4 passed, artifact11096300343 sha256 b43844c7314a57c7bb76b9ec99c047450b0ad6f63d93c4bf50b4be7c38ff2c6f. Materialized BuildMenu/Aerial adapters remain RESTART_REQUIRED. Spec gate ce29ad861f70cbf42feb37ef7d1c9662bdfbe32a requires GameInstalled=true proof for actual lookup/materialized consumers before ModPlatform coordination. Quality comparer cleanup rerun36715950526 queued.

Civis implementation candidate now includes compatibility-first SemanticSaveAdapter but default CivSaveBundle remains untouched. Spec gate419cb988bfae6d30f0eefacba0a93662f90c6d3f defines an opt-in vNext bridge with outer classification, mod resolution before guest memory, staged generation publication, v5 preservation and fault injection. Dedicated candidate run36715965888 queued.

No implementation candidate may merge solely from isolated candidate greens.
