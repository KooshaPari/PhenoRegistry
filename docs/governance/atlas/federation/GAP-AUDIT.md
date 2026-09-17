# Sufficiency audit of the attached v1.2 package

**Verdict: the conceptual foundation was present; the requested product experience was underspecified.** This is an artifact review of the mounted v1.2 ZIP, not a claim about unseen current source implementations.

The existing `architecture/APPLET-CONTRACT.md` defines recursive applets, provided/required capabilities, domain-facing ports, state and permission ownership, lifecycle/health, locality-aware lowering, child readiness, quiescence and a basic composition test. Its schema includes ports, surfaces and children, but represents `federation_policy` as an unconstrained string. The example is a synthetic CLI/library component. HLD/ALD/LLD primarily specify the atlas and assurance program, not a native composite-application experience.

| Concern | Existing coverage | Amendment |
|---|---|---|
| Recursive components and composites | Explicit | Preserve; add bounded re-export and perspective rules |
| Ports, capabilities, owned state | Explicit high-level contract | Add scoped offers, requirements, recipes and selected bindings |
| Same-process/IPC/network choice | Explicit high-level guidance | Retain optimized lowering; never make network mandatory |
| Co-install detection | No complete install/discovery protocol | Signed/custodied manifest discovery with lazy activation |
| Automatic integration | Not an operational contract | Deterministic, consent-aware recipe reconciliation |
| Opening either app as primary | Not specified | Host-relative perspective without authority switching |
| Native command/navigation experience | Generic surface labels | Slot, command, focus, accessibility, context and error contracts |
| App Center | Not defined | Optional management/workspace view over the same bindings |
| Multiple simultaneous hosts | Not defined | Shared scoped service leases, independent views, no duplicate mutations |
| Learned integration | Not defined | Learn preferences; generate proposals, not unreviewed executable bindings |
| Update/uninstall/data retention | Quiescence mentioned | Versioned plans, leases, recovery journal and owner-safe detachment |
| Composite scaling | Recursive idea | Lazy UI/service activation, expansion budgets, event-loop control |
| Cross-app qualification | Basic compose/remove test | Real installation-order, host-swap, failure, privacy and upgrade matrix |

A subfolder or trait named 'applet' is not proof of the stronger experience. Conversely, no new universal framework is justified merely because this document identifies missing behavior. Reuse existing qualified applet/service/UI facilities and add the narrow common contracts the first real consumer pair needs.

The previous schema remains readable for old examples. The new illustrative profile is additive and opt-in; it is not a silent interpretation of every old free-text policy. Production compatibility adapters must explicitly map old records or reject an unsupported profile.

The user's Apple/Google/Microsoft/Linux Foundation/GNU/Apache references are interpreted as desired qualities: immediate coherence, reliable lifecycle and recovery, platform fit, openness, inspectability, interoperability and durable ownership. They are not assertions that any vendor uniformly satisfies all those properties, nor a requirement to combine their entire stacks.
