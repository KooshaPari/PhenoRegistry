# Initial WBS, PERT, and dependency DAG

## Estimate warning

All estimates are three-point **agent-hour planning estimates**, not measured delivery commitments.

PERT expected value:

\[
E = (O + 4M + P) / 6
\]

The computed critical path below assumes unlimited parallel workers and no resource contention. It therefore excludes reviewer bottlenecks, human decisions, platform hardware, API limits, CI queues, and migration windows.

## Dependency-only critical path

**Expected length:** 605.00 agent-hours  
**Path:** T-000 → T-020 → T-040 → T-060 → T-610 → T-620 → T-700 → T-710 → T-720

The long applied-product closure task dominates this initial aggregate model. In practice it will be decomposed by family and product; this path is a portfolio-level placeholder, not one monolithic task assignment.

## Task table

| ID | Phase | Work | Predecessors | O/M/P hours | PERT | Initial status |
|---|---|---|---|---|---:|---|
| T-000 | P0 | Confirm 146-repo census and observation baseline | — | 4/8/16 | 8.67 | DONE |
| T-010 | P0 | Build repeatable GitHub live-fact observer | T-000 | 6/16/32 | 17.00 | READY |
| T-020 | P0 | Adopt typed IDs and machine schemas | T-000 | 4/10/20 | 10.67 | READY |
| T-030 | P1 | Decide live-fact versus curated-registry authority | T-010,T-020 | 8/20/40 | 21.33 | BLOCKED_DECISION |
| T-040 | P1 | Decide product-local versus cross-product spec authority | T-020 | 10/28/56 | 29.67 | BLOCKED_DECISION |
| T-050 | P1 | Decide active enforcement authority | T-020 | 8/20/40 | 21.33 | BLOCKED_DECISION |
| T-060 | P1 | Implement worker handoff and portfolio validation | T-030,T-040,T-050 | 8/20/40 | 21.33 | BLOCKED |
| T-100 | P2 | Audit vibe monitoring micro-family | T-020 | 6/14/28 | 15.00 | READY |
| T-110 | P2 | Stage monitoring consolidation/tombstones | T-100,T-030 | 8/20/40 | 21.33 | BLOCKED |
| T-120 | P2 | Forensic audit Planify and Planify2 | T-020 | 16/40/80 | 42.67 | READY |
| T-130 | P2 | Stage canonical Planify fork migration | T-120,T-030 | 16/36/72 | 38.67 | BLOCKED |
| T-140 | P2 | Forensic audit FocalPoint and phenotype-apps | T-020 | 24/64/128 | 68.00 | READY |
| T-150 | P2 | Stage FocalPoint recovery and canonicalization | T-140,T-030,T-040 | 24/64/128 | 68.00 | BLOCKED |
| T-160 | P2 | Adjudicate pheno shelf/meta role | T-020 | 4/12/24 | 12.67 | READY |
| T-170 | P2 | Close pheno meta/workspace disposition | T-160,T-030 | 6/14/28 | 15.00 | BLOCKED |
| T-200 | P3 | Scan consumers and overlap for foundation fragments | T-030,T-040,T-050 | 24/64/128 | 68.00 | BLOCKED |
| T-210 | P3 | Select foundation package homes and compatibility plan | T-200 | 16/40/80 | 42.67 | BLOCKED |
| T-220 | P3 | Stage foundation consolidation wave 1 | T-210,T-060 | 32/96/192 | 101.33 | BLOCKED |
| T-300 | P4 | Audit execution/agent family capability and lineage | T-060 | 32/96/192 | 101.33 | BLOCKED |
| T-310 | P4 | Run bounded Agentora framework pilot | T-300 | 32/72/144 | 77.33 | BLOCKED |
| T-320 | P4 | Decide execution family target topology | T-300,T-310 | 16/48/96 | 50.67 | BLOCKED_DECISION |
| T-330 | P4 | Stage execution family migration wave 1 | T-320,T-220 | 48/120/240 | 128.00 | BLOCKED |
| T-400 | P4 | Forensic audit Helios family and consolidation branch | T-060 | 32/96/192 | 101.33 | BLOCKED |
| T-410 | P4 | Run Helios app/CLI/headless comparative pilot | T-400 | 32/80/160 | 85.33 | BLOCKED |
| T-420 | P4 | Stage Helios target topology and shared-code migration | T-410,T-320 | 32/80/160 | 85.33 | BLOCKED |
| T-500 | P5 | Audit router/gateway/proxy upstream and semantic lineage | T-060 | 48/128/256 | 136.00 | BLOCKED |
| T-510 | P5 | Run router reliability/performance/DX pilot | T-500 | 40/96/192 | 102.67 | BLOCKED |
| T-520 | P5 | Select and stage routing target topology | T-510,T-220 | 24/64/128 | 68.00 | BLOCKED |
| T-600 | P6 | Audit compute/inference/fleet/fabric boundaries | T-060 | 48/128/256 | 136.00 | BLOCKED |
| T-610 | P7 | Triage and gate all applied-product families | T-060 | 48/120/240 | 128.00 | BLOCKED |
| T-620 | P7 | Run selected applied-product pilots and closure waves | T-610 | 80/240/480 | 253.33 | BLOCKED |
| T-700 | P8 | Generate public/developer/operator/history portfolio projections | T-110,T-130,T-150,T-170,T-330,T-420,T-520,T-600,T-620 | 20/48/96 | 51.33 | BLOCKED |
| T-710 | P8 | Execute approved archive/tombstone/redirect wave | T-700 | 24/64/128 | 68.00 | BLOCKED |
| T-720 | P8 | Validate final authority graph, birth policy and counts | T-710 | 12/32/64 | 34.00 | BLOCKED |

## DAG

```mermaid
flowchart TD
  T_000["T-000 Confirm 146-repo census and observation baseline"]
  T_010["T-010 Build repeatable GitHub live-fact observer"]
  T_020["T-020 Adopt typed IDs and machine schemas"]
  T_030["T-030 Decide live-fact versus curated-registry authority"]
  T_040["T-040 Decide product-local versus cross-product spec authority"]
  T_050["T-050 Decide active enforcement authority"]
  T_060["T-060 Implement worker handoff and portfolio validation"]
  T_100["T-100 Audit vibe monitoring micro-family"]
  T_110["T-110 Stage monitoring consolidation/tombstones"]
  T_120["T-120 Forensic audit Planify and Planify2"]
  T_130["T-130 Stage canonical Planify fork migration"]
  T_140["T-140 Forensic audit FocalPoint and phenotype-apps"]
  T_150["T-150 Stage FocalPoint recovery and canonicalization"]
  T_160["T-160 Adjudicate pheno shelf/meta role"]
  T_170["T-170 Close pheno meta/workspace disposition"]
  T_200["T-200 Scan consumers and overlap for foundation fragments"]
  T_210["T-210 Select foundation package homes and compatibility plan"]
  T_220["T-220 Stage foundation consolidation wave 1"]
  T_300["T-300 Audit execution/agent family capability and lineage"]
  T_310["T-310 Run bounded Agentora framework pilot"]
  T_320["T-320 Decide execution family target topology"]
  T_330["T-330 Stage execution family migration wave 1"]
  T_400["T-400 Forensic audit Helios family and consolidation branch"]
  T_410["T-410 Run Helios app/CLI/headless comparative pilot"]
  T_420["T-420 Stage Helios target topology and shared-code migration"]
  T_500["T-500 Audit router/gateway/proxy upstream and semantic lineage"]
  T_510["T-510 Run router reliability/performance/DX pilot"]
  T_520["T-520 Select and stage routing target topology"]
  T_600["T-600 Audit compute/inference/fleet/fabric boundaries"]
  T_610["T-610 Triage and gate all applied-product families"]
  T_620["T-620 Run selected applied-product pilots and closure waves"]
  T_700["T-700 Generate public/developer/operator/history portfolio projections"]
  T_710["T-710 Execute approved archive/tombstone/redirect wave"]
  T_720["T-720 Validate final authority graph, birth policy and counts"]
  T_000 --> T_010
  T_000 --> T_020
  T_010 --> T_030
  T_020 --> T_030
  T_020 --> T_040
  T_020 --> T_050
  T_030 --> T_060
  T_040 --> T_060
  T_050 --> T_060
  T_020 --> T_100
  T_100 --> T_110
  T_030 --> T_110
  T_020 --> T_120
  T_120 --> T_130
  T_030 --> T_130
  T_020 --> T_140
  T_140 --> T_150
  T_030 --> T_150
  T_040 --> T_150
  T_020 --> T_160
  T_160 --> T_170
  T_030 --> T_170
  T_030 --> T_200
  T_040 --> T_200
  T_050 --> T_200
  T_200 --> T_210
  T_210 --> T_220
  T_060 --> T_220
  T_060 --> T_300
  T_300 --> T_310
  T_300 --> T_320
  T_310 --> T_320
  T_320 --> T_330
  T_220 --> T_330
  T_060 --> T_400
  T_400 --> T_410
  T_410 --> T_420
  T_320 --> T_420
  T_060 --> T_500
  T_500 --> T_510
  T_510 --> T_520
  T_220 --> T_520
  T_060 --> T_600
  T_060 --> T_610
  T_610 --> T_620
  T_110 --> T_700
  T_130 --> T_700
  T_150 --> T_700
  T_170 --> T_700
  T_330 --> T_700
  T_420 --> T_700
  T_520 --> T_700
  T_600 --> T_700
  T_620 --> T_700
  T_700 --> T_710
  T_710 --> T_720
```

## Scheduling policy

- Run `T-010`, `T-020`, `T-100`, `T-120`, `T-140`, and `T-160` in bounded parallel lanes.
- Do not execute migration tasks until authority decisions and worker validation exist.
- Split `T-620` into one task group per applied-product family after triage.
- Re-estimate from measured audit velocity after the first three closure units.
- Maintain a resource-constrained schedule separately.
- Human-decision tasks cannot be “parallelized away” by more agents.
