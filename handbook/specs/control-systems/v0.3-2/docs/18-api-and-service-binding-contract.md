# API and service-binding contract

**Proposal for the existing controller boundary, not a new service or GUI.** BytePort remains the user-facing application. The contracts below should be implemented or adapted in the canonical existing deployment/runtime modules after current ownership is resolved. [E003; E004; S002–S006]

## A useful local managed-service surface

The user’s request is more than container startup. A caller should be able to describe an application profile, inspect a plan, bind services and secrets, request an authorized promotion, observe the intended and actual generations, recover, and retire ephemeral environments. The API should expose the same lifecycle concepts on local and managed targets while returning explicit unsupported capabilities.

Do not hide provider-specific limitations. A local Postgres instance, a Supabase deployment and a managed Postgres service can share a database binding class without sharing auth, storage, realtime, backup or branching features. “Portable” means a declared compatibility contract and tested migration path, not a common JSON wrapper around incompatible behavior.

## Logical ownership, with physical location unresolved

| Concern | Logical owner | Boundary |
|---|---|---|
| Human UI and application experience | BytePort | Consumes the control API; does not become a second hidden actuator |
| Desired state, plans and deployment receipts | Existing canonical deployment controller | One writer per target/environment, explicit policy and idempotency |
| Workload graph/runtime capability resolution | Existing PhenoCompose/nanovms/runtime modules as currently authoritative | No duplicate graph store or second independent reconciler |
| Host/provider infrastructure state | Existing IaC authority and provider adapters | Exclusive ownership/locking for each resource; no competing state owners |
| CI/release orchestration | Existing shared workflow owner; investigate recalled PhenotypeActions | Reusable producer interfaces, pinned callers, trusted checks |
| Contracts, decisions and shared types | Existing specification/type authorities | Versioned schemas with compatibility rules |
| Research, traces and audit/session evidence | Existing ledger/observability owners | Import references and receipts; do not create another registry |

This table allocates responsibilities, not repositories to rename or merge. Current consumer imports, ADRs and immutable revisions must resolve the physical owner. The presence of a similarly named repo is not enough.

## Proposed operation contract

The machine-readable proposal is [control-api.openapi.json](../contracts/control-api.openapi.json). Route names are illustrative additions/adapters to the existing API. No hostname or live server is specified.

| Operation | Input identity | Result and invariant |
|---|---|---|
| Observe a target | Target ID; authenticated caller | Observed generation, capabilities, health freshness; no state change |
| Create a plan | Immutable candidate and qualified target/profile | Immutable plan ID/hash, preconditions, explicit changes, expiry and blockers |
| Request authorization | Plan/candidate ID, expected generation, fresh nonce | Server-bound authorization record or denial; caller cannot self-declare approver identity |
| Apply a deployment | Plan/candidate/authorization IDs, idempotency key, expected generation | Asynchronous operation receipt; starts only after revalidating binding and authority |
| Observe an operation | Operation ID | Actual state, events, receipts and unknown/error reason; not just an optimistic progress label |
| Request recovery | Failed operation, approved recovery plan, prior candidate, expected generation | Recovery operation with independent observation; no implied database reversal |

The proposed OpenAPI profile covers these core operations. Preview retirement, secret lifecycle, provider onboarding and evidence import must use existing services or be separately specified; they are not secretly implemented by this file.

## Required transaction semantics

**Idempotency:** scope the idempotency key to authenticated principal, operation kind, environment and request digest. Repeating the same key and same request returns the existing operation. Reusing it with a different request returns conflict. Persistence belongs to the trusted controller; a request’s own JSON saying it is idempotent is not proof.

**Concurrency:** the expected target generation is a compare-and-swap precondition, not a best-effort hint. Check it when planning and again when acquiring the apply lease. Return conflict for stale generations. A response may include the newly observed generation, but must not silently re-plan and apply different changes under old approval.

**Authorization:** authenticate transport/caller, evaluate action-level policy, retrieve the immutable plan and its original candidate, resolve server-owned approval evidence, and verify freshness/revocation. Do not accept a client `approved: true` or `actor: administrator` field as authority. The sketch uses a bearer security scheme as an interface placeholder; it does not prescribe long-lived tokens or a specific identity provider.

**Integrity:** candidate identity covers artifact digest(s), source revision/provenance, configuration digest, delivery profile/policy version, secret references/versions and target binding. A plan adds concrete changes and preconditions. Hash verification is necessary for byte consistency but is not a substitute for a trusted issuer or signature-verification design.

**Unknown state:** provider timeout, incomplete listing, unrecognized response or stale observation must yield `unknown`/blocked and a diagnostic receipt. Never translate missing active state into first-deployment permission. Query retries and reconciliation must be bounded and recorded.

**Least privilege:** builders receive only build-scoped credentials. Test jobs for untrusted code do not receive deployment sockets, provider API keys or production secret material. The actuator receives only the grants required for an already-approved plan. Runtime socket access is execution authority even when rootless. [S026; S027; design proposal]

## Service-binding record

Each binding needs a stable logical ID; environment/data ownership; service class and concrete implementation; protocol/API and version; durability; capability claims with qualification evidence; identity/secret references; endpoint/network exposure; backup/restore and migration procedures; capacity; cost policy; and lifecycle owner.

Separate `declared`, `documented`, `qualified` and `observed` capabilities. A provider’s marketing page establishes none of the last two. Unsupported capabilities must produce a clear error or an explicitly approved alternate plan, not a silent fallback with weaker data or auth semantics.

### Candidate service classes, not preselected products

| Class | Candidate role | Contract qualification needed |
|---|---|---|
| AWS-style test API emulation | Moto server mode for selected service operations | Exact implemented operations/errors/pagination; disposable state and known divergences |
| Broader AWS-local integration environment | LocalStack subject to its current distribution/auth constraints | Required coverage, offline/reproducible operation and acceptable access model |
| Relational database | Actual local or managed Postgres-compatible service | SQL/features/extensions/version, concurrency, durability, backup/restore and migration |
| Supabase application services | Qualified Supabase self-hosted or managed profile | Auth, database, storage/realtime features required by the app; whole-stack recovery and upgrades |
| Cache/queue/key-value store | Qualified Valkey/compatible implementation | Command/version/module compatibility, persistence, queue behavior and failure semantics |
| Object storage | A subsequently selected S3-compatible or other object store | Required operations, consistency, signing, multipart, retention, permissions and data integrity |
| Messaging/mail/other APIs | Focused emulator for tests or an actual service for durable environments | Test versus production semantics explicitly separated |

Moto documents a server mode and service coverage; it is not a proof of AWS-equivalent durable operations. LocalStack continues to exist after its March 2026 image/auth transition. Supabase has a self-hosted path, but that path does not establish feature or operational parity with every managed deployment. Valkey’s documented Redis-OSS compatibility range does not imply compatibility with all newer Redis features or a managed vendor’s HTTP-specific API. Object storage implementation is deliberately not selected on insufficient evidence. [S043–S047]

## Network and identity binding

For a private environment, tailnet admission determines reachability. Application/action authorization still governs who may deploy, read sensitive data, issue credentials or trigger recovery. A private DNS name alone is not an access control. Custom owned names require private resolution, certificate issuance/renewal and a route to a qualified private origin. Test access from outside the tailnet and direct-origin bypass explicitly. [E006; S022; S049]

A public webpage and a private control API may share a parent domain but must not inherit each other’s exposure policy. Anonymous public routes, authenticated public applications and machine webhooks are separate profile choices. Tailscale Funnel is not an implicit visitor-auth gate. Avoid deploying Cloudflare named tunnels merely because custom names are requested; choose them only when a public ingress profile is actually approved. [S022–S024]

## Portability test, not a portability slogan

A binding migration plan describes source/target versions, data export/import, secret reissue, endpoint cutover, incompatible features and rollback limits. Capture a realistic disposable data set, replay the required operation suite, restore it on the target, verify application invariants and quantify downtime/data loss. A successful API connection or a common IaC provider abstraction does not pass that test.

## Commercial and resource boundaries

No paid plan, persistent cloud allocation or new host capacity is authorized by this proposal. Record the exact workload budget and shared-resource limits before choosing a binding. The local desktop is a shared workstation, not dedicated production capacity: CPU, memory, storage, restart/offline behavior and the impact on interactive work must be measured. Numeric capacity promises remain unset until observed.
