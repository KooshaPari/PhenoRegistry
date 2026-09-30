# Raw Intent Record — Durable Memory, Bulkheads, Constitution, Git Ledger

**Date:** 2026-09-29 → 2026-09-30  
**Authority:** owner-authored intent  
**Status:** incorporated in part; continuing audit required.

## Themes

- documentation as external human memory;
- high-fidelity Genesis/dossier system;
- bulkhead → deep-module documentation architecture;
- raw owner intent as durable product evidence;
- portfolio constitution and policy inheritance;
- repeated tooling/process doctrine;
- policy lineage/supersession;
- Git as immutable-ish transactional ledger;
- fast-forward preference;
- no squash/history collapse;
- retrospective readability without rewriting old SHAs;
- future commit semantic quality;
- human context overload as a portfolio risk.

## Faithful synthesis

The owner can no longer be expected to maintain the detailed chain of thought for a multi-year, many-repository, highly agent-driven portfolio.

The documentation system must therefore preserve not only current conclusions but the prerequisite reasoning that made those conclusions intelligible. This is important for the owner as much as for agents.

Specialized documents such as dossiers, Genesis, Intent, SOTA and similar zones need to be unusually comprehensive. One shallow file is insufficient. Each major domain should use a strong concise-but-detailed top-level bulkhead linking into deeper focused documents and evidence.

The system should make it easy to skim the current truth while still being able to descend into research, raw source, historical rationale and implementation evidence.

Repeated owner policies should stop depending on repeated prompts. Examples include uv, Bun, Oxc tooling, mise, file-size constraints, GitHub Actions cost constraints, polyrepo/synthetic-monorepo strategy, polyglot/native-manager strategy, architecture defaults and agent/process rules. These rules have evolved over time, so the system must preserve policy lineage and supersession rather than freezing the first statement discovered.

Git history is intentionally treated as a transactional ledger. Squashing, rebasing and force-rewriting meaningful shared history are generally undesirable because they collapse or replace transaction identity. Fast-forward is desirable because it preserves commits/ancestry. Historical commits remain useful even if poorly messaged because the diffs and parentage still preserve information.

Historical readability should therefore be improved through additive interpretation — dossiers, notes, commit maps, decision links, supersession relations — rather than by rewriting old history merely to make it prettier.

Future commits should be semantically coherent and readable. Existing history should not be over-adjusted.

The deeper motivation is that context overload is already changing how the owner communicates and recalls prior work. Without externalized lineage, the owner risks simplifying, contradicting or re-deriving ideas that once had a more robust chain of thought. The portfolio's memory system should prevent that cognitive degradation from becoming product/process drift.

## Extracted invariants

1. Human recoverability is a hard engineering requirement.
2. Major documentation domains require progressive disclosure, not flat single files.
3. Genesis preserves prerequisite reasoning and conceptual lineage.
4. Raw owner intent is primary evidence.
5. Current summaries must remain traceable to historical evidence.
6. Policy lineage must distinguish current rules from historical/superseded forms.
7. Git transaction identity has durable information value.
8. Fast-forward does not violate ledger preservation.
9. Squash/rewrite is not the normal cleanup mechanism.
10. Old history should be interpreted additively, not cosmetically rewritten.
11. Future commit quality should improve.
12. Repeated portfolio doctrine should be inherited/resolved automatically.
13. Documentation and policy systems must be useful to owner and agents.
14. Context loss/reconstruction cost is itself a portfolio-level defect.

## Incorporated into

- `docs/governance/constitution/README.md`
- `docs/governance/constitution/POLICY-LINEAGE-SEED.md`
- `docs/governance/constitution/CURRENT-OWNER-DOCTRINE-2026-09-30.md`
- `docs/governance/constitution/CROSS-CHAT-AMENDMENT-2026-09-30.md`
- `docs/governance/constitution/git/README.md`
- `docs/governance/constitution/git/HISTORICAL-READABILITY.md`
- `docs/governance/standards/PRODUCT_DOSSIER_STANDARD.md`
- `docs/governance/standards/DOCUMENTATION_INFORMATION_ARCHITECTURE.md`
- Tracera `GENESIS.md`, `DOSSIER.md`, Intent/SOTA bulkheads
- repo-local `governance/DURABLE_PRODUCT_MEMORY.md` in Tracera and AgilePlus.

## Remaining incorporation work

- comprehensive raw-intent index across prior conversations;
- full repo/history policy archaeology;
- PolicyId assignment and machine-readable schema;
- repo profile resolution;
- drift inventory;
- fresh-human/fresh-agent recoverability experiments;
- per-product expansion of dossier subtrees;
- commit-range/decision lineage reconstruction for important historical periods.
