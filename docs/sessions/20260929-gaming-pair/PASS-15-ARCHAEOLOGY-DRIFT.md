# Pass 15 — prior-conversation archaeology and source drift

Date2026-09-30. Program remains exactly Dino + Civis.

## Recovered user-intent chronology

Dino:
- Mar8 user intent: reusable libraries of assets/code/tools/knowledge/transformation recipes; adapt existing permitted assets before generating from scratch; provenance/licensing required.
- Mar10 explicit user correction: framework-first, expand beyond warfare to full DINO modding; development fully agent-driven with human reporting build/launch/in-game failures.
- Mar12: Star Wars/DINO project personal-only for now; machine-friendly CLI/API asset workflows preferred; browser automation last resort.
- Older assistant-generated Foundation Spec and later deterministic-runner ideas remain proposals unless corroborated.

Civis:
- Feb19 explicit user horizon: combine Cities: Skylines, WorldBox, DINO, Civ7 and Empire at War patterns with deep politics/governance, public/private competition, war/defense, deep economics, hybrid crowd+agent simulation and macro/detail zooms.
- February assistant multi-resolution/conservation architecture is supporting design evidence, but its deterministic seeded replay proposal is superseded by the accepted May no-global-bit-replay charter/ADR.

This chronology prevents current implementation defects from shrinking product identity and prevents old assistant architecture from being promoted into user intent.

## Current source drift

Dino main remains exactly frozen snapshot `17119051e782b32615413049c1c3cd207f0b540e`.

Civis main is now `590fad0643eb85cae89edd9e64ed6b991461de6e`, exactly one commit ahead of previously targeted concurrent source `54d5758970249c8d1f24688ea45920b530e77299`. Compare shows the only changed file is added `docs/audits/spec-only-triage-2026-09-29.md` (+339). No production code changed between those two revisions, so the reproduced persistence behaviors remain code-relevant to current main, while the new audit document becomes an additional source-ledger input rather than silently rebinding test candidate identity.
