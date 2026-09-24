# App Architecture for Screen Time

**User:**   
**Created:** 4/21/2026 21:01:27  
**Updated:** 4/22/2026 18:01:13  
**Exported:** 4/22/2026 19:32:45  
**Link:** [https://chatgpt.com/c/69e847ac-5710-83ea-8757-24775d02928b](https://chatgpt.com/c/69e847ac-5710-83ea-8757-24775d02928b)  

## Response:
4/22/2026, 5:35:32 PM

I’m turning the PRD into the full implementation scaffolding now: ADR set, repo/package map, FR index, milestones, and work-package style breakdown. I’m keeping the same Rust-core/native-shell stance instead of watering it down with framework tourism.

Thought for 4s

**Screen-time-connectors-prd**

# PRD — Connector-First Screen Time Management Platform

## Document status
Draft v0.1

## Working title
Project name TBD. Placeholder: **Latch**

## Product summary
Build a connector-first platform for screen time management that combines native device enforcement with a portable rules and gamification core. The product blocks or limits distracting apps, then adjusts restrictions using external signals from third-party systems such as Canvas LMS, calendars, tasks, health apps, finance apps, and future connectors.

The primary product differentiator is **not** basic app blocking. It is an extensible **Connector Runtime + Rules Engine + Reward/Punishment System** that can treat external systems as first-class behavioral inputs.

## Product vision
Create a system where focus enforcement can react to real-world obligations and achievements.

Examples:
- Submit a Canvas assignment before its deadline and earn 30 minutes of unlocked entertainment time.
- Miss two due-today obligations and automatically escalate device restrictions for the evening.
- Complete a study block, workout, or other verified external task and reduce friction for a controlled break.
- Require stronger unlock proof when connectors indicate the user is falling behind.

## Product goals
1. Ship a robust connector abstraction that can onboard many external systems without changing product core logic.
2. Keep enforcement native-first on iOS and Android rather than forcing fake cross-platform uniformity at the OS boundary.
3. Maintain a strict hexagonal architecture with clear inbound and outbound ports.
4. Preserve a Rust-first core for domain logic, policy evaluation, event normalization, sync orchestration, persistence, and auditability.
5. Allow polyglot outer adapters where platform realities demand them.
6. Support local-first and privacy-first operation where possible.
7. Make reward/punishment rules configurable data, not hardcoded app behavior.

## Non-goals for MVP
- Full desktop app parity.
- Browser-extension enforcement as a first-class launch target.
- Social network or community features.
- Multi-tenant SaaS organization admin product.
- Arbitrary user scripting inside the mobile clients.
- Trying to fully defeat every rooted/jailbroken bypass path.
- Building every connector category in v1.

## Primary user
An individual user who wants hard-to-bypass app restriction plus motivation systems tied to school, work, task, or health systems.

## Initial target use cases
### Use case 1: Academic enforcement
A student connects Canvas LMS. Upcoming assignments, overdue work, submissions, and grades affect app availability and break allowances.

### Use case 2: Task-based unlocks
A user connects a task/calendar system. Completing scheduled work earns flexible device access.

### Use case 3: Punishment escalation
Repeated missed obligations reduce emergency exits, remove soft breaks, or require stronger physical unlock rituals.

### Use case 4: Reward economy
The user accumulates earned credits, streaks, or tokens from verified external actions, then spends them on controlled unblocks.

## Product principles
### 1. Connector-first, not integration-bolted-on
External systems are a core product axis.

### 2. Native enforcement, portable logic
The device-control edge remains native. Domain logic remains portable.

### 3. Hexagonal architecture
UI, storage, connectors, and OS enforcement are adapters around stable domain ports.

### 4. Rust first
Rust owns the product’s core logic, state machine, normalization, persistence schema, audit model, rules engine, and connector runtime contracts.

### 5. Polyglot where justified
Swift/Kotlin are preferred at mobile boundaries. Go/Zig may be used for focused service or systems edges. TypeScript/Python are last-mile tools only when they buy concrete leverage.

### 6. Configured rules over hardcoded behavior
Gamification policies must be composable, inspectable, testable, and explainable.

### 7. Auditability
When the product punishes or rewards the user, the system should be able to explain exactly why.

## Product requirements

## FR-001 Native enforcement abstraction
The system shall expose a shared enforcement port used by domain logic while allowing separate iOS and Android implementations.

### Acceptance notes
- iOS adapter uses Apple-native Screen Time stack.
- Android adapter uses Android-native capabilities and services.
- Domain logic never depends on platform-specific API types.

## FR-002 Connector abstraction
The system shall define a stable connector manifest and runtime contract that each external source must implement.

### Acceptance notes
Each connector shall declare:
- identifier
- display metadata
- auth method
- capabilities
- sync mode
- supported entities
- emitted normalized event types

## FR-003 Normalized event ingestion
The system shall transform third-party source data into canonical domain events.

### Acceptance notes
Normalized events must include:
- event id
- connector id
- account id
- event type
- occurred at
- effective at
- dedupe key
- confidence
- canonical payload
- trace to raw vendor reference

## FR-004 Rule engine
The system shall evaluate normalized events and current state to produce reward, punishment, or enforcement decisions.

### Acceptance notes
Outputs may include:
- credit grant
- credit spend
- unlock window
- stricter block profile
- emergency-exit reduction
- stronger unlock proof requirement
- streak mutation
- reminder or intervention event

## FR-005 Reward wallet
The system shall maintain a persistent reward state.

### Acceptance notes
Wallet state may track:
- earned credits
- spent credits
- streaks
- unlock balances
- multiplier state
- debt or penalty balance

## FR-006 Penalty engine
The system shall maintain a penalty state independent from reward state.

### Acceptance notes
Penalty state may track:
- missed obligations
- escalation tier
- bypass budget
- lockout periods
- strict-mode activation windows

## FR-007 Unlock proof subsystem
The system shall support pluggable unlock proof strategies.

### Acceptance notes
Proof types may include:
- NFC tag
- QR code
- countdown/delay
- location/geofence
- accountability approval
- completion of connector-driven goal

## FR-008 Sync orchestration
The system shall support connector polling, webhook intake where possible, cursoring, deduplication, retries, and backoff.

## FR-009 Explainability
The system shall provide a user-visible explanation for any reward, punishment, or enforcement action.

### Acceptance notes
Example explanation:
- “Instagram remained blocked because 2 Canvas assignments became overdue within the last 24 hours and your evening strictness rule escalated to tier 2.”

## FR-010 Audit log
The system shall append audit records for major connector syncs, rule evaluations, enforcement actions, and unlock decisions.

## FR-011 Capability-driven UI
The system shall render connector setup and rules configuration from connector capabilities rather than hardcoded per-vendor screens wherever possible.

## FR-012 Offline-tolerant local state
The system shall continue enforcing existing policy when connector sync is unavailable.

## FR-013 Safe degradation
The system shall distinguish among:
- stale connector data
- auth-expired connector data
- missing permission for enforcement
- disabled native enforcement service

## FR-014 Canvas connector MVP
The system shall support a Canvas LMS connector in MVP.

### Canvas MVP capabilities
- connect via OAuth2
- bind to Canvas base URL / institution
- read courses
- read assignments
- read submissions
- read announcements if feasible
- emit normalized events relevant to coursework and deadlines

## FR-015 Rules authoring MVP
The system shall support a limited but powerful rules UI in MVP.

### MVP rule building blocks
- IF event/condition
- AND optional time or count condition
- THEN reward/punishment action
- duration
- cooldown
- priority
- explanation template

## FR-016 Cross-device identity model
The system shall support one user with multiple devices and a shared portable state model.

## FR-017 Privacy-first defaults
The system shall minimize server dependence for enforcement and avoid collecting unnecessary cloud telemetry in MVP.

## Architecture

## High-level architecture
The product is split into five major layers:
1. Native clients and platform enforcement adapters
2. Shared application/domain core
3. Connector runtime and sync engine
4. State, audit, and policy persistence
5. Optional backend control/sync services

## Hexagonal architecture model

### Domain core (inside)
Owned primarily by Rust.

Modules:
- identities
- connectors
- normalized events
- rule engine
- rewards
- penalties
- policy state
- unlock proof state machine
- audit log model
- scheduling and sync orchestration

### Inbound ports
- User commands
- Sync triggers
- Webhook inputs
- Native enforcement callbacks
- Timer/scheduler events

### Outbound ports
- EnforcementDriver
- ConnectorRuntime
- TokenStore
- EventStore
- WalletStore
- AuditStore
- NotificationPort
- TimePort
- Crypto/SecureStoragePort

### Outbound adapters
- iOS Screen Time adapter
- Android usage/accessibility adapter
- Canvas connector adapter
- future connector adapters
- SQLite/Postgres adapter
- local secure keychain/keystore adapter
- optional backend API adapter

## Core contracts

### Enforcement driver port
The core depends on a generic enforcement interface.

Responsibilities:
- authorize permission flows
- discover selectable app/site targets
- apply block/limit policy
- remove policy
- schedule policy
- surface usage snapshots if available
- start/complete unlock session

### Connector runtime port
Each connector must expose:
- manifest metadata
- auth strategy
- capability declaration
- sync entrypoint
- disconnect/revoke cleanup

### Rule engine port
Inputs:
- normalized events
- current wallet/penalty state
- device context
- active policy set

Outputs:
- domain decisions
- enforcement intents
- reward/penalty mutations
- explanations

## Data model

### Core entities
- User
- Device
- Connector
- ConnectorAccount
- ConnectorCapability
- ConnectorCursor
- NormalizedEvent
- Rule
- RuleEvaluation
- RewardWallet
- PenaltyState
- EnforcementPolicy
- UnlockSession
- AuditRecord

### Suggested persistence split
For MVP:
- local SQLite on device for client state and audit cache
- secure storage for tokens and secrets
- optional backend persistence for multi-device coherence

## Connector framework design

## Connector manifest
Every connector should declare:
- id
- version
- display name
- auth type
- sync mode: poll, webhook, hybrid
- capabilities list
- entity types
- event types
- health indicators

## Connector lifecycle
1. Install connector
2. Authorize connector account
3. Run initial sync
4. Normalize source data into events
5. Persist cursor/checkpoint
6. Evaluate rules
7. Update reward/punishment state
8. Trigger enforcement updates if required

## Connector categories
MVP categories:
- LMS connector: Canvas

Near-term categories:
- tasks/reminders
- calendars
- communication systems
- health/fitness
- finance/accountability

## Canvas connector design

### Inputs
- OAuth2 auth flow
- Canvas base URL / institution binding
- selected course scope if needed

### Canvas entities in MVP
- Course
- Assignment
- Submission
- Announcement if feasible

### Canonical Canvas events
- course_added
- assignment_created
- assignment_due_soon
- assignment_overdue
- assignment_submitted
- grade_posted
- announcement_posted

### Example rule mappings
- assignment_submitted before due date → reward credits
- assignment_overdue → escalate penalty tier
- all due-today assignments submitted → unlock entertainment profile for 45 minutes
- grade_posted above threshold → bonus reward

## Mobile stack decision framework

## Guiding stack choice
Use **native mobile shells** for enforcement-heavy clients. Use Rust for core logic. Use FFI rather than pretending deep blocking logic is cleanly cross-platform.

## iOS recommendation
### Preferred shell
SwiftUI + Swift concurrency

### Why
- best fit for Apple Screen Time APIs
- best fit for entitlements, extensions, system integration, NFC, and native UX
- lowest impedance with Apple-native blocking stack

### Integration model
Rust core exposed through UniFFI or equivalent Rust-friendly Swift binding layer.

## Android recommendation
### Preferred shell
Kotlin + Jetpack Compose

### Why
- best fit for UsageStats, AccessibilityService, foreground service, permissions flows, and platform lifecycle realities
- avoids React Native / Flutter glue complexity around services and accessibility edge behavior

### Integration model
Rust core exposed through JNI-generated or bridge layer bindings.

## Desktop and web considerations
Desktop is not MVP-critical for enforcement. If future desktop tools are needed for policy authoring, analytics, or administrative control, those can be separate shells over the same core.

## Alternatives considered

### Tauri
Good for desktop shells and admin/config tools. Bad default choice for primary mobile enforcement clients.

### Electron / Electrobun
Reasonable only for internal tooling or desktop control plane. Not a serious primary choice for mobile-native blocking.

### Flutter
Attractive for broad cross-platform UI, but weak fit for deep iOS Screen Time and Android enforcement surfaces that already force native work.

### React Native
Same problem as Flutter, plus additional service/bridge complexity for strict enforcement behavior.

### Kotlin Multiplatform
Potentially useful later for some shared client logic, but unnecessary if Rust already owns the portable core.

### Pure Rust UI stack
Not the right fight for MVP mobile productization given the platform integration demands.

## Polyglot stack recommendation

### Tier 1 — primary languages
- Rust for domain core, connector runtime contracts, rules engine, normalization, storage abstractions, audit model
- Swift for iOS shell and Apple-native enforcement adapters
- Kotlin for Android shell and Android-native enforcement adapters

### Tier 2 — strongly optional / selective use
- Go for small backend services, webhook fan-in, connector auth broker, or control-plane APIs if that ends up materially faster than Rust for those edges
- Zig for targeted systems utilities or packaging/build helpers where it clearly wins, not as the main application core

### Tier 3 — de-prioritized / last resort
- TypeScript for ancillary dashboards, docs tooling, or lightweight admin tools
- Python for research/prototyping or connector reverse-engineering experiments, not for product-critical core or long-lived runtime paths

## Architectural split by language

### Rust owns
- core domain model
- connector SDK/runtime contracts
- rule evaluation
- normalized event schema
- sync orchestration state machine
- persistence schema
- audit chain
- portable tests

### Swift owns
- iOS app shell
- Apple Screen Time adapter
- Apple NFC / local UX integration
- iOS permission/onboarding flows
- iOS extension plumbing

### Kotlin owns
- Android app shell
- Android enforcement adapter
- Accessibility/Usage/notification/service wiring
- Android permission/onboarding flows

### Go optional ownership
- backend auth broker
- webhook receiver
- multi-device sync API
- observability-friendly service edges

## OSS base recommendation

## Best practical approach
Do not adopt one “habit app” as the whole base. Use an enforcement-capable OSS app as a donor/reference for each platform, then build your own connector/rules core above it.

### iOS base candidate
Foqos-style base/reference
- native iPhone blocker category fit
- NFC/QR and Screen Time patterns already solved
- close conceptual match to physical-proof unlocking

### Android base candidate
Reef-style base/reference
- Android blocker/routines/usage patterns already solved
- useful for permission and service reliability patterns

## Why not one cross-platform base
Because the hardest part of the app is platform-native enforcement and bypass resistance, not a reusable UI layer.

## Security and trust requirements
- tokens stored in secure OS keystore/keychain
- connector secrets never stored in plain text
- audit entries tamper-evident where practical
- explainability for every high-impact action
- explicit stale-data indicators for connectors
- no silent downgrade from strong enforcement to weak enforcement

## Privacy requirements
- local-first where possible
- minimum viable cloud state only when needed for multi-device sync or connector/webhook handling
- explicit user control over each connected source
- connector-level revoke/disconnect support

## UX requirements

### Initial setup
- choose apps/categories to control
- grant platform permissions
- connect first external source, starting with Canvas
- configure first rule from template
- test reward/punishment flow in a sandbox

### Rule templates for MVP
- “Finish schoolwork, earn break time”
- “Miss due items, lose emergency exits”
- “All due today done, unlock entertainment window”
- “Three misses in a week, strict mode escalates”

### Explainability UI
The product must show:
- latest triggering event
- active rule name
- resulting reward/punishment
- current wallet/penalty balance
- what action can reverse or reduce the penalty

## Observability requirements
- connector sync success/failure
- connector auth freshness
- rule evaluation outcome counts
- enforcement application success/failure
- unlock proof success/failure
- stale-data state transitions

## Packaging and deployment

### MVP deployment model
- native iOS app
- native Android app
- optional small backend for connector OAuth callbacks and cross-device sync

### Backend deployment recommendation
If backend is needed in MVP, prefer a small service boundary rather than a large monolith.

Suggested components:
- auth callback service
- webhook intake service
- optional sync API

## Milestones

### Phase 0 — architecture and contracts
- finalize domain model
- finalize connector manifest/runtime contract
- finalize enforcement driver contract
- finalize normalized event schema
- finalize rule engine schema

### Phase 1 — iOS enforcement MVP + Rust core
- Rust core skeleton
- iOS shell
- iOS enforcement adapter
- local rule evaluation
- reward/penalty state
- unlock proof subsystem

### Phase 2 — Canvas connector MVP
- OAuth flow
- course/assignment/submission sync
- normalized event mapping
- Canvas-driven rules templates

### Phase 3 — Android enforcement MVP
- Android shell
- Android enforcement adapter
- permission hardening
- strict mode and service reliability work

### Phase 4 — backend and multi-device coherence
- optional sync backend
- webhook support for connectors that need it
- multi-device state merge rules

## Open questions
1. Should MVP be single-device first or multi-device from day one?
2. Is cloud sync required for launch, or can launch be local-first with optional later sync?
3. Should reward currency be explicit and game-like, or mostly implicit break credits?
4. Should punishment state ever hard-lock all breaks, or always preserve a bounded emergency path?
5. Is QR-only unlock acceptable in MVP, or is NFC mandatory?
6. Is Canvas the only educational connector in first wave, or should the abstraction reserve for Google Classroom simultaneously?
7. Should backend be Rust-first as well, or is Go acceptable for faster connector-edge iteration?

## Recommended initial ADR decisions
- ADR-001: Native mobile shells over cross-platform mobile UI frameworks
- ADR-002: Rust owns portable domain core
- ADR-003: Connector runtime as first-class product surface
- ADR-004: Reward and penalty state are separate aggregates
- ADR-005: Enforcement drivers are adapter-only and cannot host business logic
- ADR-006: Canvas is the first connector implementation
- ADR-007: Local-first state with optional backend synchronization

## Final recommendation
Build the product as a **Rust-centric hexagonal core** with **SwiftUI and Kotlin/Compose native shells**, using platform-native enforcement adapters and a connector runtime that treats Canvas and future systems as interchangeable event sources. Avoid betting the mobile product on Tauri, Electron, Flutter, or React Native for the primary enforcement clients. Use them only later, if needed, for admin or analytics surfaces.

---

# ADR Pack

## ADR-001 — Native mobile shells over cross-platform mobile UI frameworks
**Status:** Accepted

### Decision
Use native mobile shells:
- SwiftUI for iOS
- Kotlin + Jetpack Compose for Android

### Context
This product’s hardest problems are platform-native:
- iOS Screen Time / FamilyControls / ManagedSettings / DeviceActivity integration
- Android UsageStats / Accessibility / service reliability / foreground constraints
- permission flows
- bypass resistance
- unlock proof mechanisms like NFC and other native device capabilities

Cross-platform UI frameworks do not remove those problems. They mostly add another bridge layer on top of them.

### Alternatives considered
- Flutter
- React Native
- Kotlin Multiplatform UI
- Tauri mobile
- pure web wrapper approaches

### Rejected because
They centralize the wrong layer. The UI is not the hard part. Enforcement and permissioned OS integration are.

### Consequences
- best OS fit
- least impedance with native APIs
- separate client shells to maintain
- shared portable logic must be kept below the shell boundary

## ADR-002 — Rust owns the portable core
**Status:** Accepted

### Decision
Rust owns:
- domain model
- normalized event schema
- connector contracts
- rules engine
- wallet and penalty state
- sync orchestration
- persistence contracts
- audit model
- shared tests

### Context
The domain needs a portable, strict, testable core with strong type boundaries and low tolerance for accidental spaghetti between connectors, rules, and enforcement.

### Alternatives considered
- Kotlin Multiplatform as primary core
- Swift/Kotlin duplicated logic
- TypeScript backend-first core
- Go backend-first core

### Rejected because
- duplicated logic creates drift
- TS is too weak a foundation for the core state machine and invariants you want
- Kotlin Multiplatform is unnecessary if Rust already owns shared logic
- Go is fine for services but not the best single home for the full stateful product core

### Consequences
- FFI/JNI/bridge work is required
- core logic stays highly portable and testable
- shared rule behavior remains consistent across platforms

## ADR-003 — Connector runtime is a first-class product surface
**Status:** Accepted

### Decision
Treat connectors as a formal runtime model, not ad hoc integrations.

### Context
The product differentiator is the ability to connect systems like Canvas and convert their signals into a common event model that drives focus enforcement and gamification.

### Consequences
Every connector must expose:
- manifest
- auth strategy
- capability descriptors
- sync mode
- normalized event mappings
- health and staleness state

## ADR-004 — Reward and penalty are separate aggregates
**Status:** Accepted

### Decision
Keep reward state and penalty state separate.

### Context
These are not symmetric inverses.
- rewards represent earned optional flexibility
- penalties represent restriction escalation and bypass suppression

Bundling them into one score creates opaque behavior and ugly rule interactions.

### Consequences
- clearer explanations
- clearer rules
- safer escalation logic
- more state to model and test

## ADR-005 — Enforcement drivers are adapter-only and may not contain business logic
**Status:** Accepted

### Decision
Platform enforcement adapters may translate domain intent into native API calls, but may not own rules or behavioral policy.

### Context
If business logic leaks into Swift/Kotlin platform code, portability collapses and rule behavior drifts across platforms.

### Consequences
- enforcement adapters stay thin
- domain remains authoritative
- debugging becomes dramatically easier

## ADR-006 — Canvas is the first connector
**Status:** Accepted

### Decision
Canvas LMS is the first production connector.

### Context
It is a clean exemplar of the connector model:
- OAuth2 auth
- user-visible obligations
- deadlines
- submissions
- grades
- announcements
- obvious reward/punishment mappings

### Consequences
- MVP connector scope is concrete
- normalization model is forced to handle deadline-based systems well
- later connectors can reuse the same patterns

## ADR-007 — Local-first client state with optional backend synchronization
**Status:** Accepted

### Decision
The product is local-first for enforcement and core state, with optional backend synchronization for multi-device coherence and connector/webhook support.

### Context
Blocking must keep working even if the network is gone or a backend is stale.

### Consequences
- more sophisticated merge/sync work later
- stronger resilience in MVP
- cleaner privacy posture

## ADR-008 — Hexagonal architecture with polyglot outer adapters
**Status:** Accepted

### Decision
The system uses hexagonal architecture with Rust inside and polyglot adapters outside.

### Consequences
- Swift/Kotlin own OS edges
- Rust owns domain
- optional Go services can exist without infecting the domain
- TypeScript/Python remain non-core

## ADR-009 — Tauri/Electron are control-plane tools only, not primary enforcement clients
**Status:** Accepted

### Decision
Desktop/web-wrapper technologies are allowed only for non-critical surfaces such as analytics dashboards, rule authoring consoles, or internal ops tools.

### Consequences
They do not get to define the product architecture.

---

# Functional Requirements Index

## Connector and sync requirements
- **FR-CONN-001** Connector manifest model exists and is versioned.
- **FR-CONN-002** Connector runtime supports install, authorize, sync, disconnect.
- **FR-CONN-003** Connectors declare capabilities and supported normalized event types.
- **FR-CONN-004** Connector sync supports polling with cursor/checkpoint persistence.
- **FR-CONN-005** Connector runtime supports webhook ingestion where available.
- **FR-CONN-006** Connector runtime supports deduplication and idempotent ingest.
- **FR-CONN-007** Connector health tracks stale, expired-auth, degraded, and healthy states.
- **FR-CONN-008** Canvas connector supports OAuth2 and institution/base-URL binding.
- **FR-CONN-009** Canvas connector reads courses, assignments, submissions, and announcements if feasible.
- **FR-CONN-010** Canvas connector emits normalized coursework and deadline events.

## Event and rule requirements
- **FR-EVT-001** Normalized event schema includes ids, timestamps, dedupe key, payload, trace ref.
- **FR-EVT-002** Raw vendor records are never used directly by rule evaluation.
- **FR-RULE-001** Rule engine evaluates normalized events plus current state into decisions.
- **FR-RULE-002** Rule engine supports priority, cooldown, duration, and explanation templates.
- **FR-RULE-003** Rule engine outputs reward, penalty, and enforcement intents.
- **FR-RULE-004** Rules are represented as data, not hardcoded branches in connectors or UI.
- **FR-RULE-005** The system exposes a limited MVP rule builder.

## Reward and penalty requirements
- **FR-STATE-001** Reward wallet persists earned credits, spent credits, streaks, and bonuses.
- **FR-STATE-002** Penalty state persists escalation tier, bypass budget, lockout windows, and debt.
- **FR-STATE-003** Reward state and penalty state mutate independently.
- **FR-STATE-004** Every state mutation produces an auditable reason trail.

## Enforcement requirements
- **FR-ENF-001** Enforcement driver contract is portable and platform-agnostic.
- **FR-ENF-002** iOS enforcement driver applies policy using native Screen Time APIs.
- **FR-ENF-003** Android enforcement driver applies policy using native Android services/capabilities.
- **FR-ENF-004** Existing enforcement remains active during connector outages.
- **FR-ENF-005** The system distinguishes permission failure from stale data from degraded enforcement.
- **FR-ENF-006** Unlock proof subsystem supports pluggable proof mechanisms.
- **FR-ENF-007** Enforcement actions are explainable to the user.

## Persistence and audit requirements
- **FR-DATA-001** Local persistence stores connectors, cursors, normalized events, rules, reward state, penalty state, policies, unlock sessions, and audit records.
- **FR-DATA-002** Secrets and tokens live in OS secure storage.
- **FR-DATA-003** Audit log records syncs, rule evaluations, policy applications, and unlock decisions.
- **FR-DATA-004** System must remain functional offline using last-known valid policy and state.

## Client UX requirements
- **FR-UX-001** Onboarding configures enforcement before advanced connector logic.
- **FR-UX-002** The product offers first-run templates for schoolwork-driven rules.
- **FR-UX-003** The product surfaces current wallet, penalty, and active rule explanations.
- **FR-UX-004** The product surfaces connector health and auth freshness.

---

# Repository and Package Layout

```txt
focus-platform/
├── Cargo.toml
├── rust-toolchain.toml
├── README.md
├── PRD.md
├── ADR.md
├── FUNCTIONAL_REQUIREMENTS.md
├── PLAN.md
├── AGENTS.md
├── CLAUDE.md
├── docs/
│   ├── adr/
│   ├── research/
│   ├── guides/
│   ├── reports/
│   └── reference/
├── crates/
│   ├── focus-domain/
│   ├── focus-connectors/
│   ├── focus-rules/
│   ├── focus-events/
│   ├── focus-rewards/
│   ├── focus-penalties/
│   ├── focus-policy/
│   ├── focus-sync/
│   ├── focus-storage/
│   ├── focus-audit/
│   ├── focus-crypto/
│   ├── focus-time/
│   ├── focus-ffi/
│   ├── connector-canvas/
│   ├── connector-testkit/
│   └── focus-cli/
├── apps/
│   ├── ios/
│   ├── android/
│   ├── desktop-admin/        # optional later, Tauri or other
│   └── web-admin/            # optional later, TS only if justified
├── services/
│   ├── auth-broker/          # optional, Go or Rust
│   ├── webhook-ingest/       # optional, Go or Rust
│   └── sync-api/             # optional, Go or Rust
├── scripts/
│   ├── dev/
│   ├── release/
│   └── ci/
└── examples/
    ├── sample-rules/
    └── sample-connectors/
```

## Crate responsibilities

### `focus-domain`
Canonical domain entities, aggregate roots, invariants, common IDs, result types.

### `focus-events`
Normalized event schema, event factories, dedupe semantics, event serialization.

### `focus-connectors`
Connector traits, manifest models, auth abstractions, sync contracts, health models.

### `connector-canvas`
Canvas-specific adapter implementing the connector contracts.

### `focus-rules`
Rule DSL/model, evaluation engine, conflict resolution, priorities, cooldowns, explanations.

### `focus-rewards`
Reward wallet aggregate and mutation logic.

### `focus-penalties`
Penalty aggregate and escalation logic.

### `focus-policy`
Enforcement policy generation from rule decisions and user-configured app targets.

### `focus-sync`
Polling scheduler, cursor progression, dedupe, retries, reconciliation.

### `focus-storage`
Storage ports and SQLite implementations. Optional sync-ready models.

### `focus-audit`
Audit record model and append-only writer APIs.

### `focus-crypto`
Token wrapping, secure-storage helpers, integrity utilities.

### `focus-time`
Clock abstraction and deterministic time injection for tests.

### `focus-ffi`
Rust FFI export surface for Swift and Kotlin clients.

### `focus-cli`
Dev and test CLI for connector sync, rule evaluation, fixture replay, and audit inspection.

## Native client layout

### `apps/ios/`
- SwiftUI shell
- iOS onboarding
- permission and entitlement handling
- Screen Time adapter
- NFC / local unlock proof UX
- Rust FFI binding layer

### `apps/android/`
- Kotlin + Compose shell
- Android onboarding
- UsageStats/Accessibility/service lifecycle
- Android enforcement adapter
- Rust JNI/bridge layer

---

# Ports and Adapters Map

## Inbound ports
- `UserCommandPort`
- `ConnectorWebhookPort`
- `SyncTriggerPort`
- `TimerEventPort`
- `EnforcementCallbackPort`

## Outbound ports
- `EnforcementDriver`
- `ConnectorRuntime`
- `ConnectorAuthPort`
- `EventStore`
- `RuleStore`
- `WalletStore`
- `PenaltyStore`
- `AuditStore`
- `SecureSecretStore`
- `NotifierPort`
- `ClockPort`

## Adapter map

### Swift adapters
- `IosEnforcementDriver`
- `IosNfcUnlockAdapter`
- `IosNotificationAdapter`
- `IosSecureStoreAdapter`

### Kotlin adapters
- `AndroidEnforcementDriver`
- `AndroidNotificationAdapter`
- `AndroidSecureStoreAdapter`

### Rust adapters
- `CanvasConnectorAdapter`
- `SqliteEventStore`
- `SqliteRuleStore`
- `SqliteWalletStore`
- `SqlitePenaltyStore`
- `AuditLogStore`

### Optional service adapters
- `OAuthCallbackService`
- `WebhookIngestService`
- `SyncApiService`

---

# Milestones and Work Breakdown

## Phase 0 — Foundation and architecture lock

### WP-0001 Repository bootstrap
Deliverables:
- Cargo workspace
- root docs scaffold
- CI baseline for fmt, clippy, tests
- native app directory scaffolds

### WP-0002 Domain contracts
Deliverables:
- domain IDs and aggregates
- connector traits
- normalized event schema
- enforcement driver interface
- audit model

### WP-0003 ADR lock
Deliverables:
- ADR-001 through ADR-009 written and accepted
- stack boundary decisions frozen for MVP

## Phase 1 — Rust core MVP

### WP-0101 Event system
Deliverables:
- normalized event types
- dedupe model
- serialization
- trace references

### WP-0102 Rule engine MVP
Deliverables:
- simple rule model
- priority resolution
- cooldowns
- explanation templates
- unit test matrix

### WP-0103 Reward and penalty aggregates
Deliverables:
- wallet aggregate
- penalty aggregate
- mutation rules
- audit hooks

### WP-0104 Storage and audit
Deliverables:
- SQLite schema
- secure token abstractions
- append-only audit writer

## Phase 2 — iOS MVP

### WP-0201 iOS shell
Deliverables:
- SwiftUI app shell
- FFI wiring
- onboarding skeleton

### WP-0202 iOS enforcement adapter
Deliverables:
- target selection
- policy apply/remove
- unlock session bridge
- permission/error state model

### WP-0203 iOS unlock proof MVP
Deliverables:
- delay proof
- QR or NFC proof
- unlock explanation screen

## Phase 3 — Canvas connector MVP

### WP-0301 Canvas auth and account binding
Deliverables:
- OAuth2 flow
- base URL/institution binding
- token storage

### WP-0302 Canvas sync and normalization
Deliverables:
- course sync
- assignment sync
- submission sync
- normalized event emitters
- cursoring and retries

### WP-0303 Canvas rules templates
Deliverables:
- prebuilt reward templates
- prebuilt penalty templates
- first-run setup flow for academic mode

## Phase 4 — Android MVP

### WP-0401 Android shell
Deliverables:
- Kotlin/Compose shell
- JNI/bridge wiring
- onboarding skeleton

### WP-0402 Android enforcement adapter
Deliverables:
- service/permission lifecycle
- policy apply/remove
- unlock session bridge
- degraded-state handling

### WP-0403 Android hardening
Deliverables:
- reboot persistence strategy
- service death recovery
- permission drift detection

## Phase 5 — Optional backend and multi-device sync

### WP-0501 OAuth/webhook edge service
Deliverables:
- auth callback endpoint
- webhook intake endpoint
- connector health reporting

### WP-0502 Multi-device state sync
Deliverables:
- user/device model
- state merge rules
- conflict handling

### WP-0503 Remote observability
Deliverables:
- sync telemetry
- rule evaluation metrics
- enforcement outcome metrics

---

# Test Strategy

## Rust core tests
- unit tests for aggregates and rule evaluation
- property tests for event normalization and rule invariants
- fixture replay tests for Canvas payloads
- storage round-trip tests
- audit integrity tests

## iOS tests
- adapter contract tests against mocked core intents
- permission-state tests
- unlock flow tests
- UI integration tests for explanations and setup

## Android tests
- adapter contract tests
- service lifecycle and permission drift tests
- unlock flow tests
- UI integration tests

## End-to-end tests
- replay Canvas fixtures into sync engine
- evaluate rules
- generate enforcement intents
- assert wallet/penalty/audit outcomes

---

# Traceability Skeleton

## Rule trace format
Every decision should be traceable as:
- source connector account
- normalized event ids
- matched rule ids
- prior state snapshot ref
- resulting mutations
- resulting enforcement intent
- user-visible explanation

## Example trace
1. Event `assignment_due_soon`
2. Rule `schoolwork_due_today_requires_lockdown`
3. Penalty mutation `tier += 1`
4. Enforcement intent `block entertainment category until 21:00`
5. Explanation generated and stored in audit

---

# Initial backlog seeds

- `EPIC-001` Rust domain core
- `EPIC-002` iOS enforcement MVP
- `EPIC-003` Canvas connector MVP
- `EPIC-004` Android enforcement MVP
- `EPIC-005` Optional backend sync plane
- `EPIC-006` Admin/analytics surfaces

# Blunt stack conclusion
The architecture should be:
- **Rust first** in the center
- **Swift and Kotlin** at the mobile boundaries
- **Go optional** for small service edges
- **Zig optional** for niche systems/build tooling
- **TS/Python last** and kept out of core logic

And the product should remain **hexagonal and polyglot by boundary, not polyglot by chaos**.

Done. I expanded it into:

*   a full **ADR pack**
*   a **functional requirements index**
*   a **repo/package layout**
*   a **ports/adapters map**
*   a phased **milestone + work-package breakdown**
*   a **test strategy**
*   a **traceability skeleton**
*   initial **epic/backlog seeds**

The stack line is now explicit and hard:

*   **Rust first** in the core
*   **SwiftUI** for iOS
*   **Kotlin/Compose** for Android
*   **Go optional** for small service edges
*   **Zig optional** for targeted tooling
*   **TS/Python last** and kept out of core logic

Also locked in:

*   native mobile shells over framework tourism
*   connector runtime as a first-class product surface
*   reward and penalty as separate aggregates
*   enforcement adapters forbidden from containing business logic
*   Tauri/Electron only as later control-plane/admin surfaces, not primary enforcement clients

The document is in the canvas and ready for the next step.

The right next move is to turn this into the repo’s canonical root docs set:  
**`PRD.md` + `ADR.md` + `FUNCTIONAL_REQUIREMENTS.md` + `PLAN.md` + `AGENTS.md` skeletons** with numbered ADR files and work-package IDs.

## Prompt:
4/22/2026, 5:57:22 PM

Let's talk the connectors which we really want to encourage a community aspect to to help . grow this app. View this app as a bootstrapped serious startup idea. Never seeded or plan to be seeded.

## Response:
4/22/2026, 5:57:22 PM

> Thought for 4s

Then the connector system cannot be just an internal plugin API. It has to be a **product surface**, a **distribution surface**, and a **community moat**.

If this is a serious bootstrap company and you do not plan to raise, then connectors are one of the few parts that can compound without linear payroll growth.

The right framing is:

**the blocker app is the wedge**  
**the connector ecosystem is the compounding engine**

The strategic goal
------------------

You want third parties and power users to help answer:

*   “Can this app work with my school/work/life stack?”
*   “Can I make it useful for my weird niche workflow?”
*   “Can I contribute support for the system I already use?”

That means your connector model needs to be:

*   easy to understand
*   hard to abuse
*   safe to install
*   powerful enough to be worth contributing to
*   constrained enough that low-quality junk does not rot the platform

If you get this right, the community expands your TAM without you hiring a giant integrations team.

What connectors should be, strategically
----------------------------------------

There are really **four connector classes**, and you should treat them differently.

### 1\. First-party flagship connectors

These are the ones you build and maintain because they define the product category.

Examples:

*   Canvas
*   Google Calendar
*   Todoist
*   Google Classroom
*   Notion
*   GitHub
*   Slack
*   Apple Health / Google Fit class equivalents where relevant

These are:

*   high-value
*   common
*   good for marketing
*   good for onboarding templates
*   good for “this app actually works” credibility

These are your **core SKU multipliers**.

### 2\. Community connectors

These are long-tail systems the community builds.

Examples:

*   specific LMSes
*   niche university portals
*   enterprise ticket systems
*   weird productivity apps
*   game launchers
*   habit apps
*   finance apps
*   home automation systems
*   self-hosted tools

These are your **coverage moat**.

### 3\. Private/local connectors

These are user-authored or org-authored connectors that never go public.

Examples:

*   a custom school portal
*   a personal webhook source
*   a private Notion database convention
*   a family accountability workflow
*   an internal API at someone’s company

These matter because serious users often have one weird thing that makes or breaks stickiness.

### 4\. Derived/meta connectors

These do not talk to a third-party source directly. They transform or combine signals.

Examples:

*   “all\_due\_today” aggregator
*   “study\_day\_score”
*   “late-night-risk” behavioral model
*   “semester stress mode”
*   “reward broker”
*   “multi-source obligation scorer”

These are incredibly important because they make the ecosystem more than a pile of adapters.

The business truth
------------------

A connector ecosystem can help a bootstrap startup grow, but only if it creates one or more of these:

*   more install/use cases
*   more retention
*   more user-generated expansion
*   more public discoverability
*   more switching costs
*   more template sharing/network effects

If connectors are just “integration checkboxes,” they do not matter enough.

You want connectors to produce:

*   **templates**
*   **recipes**
*   **marketplace pages**
*   **SEO surfaces**
*   **community bragging / sharing**
*   **viral niche adoption**

Example:

Not just:

*   “Canvas connector available”

But:

*   “Canvas: 12 community rule packs”
*   “ASU student rule pack”
*   “premed semester survival pack”
*   “law school blackout pack”
*   “ADHD-friendly soft punishments pack”
*   “exam week lockdown template”
*   “GitHub + Todoist sprint mode pack”

That is way more defensible than raw integrations.

The ecosystem model I’d push
----------------------------

You should think in terms of a **three-layer ecosystem**:

### Layer 1: Connectors

Source adapters that emit normalized events.

### Layer 2: Rules packs / templates

Reusable logic built on top of those events.

### Layer 3: Unlock mechanics / enforcement behaviors

What the product does in response.

That means the community can contribute at more than one level.

Some people can build connectors.  
Most cannot.

But many more people can build:

*   rules packs
*   course/study modes
*   punishment ladders
*   reward economies
*   life-system templates

That is critical. If contribution requires writing connector code, your community will stay small.

What to open vs what to keep closed
-----------------------------------

Since this is a bootstrap serious startup, do **not** fully open everything.

You want a **selectively open ecosystem**, not total openness.

### Open:

*   connector SDK/spec
*   normalized event schema
*   manifest format
*   connector packaging spec
*   local dev tools
*   simulator/fixture framework
*   template/rules pack format
*   community submission path
*   docs
*   example connectors

### Probably closed or tightly controlled:

*   native enforcement internals
*   anti-bypass logic details
*   ranking/reputation systems
*   premium marketplace distribution controls
*   signing/verification services
*   any proprietary analytics or trust-scoring
*   app store distribution specifics
*   monetization levers

Why?

Because the connector community helps distribution and retention, but the **real product power** is still the combination of:

*   reliable enforcement
*   anti-bypass UX
*   great onboarding
*   tasteful product design
*   trust/safety and packaging
*   high-quality flagship connectors
*   smart rule templates

Do not give away the whole company in the name of “community.”

The connector product should feel like this
-------------------------------------------

A connector should not be perceived as code first.

It should be perceived as:

*   a capability
*   a listing
*   a trust object
*   a reusable building block

Each connector page should have:

*   name
*   what it can read
*   what events it emits
*   required permissions
*   who maintains it
*   verification status
*   install count
*   last updated
*   sample rules/templates
*   risk level
*   privacy notes

That turns connectors into real product assets.

Verification tiers
------------------

You need trust tiers from day one.

### Tier A — First-party verified

Maintained by you. High trust.

### Tier B — Community verified

Maintained by community, but reviewed, tested, signed, and listed officially.

### Tier C — Unverified local

Importable locally, maybe hidden behind advanced mode, but not listed in the public marketplace.

Without this, you get connector slop, broken auth, privacy disasters, and user mistrust.

What the SDK should optimize for
--------------------------------

If you want community contribution, the SDK needs to be **boring** and **strict**.

A good connector author should only need to care about:

*   auth
*   fetch
*   map to normalized events
*   declare capabilities
*   handle cursors/checkpoints
*   provide fixtures/tests

Not about:

*   core app internals
*   enforcement APIs
*   wallet logic
*   rules engine internals

That means the connector contract should be extremely narrow.

Something like:

*   `manifest`
*   `authorize`
*   `refresh_auth`
*   `sync`
*   `disconnect`
*   `healthcheck`

That is it.

Packaging model
---------------

You have three realistic packaging options.

### Option 1: Built-in compiled connectors

Safest, simplest, weakest for community scale.

### Option 2: Signed connector bundles

Best long-term answer.

A connector bundle contains:

*   manifest
*   adapter code or declarative mapping logic
*   fixtures
*   tests
*   icon/metadata
*   capability declaration

Signed by:

*   you for official/community-verified listings
*   user-local self-sign or unsafe mode for private connectors

### Option 3: Fully remote connector execution

Most scalable for complex integrations, but introduces trust and hosting complexity.

For bootstrap, I would not start here as the default.

What I would actually do
------------------------

For a bootstrap startup, I would use a **hybrid model**:

### MVP

*   first-party connectors compiled into app/backend
*   community **rules packs/templates** open much earlier than community connectors
*   connector SDK/spec published early but marked experimental
*   one or two example connectors as reference

### V1 ecosystem

*   signed connector bundles
*   local connector dev kit
*   connector simulator + fixtures
*   public connector registry
*   verification process
*   template marketplace

### V2

*   optional hosted connector runtime for harder connectors
*   org/private registries
*   premium verified connector program
*   connector analytics for maintainers

This is the right bootstrap order because:

*   rules/templates give you community motion sooner
*   connectors come later once trust/distribution infra is real
*   you avoid drowning in support burden too early

The biggest mistake to avoid
----------------------------

Do **not** launch with a “build anything” plugin story before you have:

*   stable normalized event schema
*   stable connector manifest
*   review/signing flow
*   fixture-based test harness
*   clear trust tiers
*   connector UX in the app

Otherwise you will get:

*   brittle connectors
*   angry users
*   no trust
*   huge support load
*   no real moat

Community growth loops you actually want
----------------------------------------

Here is how connectors help growth in a bootstrap context.

### Loop 1: niche coverage

A user wants support for some system.  
They or someone else builds it.  
That unlocks a whole niche market.

### Loop 2: template virality

A connector enables a popular rules pack.  
That rules pack gets shared in communities.

### Loop 3: contributor identity

People like seeing “maintainer of the Canvas Honors Student Pack” or “maintainer of Blackboard connector.”

### Loop 4: SEO/indexed pages

Every connector and rule pack becomes a landing page:

*   “Canvas app blocker”
*   “ADHD study mode app blocker”
*   “Notion screen time rewards”
*   “GitHub productivity lockout”

That matters a lot when bootstrapped.

### Loop 5: institution clusters

One student community or one workplace adopts templates tied to a shared connector ecosystem.  
That creates natural local network effects.

Monetization angle without poisoning the ecosystem
--------------------------------------------------

You do not need seed money if monetization is clean and the product is sticky.

Possible model:

### Free

*   basic blocking
*   a few first-party connectors
*   community templates
*   local-only usage

### Paid

*   premium flagship connectors
*   multi-device sync
*   advanced rule engine
*   stronger unlock mechanics
*   verified marketplace access
*   private connector hosting
*   analytics/history
*   institution/family packs
*   premium anti-bypass features

### Marketplace revenue later

*   paid premium template packs
*   paid premium verified connectors
*   optional rev share with maintainers

But do not rush this. Early on, ecosystem density matters more than extracting every dollar.

Governance model
----------------

You need connector governance like a mini package ecosystem.

At minimum:

*   semantic versioning
*   API/schema compatibility policy
*   deprecation windows
*   fixture/test requirements
*   permission declaration requirements
*   privacy declaration requirements
*   signing/verification process
*   maintainer policy
*   abuse/report flow

Without governance, community ecosystems rot.

The real moat
-------------

If you do this well, the moat is not just “we integrate with Canvas.”

The moat becomes:

*   best enforcement UX
*   best connector model
*   best rules/template ecosystem
*   best long-tail coverage
*   strongest trust and verification
*   best lifecycle around real obligations

That is a real bootstrap company shape.

What I would prioritize first
-----------------------------

In order:

1.  **Flagship connectors**
    *   Canvas
    *   Google Calendar
    *   Todoist
2.  **Template ecosystem**
    *   school packs
    *   work packs
    *   ADHD / soft-friction packs
    *   strict-mode packs
3.  **Connector SDK spec**
    *   published early
    *   community interest building
    *   but not fully opened until stable
4.  **Verification and registry**
    *   listing pages
    *   trust tiers
    *   test harness
5.  **Community connectors**
    *   after you have real product-market pull

Because bluntly: a community connector platform with no core user demand is just unpaid architecture cosplay.

My recommendation
-----------------

Treat the connector strategy as:

**First-party connectors create credibility.**  
**Community templates create growth.**  
**Community connectors create coverage and moat.**

That ordering matters.

If you want, I’ll turn this into a **connector ecosystem strategy doc** with:

*   governance model
*   registry architecture
*   verification flow
*   maintainer incentives
*   monetization plan
*   MVP vs V1 vs V2 rollout.

## Prompt:
4/22/2026, 5:59:36 PM

Mascot? Perhaps mix of the mee2 from Rick and morty design -> flat blob character design reminiscent of typical amorphic corporate Memphis like mascots in these sorts of apps, w duolingo's fiery personality and llm based responses / adjustments to character model (e.g. Complex one I'll just say spline since that's the one concept I understand that the llm can play with for complex change of pose emotion etc

Other aiml and general smart or intelligent and learning features as relevant too

## Response:
4/22/2026, 5:59:36 PM

Thought for 1m 30s

Edit



---
Powered by [ChatGPT Exporter](https://www.chatgptexporter.com)