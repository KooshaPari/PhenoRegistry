# Harness lineage correction — succession, donors, and intended convergence

Date: 2026-09-30.

## Correction

The Helios CLI family must not be modeled as several independently conceived permanent products that coincidentally overlap.

The lineage is chronological. Forks were created at different times, often with a substantial gap. At the time Helios CLI was created, later forks were not necessarily intended or anticipated. A later fork was adopted because its upstream/base appeared better or more useful than the then-current owned runtime either overall or in particular dimensions. Consequently Helios CLI, HeliosLite and KCode overlap because they are successive attempts to find/build the best coding-agent CLI/runtime, not because the mature portfolio requires three overlapping CLIs.

Historical chronology therefore matters to product intent:
- presence of a feature in an older fork can preserve accepted intent even if the newer fork does not yet contain it;
- absence from a newer fork does not automatically mean the capability was rejected;
- presence in multiple forks does not imply three independent mature requirements;
- a later fork is evidence that the earlier architecture/base had perceived deficiencies, but the exact deficiency must be recovered rather than guessed;
- sunk implementation in any lineage does not create a requirement to preserve that lineage as a standalone product.

## Product-family model

### Helios CLI
Earliest owned CLI lineage in this family. Codex-derived. Historically valued especially as a UX/product-interaction donor. Later forks were not necessarily contemplated when it was created.

Default mature disposition is therefore not “prove Helios CLI must remain a separate CLI.” Recover its accepted UX/interaction/runtime obligations and test whether they belong in the converged CLI/runtime, shared SDK, or HeliosLab.

### HeliosLite
Later Forgecode-derived lineage. Historically selected because Forgecode offered materially attractive performance/headless/runtime characteristics relative to what existed before. It is both a current implementation candidate and a donor of runtime/performance/CLI ideas.

Its existence gate asks two questions separately:
1. which HeliosLite behaviors/architecture survive into the mature system?
2. does HeliosLite itself remain the canonical CLI/runtime?

Do not conflate them.

### KCode
Later jcode-derived lineage and another candidate canonical CLI/runtime. Its creation is evidence that jcode offered capabilities/architecture that appeared better or more useful than the preceding owned lineages in whole or part. The current upstream-vs-fork gate determines how much owned KCode delta remains necessary, while the family-level gate compares the *base/runtime architecture* against HeliosLite/Helios CLI obligations.

KCode may win capabilities without winning product identity; it may be a donor, canonical base, thin fork, upstream contribution set, or be absorbed.

### HeliosLab
Different product role. HeliosLab is the GUI/application workbench, intended as a direct competitor to the Codex app / Claude Desktop-style coding workbench rather than merely a GUI wrapper around one CLI.

Mature intent:
- controlled first-class GUI/interaction model rather than being constrained to a direct CLI-to-UI projection;
- highly optimized real-time and at-scale execution;
- performance/operational characteristics inspired by CMux/Herder-class optimized runtimes or equivalent approaches;
- intuitive product design that can exploit GUI-native interaction;
- consumes the best runtime/SDK/harness capabilities recovered from the CLI succession rather than inheriting one CLI's UI model wholesale.

HeliosLab is therefore not a third/fourth CLI existence candidate. It is an application product that should sit over reusable runtime/SDK primitives.

### Agentora / shared runtime layer
Historical family intent includes one SDK/runtime foundation underpinning app/CLI where justified. Agentora/PhenoShared are relevant architectural donors/dependency surfaces, but not additional primary products in this two-repository recovery program.

## Correct convergence question

Do not ask:
“Which of Helios CLI, HeliosLite and KCode deserves to exist because each has unique features?”

Ask:
“What is the best mature coding-agent CLI/runtime after recovering the accepted obligations and strongest architecture from all three chronological lineages and current external alternatives?”

Then determine the minimum justified product topology. Historical preference was one app, two CLI lineages, one SDK, with CLI convergence preferred unless distinct roles survive a separation gate. The current archaeology may reduce two CLIs to one if no durable role separation survives.

A separate CLI is justified only by a stable user/runtime role boundary, not by fork ancestry.

## Required lineage matrix

For every material capability recover:
- first known appearance/date;
- originating upstream/fork;
- user intent at that time;
- why the next fork/base was explored;
- whether capability was carried forward, reimplemented, dropped accidentally, superseded, or explicitly rejected;
- current best implementation among owned/external alternatives;
- mature destination: canonical CLI, HeliosLab, shared SDK/runtime, adapter, upstream contribution, retire.

This lineage matrix becomes an input to both HeliosLite and KCode existence gates.

## Consequence for current work

The existing HeliosLite/KCode pair remains the two active implementation/specification subjects. Helios CLI and HeliosLab are lineage/intent/architecture evidence, not third/fourth active repos.

KCode's “upstream + thin overlay” challenger remains valid for KCode-specific maintenance, but it is insufficient as the family-level answer: it must also satisfy recovered Helios CLI UX obligations and HeliosLite runtime/performance obligations.

Likewise, HeliosLite surviving its own fork gate does not prove it should be the canonical family CLI if KCode/jcode provides a better base after accepted obligations are ported.

No current implementation is presumed the winner.
