# Four-drive + Mac storage-agent toolkit

This package contains an inventory and nine original Agent Skills workflow templates. **It does not install tools, connect either computer, provide an executor, enforce permissions, or authorize cleanup.** No runtime tests have been performed on the user's machines.

Start with `INVENTORY.md`. `tool-inventory.json` supplies the machine-readable inventory; `sources.json` contains primary documentation references. `skills/` contains self-contained `SKILL.md` templates with required metadata. Point your agent runtime at the chosen skill directories using that runtime's documented installation/discovery mechanism.

`storage-policy.example.json`, `inventory-record.example.json` and `operation-plan.example.json` are proposed integration contracts, not configuration consumed by an implemented service. All host lists and roots are intentionally empty; all mutations are disabled. Runtime adapters and OS permissions must enforce policy independently of these documents.

Suggested adoption: authorize a read-only host/volume survey; validate the selected collector on a small permitted tree; verify coverage and reports; establish independent backup plus restore evidence; only then implement and review the approved-plan executor. Add ordinary SSH in one direction first, then the other. Do not load unreviewed third-party skill packs with broad permissions merely because their names match this inventory.

The source upload is not bundled. The baseline was used to identify requirements and evaluate its example code. Public project documentation was researched; a README review is not a source-security audit, package provenance audit or performance benchmark.
