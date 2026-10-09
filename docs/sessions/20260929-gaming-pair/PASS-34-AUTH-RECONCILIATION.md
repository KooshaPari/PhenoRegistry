# Pass 34 — authorization and interrupted-publication reconciliation

Date 2026-09-30. Exactly Dino + Civis.

## Dino PR491

Host-independent path seam now has conservative authorization:
- PackRootResolver chooses/canonicalizes requested vs configured root.
- PackRootPolicy by default permits configured root or descendants only.
- override outside configured root is rejected unless an explicit future policy enables it.

This prevents fixing reloadPacks(path) by accidentally granting arbitrary filesystem pack-root selection. Host/runtime still must wire resolved authorized root into ModPlatform shared loading and receipt.

Candidate50d677b8b1074a4b27f12374cd9b252b14d9b83f run36717763618 in progress.

## Civis PR1569

SemanticGenerationPublisher now has reconciliation semantics for interrupted pre-publication intent:
- orphan CURRENT.next is discarded, never auto-promoted;
- CURRENT remains prior accepted generation;
- staged candidate remains inspectable;
- CURRENT pointing to an invalid generation is an explicit reconciliation error.

This chooses a conservative authority rule: a durable intent file is not proof publication completed. Cross-platform fsync/rename durability remains unproven.

Candidate b8b99f9814fe8aa0401cf55c9735874829cf503d run36717765574 queued.

No third product; no default-path replacement or merge authorization.
