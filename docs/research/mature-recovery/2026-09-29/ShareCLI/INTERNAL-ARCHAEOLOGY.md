# ShareCLI — internal archaeology, pass 1

Observed 2026-09-29. Product `KooshaPari/ShareCLI` ID1191459198, snapshot `4f01d0199e82b62bcf20399afcc102f58a10ad07`. Registry snapshot `85d7cd00cf59c379c05b740e8130a85b0d5bd31b`. Detailed source IDs SC-S01–13 are in the product-local source ledger. This pass has not exhausted useful history.

## Alias and lineage map

| Name / concept | Relation and authority | Evidence and search outcome | Remaining falsification |
|---|---|---|---|
| ShareCLI / sharecli | Current product/case alias | Current repository and root docs | Check old remote renames and branch roots |
| agent-harness / agent harness | February predecessor concept, not present remote identity | Accepted-marked ADR0006 and recovery map; independent registry alias search found agent-mesh-wbs-plan-v2 | Raw February conversations and vault contents; remote-restorability claim is historical, not reverified |
| harness-fuse / agent-harness fuse | Predecessor FUSE surface | ADR0006 explicitly says February included FUSE | Reproduce artifact behavior; source absent from described vault |
| core.sh / bin/harness / rules.conf / agents.conf | Historical implementation and configuration terminology | Recovery map and February plan excerpt | Independently inspect each file, parser semantics and provenance |
| Lock-Wait-Cache / coalesce / debounce / nocache / queue | Capability concepts crossing names | Functional index, IPC/core source | Complete input equivalence, mutation classification and recovery behavior |
| thegent-sharecli | March 25 process-manager twin/Python absorb stub, NOT February FUSE donor | ADR0006 and recovery notes | Read frozen restored history before treating artifacts as equivalent |
| thegent mesh substrate | Related repository donor; NOT a second canonical owner or new product workstream | Recovery note names task_queue.py/smart_merge.py/git_parallelism.py | Freeze donor SHA if source inspected; compare semantics before declaring port parity |
| agent-mesh / WorktreePool / MaildirQueue / SmartMerger | Related capability lineage; some proposed orchestration remains out of band | FR010 and registry February WBS snippet | Separate accepted mesh substrate from later consensus/blackboard proposals |
| tray / serve / harness TUI | Different user-experience eras, not interchangeable products | ADR0006 marks tray/serve current, TUI historical optional reference | Installed user journeys and parity not proven |

## Chronology supported by inspected records

The accepted-marked July 19 lineage ADR describes February agent-harness with FUSE, a March 25 orphan Git DAG for the new supervisor remote, and June 21 canonical ownership moving to ShareCLI. These are documented design/history claims; they are not evidence that the entire donor chain was recovered. The vault is described as an artifact dump, not a clone, without original FUSE Rust sources.

Commit metadata independently located `e9459ad8c223b8d2b179135f44073b3c47f4b908` (June 21, native harness absorption) and `ab700c5c1e6f181fe55efa2cc4a012f44bafd271` (July 2, FUSE scaffold). Only selected search results were inspected, not every commit or ancestry relation. June/July scaffold or test claims do not certify September behavior.

Registry atlas STATE describes September 16 PR858 compression at `19cdb88da5e79f0b06953499d51444016c07e8d2` and explicitly leaves public-surface parity unestablished. Preserve useful cleanup; absent internal references do not prove absence of public consumers. Mirrored atlas/handbook records are not independent observations.

Open PR876 reports further honest-stop, IPC spawn and bounded-read/write fixes. Treat this as an implementation-candidate lead. Its author reports the broad integration result UNKNOWN; do not import selected successful suites into main-snapshot acceptance.

## Conversation provenance

Name and concept retrieval recovered the user's September 18 request for substantive product shaping/specification work and August requests to include ShareCLI in substrate/spec research. The prior September assistant's product phrasing is **ASSISTANT_SUGGESTION**, not newly discovered USER_INTENT. A targeted agent-harness/FUSE conversation search failed technically. This is an unperformed search, not evidence that conversations never existed.

Raw historical transcript identifiers/exports, exact accepting statements for every later extension, restored twin history, complete donor vault and full current DAG remain open. Sources in the product ledger distinguish accepted-marked designs from user statements and code facts.

## First semantic attack

The current Git cache key hashes HEAD plus porcelain status, not edited file contents. Two edits can preserve that fingerprint; a source-derived local model reproduced equal keys with unequal actual command output. Queue aging casts to u8 before saturation; an old critical ticket wraps at 256 seconds in an arithmetic model. Ticket lexicographic tie ordering can prefer sequence 10 over 2. These counterexamples challenge generic safe-sharing/fairness interpretations; they are not Rust integration runs.

Do not recover an unsafe historical mechanism merely because it is historical. Recover its intended outcome, then test a safe architecture against existing alternatives. No full-coverage, migration-parity, or product-readiness claim is made.

## Primary internal pointers

- https://github.com/KooshaPari/ShareCLI/blob/4f01d0199e82b62bcf20399afcc102f58a10ad07/docs/adr/0006-feb-harness-recovery-lineage.md
- https://github.com/KooshaPari/ShareCLI/blob/4f01d0199e82b62bcf20399afcc102f58a10ad07/docs/ops/feb-recovery.md
- https://github.com/KooshaPari/ShareCLI/blob/4f01d0199e82b62bcf20399afcc102f58a10ad07/crates/sharecli-ipc/src/cache_key.rs
- https://github.com/KooshaPari/PhenoRegistry/blob/85d7cd00cf59c379c05b740e8130a85b0d5bd31b/docs/governance/atlas/products/ShareCLI/STATE.md
