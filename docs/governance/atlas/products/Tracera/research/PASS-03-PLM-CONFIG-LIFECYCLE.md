# Tracera Research Pass 3 — PLM, Configuration, Digital Thread and Lifecycle Semantics

**Status:** INCOMPLETE / architecture-changing.
**Date:** 2026-09-29.

## 1. Why PLM changes the ontology

Software-oriented traceability often models static links between requirements, code and tests. PLM/configuration management adds a harder question:

> Which exact product structure, revision, variant, configuration, unit/fleet population, environment and time interval does this fact apply to?

Without this, a canonical graph lies as soon as multiple variants/releases/configurations coexist.

## 2. Product structures and views

PLM commonly distinguishes multiple structures/BOMs for the same product and lifecycle purpose.

Transferable Tracera model:

```text
Product
  -> ProductStructureView
       kind = experience | functional | architecture | source |
              supply-chain | verification | deployment | service | ...
       root / membership / ordering / relation semantics
```

Views are not copies of the product. They are projections over shared canonical entities and relations.

### Import decision

Adopt the PLM principle of multiple purpose-specific product structures. Do not force one universal tree.

## 3. Revision vs version vs configuration

These must be distinct.

- **Entity identity:** stable thing across change.
- **Revision:** accepted evolution of that thing's definition.
- **Artifact version:** concrete produced/versioned artifact.
- **Configuration:** compatible selection of exact revisions/versions/options that constitutes a product state.
- **Baseline:** frozen named configuration/contract snapshot for a purpose.

Current Tracera BaselineRevision is too narrow to carry all of these semantics by itself.

## 4. Effectivity / applicability

A relationship or requirement may apply only under conditions.

Candidate applicability dimensions:
- product/edition/variant;
- component revision;
- release/version range;
- platform/OS/architecture;
- deployment/environment;
- tenant/customer class;
- geography/regulatory regime;
- feature-flag/evaluation context;
- date/time interval;
- rollout cohort;
- hardware/device model;
- configuration expression.

Candidate relation shape:

```text
Relation
  source
  target
  type
  valid_time
  transaction_time
  applicability/effectivity predicate
  provenance
  authority
  confidence
```

### Import decision

Effectivity becomes a first-class Tracera research requirement. A static edge is insufficient for mature product truth.

## 5. Variant / product-line management

Do not model variants as independent duplicated products when they share a product family.

Need semantics for:
- common core;
- optional/alternative features;
- constraints between options;
- inherited requirements/evidence;
- overridden requirements;
- variant-specific implementation;
- variant-specific verification;
- evidence reuse and invalidation.

Codebeamer/Polarion/PLM product-line practices and feature-model research should inform this.

## 6. As-intended / as-designed / as-built / as-deployed / as-observed

PLM's as-designed/as-built/as-maintained distinction maps strongly into Tracera.

Candidate generalized states:

- **accepted intent** — what should exist;
- **designed** — architecture/design realization;
- **implemented** — source/config realization;
- **built** — exact artifacts produced;
- **released** — approved product configuration;
- **deployed** — exact environment configuration;
- **observed** — runtime behavior/evidence;
- **maintained/current** — current supported operational configuration.

These are not one mutable status. They are related projections/facts with possible disagreement.

**Dissatisfaction often is the delta between them.**

## 7. Change objects

PLM Engineering Change Request/Order semantics are close to Tracera graph delta.

Candidate Tracera change object:

```text
ProductChange
  motivation / dissatisfaction
  proposed graph delta
  affected configurations
  impact analysis
  authorization
  realization references
  migration/rollout plan
  verification obligations
  evidence invalidation
  effective configuration/time
  reconciliation status
```

AgilePlus may execute realization, but Tracera owns the product-change meaning and reconciliation.

## 8. Lifecycle maturity

Avoid one simplistic ProductStatus.

Entities/configurations may move through distinct lifecycle states such as:
- concept/proposed;
- working;
- reviewed;
- accepted;
- released;
- supported;
- deprecated;
- retired/obsolete.

Different entity kinds can have different lifecycle state machines.

Release channels (nightly/canary/preview/stable/LTS) are orthogonal to lifecycle maturity and may coexist.

## 9. Software delivery lifecycle projection

Tracera should understand but not own external execution systems for:

```text
intent
 -> design
 -> implementation
 -> build
 -> verification
 -> release candidate
 -> release
 -> rollout/deployment
 -> operation
 -> observation
 -> incident/problem/dissatisfaction
 -> change
 -> deprecation/migration
 -> LTS/support
 -> retirement
```

Each stage emits facts/evidence into the product model.

## 10. Configuration compatibility and evidence

Evidence is only reusable when its applicability covers the target configuration.

Example:

```text
test result:
  source revision = abc
  API schema = 12
  DB schema = 18
  browser = Chrome 141
  platform = Windows
  feature flags = {...}
  environment = staging
```

A green result cannot automatically validate another configuration.

Need compatibility/subsumption rules rather than exact-equality-only matching, or verification becomes prohibitively expensive.

## 11. Temporal model

At least four time concepts may matter:
- fact recorded_at / transaction time;
- real-world valid/effective time;
- accepted baseline/revision;
- observed/execution time.

Do not conflate these.

Bitemporal database patterns are relevant but may not be sufficient because configuration/effectivity is multidimensional, not only temporal.

## 12. Digital thread

The useful digital-thread concept is not "put everything in one database."

It is persistent identity and traversable provenance across lifecycle transitions and authoritative systems.

Tracera should preserve:
- native source-system identity;
- canonical Tracera identity where needed;
- mapping/provenance;
- version/configuration context;
- transformation/derivation history.

## 13. Digital twin caution

"Digital twin" is useful only if Tracera actually maintains a meaningful synchronized representation of product state. Avoid the term as marketing if the model is merely linked documentation.

A stronger software-product twin requires observed realization/runtime state and reconciliation with accepted intent.

## 14. Lifecycle concepts likely NOT to copy wholesale

- manufacturing routing/shop-floor execution when irrelevant;
- supplier approval ceremony for ordinary software;
- document-signature workflows where risk does not justify them;
- physical serial/lot tracking unless hybrid/device products require it;
- heavyweight release boards.

Import semantics, not enterprise ceremony.

## 15. Architecture amendments implied

Current Tracera design likely needs explicit first-class concepts for:
- ProductFamily / Product / Variant;
- ProductStructureView;
- Revision;
- Configuration;
- Baseline;
- Applicability/Effectivity;
- ProductChange / GraphDelta;
- LifecycleState;
- Release/Channel;
- BuildArtifact;
- Deployment;
- Environment;
- Observation applicability;
- supersedes/derives/from/configured-by relations.

These are candidates pending Pass 3 falsification, not yet final schema.

## 16. Pilot implications

The eventual pilot should include ordinary software cases where these semantics may or may not pay off:
- web app with feature flags and canary rollout;
- multi-platform desktop app;
- API with old/new client compatibility;
- SaaS editions/tenant variants;
- dependency vulnerability affecting only some configurations;
- LTS vs current release;
- optional hybrid hardware/software product.

Measure whether agent-maintained applicability/configuration materially improves impact accuracy and false-green prevention without unacceptable overhead.

## 17. Remaining Pass 3 work

- deeper Teamcenter/Windchill/Aras/3DEXPERIENCE comparison;
- standards: STEP/AP242 where relevant, ReqIF, OSLC CM, SysML configurations;
- software product-line engineering and feature-model literature;
- semantic-version/compatibility and deployment/progressive-delivery models;
- configuration-management standards/practices;
- explicit lifecycle state-machine synthesis;
- map these concepts against current Tracera schema and identify migration cost.

Do not treat Pass 3 as closed.
