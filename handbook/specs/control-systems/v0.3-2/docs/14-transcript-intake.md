# Full-session intake and remaining evidence

## Intake is complete for the supplied export

The full stored export has been received and structurally indexed. Do not ask the user to upload the same transcript again. The raw file is external to this distributable package; its exact filename, file ID, byte count, SHA256 and export timestamp are in [the intake manifest](../evidence/session/intake-manifest.json). The [conversation index](../evidence/session/conversation-index.json) contains 81 conversation records with parent links and source-message ranges. [S032]

This intake cannot recover messages removed before export. All records carry a compression flag. The document’s readable and lossless sections are two representations of stored content, not independent corroborating witnesses. User-role compaction frames must not be confused with newly issued user commands.

## Evidence retained

The [evidence index](../evidence/session/evidence-index.json) lists 16 selected excerpts. E001–E005 preserve direct user scope; E006 preserves a compaction-embedded access requirement; E007–E011 preserve pilot configuration and working-tree observations; E012–E014 preserve prior conclusions to audit; E015 records the last retained failed GitHub follow-up fetch; and E016 preserves a compacted readiness claim.

Three exact report write payloads were recovered and retained with an unverified-history header: GitOps updates, portability substrates and rollback. They are not merged into the normative design. Other named reports have partial reads, patches, summaries, script-embedded content or no directly recoverable body. See [report recovery](../evidence/session/report-recovery.json) for exact dispositions.

The scanner’s `no_direct_body_recovered` classification is deliberately narrow. It means no direct exact-path read/write body was selected by that scanner—not that a file never existed, was fabricated, or cannot be recovered from the original workstation. In particular, script-embedded report strings and compaction summaries need separate provenance-aware extraction before they are promoted to complete reports.

## Remaining closure inputs are narrower now

| Evidence | Why it still matters | Preferred recovery route |
|---|---|---|
| Original approved trio run/check identities | Job names are recovered but do not establish trusted producers, exact run identity or risk policy | Existing review records and actual current check-run API responses |
| Current workflow and caller refs | Historical pilot is untracked/modified in its displayed worktree; an exact current path returned 404 | Resolve the current canonical module and immutable commit; inspect callers |
| Applied GitHub settings and plan | Files and feature documents are not observed enforcement | Authorized read of current repository settings and actual activated entitlement |
| Final GitHub/Podman follow-up report bodies | Retained children do not provide finished, reliable audit packets | Read the exact original report files or record genuine absence; do not recreate them under the same identity |
| Runtime and network versions | WSLC, Podman and WSL2 are not interchangeable | Read-only installed-version/capability inventory |
| Deploy, data and recovery receipts | No successful target-environment proof is established here | Authorized disposable-target tests with observed identity and restore verification |

## Intake protocol for later evidence

Record source identity, acquisition time, original and derivative hashes, source revision, producer/run ID, exact range and redaction status. Append claim dispositions: confirmed, corrected, superseded, conflicting, still unverified or out of scope. Idempotently import by original identity/hash and message location into the **existing** evidence/session/research owner; this package is not a new registry.

A write argument, successful write result, readback, committed file, resolved shared workflow, started job, completed deployment, observed healthy candidate and accepted recovery are separate milestones. Never collapse them into “done.”

## Publication

Keep raw export bytes and any credential values in the original private context. Only sanitized derivatives belong in broadly shared docs. Redaction changes bytes and therefore requires a derivative hash. The limited detectors and selected-excerpt review used here are not a general DLP certification; review source metadata and workstation paths before public release.
