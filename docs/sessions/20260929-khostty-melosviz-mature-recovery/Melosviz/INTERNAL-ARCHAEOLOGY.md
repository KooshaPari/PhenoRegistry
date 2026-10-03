# Melosviz internal archaeology — pass 1

Observed 2026-09-29. Product source 1aec20a2ba41a01ed557d1c7f63f9a0089f842cf; registry 85d7cd00cf59c379c05b740e8130a85b0d5bd31b.

## Alias / concept / lineage map

| Name or conceptual phrase | Source and meaning | Authority / resolution |
|---|---|---|
| Melosviz / MelosViz | Current repository and package name | Repository identity verified |
| Programmable Music Visualizers | Earlier April–May 2026 conversation, before later studio framing | Retrieved user-intent paraphrases; primary transcript unavailable |
| spec-first conductor / hybrid scenes / scanners | Registry ADR0003 and repo SPEC scene models | Design record claims adoption; approving primary decision unresolved |
| Director's Console / ComfyUI-centric studio pivot | AGENTS, STUDIO_PIPELINE, August 28 commit | Implementation/design evolution verified as source assertions; supersession authority open |
| browser R3F visualizer / BeatPulse / Canvas / lyric video | README and earlier intent | Distinguish a retired implementation from a retained user outcome |
| backend / MelosViz scoring engine | Registry backend-melosviz boundary | Predecessor lead with redacted owner; not confirmed current canonical home |
| phenotype-python-sdk/packages/melosviz | Same boundary records July 17 absorption, bbeedd5 on wip/2026-07-16-0030-auto | Imported historical assertion; full revision/ancestry/owner not verified |
| recovery/melosviz-local-20260726 / feat/comfyui-studio-pivot | AGENTS historical refs | Leads requiring independent ref/history inspection |

Search each concept independently in the next history/conversation pass. Current-name matching is insufficient. This map records discovery, not exhausted archaeology.

## Recovered user intent versus assistant architecture

Targeted retrieval from the earlier conversation returned these paraphrases: April 18 22:56:35Z, input-WAV-driven visuals with reliable synchronization rather than loosely aligned loops; 22:57:15Z, strong script/API-first agent operation with a substantial GUI for review and small edits; 23:00:22Z, hybrid club/performer imagery and photo/mesh/splat transitions controlled spatially, including occlusion/rotoscoping; 23:03:35Z, simpler programmed graphics, lyric videos and short loops are also useful. May 30 23:56:44Z expands analysis-driven presets and expressive inputs.

These are retrieval-mediated paraphrases, not verbatim/hash-verified transcripts. Earlier assistant tool proposals (such as TouchDesigner-first design) are not user mandates. The registry ADR refers to a local transcript path unavailable to this session. A later targeted search for studio-pivot authority failed. No claim that the user approved removal of the original horizon follows from that failure.

## Exact historical leads

- ff5f1fc4215ef6940b2c701b5ee04d2f275c58fb, 2026-08-28: ComfyUI-centric multi-tool studio pivot.
- 99127a6ba8ff312f3fe4c26e352d7614566cf71e, 2026-08-28: removal of legacy Rust crates.
- b804174d7acc02a765a47ef4c5545abfdfdddaf1, 2026-09-12: delivery extensions, cache/provenance, reintroduced Rust scaffolds/analyzer and historical offline-env repair.
- 316bac0be7c3c983d236825342e6853b4091a76a, 2026-09-17: release-note/tag-content reconciliation and Tauri artifact claims.

Commit messages were inspected; complete diffs and approval discussions were not. Do not convert message test counts into measured current results.

## Registry sources

All paths bind to the registry frozen SHA above:
- docs/org-audits/adr/0003-melosviz-architecture.md, blob f77eb8f0da3093e8a8d2acd00f0de21b4cd906fb: full read; adopted-pending-build assertion, hybrid domains and GUI-to-structured override principle.
- docs/governance/atlas/products/Melosviz/STATE.md, blob 8ba56173ae8355eb224705d8d050ceae1506a89c: historical bounded assessment; PIPELINE_REHEARSAL_NOT_PRODUCT_PROOF is not certification of current main.
- docs/boundary/backend-melosviz.md, blob 0f64c3fefe8845410a2e350efdf6d528d8aed5da: full read; unverified predecessor/absorption assertions.
- Other atlas and generic audit catalogs: discovered, not semantically validated; excluded from grading.

## Reconciliation consequences

A browser renderer can be deprecated without deleting the user's desire for programmable visuals. A studio pipeline can incorporate, rather than supersede, hybrid scenes—but that is a candidate interpretation, not a decision made here. Canonical scope must separately decide outcomes, scene semantics, editing authority, tools and deployment modes. Read mounted CLI/HTTP/UI paths and actual schemas only after the accepted horizon becomes credible; present current code observations as reconnaissance until then.

No full source-family or alias/history denominator is closed. Product-local findings preserve corrected assumptions: the global offline-environment mutation was already repaired; same-size cache reuse, unknown media classification and per-scene accounting remain current source-level risks requiring scoped experiments.
