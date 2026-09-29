# Khostty internal archaeology — pass 1

Source date 2026-09-29. Product baseline `a29aa9c6553d9f42aa68e2919116c0f6d53f329d`; registry baseline `85d7cd00cf59c379c05b740e8130a85b0d5bd31b`.

## Alias and lineage map

| Alias / concept | Evidence / authority | Search disposition |
|---|---|---|
| Khostty / khostty | Current repository identity, deterministic GitHub metadata | Exact repository resolved; source and branch frozen |
| phenotype-khostty | README working-name assertion | Targeted context search did not recover product-specific user intent; history search incomplete |
| Ghostty fork / owned terminal runtime | README description; GitHub parent/source ghostty-org/ghostty | Parent metadata verified; exact upstream merge-base and fork delta not recovered |
| 1jehuang/khostty | README clone URL | Unverified predecessor/clone-reference lead, not proven Git parent; search independently next |
| agent IPC / pane Host / AppHost | Protocol and actual implementation | Fork-inclusive REST code search returned source, protocol and deep WBS; real runtime mounting unresolved |
| native Windows terminal / embedding / libvt / FFI | README roadmap and build instructions | General prior ecosystem conversation not attributable to this product; recover originating decision |

A zero-result generic code search was falsified by a fork-inclusive search returning the known files. Subsequent archaeology must include forks explicitly. No deleted repository or alternate owner is assumed from a name similarity.

## Authority ledger

Current user's September 29 mission: USER INTENT for process, scope limited to these two products. README owned-runtime/embedded-consumer scope: imported repository assertion, not independently recovered user approval. Protocol v1: candidate normative design within its stated scope, still requiring authority and conflict reconciliation. app_host/server/pane bodies: CURRENT IMPLEMENTATION facts at the frozen revision, not proof of execution. General earlier terminal/FFI suggestions: ASSISTANT SUGGESTION or unattributed ecosystem discussion until linked; do not promote to Khostty intent.

## Source anchors and inspected extent

Prefix: https://github.com/KooshaPari/Khostty/blob/a29aa9c6553d9f42aa68e2919116c0f6d53f329d/

- README.md: primary fork capability narrative; long tail not certified fully inspected.
- AGENTS.md: inherited build guidance; conflicting instructions against the user's explicitly authorized PR work are not followed.
- src/apprt/ipc/protocol.md, lines 1–290, blob d04ccbbd3d222b0c12602ea58df2647a48be371e: VT injection intentionally differs from PTY input; AppHost not yet in build graph.
- src/apprt/ipc/app_host.zig, lines 1–460, blob 282d0df2b969ce46b401201fd6b408e8009c4820: GTK-only real host; unsupported focus/search; unfinished app-thread integration; create options and request attribution unresolved.
- src/apprt/ipc/server.zig 1–260 and pane.zig 1–240: bounded module reads, not complete lifetime/security proof.
- docs/sessions/20260916-fork-assessment/02_DEEP_WBS.md: discovered, unread.

Registry STATE: https://github.com/KooshaPari/PhenoRegistry/blob/85d7cd00cf59c379c05b740e8130a85b0d5bd31b/docs/governance/atlas/products/Khostty/STATE.md . It sampled a September 16 state at 79e27b63f96669b26f1346a1b9985c327311bd6e and explicitly had bounded inspection. Other atlas records and handbook mirrors remain to review/deduplicate.

## Falsification results and boundaries

Falsified: README clone URL proves Git parent; empty wrapper search proves file absence; VT write necessarily means typing into child; historical registry snapshot is current implementation truth. Not established: complete native IPC mounting, Windows GUI usability, broad security/recovery, embedding ABI quality, or whether a full fork is justified. The source commit repaired historical CI ecosystem skips; current expected-job coverage still needs execution evidence.

The product-local SOURCE-COVERAGE-LEDGER is authoritative for coverage status. All alias/history families remain open; this pass has not exhausted useful Git history, deleted concepts or primary conversation authority.
