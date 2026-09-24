# Architecture and ownership reconciliation

**v0.2 scope clarification:** the direct user message reserves the GUI/application layer for BytePort and asks this work to stay at API/automation planning. Logical roles below do not authorize a new GUI, another controller, or repository migration. The recalled PhenotypeActions is a discovery target, not a confirmed owner. Local dev placement and typed non-web release profiles are defined in documents 17–18. [S032; E001–E005]

**Status: proposed logical architecture. Repository destinations are not implementation-completeness claims.**

## Architecture in one paragraph

Use an application contract to describe intent; resolve it against an observed target’s capabilities; construct an immutable release candidate; have the existing verification/review path assess that candidate; obtain authorized approval; and let **one trusted actuator** reconcile the approved candidate. Runtime, ingress and provisioning integrations implement explicit ports. Logs and receipts report what actually happened. The UI is a client of this flow, not a separate deployment authority.

```text
Application repo + pinned artifact + config references
                         |
                 Contract / plan compiler
                         |
        Capability check + immutable release candidate
                         |
 Existing checks / review adjudication / human authorization
                         |
             ONE trusted deployment actuator
              /              |              \
       Runtime adapter  Ingress adapter  Provisioning request
       Podman / WSLC    private/public   one IaC state owner
              \              |              /
                Observed state + receipts
                         |
       Existing evidence, audit and observability consumers
```

The diagram is a proposed component boundary, not a report that this complete system exists. [S002–S007]

## Preserve ownership by role

| Concern | Evidence-backed role or candidate | Required reconciliation |
|---|---|---|
| Ecosystem index | phenotype-registry | Link approved artifacts; do not copy all contracts into a second index. |
| Cross-repository contracts and ADRs | PhenoSpecs | Reconcile its current spec index and change process. |
| Shared machine types/schema implementation | phenotype-types | Generate or adopt the domain contract under the existing type owner. |
| Conventions and reusable explanations | PhenoHandbook | Keep guidance distinct from authoritative deployment state. |
| Policy enforcement workflows | phenotype-org-governance | Inspect actual active workflows and settings before modifying gates. |
| Code-review orchestration | Existing reviewer integration; domain map names **tehgent** | Do not confuse it with **thegent** agent runtime or install a duplicate bot. |
| Deployment product/API/UI | BytePort logical candidate | README explicitly reserves some delivery behavior as planned. |
| Runtime/app-graph implementation | PhenoCompose / nanovms / thegent / phenotype-infra declarations | Resolve actual module and consumer locations; no new independent graph store by default. |
| Consolidated infrastructure implementation | phenotype-infra candidate | Preserve its declared human-apply boundary pending current authoritative review. |
| Auth/secrets | Authvault | Confirm actual integration rather than replacing it with a bespoke secret service. |
| Testing and observability | TestingKit / PhenoObservability | Attach conformance tests and receipts to the existing consumers. |
| Audit/program evidence | Existing audit/Tracera-related workflow | Import into the actual ledger contract; no invented second global ledger. |

Sources: S002–S007. These are observed document declarations, not proof that every listed integration is implemented.

## Resolve the apparent overlap before splitting or merging code

For each deploy/runtime concern, identify the active executable, package imports, API consumers, integration tests, release artifact, ownership ADR and migration receipt. Then choose one of: **canonical existing**, **canonical with missing implementation**, **deprecated compatibility shim**, **migration still in progress**, or **unresolved**. A README saying “merged” does not by itself justify archival; a README saying “planned” does not prove a feature is absent from every branch.

The useful question is not “Which repository has the right name?” It is “Which implementation owns this state transition today, and what is the supported entry point for consumers?” Create an ownership delta with references before proposing code movement. Do not bulk-rename, absorb, archive or delete repositories from this package.

## Ports and minimum responsibilities

| Port | Read operations | Mutating operations | Must not own |
|---|---|---|---|
| Contract compiler | Validate intent, resolve refs, capability report, generate plan | Publish a content-addressed candidate | Running services or credentials |
| Review/gate integration | Fetch trusted checks, adjudicate findings, evaluate policy | Record review/authorization receipts | Runtime socket or arbitrary host shell |
| Deployment actuator | Observe generation and health; verify approval | Apply approved generation; explicit rollback | Candidate-controlled arbitrary provisioning scripts |
| Runtime adapter | Discover, inspect, logs, stats, health | Create/start/stop approved workloads | Global review policy or DNS policy |
| Ingress adapter | Inspect routes, protocol and identity policy | Apply approved route generation | Runtime selection or secret authority |
| Provisioning owner | Preview inventory and state | Apply one authorized IaC plan | Independently auto-updating actuator-owned containers |
| Evidence consumer | Index receipts, display freshness, correlate traces | Append audit events through existing interfaces | Granting approval based on an LLM summary |

All mutating ports require scope, candidate identity, generation precondition, lease/idempotency context and authorization evidence. Read APIs must not imply permission to mutate.

## Single-writer rule at practical boundaries

Quadlet may own the lifecycle of a container service. In that case Pulumi may provision its host, network prerequisites or secret references, but must not separately reconcile that same container object. Conversely, a qualified PaaS may own an application deployment; the outer actuator then delegates to that PaaS and does not also start replacement containers directly. One owner can delegate, but two independent desired-state loops must not race.

An optional UI such as Cockpit is an observation surface by default. Any administrative write is an explicit break-glass or approved operation that produces drift/reconciliation receipts. The presence of a UI does not justify bypassing the control path. [S021; design proposal]

## Counterexamples this architecture must survive

A failed apply must not be made green by the UI. An independently triggered review bot must not start infinite review rounds. A human approval must not survive a changed image digest. A managed provider accepting an API call must not be reported as a healthy service before observation. A runtime adapter must be allowed to say **unsupported**, rather than silently reducing the requested isolation or persistence.
