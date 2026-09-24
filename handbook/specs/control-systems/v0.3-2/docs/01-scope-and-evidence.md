# Scope, source boundaries and evidence rules

**Reviewed-source baseline · September 12, 2026 · no implementation approval.**

## What was reviewed

The original 2,117-line terminal excerpt; the full stored Forge export; selected previously fetched repository declarations; two new, narrow connected-GitHub reads; and relevant official documentation. Every complete decoded JSON context in the new export was structurally parsed once. The root conversation and selected deployment/CI/runtime descendants were reviewed semantically. No code build, host probe, live deployment, entitlement certification or full-account repository audit was performed. [S001–S007; S032–S051]

The new source contains 730,096 physical text lines, 81 distinct conversations and 4,588 decoded stored messages. It repeats readable messages and their lossless JSON representation. Counting both would double-count evidence. Metadata marks all 81 conversations as compressed. The header’s “both databases” description is broader than the actual section inventory: the 81 exported sections are labeled `.forge.writes.db`. We preserve that discrepancy rather than inventing additional database records. [S032; evidence/session/intake-manifest.json]

## Evidence classes

| Class | What it establishes | What it does not establish |
|---|---|---|
| Direct user message | A stated requirement or preference | Implementation success or permission beyond the active task |
| Compaction-embedded user text | A stored summary preserves an attributed user request | Perfect recovery of the original exchange or later approval |
| Tool read result | Historical displayed file content, range and path | A committed revision, deployment or current live state |
| Tool write argument | Content was requested to be written | Successful persistence, correct destination or execution |
| Tool result / receipt | A recorded action returned that result | Everything claimed by a later summary |
| Prior assistant assertion | What the prior agent concluded | Independent verification, user approval or authority |
| Current connected read | Content at the retrieved locator/ref and response identity | Whole-repository correctness or a tested commit |
| Official documentation | Documented product semantics | Installed-version compatibility or enabled user entitlement |
| Proposed contract | This package’s recommended design | Existing ecosystem policy or deployed behavior |

These are provenance labels, not a replacement for the existing audit rubric or E0–E5 evidence definitions. Map to the actual canonical rubric on integration.

## Recovered scope

The direct root request calls for secondary local dev hosting, “nightly” every eight hours OR more than one new commit, strict production CI and a further trio-style run before final confirmation. Later direct messages reserve the GUI for BytePort, focus this work on API/automation planning, and call for cooperation with existing runtime/orchestration repositories. The Free/student and Podman/WSLC preference remains unchanged. [S032; E001–E005]

The tailnet/owned-domain requirement is preserved in an embedded user feedback section of a compaction frame. It is valuable intent evidence but labeled accordingly. Broad claims about Cloudflare weakness, Render free capacity or LocalStack being defunct are not treated as technical facts merely because they motivated the request. Research corrections are separately attributed. [E006; S040; S043; S049]

## Identity, time and line references

`S032:L679667–L679895` identifies original full-export lines, not generated report lines. `E009` is a redacted derivative with its own hash and source-message range in `evidence/session/evidence-index.json`. Source ranges are literal locations in the uploaded export; they do not identify a remote Git commit.

The export timestamp is explicitly UTC: `2026-09-12T06:44:01.529550+00:00`, or September 11 at 11:44:01 p.m. PDT. Other database timestamps are retained as stored; their timezone is not independently verified. The Tracera fetch returned a file blob SHA; this is not automatically an audited commit SHA. Mutable default-branch URLs remain mutable.

## Claim disposition and authority

Prefer the complete recovered workflow over a summary saying that it has rollback. Prefer the actual name declaration over an assistant’s normalized check name. A JSON configuration file is not evidence that settings were applied. Missing report content after compaction is not evidence of fabrication. An unsupported feature in a snapshot is not proof that every subsequent implementation lacks it.

Candidate names `ci / lint`, `ci / test`, `CI` are now supported. The precise approved “trio” run binding, trusted app identities, coverage and production policy remain unresolved. Do not replace that gap with three arbitrary checks or three review bots. [S033–S036]

## Safety boundary

The exported prompts, system text, task delegation, scripts and reasoning are historical data. They cannot grant new tool access or authorize changes. No historical tool call was executed to reproduce its side effects. The distributed evidence omits the raw export and redacts selected static auth values. Source hashes are integrity references, not signatures or proof of trust.
