# Federation requirement catalog

All entries are proposed implementation obligations linked to INT-005, not claims about live product behavior. Existing stronger accepted contracts remain.

## FED-01-01 — Independent base usefulness

Each qualified application shall remain usable with its declared base dependencies when optional peers or App Center are absent.

**Acceptance:** Launch A without B and complete its base task; missing base dependency is explicit, not mocked.

**Critical:** true · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-01-02 — Host-relative primary perspective

Opening an app deliberately shall choose that window/workspace perspective without changing authoritative records.

**Acceptance:** Open A and B concurrently on one subject; chrome differs but object IDs/state authorities agree.

**Critical:** true · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-01-03 — Separate operation kinds

Source consolidation, installation, runtime composition, view composition and data migration shall be represented as different operations.

**Acceptance:** Installing an extension neither rewrites repositories nor migrates domain data.

**Critical:** true · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-01-04 — Stable scoped identities

Packages, products, applets, processes, bindings, users, workspaces and surfaces shall have distinct stable scoped identifiers.

**Acceptance:** A rename or second host does not create a second logical task or broaden scope.

**Critical:** true · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-01-05 — Bounded recursive exports

A composite shall declare exactly the capabilities and obligations it re-exports.

**Acceptance:** A nested consumer cannot call an unexported child operation or see child-only private settings.

**Critical:** true · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-01-06 — Meaningful reciprocity

Supported integration directions shall be explicit; reciprocal support shall not be inferred from one embedded panel.

**Acceptance:** Exercise both declared host directions; unsupported directions are shown as unsupported.

**Critical:** false · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-01-07 — Optional app-center UI

The visible App Center shall not be required to launch/use already-qualified independent apps and bindings.

**Acceptance:** Disable the Center UI; the selected local base and valid cached binding still work.

**Critical:** false · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-01-08 — No silent default takeover

New installation or background activation shall not change a user-selected provider or primary perspective silently.

**Acceptance:** Install a competing provider while editing and verify pinned routes/focus remain unchanged.

**Critical:** true · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-02-01 — Typed capability manifests

Installed providers shall expose bounded validated metadata describing versions, interfaces, scopes and host support.

**Acceptance:** Reject oversized/malformed manifests and incompatible contract profiles before activating code.

**Critical:** true · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-02-02 — Source-backed artifact identity

Discovery shall bind metadata to an actual trusted package/artifact under explicit policy.

**Acceptance:** A copied display name or mismatched digest cannot activate a trusted binding.

**Critical:** true · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-02-03 — Install-order convergence

Given the same packages and policy, supported A-then-B and B-then-A installs shall converge to the same selected capabilities.

**Acceptance:** Run both clean install orders; compare resolved plans excluding permitted instance-local IDs.

**Critical:** false · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-02-04 — Lazy activation

Metadata discovery shall not launch every provider or its entire desktop UI.

**Acceptance:** Install multiple idle providers; measure zero unrequested heavy backend activations.

**Critical:** false · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-02-05 — Deterministic provider selection

The resolver shall honor valid user pins, compatible policy and deterministic ambiguity handling.

**Acceptance:** Provide two candidates; show why one is selected or require a choice rather than oscillating.

**Critical:** false · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-02-06 — Separate discovery and permission

Presence shall not imply permission; scopes must be sufficient for the exact binding and operation.

**Acceptance:** Co-install a provider requiring new private data; activation remains awaiting consent or denied.

**Critical:** true · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-02-07 — Inspectable adaptation

Learned suggestions and preferences shall be scoped, explainable, reversible and not executable authority.

**Acceptance:** Reject auto-execution of newly generated adapter code; reset a preference without deleting data.

**Critical:** true · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-02-08 — Incremental reconciliation

Changed package/policy observations shall invalidate affected bindings without rebuilding unrelated workspaces.

**Acceptance:** Update one provider; retain unrelated known-good bindings and distinguish incomplete inventory.

**Critical:** false · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-03-01 — Contextual host contributions

Contributions shall use declared slots and context/enablement rules instead of nesting complete app chrome by default.

**Acceptance:** Mount a relevant panel and command; unrelated provider navigation does not invade the host.

**Critical:** false · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-03-02 — Stable object handoff

Host transitions shall carry permitted object references and versions without manual ID/path copying.

**Acceptance:** Open the same task in both perspectives and preserve selection, source identity and permission.

**Critical:** true · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-03-03 — Focus and shortcuts

One view shall own each input event, with documented host/platform shortcut precedence.

**Acceptance:** Test keyboard, IME, accessibility and conflicting shortcuts without duplicate invocation.

**Critical:** true · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-03-04 — Semantic accessibility

Native/semantic integration claims shall include verified accessible structure and focus behavior.

**Acceptance:** Screen-reader and keyboard users complete the workflow; remoted pixels advertise their limits.

**Critical:** true · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-03-05 — Consistent command semantics

Menus, palette, shortcuts, CLI and API entrypoints shall invoke the same authorized command contract.

**Acceptance:** An invisible or disabled menu does not bypass backend authorization through another entrypoint.

**Critical:** true · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-03-06 — Explicit undo semantics

Commands shall declare local undo, compensation or irreversibility; multi-owner actions must report partial outcomes.

**Acceptance:** Abort a cross-owner operation and observe defined compensation rather than fictional global rollback.

**Critical:** true · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-03-07 — Unified bounded status

Shared search, progress, notifications and settings views shall preserve owner namespaces and avoid duplicate signals.

**Acceptance:** One operation produces one appropriate notification per audience; denied search content never appears.

**Critical:** true · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-03-08 — Richness with graceful reduction

Motion, materials and optional 3D content shall have usable low-resource, reduced-motion and contrast alternatives.

**Acceptance:** Run the complete task under reduced-motion/high-contrast and the accepted low-resource profile.

**Critical:** false · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-04-01 — Explicit binding state

Installed, resolved, authorized, active, degraded, quiescing and detached states shall be separately observable.

**Acceptance:** A process that starts but fails readiness cannot appear as an active required capability.

**Critical:** true · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-04-02 — Idempotent reconcile

Repeated package events and retries shall not duplicate services, commands, migrations or jobs.

**Acceptance:** Deliver the same event repeatedly and compare durable resulting bindings and side effects.

**Critical:** true · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-04-03 — Recover unknown outcomes

A lost acknowledgment shall trigger operation-ID reconciliation before a mutation is repeated.

**Acceptance:** Kill the host after provider acceptance; resume without executing a duplicate mutation.

**Critical:** true · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-04-04 — Versioned active plans

Updates shall not silently replace in-use contracts or a pinned provider.

**Acceptance:** Update B while A edits; the active version is stable until an approved safe transition.

**Critical:** true · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-04-05 — Safe quiescence

Removal or update shall drain/cancel/checkpoint work under a declared lifecycle and lease policy.

**Acceptance:** Attempt detach during a long operation; report its completion/cancellation and unresolved effects.

**Critical:** true · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-04-06 — Honest hot-unload support

Providers shall declare whether live replacement is supported or a restart is needed.

**Acceptance:** A native non-unloadable adapter requests restart rather than freeing active resources.

**Critical:** true · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-04-07 — Uninstall is not deletion

Uninstall or detach shall preserve authoritative user data unless separately authorized for deletion.

**Acceptance:** Uninstall and reinstall B; A base use survives and owned data remains recoverable.

**Critical:** true · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-04-08 — Reference-aware termination

Closing a view or removing one consumer shall not kill another valid consumer or orphan an unowned process.

**Acceptance:** Two hosts share a permitted instance; close one, then both, and inspect leases/background policy.

**Critical:** true · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-05-01 — Scoped delegated authority

Operations shall bind user/workspace/resource/audience/action/expiry and enforce revocation.

**Acceptance:** A valid token for workspace X or audience B fails against workspace Y or audience C.

**Critical:** true · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-05-02 — Provider-side enforcement

Each provider shall check request scope and object-version preconditions, independently of UI visibility.

**Acceptance:** Bypass the host menu and send a forbidden operation; the provider rejects it.

**Critical:** true · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-05-03 — No credential copying

Integration shall use scoped references/brokering rather than a universal shared credential configuration.

**Acceptance:** Inspect distributed artifacts, traces and configs for real secrets; another app cannot read owner tokens.

**Critical:** true · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-05-04 — Explicit data owners

Each state contract shall name its writer authority, read projections and consistency/migration semantics.

**Acceptance:** Edit from two hosts; detect conflicts and retain one defined authority rather than divergent copies.

**Critical:** true · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-05-05 — Trust-matched isolation

In-process, web, process, VM and network modes shall be selected by compatible trust and performance policy.

**Acceptance:** An untrusted extension cannot enter a high-trust native host merely because its interface matches.

**Critical:** true · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-05-06 — Safe external inputs

Manifests, routes, deep links, contexts and integration messages shall be bounded and validated as data.

**Acceptance:** Reject malicious schemes, traversal, context substitution and prompt-like policy overrides.

**Critical:** true · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-05-07 — Derived-data privacy

Caches, search, telemetry, screenshots and generated summaries shall inherit source sensitivity.

**Acceptance:** Revoke access; stale previews/counts/snippets cannot reveal restricted source content.

**Critical:** true · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-05-08 — Inspectable exit

Users shall be able to see providers/permissions/state owners and detach or export under documented contracts.

**Acceptance:** Complete a detach/export workflow without forced account sign-in or unrelated product install.

**Critical:** false · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-06-01 — No recursive shell loop

Mount graphs and strict startup dependencies shall be acyclic for the initial supported profile.

**Acceptance:** Reject A-shell-in-B-shell-in-A-shell and a circular required startup plan.

**Critical:** true · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-06-02 — Bounded cyclic event protocols

Permitted event cycles shall carry origin/correlation/deduplication and bounded feedback policies.

**Acceptance:** Create a reflected event; verify it does not become an unbounded command or notification loop.

**Critical:** true · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-06-03 — Scope-safe service reuse

Shared instances shall require compatible principal, workspace, configuration, tenancy and isolation.

**Acceptance:** Requests from separate tenants are isolated despite identical command or provider names.

**Critical:** true · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-06-04 — Locality-aware lowering

Same-process/host composition shall use an appropriate qualified local path where feasible, not compulsory network RPC.

**Acceptance:** Compare selected path and allocations against a native direct baseline at the accepted profile.

**Critical:** false · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-06-05 — Resource admission

Discovery, providers and optional graphics shall obey admitted CPU/GPU/memory/network/background budgets.

**Acceptance:** Saturate builds/inference while using the host; retain the declared foreground latency/audio contract.

**Critical:** true · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-06-06 — Failure-domain containment

A provider or broker failure shall have explicit effects and bounded recovery rather than an app-wide crash loop.

**Acceptance:** Crash one optional provider; independent base functions remain useful and diagnostics identify the cause.

**Critical:** true · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-06-07 — Capability-oriented reuse

New hosts shall consume shared capabilities/SDK contracts instead of copying providers or adding arbitrary pairwise data hacks.

**Acceptance:** Add a second host and measure reused logic, adapter size and no competing state authority.

**Critical:** false · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-06-08 — Platform-specific conformance

Each native/embedded/remote tier shall declare supported platform, packaging, permissions and degraded behaviors.

**Acceptance:** Install the real package on each required profile and verify its claimed integration tier.

**Critical:** true · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-07-01 — Separate structural and product proof

Schemas and local validator passes shall not be represented as live product correctness or authorization.

**Acceptance:** Every synthetic fixture and result is marked; missing native proof keeps graduation open.

**Critical:** true · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-07-02 — Independent suite coverage

Composed paths shall meet independent accepted unit/integration/E2E and other applicable floors without averaging.

**Acceptance:** Below-floor, missing, skipped and wrong-revision required reports each reject qualification.

**Critical:** true · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-07-03 — Complete critical evidence

All critical federation obligations shall have actual meaningful verification evidence for the selected profile.

**Acceptance:** A green aggregate cannot conceal a missing permission, preservation or recovery scenario.

**Critical:** true · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-07-04 — Two independent consumers

Shared contract graduation shall include two meaningfully different consumers and one recursive-composite witness.

**Acceptance:** Demonstrate reused contracts rather than duplicate bespoke adapters or mocked providers.

**Critical:** false · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-07-05 — Comparative product pilot

The same useful job shall be compared against standalone/manual, handoff and conventional integration baselines.

**Acceptance:** Retain successful and failed trials, setup effort, maintenance changes and performance distributions.

**Critical:** false · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-07-06 — Authentic media

Journey recordings and screenshots shall depict the tested actual profile; authored assets remain separately labelled.

**Acceptance:** Trace displayed claims to source/run/artifact; a mock UI cannot qualify an embedded product.

**Critical:** true · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-07-07 — Owner-coordinated rollout

Cross-repo provider/consumer changes shall have one integration lead, explicit leases and actual permissions.

**Acceptance:** No worker edits another owner checkout or marks consumer adoption from provider-only tests.

**Critical:** true · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.

## FED-07-08 — Incremental adoption

First real bindings shall ship without requiring every product to join or an entirely new platform to exist.

**Acceptance:** Two apps remain individually installable and the rest of the estate can ignore federation.

**Critical:** false · **Source:** INT-005 · **Spec:** SPEC-12 · **Evidence:** not yet executed.
