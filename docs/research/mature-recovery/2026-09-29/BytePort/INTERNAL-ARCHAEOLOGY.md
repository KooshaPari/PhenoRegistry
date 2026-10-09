# BytePort — internal archaeology, pass 1

Observed 2026-09-29. Product `KooshaPari/BytePort`, ID861430079, snapshot `0232cca16fedb7963a8c6f556dc5eee5c8c1674e`. Registry snapshot `85d7cd00cf59c379c05b740e8130a85b0d5bd31b`. Product-local source ledger BP-S01–10 records inspected extent and contradictions. This is not an exhaustive history certificate.

## Alias/concept map

| Search term | Relation | Evidence and authority | Open work |
|---|---|---|---|
| BytePort / byteport | Current product/case alias | Repository identity and user-attributed conversation records | Remote rename/origin history |
| MicroVM Cloud Management and Portfolio Integration | Historical product-description title | User-attributed November 20, 2024 conversation retrieval | Raw transcript export and accepted revisions |
| self-service deployment and productization | Mature outcome phrase | User-attributed August 25, 2026 retrieval | Reconcile current scope docs against this later intent |
| .nvms / NVMS manifest / nanoFile / odin.nvms | Manifest/file concepts, not repository aliases | November/December user-attributed descriptions; current SPEC/PLAN snippets | DSL boundaries, versioning and translator history |
| byteport/project/instance | Product identity hierarchy | User-attributed November 20, 2024 discussion | Map to actual DB/API/provider IDs without conflating them |
| portfolio / Slick / generated project pages / endpoint registration | Productization journey and integration concepts | Recovered user statements and SPEC.md | Ownership, publication authority, freshness and privacy semantics |
| NanoVMS / nvms | Separate branded runtime/dependency, NOT BytePort alias | User-attributed 2024-11-20T06:12:57Z explicitly separated branding | Freeze runtime source/API before experimental integration; no third product recovery |
| ByteBridge / bytebridge / Fermyon / Spin | Historical module/runtime experiment | backend/README retirement note; independent registry ByteBridge search | Commit-level removal and accepted-vs-experimental scope |
| Rust / Loco.rs / Go API / github.com/byteport/api | Architecture generations, not accepted product identity | SPEC.md and backend README | Recover decisions and public compatibility obligations |

## Recovered user-intent chronology

The entries below came from conversation retrieval summaries with attributed user/date. They are stronger evidence of user authorship than an assistant summary, but the original full transcripts and permanent message links are not materialized here. No invented source file or transcript hash is supplied.

| Attributed user time | Recovered substance | Consequence |
|---|---|---|
| 2024-11-20T02:48:26Z and 06:12:18Z | Git-based MicroVM cloud deployment with AWS EC2/S3/IAM and portfolio pages/descriptions/screenshots | Mature horizon includes cloud and publication, not just local container control |
| 2024-11-20T06:12:57Z | NanoVMS and BytePort explicitly separate branding | Runtime is not an alias or identity replacement |
| 2024-11-20T21:04:54Z | byteport/project/instance hierarchy; manifest analogous to deployment/workflow files; deployment and portfolio actions | Product/project/deployment/provider identities and user journeys matter |
| 2024-11-30T06:00:55Z | GitHub repository or ZIP, YAML NVMS and AWS account; static/full-stack/distributed deployment | Source acquisition and manifest-to-target behavior need recovered contract |
| 2024-12-19T02:19:34Z and 02:31:39Z | One NVMS plus Git repository; retrieve/parse/upload code and deploy services | A hard-coded placeholder image does not satisfy selected-source deployment |
| 2026-08-25T06:59:17Z | Self-service deployment and productization with GitHub OAuth, secure sessions, AWS provisioning, endpoint registration, observability and portfolio generation | Broad horizon persisted into 2026 in retrieved user statements |

An assistant's Spin/Wasm architectural proposal is not promoted into user intent. A broad later federation discussion is a research lead, not blanket authorization for every distributed-system feature.

## Explicit correction of the local-only assumption

Registry docs/intent/BytePort.md was filled on September 20 and calls BytePort desktop/local-only in mature identity. It lists 39 prompt references but explicitly reports the curated source corpus absent. Those references are not 39 inspected user messages. SPEC.md's opening and recovered user chronology instead describe Git-to-cloud deployment plus portfolio generation. No accepted pivot eliminating that horizon was found in inspected evidence.

**Working interpretation, not a frozen architecture:** local-first desktop may be a valid earlier-stage projection or control-plane choice; it must not silently erase the broader intended outcome. Reconcile the contradiction through recoverable authority. Do not replace the registry intent file wholesale on the strength of this partial pass.

## Current implementation observations, not user intent

The mounted Gin /deploy handler builds a NanoVMS request with alpine:latest/native. It does not translate the selected repository into the requested artifact in this handler. It creates a product UUID, stores the distinct returned sandbox ID in the deployment map, but /terminate sends project.UUID upstream. Remote provisioning occurs before local database persistence; failure after remote success needs an explicit recovery design. The server binds 0.0.0.0 by default, a separate trust decision from local data sovereignty.

backend/README says old API and bytebridge modules retired September 20; root README and registry still contain contrary descriptions. A newer cleanup note is not proof all references/callers/migrations are handled; verify history rather than destroying legacy artifacts.

## Primary source pointers

- https://github.com/KooshaPari/BytePort/blob/0232cca16fedb7963a8c6f556dc5eee5c8c1674e/SPEC.md
- https://github.com/KooshaPari/BytePort/blob/0232cca16fedb7963a8c6f556dc5eee5c8c1674e/backend/byteport/routes/deployment.go
- https://github.com/KooshaPari/BytePort/blob/0232cca16fedb7963a8c6f556dc5eee5c8c1674e/backend/byteport/main.go
- https://github.com/KooshaPari/PhenoRegistry/blob/85d7cd00cf59c379c05b740e8130a85b0d5bd31b/docs/intent/BytePort.md

Full Git ancestry, local-only pivot search, original prompt corpus, retired implementation contracts, dependency snapshots and fresh independent review remain open.
