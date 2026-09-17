# Typed traceability from human thought to adopted behavior

## One evolving product model, multiple authoritative sources

Human words -> interpretation/assumption -> product job -> capability -> requirement/invariant -> design/architecture/contract -> source/config/asset -> test/evaluator -> actual run -> artifact -> installation/deployment -> observed user outcome -> dissatisfaction/change.

This is a graph, not a mandatory linear assembly line. Research can revise a design; a runtime incident can expose a missing requirement; a prototype can precede a finalized specification. Preserve that provenance and uncertainty instead of retroactively pretending every discovery was planned.

Subject repositories own declared source artifacts. Native engines own scoped mutable work state. Tools render, validate and reconcile records. Tracera owns its persistent product model and links; it does not secretly appropriate every underlying data authority. The inventory and grading views are projections, not separate competing registries.

## Artifact families to account for

Exact prompts, intent synthesis, glossary/assumptions, persona/jobs, capability models, FR/NFR/system/interface requirements, domain/data/state models, HLD/ALD/LLD, ADRs, research/hypotheses/experiments, SOTA and pilot evidence, designs/mockups/fixtures/assets, source and generated code, dependencies/patches/licenses, contracts/configuration, schemas/migrations, tests/fuzz/property/mutation corpora, test tools/oracles, WBS/work/DAG/estimates, builds/packages/signatures/SBOMs, deployment/IaC/permissions/secrets references, runbooks/SLOs/restore procedures, docs/examples/translations, actual runs, performance/captures, releases/installations, incidents, feedback and accepted changes.

Account for meaningful semantic units and spans. Generated and vendored files inherit their producer/upstream contract and local delta. Do not handwrite a paragraph per token or require a thousand ADRs because there are a thousand scenarios. Expand real uncertainty and behavior, not arbitrary document counts.

## Both directions are mandatory

Forward: every accepted requirement reaches appropriate implementation/design/tests/evidence or an honest unimplemented/blocked/research record.

Reverse: every public surface, significant source unit, dependency, asset, workflow and distributed artifact has a role, owner, rationale and applicable obligations. Find undocumented code as well as unimplemented requirements. A file moved under docs or excluded from a workspace is not thereby out of product scope.

## Typed evidence prevents category errors

'Builds' proves buildability; it does not prove usability. 'System initialized' proves initialization; it does not prove visible content. 'Screenshot exists' proves capture existence; it does not prove its content, freshness or expected pixels. 'Mock passes' proves the mocked contract path; it does not prove the live provider. 'Approved mockup' proves intended design; it does not prove installation. 'All known FRs linked' proves closure against a known inventory; it cannot prove no requirement is missing.

Relations therefore carry subject, revision, profile, claim type, source locator, producer and timestamp. Work status, requirement status, evidence status, publication and adoption are independently represented. Historical evidence stays accessible but may no longer qualify a new candidate.

## Specification adequacy and scope versioning

A grade needs an explicit rubric universe. Define artifact-role applicability, capability/state/failure/support matrices and risk boundaries before grading. Use independent gap analysis, user feedback and adversarial scenarios to find omissions. Record specification adequacy separately from implementation satisfaction. Do not certify completeness for all possible ideas.

Preserve full-horizon intent and a bounded current viable product scope. Both can have percentages, but always with their own scope/rubric IDs. Adding real requirements can lower the current percentage without negating useful progress. Show old-scope/new-scope and scope-change effects separately. Never erase requirements merely to improve the grade.

## Refresh and interchange

Use stable IDs, content/version hashes and source anchors, not paths alone. Update affected subgraphs incrementally. A changed source or artifact marks dependent evidence stale unless an independently accepted applicability proof permits reuse. Cached local records do not establish current remote or installed state. Work engine receipts are queried from the actual scoped service rather than inferred from generated docs.

One owner can produce and maintain the graph through portable repo-local records now. The shared schema and adapters enable later ingestion without blocking real improvements on complete platform implementation. Recover SROC/CDP source definitions separately; this graph does not invent them.
