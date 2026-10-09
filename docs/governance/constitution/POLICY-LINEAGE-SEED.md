# Policy Lineage and Repetition Register

**Status:** seed register; incomplete until full repo/history/conversation archaeology.

This register captures recurring owner instructions that should no longer require repeated chat explanation. It distinguishes current direction from historical formulations.

| Domain | Repeated rule / issue | Current interpretation | Historical/evolution note | Final audit needed |
|---|---|---|---|---|
| Python | uv | default native Python project/workspace/package management where applicable | repeated across agent/tooling discussions | yes |
| JS/TS | Bun | qualified default package/runtime/tooling layer; preserve ecosystem compatibility | evolved from local fast tool usage into broader default | yes |
| JS/TS quality | Oxc/Oxlint/Oxfmt | preferred modern lint/format direction where contract/maturity fit | replaces mixed ESLint/Prettier/Biome defaults in many contexts | yes |
| Toolchain | mise | outer version/env/task coordination; native managers own dependency truth | emerged from polyglot consolidation work | yes |
| Hooks | Lefthook | preferred cross-language hook orchestration where applicable | canonicalization work Sep 2026 | yes |
| MCP | FastMCP | preferred MCP server primitive where appropriate | canonicalization work Sep 2026 | yes |
| Source size | ~500 LOC/file | decomposition trigger/guardrail, not blind hard splitter | repeatedly restated; exact exceptions need archaeology | yes |
| CI cost | no paid Actions compute | public standard hosted when safe/free; private/heavy self-hosted/already-paid; no silent paid fallback | strengthened through repeated billing/churn incidents | yes |
| CI scope | affected-only | component/path/impact-aware execution; cheap gates first | especially important for multi-app/synthetic monorepos | yes |
| Repo topology | polyrepo + synthetic monorepo | independent repos/releases plus graph-aware coordinated views/snapshots | rejects both naive mega-monorepo and isolated repo silos | yes |
| Multi-app repo | repo != build boundary | target-aware switches/plans; do not compile everything by co-location | explicit Sep 29 2026 requirement | yes |
| Polyglot | native managers | do not invent one universal dependency store; shared caches okay | evolved with mise/uv/Bun/Cargo strategy | yes |
| Architecture | modular monolith first | vertical slices/modules; hexagonal seams at meaningful boundaries; services when justified | supersedes generic microservice-heavy early guidance | yes |
| Microservices | evidence required | scaling/deploy/ownership/isolation/lifecycle justification | earlier study/exploration was more microservice-positive | yes |
| Hexagonal | meaningful boundaries | ports/adapters for volatility/effects/trust, not ceremony everywhere | matured from broad Clean/hexagonal enthusiasm | yes |
| Shared code | narrow PhenoShared | independently consumable capabilities, avoid god-shared library | repeated consolidation concern | yes |
| Agent work | bounded + resumable | exact scope/context/acceptance/evidence; workers replaceable | matured into MACE/AgilePlus model | yes |
| Evidence | source-backed | CI/git/log/test evidence outranks agent claims | recurring since early agent governance | yes |
| Docs | durable external memory | recovery-grade bulkheads + deep modules + raw intent | strengthened Sep 29 2026 from agent docs to owner-memory system | yes |
| Forks | upstream=input | hard forks legitimate; preserve lineage; selective sync | formalized Mar/Apr 2026 | yes |
| Release | automation except stable authority gates | non-stable + post-stable lifecycle automation; stable/official requires HITL/traceability | Sep 2026 release lifecycle work | yes |
| Experiments | optimality allowed | exotic languages/tools welcome when justified; agent tractability/user outcome constrain | recurring 2026 preference | yes |

## Required follow-up

For each row:
1. find earliest known user statement;
2. find major restatements;
3. find contradictory/superseding statements;
4. inspect actual repo adoption;
5. research current external state;
6. adjudicate canonical policy;
7. assign PolicyId;
8. define applicability/profile;
9. define enforcement/evidence;
10. identify repos currently drifting.

Rows may split into multiple policies.

Do not infer that repetition alone means a rule is universally applicable. Repetition establishes importance; scope still requires adjudication.
