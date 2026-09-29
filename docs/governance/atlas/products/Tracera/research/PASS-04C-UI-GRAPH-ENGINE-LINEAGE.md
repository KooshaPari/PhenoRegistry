# Tracera Research Pass 4C — UI, Graph Engine and Internal-Lineage Constraints

**Status:** active research supplement.
**Date:** 2026-09-29.

## 1. Internal lineage constraints recovered

Additional prior-conversation archaeology confirms:

- By 2026-06-25 Tracera was intended as editable multi-view node graphs spanning SBOM→UI trees→functional requirements with default tracing to requirements/tests/entities.
- The longer-term direction explicitly moved from agent dispatch toward a PM-first/no-code product editor using reusable code/patterns.
- By 2026-09-15 the persistent traversable/searchable product model and continuous-improvement loop were explicitly primary; audit/evidence ledger was subordinate.
- Dissatisfaction included bugs, missing capabilities, performance/usability issues and other gaps, with automated detection/resolution and bounded expansion/collapse.
- Accepted intent, observed state and hypotheses should remain distinct, with uncertainty/staleness represented.
- Tracera owns product state/relationships/assessment; AgilePlus owns work/change lifecycle; workers are replaceable adapters.

These are architectural constraints, not merely historical flavor.

## 2. Graph editor SOTA

### React Flow

Strengths:
- MIT/open source;
- React-native;
- node/edge creation, dragging, selection, zoom/pan and custom rendering;
- enormous ecosystem/adoption;
- good substrate for highly custom product-specific editor UX.

Likely role:
**default implementation baseline** for an open/custom Tracera graph editor, subject to large-graph performance and accessibility validation.

### yFiles

Strengths:
- extremely mature commercial graph visualization/editor SDK;
- grouping/folding;
- filtering;
- level-of-detail rendering;
- rich interactions;
- automatic layouts;
- graph analysis/pathfinding;
- large-graph visualization;
- incremental layout preserving mental map;
- extensive customization.

Likely role:
**UX/capability benchmark** and possible commercial dependency if licensing economics are acceptable. Tracera's editor should not be called SOTA without comparing against yFiles interaction/layout capabilities.

### Rete.js

Strengths:
- visual workflow/programming editor;
- dataflow/control-flow engines;
- multiple renderer integrations.

Likely role:
useful if a Tracera projection contains executable node flows. Less obviously the primary product-graph editor because Tracera edges are primarily semantic/product relations, not only executable sockets.

### Cytoscape/ELK and others

Still require dedicated comparison for visualization/analysis/layout, especially where editing is secondary.

## 3. Editor architecture implication

The graph editor must not own product truth.

```text
canonical product graph API
        |
projection/query
        |
editor view model
        |
React Flow/yFiles/etc.
        |
proposed edit operations
        |
typed ProductChange / GraphDelta
        |
validation/impact/authorization
```

This preserves the original "editing the graph edits the product" thesis without coupling domain semantics to a UI library.

## 4. Product-editor requirements suggested by lineage

The eventual editor must support, where semantically applicable:
- projection switching without losing canonical identity;
- hierarchical expand/collapse with explicit floor/ceiling;
- local-neighborhood focus;
- page/section/action experience trees;
- cross-projection trace reveal;
- proposed edits vs accepted graph distinction;
- impact preview;
- reusable product patterns/templates;
- agent-assisted edit realization;
- graph delta review;
- dissatisfaction overlays;
- stage/grade overlays;
- uncertainty/inferred-link overlays;
- configuration/effectivity context selection;
- historical/revision comparison;
- no-code/low-code interactions where deterministic transforms/patterns exist.

## 5. Graph engine findings

### LadybugDB / Kuzu lineage

Kuzu historically offered an attractive embedded property graph with Cypher, ACID transactions, full-text/vector indexes and Rust bindings, but the original Kuzu project was archived and continued as LadybugDB.

**Lesson:** dependency health matters. Do not select a graph engine based on stale benchmarks/reputation.

### Vellis/Bibliotek

Typed local-first reified graph with schema validation, migration, snapshots/replay and MCP is relevant as an architecture/library reference for agent-facing local graph systems.

### Storage decision remains open

The domain requires:
- typed relations;
- local-first/offline;
- incremental updates;
- bounded and reverse traversal;
- effectivity/configuration resolution;
- history/provenance;
- high write/read reliability;
- export/migration;
- possibly relational joins and analytical aggregation.

A logical graph API plus benchmark corpus should precede commitment to Neo4j/Ladybug/etc.

## 6. Next experiments

- Build representative query corpus from real Tracera requirements.
- Compare SQLite/Postgres recursive relational model vs LadybugDB vs Neo4j/other credible candidates.
- Prototype editor projection in React Flow and benchmark against yFiles UX/capabilities.
- Test large graph + grouping/folding + local-neighborhood expansion.
- Test graph delta generation independent of UI library.
- Test configuration/effectivity context filtering in editor.
