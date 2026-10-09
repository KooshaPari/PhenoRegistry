# Pass 49 — non-execution finality

Date: 2026-10-01.

The user requested continuation until specification, documentation, test/oracle design and all non-code/non-execution layers reach finality.

## Fresh SOTA corrections
Current vLLM now exposes experimental per-request speculative acceptance metrics plus aggregate counters. PhenoMLX therefore uses/adapts native metrics first rather than custom-patching vLLM acceptance counters. Receipt `30cfd2be85032a6fcc6264af4e0f24c354ed4707`.

Modern Harbor docs clarify environment definitions are backend-specific by design; Harbor does not literally require a Dockerfile for every environment. Portage thesis is corrected to portable materialization/reduction of duplicate backend definitions and native/non-Docker parity, not replacing BaseEnvironment. Receipt `0e45cb7ba6ac8a24c04c237e463277c5c01b71d2`.

## Non-exec gate
Gate documents:
Portage `76c7473a5b10561e17af02cbb0d8a12d55b23408`.
PhenoMLX `ca4f6008102ad78162ea92566a686f536a335266`.
PhenoLab `d1c76c6cbc8d7607987d67ef89d2961b54e6f29c`.

## Fresh falsification
Hostile review found three MATERIAL non-runtime gaps:
- Portage portable task semantics omitted secrets/users/health/dependency/volume/lifecycle details → repaired `b0ad48d005facecdc27a0bca076876acef28a01d`.
- PhenoMLX extension API/ABI/lifecycle and experiment-factor isolation under-specified → repaired `880803f3ecfa48665f97795627b4bf5e3bd1048c`.
- PhenoLab metric/target/budget units and Pareto/non-inferiority semantics under-specified → repaired `6113924babe843b9f590a7b0b8aa3b8e499dd642`.

Fresh-review results after repair:
Portage `a1480500fa9e1c855ae5ebe489c4f2c08076f956`.
PhenoMLX `f1df7d6174be812206a43eea3f8f15dca83815ba`.
PhenoLab `09a8a28e1a900ad876231936aa623084c2d5ca80`.

No additional BLOCKING non-runtime interpretation was identified in the rerun.

## Final pre-runtime status
All three are now:
**NONEXEC_FINAL_RUNTIME_BLOCKED**

Status receipts:
Portage `937138171edbf88fdccb817a0b96c2ec37e8170c`.
PhenoMLX `9a3c41bccc26b50c0852afe939663b1979bf7961`.
PhenoLab `2f01c1b31ab57ae4582f679b65e4cd4b25d2a4d9`.

This is deliberately not "100% specification/design complete": the original strict gate requires high-risk architecture unknowns experimentally closed. The remaining blockers are product experiments EXP-P1/M1/L1 and their implementation/runtime prerequisites.

## Reopen rule
Specification reopens only if runtime falsifies an assumption, new user intent changes the thesis, new SOTA changes the alternative stack, inaccessible history contradicts lineage, or a concrete fresh-review counterexample appears.

Further requirement/doc expansion without such a trigger is scope inflation.
