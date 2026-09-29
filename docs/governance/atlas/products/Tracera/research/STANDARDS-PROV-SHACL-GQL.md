# Tracera Standards Addendum — Provenance, Validation and Graph Query

**Date:** 2026-09-29.
**Status:** research candidate decisions.

## W3C PROV

PROV provides interoperable provenance concepts around Entity, Activity and Agent plus derivation/generation/attribution/influence.

### Tracera implication

Before inventing a proprietary provenance graph for:
- generated artifacts;
- observations;
- agent/human actions;
- transformations;
- evidence derivation;
- imported facts;
- graph deltas;

map Tracera provenance onto PROV-DM/PROV-O and identify actual gaps.

Authority/confidence/product semantics remain Tracera-specific, but provenance should interoperate where practical.

## SHACL

SHACL validates data graphs against immutable shape graphs and emits structured validation reports. Shapes can also drive UI, code generation and data integration.

SHACL 1.2 is under active W3C development in September 2026.

### Tracera implication

Evaluate SHACL-like or SHACL-native structural validation for:
- product graph invariants;
- projection-specific required relations;
- cardinality/type constraints;
- stage structural prerequisites;
- adapter/import validation.

This is complementary to executable behavioral graders. Structural graph conformance is not behavioral product acceptance.

The immutability rule during validation aligns strongly with anti-Goodhart grader separation.

## ISO GQL

ISO/IEC 39075:2024 defines a standard property-graph data/query language; edition 2 is already under development.

### Tracera implication

The logical graph API/storage benchmark should consider standards trajectory and query portability, not only current Neo4j Cypher ergonomics.

Do not make Tracera's domain model depend on one vendor dialect when a standardized property-graph language exists.

## Decision gate

For PROV, SHACL and GQL:
- prototype mapping;
- identify semantic gaps;
- assess implementation/library maturity;
- decide native use vs adapter-compatible internal representation;
- add conformance/interchange tests if adopted.
