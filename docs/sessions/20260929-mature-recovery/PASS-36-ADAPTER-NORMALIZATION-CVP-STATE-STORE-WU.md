# Pass 36 — adapter normalization, CVP state fixtures, profile-store work unit

Date 2026-09-30.

## Portage adapter normalization
Receipt `54011f371c90eb31d8afd95e504bf7138a5f7c02`.

Directory-level benchmark identity overlap:
- coding: 20 adapters/ identities, 20 benchmark_adapters/, **20 overlap**;
- reasoning: 14 / 14, **14 overlap**;
- database: 3 / 3, **3 overlap**;
- transpilation: 1 / 1, **1 overlap**;
- agent: 2 adapters/ vs 5 benchmark_adapters/, 2 overlap and 3 benchmark-only.

Thus most large adapter categories are duplicated at identity level across the two trees. This does not prove byte/semantic equivalence, but raw file/tree counts massively overstate independent product breadth.

Next normalization class per overlap: CANONICAL / GENERATED_MIRROR / LEGACY / INTENTIONAL_VARIANT.

## PhenoLab CVP state machine
Receipt `13139fa49b0ab2fc666b3fcb783410a9fdd854a2`.

Spec-side executable fixtures now cover create→candidate→assessment→decision, worker replacement preserving budget/Decision, unknown-Assessment rejection and duplicate Decision conflict. This operationalizes UJ-01/03/04/06/07 identity semantics without pretending current product UI exists.

## PhenoMLX profile-store developer unit
Receipt `57b1f07095def5cdd802fe7613562e39795c6279`.

A bounded implementation package is now ready independent of the unavailable two-engine runtime:
- append-only simple store first;
- immutable/idempotent/versioned semantics;
- restart/reindex;
- current projections;
- corruption/concurrency/reference tests;
- KernelRegistry evidence referenced, not duplicated.

Completion of this work unit closes only profile-store semantics, not native qualification or CVP.

## Source denominator
No CLOSED numerator change. Portage duplication is now quantified but semantic equivalence/current use remains; PhenoLab fixtures are spec evidence; PhenoMLX store is not implemented yet.

Next:
1. compare representative duplicate adapter pairs structurally to infer mirror-generation pattern;
2. PhenoLab machine usability/oracle fixtures for the interaction contract;
3. Portage src/portage direct semantic mapping;
4. developer agents may independently implement the PhenoMLX profile-store work unit while VS-01 runtime remains blocked.
