# Pass 9 — independent grading of experimental candidates

Observed 2026-09-30.

## Worker separation discovered

The experiment branches created from the frozen source were subsequently implemented by another worker under the repository owner identity. They are therefore treated as implementation candidates, not recovery-author work.

- Melosviz worker head reviewed: `1066a61cabadfd3578c1e3561d23b7b5943f2a8c`, 24 commits ahead, six final changed files.
- Khostty worker head reviewed: `1a146ee2e62d94e1ffa2308652365adc2060fe72`, six commits ahead, two final changed files.

No credit is assigned from commit messages or CodeRabbit success.

## Melosviz M-E02 verdict: FAIL / REVISE

Candidate materially improves selector use, scene-indexed results, single-scene adapter projection, output isolation, cache overwrite, assembly collection, done-event outcome, structured bridge manifest and UI produced-vs-accepted language.

Critical failures remain:
1. media validity still accepts nonempty garbage MP4; the candidate's own positive SceneAdapter writes text bytes to clip.mp4 and labels it render;
2. cache hit can trust historical outcome metadata without current independent media validation;
3. web Studio status union excludes done, but generate still assigns status done;
4. no candidate-bound pytest/TypeScript/external-oracle execution receipt was found.

Independent grader review was committed onto the experiment branch at `555007ea172da914f14637f3dd593a75ca813eae`. This is feedback, not acceptance.

## Khostty K-E03 verdict: PARTIAL / EXECUTION REQUIRED

The two-file candidate is appropriately narrow. It adds fail-closed evidence-mode linking and an out-of-tree Rust/direct-C harness. It explicitly discloses unauthenticated source/origin claims and that a true upstream comparison needs separately built artifacts.

Blocking gaps:
1. library SHA authenticates bytes but not source/build provenance;
2. Rust journey is create/write/resize/render/search/snapshot, while direct C is only create/write/free—no like-for-like complexity comparison yet;
3. ABI drift/install/package evidence incomplete;
4. no exact-candidate harness execution receipt was found.

Independent review commit: `284cb52c79d23a5c4129f4996962f8dc3fedd923`.

## Handoff state

Both remain READY FOR EXPERIMENTAL IMPLEMENTATION only.
- M-E02 has an implementation candidate that must be revised and executed.
- K-E03 has a verifier candidate that must be expanded to equivalent comparison and executed with authenticated build receipts.
General dev handoff remains blocked.
