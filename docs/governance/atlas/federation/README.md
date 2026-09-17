> **v1.4:** federation can have zero peer UI mounts. Features, results, workflows and headless services are the primary composition units. See [capability-first clarification](../proof/CAPABILITY-COMPOSITION.md).

# Reciprocal application federation — revision 1.3

**Design and integration amendment; not a new live repository audit or an implemented runtime.** The original 24-owner September 16 snapshot is retained, not refreshed. One existing chat per current repository remains the staffing rule. No new app-center repository, migration, deployment, security exception, or lifecycle operation is authorized here.

The required experience is **independently useful applications that discover compatible peers and become one coherent, host-relative workspace, without losing their ownership, standalone use, safety boundaries or reversibility**. Opening A makes A primary and exposes useful parts of B in A's language. Opening B reverses the presentation where meaningful; the underlying data and work do not fork.

## Reading order

1. [Gap audit](GAP-AUDIT.md): what v1.2 actually covered and what it did not.
2. [Product contract](PRODUCT-CONTRACT.md): semantics, scope, host perspectives, App Center and examples.
3. [Experience contract](EXPERIENCE-CONTRACT.md): what integral means beyond a shared theme.
4. [Runtime architecture](RUNTIME-ARCHITECTURE.md), [lifecycle](LIFECYCLE-AND-RECOVERY.md), [security/data](SECURITY-AND-DATA.md), [platform lowering](PLATFORM-LOWERING.md).
5. [Requirements](REQUIREMENTS.md), [acceptance scenarios](ACCEPTANCE.md), [research/pilot](RESEARCH-AND-PILOT.md), [work plan](WORK-PLAN.md).
6. [Owner matrix](OWNER-MATRIX.md) and each existing owner's `FEDERATION.md`.

[Reference sources](SOURCES.md) identify reused ideas and limitations. [Schema guide](schemas/README.md) explains the illustrative machine-readable contracts. [Validation](VALIDATION.md) distinguishes document/schema checks from product qualification. [Reading PDF](RECIPROCAL-APPLICATION-FEDERATION.pdf) is a selected reading edition; Markdown/JSON remain the editable specification.

## Core boundary

A source-repository merge, installation, runtime wiring, view composition and data migration are five different operations. This amendment concerns compatible runtime and experience composition. It must not be used as permission to copy whole source trees, delete donors, merge databases, reuse ambient credentials, weaken sandboxes, or launch every installed application.

A visible App Center is optional. A minimal local discovery/resolution service may be required by a selected deployment, but its UI is not a mandatory launcher and its metadata is not another portfolio SSOT. Existing apps and CLIs use the same contracts directly. Data owners remain data owners.
