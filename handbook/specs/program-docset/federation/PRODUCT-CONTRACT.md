> **v1.4:** federation can have zero peer UI mounts. Features, results, workflows and headless services are the primary composition units. See [capability-first clarification](../proof/CAPABILITY-COMPOSITION.md).

# Product contract: independently useful, better together

## Definition

**Reciprocal, host-relative application federation** is a capability- and policy-driven composition system in which installed applications can provide selected services and surfaces to one another. Each application remains independently usable under its declared base dependencies. The application the user deliberately opens supplies the primary workspace and interaction grammar; other compatible applications contribute contextual capabilities that feel integral rather than like nested full applications.

Reciprocal means that both directions are possible where useful and implemented. It does not require identical features in both directions, every pair to integrate, or a graphics library to become a GUI host. A composition may itself expose a bounded applet contract to a larger composition. A repo, installed package, process, applet, product and window are distinct identities.

## The central distinction

**Perspective changes; authoritative ownership does not.** Opening Tracera can foreground a product graph and show an AgilePlus work panel for the selected capability. Opening AgilePlus can foreground the work item and show Tracera's product context and dissatisfaction. The same work item and product entity remain the same records. Neither program manufactures a second database to make its own UI look self-contained.

Primary is relative to a window/workspace/session, not a global 'last launched app wins' setting. Two windows can simultaneously have different primary apps without oscillating defaults, stealing focus or changing the user's chosen provider. A background launch cannot reorder visible navigation or take over the primary perspective. A user can explicitly reframe a workspace while retaining its stable object context.

## Five operations that must never be conflated

1. **Source consolidation:** development-time changes to repositories and package ownership, with separate authorization.
2. **Installation:** place a signed/qualified package in an allowed environment and register its capabilities.
3. **Runtime composition:** select and connect compatible providers to consumers under a scoped plan.
4. **Experience composition:** present contextual commands, views, objects and workflows coherently in a host.
5. **Data migration:** change data format/ownership/storage under explicit migration rules; not an automatic side effect of composition.

The user's 'absorbed' feeling is chiefly operations 3 and 4. It does not mean the other app vanished or its state was annexed.

## Discovery and automatic setup

When B is installed after A, eligible hosts observe metadata changes, validate artifact identity and the declared compatibility profile, and reconcile approved recipes. Safe integration inside an already-approved principal/workspace/resource scope can activate without repeated dialogs. New sensitive scopes, new external transfers, purchases, installs, destructive commands, background services or ambiguous providers require the appropriate explicit decision.

The reverse install order yields the same usable capability set under the same selected versions/policy. Discovery alone does not start B's complete desktop UI or its expensive backend. No manual path/port/API-key copying is required for the qualified first-party local integration path. Credentials are not copied between apps: use scoped brokers/references and independent enforcement by the authoritative provider.

A missing optional peer leaves a useful standalone app, not a broken shell or a wall of advertisements. A missing base dependency is reported honestly. Installing C must not silently replace a user-pinned B provider or add every C command to every menu.

## App Center

The optional App Center provides discover/install/update/repair, capability and permission inspection, provider choices, workspace presets, conflict explanation, detach/export and recovery. Its user-visible model is 'apps and useful capabilities', not a compulsory giant dashboard.

It is another perspective and consumer of the same APIs, not a second installation database, work ledger or source authority. Apps can activate integrations and work offline under cached approved local plans without opening the Center. An always-on cloud account is not required for qualified local composition. Cloud or multi-device dependencies remain explicit where the workflow needs them.

Packaging can begin as a view or applet in an existing accepted shell (for example a scoped PhenoApps consumer), not an automatically approved new repo/product. The correct home follows actual consumer and release ownership, not the aesthetic appeal of a platform name.

## 'Learning to merge'

Use deterministic discovery, typed compatibility and explicit recipes before learning. The system may learn that the user prefers B for previews, retains a certain panel layout or repeatedly creates a useful composition. The result is an inspectable preference or suggested recipe, scoped to its environment and easy to reset.

A model may propose an adapter as development work. It cannot invent compatible contracts, execute generated glue on installation, infer permission from co-presence, migrate data, accept itself as verified, or change a user's default invisibly. Confidence is not authority. Declining a suggestion should be durable and quiet.

## Proposed first product witness

Use Tracera and AgilePlus after confirming both standalone paths. Bind one real subject, capability and work item; display actual work inside Tracera, then actual product context inside AgilePlus. Keep each data authority intact and obtain real work-engine receipts. Update an item, open both perspectives, restart one provider, revoke a write scope, detach and reinstall. Verify continuity and audit the exact native UI/keyboard/accessibility paths. This is planned, not an assertion that either host already implements it.

A second distinct pair (for example BytePort + ShareCLI) tests whether the contracts are truly reusable. A third nesting test exposes a composite's reduced public capability without recursively embedding complete app chrome. Broader automatic composition comes after these witnesses, not before useful product delivery.
