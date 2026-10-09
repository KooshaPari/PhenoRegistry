# MACE / acceptance control loop — doctrine v0.1

Date2026-09-29. Normative source for this program: current user mission. 'MACE' denotes the loop supplied in that mission; no external paper or framework identity is asserted. This is a draft architecture contract, not deployed enforcement.

## Three lifetimes and authority

WorkerAttempt is ephemeral: actor/model/tool/sandbox/lease/messages/actions. DevelopmentEffort is durable: authorized change intent, contract versions, work packages/dependencies/reviews/execution receipts and grader results. ProductState survives both: accepted product intent, world/install/pack/config identities, realized artifacts, releases, observed behavior and evidence.

Relations carry source identity, source role, observed/valid time, authority, validation state and supersession. Accepted fact, authorized decision, deterministic source fact, verified observation, imported assertion, inference and historical fact are different values. High confidence does not confer authority. Replacing a worker must not change accepted scope, erase prior attempts or reset the product's grade.

## Control loop and minimal feedback

Accepted contract/assignment -> bounded context -> worker action -> independent grader -> dimensional result -> localized feedback -> next minimal context -> retry/replan/clarify/escalate. Feedback contains failed criterion IDs, exact candidate/configuration, nearest relevant source/counterexample, raw evidence references and permitted next action. Do not send the whole repository after every failure. Worker may know rubric; policy independence, provenance and adversarial checks provide the defense, not obscurity.

Rubric changes are separately authorized scope changes, not engineering improvement. Implementation workers cannot edit a required criterion, suppress a collector failure or replace raw evidence to mark their own attempt accepted. Required policy/approved verifier digests and authorization decisions must be stored outside the worker's writable candidate tree. Signatures/branch protection/trust-root deployment are still outstanding, not supplied by this Markdown.

## Evidence identity

An evaluation binds product; capability/journey subject; accepted contract and criterion revision; implementation/build/artifact candidate; configuration including feature flags, content/mod/model versions; environment and host/world/install identity; verifier name/version/build; run/evaluation ID; observed timestamp and permitted freshness window; raw artifact digests and provenance. Bind build provenance separately from gameplay/model predicates, using in-toto Statement v1/SLSA1.2 where appropriate rather than inventing a signing scheme.

Absence, skip, collection error, stale identity, wrong candidate, conflicting observations, unknown criterion, zero executed cases and a mere historical work-completion label cannot be green. Critical dimensions are conjunctions, not compensating averages. A legitimate partial result is useful but must remain partial.

Dino's evidence additionally binds host game/Unity/backend/loader, running installation root, scene/world generation and pack bytes. Civis binds world/model version, authoritative runtime mode, snapshot/component identities and intervention; global future bit-identical replay is not imposed against the explicit charter.

## Bidirectional trace constraints

Required chain: accepted source -> decision/design -> semantic obligation/quality overlay -> journey/stage -> actual implementation symbol plus mounted caller -> oracle -> evaluation -> artifact -> observed runtime subject. Reverse lookup must locate accepted reasons for shipped behavior and candidate/version qualified by a passing test. Every edge preserves provenance and authority. Quarantine generated IDs, invented paths, same-ID/different-meaning collisions and stale catalog rows until semantically reconciled. No file-name match can be treated as implementation evidence.

Functional behavior and quality overlays remain separate. Latency/reliability/security/accessibility claims bind the subject, workload, environment and exact policy target they qualify. Targets not recovered/accepted are unresolved, never guessed 'industry standard' thresholds.

## Measurements

Track separately: contract resolution; functional realization; trace validity; current evidence; required journey closure; regression; applicable quality dimensions; uncertainty; transition debt; external-user outcomes. Denominators and weights must be versioned/accepted. Unknown denominators mean no percentage. A stage passes only when required actor-to-outcome journeys and critical quality gates close; broad scaffolding is not a narrow usable product.

For stable definitions across multiple comparable observations, calculate position, engineering delta, scope delta, evidence age, regressions and velocity. Stagnation/oscillation require history; no slope or asymptote from a single sample. Optional/scoped-out features cannot be silently included/excluded to manipulate a grade.

## Adversarial review matrix

| Attack | Required defense / expected result |
|---|---|
| Worker emits pass with no executed cases or raw artifact | Block; collector completeness and nonempty cases/artifacts required |
| Receipt from last week's different binary/pack/world | Block exact mismatch or freshness violation, retain historical observation |
| Same criterion appears twice, once fail and once pass | Conflict blocks; never select whichever result is favorable |
| Worker shrinks rubric or disables critical check in candidate | External accepted policy and approved verifier identity remain authoritative |
| Build attestation substituted for user journey | Predicate/subject mismatch; build success not behavior qualification |
| SDK/unit smoke substituted for installed DINO or different Civis mode | Host/runtime subject mismatch; mounted journey required |
| Saved metadata removed to bypass current-format obligations | Explicit classification and corruption control, not implicit legacy green |
| Game shows fixed 'emergent' labels after causal subsystem removed | Behavioral ablation/control exposes manufactured success |
| Worker lease/model/process replaced | Durable effort/evidence/history remain; no reset of accepted product state |
| Fresh review uses same worker's summary without raw sources | Not independent evidence; review must actively seek missing interpretations |

## Synthetic predicate experiment

A local Python experiment tested a narrow fail-closed conjunction predicate with synthetic identity-bound fixtures. It exercised valid evidence, worker replacement, each missing/wrong identity dimension, failed/skipped/malformed outcomes, empty/missing/duplicate/conflicting criteria, worker rubric-shrinking, stale/future timestamps, collector errors and absent/tampered artifacts. All50 expected classifications matched in the initial execution. **This is not Dino/Civis verification, not an independent review, not authentication/security proof, and not full input fuzzing.** Exact source digest and raw receipt are preserved in the experiment artifact/receipt when attached. Source SHA256: `70571917cc59c39eb99da4219bfa2777ee5248c2550237c8da61401b674e826d`.

Policy and collector inputs were assumed independent/trusted in that experiment. An authenticated collector lying, trust-root compromise, hostile code changing both implementation and grader, artifact-signature verification and protected policy deployment remain untested. The experiment is quarantined from product-completion grading.

Primary references accessed2026-09-29: https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md and https://slsa.dev/spec/v1.2/provenance . Their formats establish provenance vocabulary, not the truth of a domain-specific behavioral predicate.
