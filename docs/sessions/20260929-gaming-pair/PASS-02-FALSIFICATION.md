# Pass 2 — falsification receipts

Date 2026-09-29. Program `gaming-pair-20260929`. Exactly Dino and Civis remain the product scope.

## Dino

Product-local commit `1f22a8c0209d8d6aefce603f9fd706eedaec9e9f` adds `PASS-02-ACTIVATION-TRANSACTION.md`.

The initial null-schema finding was narrowed: RegistryImportService skips schema validation when the runtime passes null, but every inspected core registration path calls `JsonGuard.ValidateOrThrow`, and current source searches show the principal registered models implement `IValidatable`. Therefore the live question is schema/semantic parity by content type and ingress, not "no runtime validation."

A stronger architecture issue survived source attack: registration mutates entries incrementally, LoadPacksImpl continues downstream runtime initialization/application when aggregate load has errors, and HotReloadBridge explicitly applies partial updates after a failed reload when UpdatedEntries is nonempty. The mature design must choose transactional activation or define partial activation precisely; implicit partial state is not adequate for reliable automation.

## Civis

Product-local pass2 was first committed at `3f3efd60a272596a40a4e8f61f295ccf0467d680` and then corrected at `1b5e776ceff19c22069fe625dcbfc892ed0272de` after deeper caller tracing.

The first pass2 hypothesis — a normal Save/Load click might mutate both local and server worlds — was **falsified**. SimBridgePlugin intentionally creates SimState only outside Server attach mode, with unit tests for that invariant; LiveAttachPlugin inserts ServerBridge in Server mode. This is evidence of a sound intended single-authority split.

The replacement finding is more concrete: SaveLoadUiPlugin disables Save As/Load/Delete based on `has_local_sim`. In normal Server mode SimState is intentionally absent, so the UI prevents reaching its own remote `save.slot`/load RPC branch. Remote save/load needs server-capability/connection gating and server acknowledgement rather than local-simulation gating.

A separate source-level race survived: autosave obtains `tick_for_filename` under one simulation lock, releases it, then reacquires and writes/records `tick_at_write`. The simulation can advance between acquisitions, making the tick-encoded filename disagree with archive/DB/event identity. This needs a single snapshot/identity boundary.

Filesystem archive and metadata DB authority also remains unresolved: archive write precedes DB insertion; eviction can update metadata then fail to delete the file. Recovery/reconciliation semantics must be explicit.

Concurrent engine source also contains explicit compile-recovery placeholder/stub declarations. They are transition debt, not evidence that the whole engine is a stub and not mature-product credit merely because the workspace compiles.

## Method consequence

These corrections are the intended behavior of the program: each candidate interpretation is attacked by tracing actual composition and callers. Falsified findings are replaced, not accumulated. No requirement count or progress percentage is generated from the number of findings.

Native experiments remain outstanding; source-level findings do not receive runtime/product acceptance credit.
