# Requirement record schema and decomposition rules

A normative obligation record contains:
- stable ID;
- statement;
- rationale;
- authority/provenance sources;
- ontology subject/parent;
- dependencies/invariants;
- mature role;
- stage projection;
- journey membership;
- positive acceptance;
- negative/counterexample acceptance;
- quality-overlay references;
- implementation surfaces (zero or more);
- verification/oracle;
- evidence identity requirements;
- growth disposition: retain/enrich/adapter/supersede/remove;
- status: accepted/proposed/contradicted/blocked/superseded.

Rules:
1. Count is output, never target.
2. One record per distinct obligation, not per generic quality dimension.
3. Shared invariants are referenced, not mechanically cloned.
4. Acceptance must discriminate correct from plausible-wrong behavior.
5. Unknown intent remains a finding/question, not an invented requirement.
6. Historical implementation is not accepted intent unless authority supports it.
7. Stage projections select/strengthen mature obligations; they do not invent disposable alternate state models.
8. Every requirement must trace to a journey or justify why it is infrastructure/constraint-only.
9. Every implemented claim needs mounted/reachable evidence, not file-name existence.
