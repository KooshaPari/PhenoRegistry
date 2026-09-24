# Phenotype 146-repository portfolio control program

**Version:** 0.1  
**Observation date:** 2026-09-01  
**Scope:** all 146 owner-affiliated `KooshaPari` repositories  
**Status:** audit governance, exact census, preliminary routing map, and worker contracts complete; repository-by-repository deep audits not yet complete.

## Purpose

This package converts the user’s portfolio request into an executable, evidence-driven program.

It provides:

- A corrected definition of completeness across intent, product, specification, architecture, code, quality, evidence, operations, market and governance.
- G0–G6 maturity gates.
- Repository birth, survival, incubation, fork, archive and migration rules.
- A closure-first WBS rather than a “10% everywhere” campaign.
- A fair SOTA and pilot protocol.
- Risk-triggered Git/branch regression forensics.
- An exact 146-row owner inventory and provisional family routing.
- Initial central authority decisions.
- Machine-readable schemas and worker handoff contracts.
- Copy-paste prompts for the portfolio coordinator, family leads, per-repo closure agents and pilot agents.

## What this package is not

- It is not a completed line-by-line audit of all repositories.
- It does not declare final merge/archive decisions.
- It does not accept existing ecosystem maps as current.
- It does not force every repo into the same docs folder.
- It does not authorize destructive migration.
- It does not assume every fork is clutter or every small repo should merge.
- It does not use an arbitrary file count as documentation completeness.

## Confirmed census

| Count | Value |
|---|---:|
| Raw owner repositories | 146 |
| Public in captured metadata | 112 |
| Private in captured metadata | 34 |
| Archived in captured metadata | 29 |
| Non-archived in captured metadata | 117 |

The visibility/archive extraction must be refreshed by the planned live observer before destructive decisions. Local-only refs, worktrees and reflogs are not represented by GitHub census.

## Main conclusion

The target should be a **capability-first layered polyrepo**, not one giant monorepo and not 146 equally prominent authorities.

A working prior is:

- 45–70 canonical active/maintenance repositories.
- 10–20 public product brands.
- 6–12 strategic forks/adapters/packaging repos.
- 3–6 simultaneous active incubators.
- archives counted separately.

This range is a hypothesis. Consumer, lifecycle, security, license, upstream, deployment, co-change and agent-context evidence decides the final topology.

## Start here

1. `00-EXECUTIVE-DECISION.md`
2. `01-AUDIT-CHARTER.md`
3. `02-COMPLETENESS-MODEL.md`
4. `03-REPOSITORY-BOUNDARY-POLICY.md`
5. `04-SOTA-PILOT-CASE-STUDY-PROTOCOL.md`
6. `05-FORENSIC-HISTORY-POLICY.md`
7. `06-CLOSURE-FIRST-WBS.md`
8. `07-CURRENT-146-REPO-INVENTORY.md`
9. `08-PROVISIONAL-FAMILY-MAP.md`
10. `09-TARGET-STATE-HYPOTHESIS.md`
11. `10-ECOSYSTEM-SSOT-AUTHORITY.md`
12. `11-INITIAL-DECISION-QUEUE.md`
13. `12-INITIAL-WBS-PERT-DAG.md`
14. `13-MEASUREMENT-FRAMEWORK.md`
15. `14-AGENT-OPERATING-MODEL.md`

## Prompts

- `prompts/MASTER-PORTFOLIO-COORDINATOR-PROMPT.md`
- `prompts/FAMILY-ADJUDICATOR-PROMPT.md`
- `prompts/PER-REPO-AUDITOR-AND-CLOSURE-PROMPT.md`
- `prompts/SOTA-PILOT-AGENT-PROMPT.md`

The master prompt is self-contained. The other prompts are intentionally narrower and should receive a central assignment envelope.

## Machine-readable artifacts

- `manifests/repo-inventory.json`
- `manifests/provisional-clusters.json`
- `manifests/decision-queue.json`
- `manifests/initial-work-queue.json`
- `schemas/repo-assessment.schema.json`
- `schemas/capability-record.schema.json`
- `schemas/ecosystem-decision.schema.json`
- `schemas/worker-handoff.schema.json`

## Key initial decisions

The first accepted decisions must resolve:

- Live GitHub facts versus curated ecosystem roles.
- Product-local specs versus cross-product contracts.
- Active policy/enforcement ownership.
- FocalPoint/phenotype-apps.
- Planify/Planify2.
- `pheno` shelf/meta role.
- Current AGSLAG/portfolio strategy authority.
- Agent execution family layering.
- Helios family layering.
- Router/gateway/fork topology.
- Foundation package homes.
- New distributed compute/data/I/O fabric repo boundaries.

## First execution wave

Run in parallel but with WIP limits:

### Authority lane

- Build repeatable GitHub observation.
- Adopt schemas and typed IDs.
- Repair registry authority.
- Decide specs/conventions/enforcement boundaries.
- Implement worker handoff validation.

### Closure lane

- Audit vibe-monitoring micro-family.
- Forensic Planify pair.
- Forensic FocalPoint pair.
- Adjudicate `pheno`.
- Then foundation compression and agent/Helios families.

## Use with local agents

Do not paste only the target repo name and ask an agent to “complete it.” Provide:

- repo/family ID;
- observed immutable ref;
- authorized mode;
- central role hypotheses;
- related decision IDs;
- bounded paths and resources;
- expected schema and artifacts;
- explicit forbidden sibling/destructive operations.

The repository agent submits evidence. The family and portfolio adjudicators settle boundaries.

## Validation

See `VALIDATION_REPORT.md`. The package validates JSON syntax, schema documents, unique repository IDs/names, complete cluster assignment, task DAG acyclicity, predecessor integrity, computed PERT fields, internal file inventory and checksums.

## Evidence caveat

Initial GitHub README findings establish obvious contradictions and stale authority, but they do not replace deep code/history/consumer audit. The program is designed to perform that audit without overclaiming current coverage.
