# Pass 17 — cross-object state machines, contract v0.3, source coverage

Date 2026-09-30.

All three next-step cross-object state-machine prototypes were implemented on specification branches, reviewed adversarially and used to revise the candidate contracts.

## Portage
State machine `12578a57449555206beb2dbaf92ca1713ba1bf52`; review `8a17f8269c6cdf32d8d6508bd97b4137be10dc04`; v0.3 `ec711fc343df84eaa2cd274cc5cfb955fb7d2ce1`; coverage `386d6f45d400d7d0b2a7ed9a75a0ca5fff501996`.

Prototype covers duplicate delivery, cancellation+late evidence, required artifact failure, regrade preservation, evidence disposal and imported status.

Contract correction: historical Assessment validity is distinct from present reverification state. Legitimate retention expiry can make regrade unavailable without silently rewriting historical accepted state.

Tree audit also confirms substantial existing security/network/secrets/release/CLI/persistence/viewer machinery; remaining gap is semantic authority/export, not absence of surfaces.

## PhenoMLX
State machine `a12bb3d63675dcd982483c0ff31a83ec81eaca4a`; review `bfdf6a28802313bac25e0446c218144d4bbf17c6`; v0.3 `73108f4284f14b736eaa7047b96aa9ec2d802be2`; coverage `3fd8c8c365a2a608a409aea710ca331c7b42c2ab`.

Prototype covers fallback identity, generation stickiness, partial stream, support-vs-admission, cache-domain identity and withdrawal.

Contract correction: SupportEnvelope is a versioned projection over immutable profile identity; withdrawal never mutates historical RealizedProfile/QualificationAssessment. CapacitySnapshot must be time/generation/environment scoped.

## PhenoLab
State machine `f42ed7675b5993082aa5a2bfd5b787a08ebadb93`; review `d3989323a6fb76c6c7e229c79b28b2e2446182ca`; v0.3 `e5a3a08a41d1ff1549660248d255ae75c400c0dd`; coverage `81d8264c5fae17574e5ce0b20ee1c810ab2e832b`.

Prototype covers wrong-candidate evidence, epoch changes, missing/critical evidence, human Decision vs Assessment, worker replacement, rebase and imported evidence.

Contract correction: Decision references Assessment IDs; human rejection can disagree with green Assessment without rewriting it; designated non-overridable gate cannot be overridden under same epoch—policy change requires new epoch/reassessment. PromotionRecord references exact accepted subject revision.

## Gate consequence

The state models survived this isolated cross-object falsification pass. That is meaningful architecture evidence but not native integration validation.

v0.3 is now the current candidate contract for each product. None is promoted to accepted baseline.

Next frontier:
1. implement spec-side integration adapters against **real existing classes** where dependency-light:
   - Portage canonical subject projection from real TrialConfig/TrialResult shapes;
   - PhenoMLX typed profile wrapper around two real BackendBase subclasses without loading models;
   - PhenoLab adapter from existing gate/promotion primitives into typed Assessment/Decision records.
2. execute those tests if repository imports permit; record exact failures otherwise.
3. expand source coverage on remaining API/security/release/integration boundaries.
4. then run another architecture falsification review and decide whether v0.3 can become candidate baseline.

No production mutation or completion percentage.
