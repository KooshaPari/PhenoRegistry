# Pass 33 — host-independent subject selection and staged save publication

Date 2026-09-30. Exactly Dino + Civis.

## Dino PR491

Latest admitted candidate1c177fe7125ce4439335be3e0a60c3a9517a50de run36716747784 is green and includes receipt representational fields.

A CI-safe PackRootResolver now isolates subject selection before ModPlatform integration:
- requested nonblank root wins;
- absent request uses configured root;
- selected root is canonicalized with Path.GetFullPath.

Tests bind this independently of the licensed host. This does not yet authorize arbitrary paths; allow/authorization policy remains a separate security/product decision.

Head dbec01050f1fc86597f39fa96bee169bb142a7b2 run36717315715 queued.

## Civis PR1569

Candidate now includes SemanticGenerationPublisher around the opt-in bridge:
- generations/<id>/ contains staged bundle + semantic-state + GENERATION identity;
- validate required semantic component and generation identity before publication;
- CURRENT.next is written then renamed to CURRENT last;
- prior generation directories remain preserved.

Fault controls:
- remove required semantic-state from staged g2 -> commit fails, CURRENT remains g1;
- corrupt GENERATION identity -> commit fails, CURRENT remains g1;
- valid g2 -> CURRENT switches to g2 while g1/g2 remain present.

This is host-independent transaction-shape evidence only. Cross-platform atomic rename/durability/fsync/crash behavior remains open and must be tested on target filesystems before production acceptance.

Head42576d7d7686b8e659b8aece308a19cacc87857c run36717376922 queued.

No third product.
