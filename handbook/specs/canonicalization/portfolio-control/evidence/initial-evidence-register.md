# Initial evidence register

**Observation date:** 2026-09-01

This register records the source facts used to establish the program. It is not a substitute for full repository dossiers.

| ID | Evidence class | Source | Observation | Implication |
|---|---|---|---|---|
| EVD-INIT-001 | OBSERVED_STATIC | Connected GitHub owner inventory | 146 unique repositories owned by `KooshaPari` were returned | Existing 88/111-repo maps are not current |
| EVD-INIT-002 | OBSERVED_STATIC | `phenotype-registry/ECOSYSTEM_MAP.md` | File labels its 111-repo narrative stale and points to an 88-repo machine catalog | Registry authority/freshness must be repaired before broad delegation |
| EVD-INIT-003 | OBSERVED_STATIC | `phenotype-apps/README.md` | Repository presents itself as FocalPoint and includes contradictory build-state claims | Product authority and status require forensic recovery |
| EVD-INIT-004 | OBSERVED_STATIC | `FocalPoint/README.md` | Repository says “Phenotype-org dependency management” | Conflicts with FocalPoint product claim in `phenotype-apps` |
| EVD-INIT-005 | OBSERVED_STATIC | `Planify/README.md` | Repository is a Plane-derived Planify fork/candidate and retains mostly upstream README | Competing fork authority and public truth-hygiene issue |
| EVD-INIT-006 | OBSERVED_STATIC | `Planify2/README.md` | Repository also calls itself Planify and claims to be the consolidated Plane fork | Requires lineage/consumer/target decision |
| EVD-INIT-007 | OBSERVED_STATIC | `pheno/README.md` | Repository describes itself as an organizational shelf containing independent repos | Likely meta/workspace role, not ordinary product authority |
| EVD-INIT-008 | OBSERVED_STATIC | `PhenoSpecs/README.md` | Claims central ADR/contracts authority and names `phenotype-org-governance` as enforcement | Current exact active enforcement authority is unclear |
| EVD-INIT-009 | OBSERVED_STATIC | `phenotype-registry/README.md` | Claims canonical index and 90% progress, while pointing to stale counts/role spine | Claims and actual catalog freshness diverge |
| EVD-INIT-010 | OBSERVED_STATIC | `phenoAI/README.md` | Claims routing, MCP and embeddings in one generic AI workspace; references shared repos/names not present in current inventory | Generic scope and authority overlap require consumer-driven decomposition |
| EVD-INIT-011 | OBSERVED_STATIC | `Agentora/README.md` | Repo named Agentora contains crate/CLI `agentkit`, explicitly not a Python package, and claims agent framework role | Naming/packaging clarity and overlap with execution family require adjudication |
| EVD-INIT-012 | ACCEPTED_CONTRACT candidate | `sharecli/README.md` and prior ecosystem docs | ShareCLI claims OS/kernel-adjacent supervision, FUSE/coalescing/thermal and independent process-supervisor value | Do not absorb it into generic orchestration without consumer/product evidence |
| EVD-INIT-013 | ACCEPTED_CONTRACT candidate | `AgilePlus/PRD.md` | AgilePlus claims governed feature/WP lifecycle, evidence gates and DAG planning | Portfolio work should integrate rather than duplicate its work authority |
| EVD-INIT-014 | PRIOR_HYPOTHESIS | Prior Phenotype whitepapers | Earlier target proposed 32 canonical repos plus forks and a strategy→execution→evidence spine | Useful alternative, not current authority |

## Source locations

- https://github.com/KooshaPari/phenotype-registry/blob/main/ECOSYSTEM_MAP.md
- https://github.com/KooshaPari/phenotype-registry/blob/main/README.md
- https://github.com/KooshaPari/phenotype-apps
- https://github.com/KooshaPari/FocalPoint
- https://github.com/KooshaPari/Planify
- https://github.com/KooshaPari/Planify2
- https://github.com/KooshaPari/pheno
- https://github.com/KooshaPari/PhenoSpecs
- https://github.com/KooshaPari/phenoAI
- https://github.com/KooshaPari/Agentora
- https://github.com/KooshaPari/sharecli
- https://github.com/KooshaPari/AgilePlus

## Limitations

- This is not yet a line-by-line code or history audit.
- GitHub metadata was captured through the connected account, but local-only refs/worktrees/reflogs are not represented.
- The initial private/archive transcription should be reconciled into the live registry by an automated GitHub observation job.
- Role hypotheses remain provisional.
