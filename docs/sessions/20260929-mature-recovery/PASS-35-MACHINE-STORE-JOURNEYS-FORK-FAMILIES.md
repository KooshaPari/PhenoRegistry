# Pass 35 — executable store contract, machine journeys, fork-family classification

Date 2026-09-30.

## PhenoMLX
Profile-store semantic tests `254785131c20b3e7ad55eb675af092d0223b6a1c`.

Tests now encode idempotent identical append, conflicting duplicate rejection, support withdrawal without profile mutation, stale capacity and qualification correction via new record. This is still spec-branch/static evidence, not a production store.

## PhenoLab
Machine journey graph `c24d344a0e525d85031d0c0cffd30a6d549aec55`.
Minimal CVP interaction contract `ee4caff0fc97ce6e50d4ff66829f8b421a97e946`.
Current journey map from prior pass shows none of UJ-01..09 fully closed.

CVP can use CLI/TUI/small web/API; visual polish is not the gate. Reviewer must create experiment, inspect durable state/candidate/evidence, compare, decide and resume after worker loss without reading raw JSON/chat.

## Portage
Major fork-family classification `6ec75a3b68babced22fc3734fb0e897140499c0d`.

Frozen tree confirms:
- benchmark_adapters: 895 files;
- adapters/coding: 263;
- adapters/reasoning: 207;
- src/portage: 12;
- src/helios_bench: 15;
- packages/harbor-pheno: 20;
- crates/portage-trial: 11.

Many benchmark identities appear in both benchmark_adapters/ and adapters/, suggesting migration/generated duplication; do not count both as independent breadth.

src/helios_bench and harbor-pheno are now explicitly subject to relation typing: co-location does not make them Portage mature capabilities.

The likely Portage core remains small while adapter breadth may be a compatibility catalog around it.

## Source denominator
No CLOSED change. Each pass is narrowing uncertainty, but production/native/caller evidence remains required.

Next:
1. normalize Portage adapter identity/duplication ledger;
2. produce PhenoLab CVP resource/state machine and usability oracle fixtures;
3. map PhenoMLX store contract to VS-01 schema/trace and determine minimal implementation work package;
4. await native evidence.
