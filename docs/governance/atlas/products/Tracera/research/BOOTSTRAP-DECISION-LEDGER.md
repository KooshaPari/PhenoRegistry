# Tracera Bootstrap Decision Ledger — Draft 1

**Date:** 2026-09-29.
**Status:** decisions are provisional until architecture experiments/implementation-fit review.

| Capability | Candidate | Direction | Why / caveat |
|---|---|---|---|
| Repo-local structured requirements/docs | StrictDoc | ADAPT/INTEGRATE | Mature source/test traceability, custom fields, ReqIF, coverage maps; document-centric, so not canonical whole-product model |
| Lightweight requirements-as-code | Doorstop | ADAPTER | Stable VCS-native YAML/tree/validation; useful import/export, narrower than Tracera |
| Lightweight trace scanning | OpenFastTrace | ADAPTER | Mature CI trace suite; useful source tags/coverage, not product model |
| Safety-oriented software traceability | BASIL | STUDY/ADAPTER | Work-item/spec/source completeness; REST; useful regulated-software patterns |
| Variability/configuration language | UVL + FeatureIDE/flamapy | ADAPT/INTEGRATE | Standardized feature-model pivot language/tooling; test for software effectivity |
| Code/repository graph | SCIP/LSP/tree-sitter + agentforge-graph/ContextGraph class | INTEGRATE | Do not hand-roll multi-language parsing; retain filesystem/source authority |
| Requirements interchange | ReqIF | INTEGRATE | Open non-proprietary cross-tool requirements exchange |
| Lifecycle federation/config | OSLC RM/CM | INTEGRATE/MAP | Versioned cross-domain links/configuration semantics |
| Systems model interchange | SysML v2 API/KerML | MAP/INTEGRATE | Requirements/behavior/structure/verification and standard model API |
| Supply-chain model | CycloneDX/SPDX | INTEGRATE | BOM/evidence/attestations/claims; avoid proprietary SBOM model |
| Build/execution provenance | in-toto/SLSA | INTEGRATE | Signed materials/products/steps and provenance trust |
| Runtime observations | OpenTelemetry | INTEGRATE | Standard semantic conventions for runtime evidence |
| Static findings | SARIF | INTEGRATE | Standard analysis-result interchange |
| Provenance ontology | W3C PROV | MAP/ADAPT | Entity/Activity/Agent derivation/attribution semantics |
| Graph structural validation | SHACL concepts/native where useful | ADAPT/PROTOTYPE | Immutable shape-vs-data validation + structured reports; complements behavioral oracle |
| Property-graph query portability | ISO GQL | TRACK/ALIGN | Avoid vendor-specific logical semantics |
| Embedded graph storage | LadybugDB | BENCHMARK | Attractive embedded graph/Rust; project lineage changed from Kuzu, benchmark health/perf |
| Relational graph storage | SQLite/Postgres | BENCHMARK/KEEP | Existing Tracera investment; may remain best local-first canonical store |
| Server graph storage | Neo4j | BENCHMARK/OPTIONAL | Powerful traversal/ecosystem but should not be required product semantics |
| Graph editor OSS | React Flow | PROTOTYPE | Strong open/custom editor baseline |
| Graph editor SOTA | yFiles | BENCHMARK/POSSIBLE BUY | Mature grouping/folding/LOD/layout/analysis; licensing decision later |
| Executable visual flows | Rete.js | OPTIONAL PROJECTION | Useful only where graph nodes have executable flow semantics |
| Product context/service catalog | Backstage-compatible metadata | INTEGRATE | Commodity service/entity catalog data should be imported, not recreated |
| Product graph kernel | Tracera | BUILD | Cross-projection identity/authority/configuration/reconciliation remains custom |
| Graph delta/product change | Tracera | BUILD | Core original thesis; external work systems execute but do not own meaning |
| Evidence applicability/invalidation | Tracera | BUILD using imported semantics | Requires product-specific configuration + suspect-link semantics |
| Dissatisfaction engine | Tracera | BUILD | Cross-projection disagreement/gap detection |
| Product MACE trajectory | Tracera | BUILD | Persistent multidimensional product-level oracle/control loop |
| Work execution | AgilePlus/external systems | FEDERATE | Explicitly not Tracera ownership |

## Rule

A BUILD decision is not permission to hand-roll dependencies underneath it. The custom kernel should compose standards/libraries wherever they satisfy the lower-level primitive.
