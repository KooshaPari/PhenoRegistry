# Pass 39 — first real Civis integration semantic red

Date 2026-09-30. Exactly Dino + Civis.

Dino remains frozen and ready for game-host handoff.

Civis candidate88b350f45202e6473b655baad76bbd0691d8a1ab run36749851118 is the first clean execution of the full semantic lib-only candidate graph:
-17 tests executed;
-16 passed;
-1 failed;
- artifact11113549494 sha256 f0a1e39ec15577a5342a78205609c8d58d4c8579bd7ac625ead39a5a56a692bf.

Real semantic failure: `semantic_save_adapter_surfaces_orphan_guest_memory_before_apply` expected missing-mod to be rejected but compatibility returned Ok. Root cause: SemanticStateManifest persisted active_mods but not ownership IDs of saved guest-memory blobs; validation queried the resolved environment's guest memory, which is naturally empty before import. Thus it had no saved namespace to compare against resolved active mods.

Repair changes the model rather than the test:
- semantic manifest persists sorted/deduped `guest_memory_mod_ids` from the save;
- compatibility compares those saved owner IDs against the resolved ModHost active IDs before guest-memory import;
- existing prototype helper still checks saved guest owners against saved active-mod declaration.

Repair commits5418426496edf1e03b388c431497f28081dd16a7 / eb1e9aa02979dd4e88e94ad0eeb08d85b50a5f9a; exact rerun candidate1d6a3182b44c013d4ea66191e9e0fd6540e4b881 pending.

Civis handoff remains conditional until rerun.
