# Pass 19 — publication, classification, and atomicity prototypes

Date 2026-09-30. Exactly Dino + Civis.

## Dino

Architecture evidence before this pass:
- production reload controls: removed content stale, repeated reload conflict, stale patch cache — all reproduced;
- fresh isolated-generation prototype: all three counterexample classes green;
- per-consumer observed-generation acknowledgement green.

This pass adds:
- digest-derived generation identity over sorted relative path + exact file bytes;
- desired-vs-active two-phase activation with ACK/NACK;
- fail-closed machine receipt exposing desired generation, active generation, FullyActive, and NACK reasons.

The intended semantics now match the local product problem and established control-plane patterns: a candidate can be desired without being fully active; a required consumer NACK keeps the prior active generation authoritative.

Current prototype head: `31d0ab8a6d673a57d45baac5bcaff2440e8df3e3`; recovery run `36700623226` queued at receipt.

## Civis

Architecture evidence before this pass:
- six production reds: economy PolicyInput, research, loaded-mod identity, control-policy kind, market state, metadata-downgrade classifier;
- semantic manifest prototype green for policy/research/orphan detection.

This pass adds:
- semantic manifest support for control-policy kind and market prices;
- fail-closed semantic schema validation;
- deserialization failure on missing required semantic component;
- rejection of unsupported future semantic schema;
- outer format classifier distinguishing explicit metadata, metadata-less legacy candidate, and suspicious metadata-deleted modern component set;
- immutable save-generation staging + CURRENT pointer prototype:
  - failed staged candidate must not replace current accepted generation;
  - successful commit switches CURRENT while preserving prior generation directory.

The pointer prototype reduces the multi-component commit problem to publishing one small generation reference after the staged save has been fully built and validated. Real cross-platform durability/fsync/rename semantics remain an implementation-specific experiment; this test does not assert that a plain remove+rename sequence is crash-proof on every filesystem.

Current prototype head: `70a918d8506464f2bf9290d70b176e00aafc678c`; recovery run `36700592823` queued at receipt.

## Targeted prior art

Pass18 records primary-source research:
- Envoy xDS version ACK/NACK;
- Nix immutable generations/rollback;
- Kubernetes desired vs observed generation / ownership;
- SQLite atomic commit and recovery boundary;
- TUF consistent snapshots/version rollback resistance;
- Cap'n Proto explicit schema evolution.

These are conceptual bootstrap sources, not dependencies or claims of product equivalence.
