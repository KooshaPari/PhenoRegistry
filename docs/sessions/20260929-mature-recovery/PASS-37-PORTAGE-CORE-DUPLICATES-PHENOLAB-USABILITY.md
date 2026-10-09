# Pass 37 — Portage core correction, adapter duplicates, PhenoLab usability

Date 2026-09-30.

## Portage current core correction

Direct source inspection found the contributor tour explicitly says:
"src/harbor/ holds the runtime; src/portage/ is a back-compat shim."

Semantic map `a0b7d86c918681047ac7a12cd9f6ae525f3e604f`.

This falsifies the shortcut that src/portage must be the mature core because of its name. Current modules include placeholder CLI/status/query/serve, a parallel distributed target manager, a basic SQLite run ledger, scalar RL tracking and generic utility API. Plugin/extension seams may survive; generic run/distributed/tracking should reuse Harbor or retire after caller checks.

This is implementation evidence, not direct user intent, but it aligns strongly with the mature thin-envelope hypothesis.

## Adapter duplicate comparison

Receipt `23bbc5089b33ea68c1d52eda3f8fec15d9ba7e41`.

Representative same-name pairs:
- gpqa-diamond: blob-identical adapter.py;
- dabstep: blob-identical;
- crustbench: blob-identical;
- aider_polyglot: divergent but related;
- bfcl: divergent but related.

Therefore duplicate trees mix exact mirrors and evolved variants. Whole-tree deletion is unsafe; normalization must occur per benchmark identity.

## PhenoLab usability

Actor-facing CVP oracles `02e9ede188ac1ecad42ab39d3768e57de0f89da6`.

Controls now require a reviewer without worker chat to:
- create valid experiment;
- understand blocked candidate/evidence;
- traverse provenance;
- see uncertainty without forced winner;
- record authorized Decision;
- recover after worker death;
- retrieve negative learning;
- distinguish infrastructure from candidate failure.

Pure R&D experiments remain valid without application.

## Denominator
Portage semantic fork understanding materially improved but callers still block closure. PhenoLab usability is specified, not implemented. No CLOSED numerator change.

Next:
1. systematic per-benchmark duplicate classification sample/automation design;
2. direct caller search for src/portage plugin/run/tracking surfaces;
3. machine usability journey acceptance map;
4. PhenoMLX profile-store work unit awaits developer implementation/native evidence.
