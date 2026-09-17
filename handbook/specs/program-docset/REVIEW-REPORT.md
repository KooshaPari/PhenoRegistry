# REVIEW-REPORT.md — docs-5 (Phenotype Atlas & Assurance Program v1.4)

**Reviewer:** Jcode (direct, subagents failed on OpenCode/OpenAI auth)
**Date:** 2026-09-17
**Files reviewed:** ~351 .md files (structural review of key files, all directories surveyed)

---

## Executive Summary

docs-5 is the **Phenotype ecosystem's master documentation corpus**, currently at **revision 1.4** (September 16, 2026). It contains 166 proposed program requirements, 132 planned work packages, 34 product dossiers, 15 ADRs, and a comprehensive federation amendment. The documentation is mature, well-structured, and current. The primary issues are **volume** (351 markdown files is excessive for a 24-repo ecosystem) and **overlap** between multiple documents covering similar ground.

---

## Directory-by-directory Assessment

### Root-level documents (20 files)

| File | Usefulness | Notes |
|------|-----------|-------|
| START-HERE.md | HIGH | Clean entrypoint, current at v1.4, links to all key docs |
| README.md | HIGH | Good overview, 166 requirements, 132 work packages |
| PRD.md | HIGH | Product requirements document |
| HLD.md | HIGH | High-level design |
| LLD.md | HIGH | Low-level design |
| ALD.md | HIGH | Abstraction-layer design |
| SPECIFICATION.md | HIGH | Normative specification |
| REQUIREMENTS.md | HIGH | Program-level requirements |
| DOMAIN_MODEL.md | MEDIUM | Domain model - useful but verbose |
| ROADMAP.md | HIGH | Outcome-based roadmap (Phases A-D), no fabricated timelines |
| INDEX.md | MEDIUM | Navigation index - overlaps with README.md |
| SSOT_AUTHORITY.md | HIGH | Clear authority chain, no competing writable copies |
| OWNER-QUICKSTART.md | MEDIUM | Agent dispatch guide - overlaps with prompts/ |
| TRACEABILITY.md | HIGH | Intent-through-installation traceability |
| VALIDATION_REPORT.md | MEDIUM | Validation results |
| REVISION-1.1.md | LOW | Historical revision record |
| CHANGELOG-V1.2.md | LOW | Historical changelog |
| CHANGELOG-V1.3.md | LOW | Historical changelog |
| CHANGELOG-V1.4.md | LOW | Historical changelog |
| VALIDATION-V1.2.md | LOW | Historical validation |

### adr/ (15 files)
- **Usefulness:** HIGH — Well-structured ADRs covering key decisions
- **Overlap:** ADR-001 through ADR-014 overlap significantly with canonicalization packet's 24 decisions
- **Freshness:** Current

### architecture/ (5 files)
- **APPLET-CONTRACT.md** — Recursive applet boundaries (HIGH)
- **ATLAS-EXTRACTION.md** — Atlas extraction procedures (MEDIUM)
- **DEPENDENCY-ADOPTION.md** — Tool/language adoption decisions (HIGH, overlaps with canonicalization)
- **ECOSYSTEM-FIRST-EVOLUTION.md** — Consumer-driven evolution (HIGH)
- **INCREMENTAL-STATE.md** — Incremental state management (MEDIUM)

### federation/ (17 files)
- **Usefulness:** HIGH — The v1.3 amendment is the most recent major addition
- **Core concept:** "Independently useful applications that discover compatible peers and become one coherent workspace"
- **Key docs:** PRODUCT-CONTRACT.md, EXPERIENCE-CONTRACT.md, RUNTIME-ARCHITECTURE.md, SECURITY-AND-DATA.md
- **Overlap:** Extensive internal overlap (17 files for one concept)

### portfolio/ (3 files)
- **ROSTER.md** — 42 repos, 24 non-zz active (HIGH)
- **CURRENT-REPO-INDEX.md** — Same data as ROSTER.md (DUPLICATE)
- **TAXONOMY.md** — Topic taxonomy (MEDIUM)

### prompts/ (11 files)
- **Usefulness:** MEDIUM — Agent prompt templates
- **Overlap:** ONE-CHAT-PER-REPOSITORY.md, MASTER-COORDINATOR.md, PRODUCT-OWNER.md cover similar ground
- **Note:** These are operational prompts, not documentation

### proof/ (11 files)
- **Usefulness:** HIGH — Capability composition, grading, visual verification
- **Key docs:** CAPABILITY-COMPOSITION.md, GRADING.md, VISUAL-VERIFICATION.md, DESIGN-STATE.md
- **Freshness:** v1.4 (September 16, 2026)

### qa/ (5 files)
- **ASSURANCE-CONTRACT.md** — QA/QC/QE contract (HIGH)
- **METRICS.md** — Measurement families (HIGH)
- **NEGATIVE-CONTROLS.md** — Instrument qualification (HIGH)
- **DOCUMENTATION-COVERAGE.md** — Doc coverage (MEDIUM)
- **MATRIX-DESIGN.md** — Matrix design (MEDIUM)

### specs/ (16 spec subdirectories)
- **Usefulness:** HIGH — Each spec has plan/research/spec/tasks
- **Overlap:** Many specs cover overlapping concerns (identity, intent, atlas, specification, assurance)
- **Note:** 16 specs for 24 repos suggests heavy process overhead

### products/ (34 directories, ~238 files)
- **Usefulness:** HIGH — Per-product dossiers with AGENT-PROMPT, DOSSIER, FEDERATION, NEXT-ACTIONS, PROOF-AND-GRADE, START-HERE, STATE
- **Overlap:** Many products share similar dossier structure (good) but some have stale STATE.md
- **Key products:** Melosviz, OmniRoute, PhenoMLX, HeliosLab, Portage, Tracera, Substrate

### Other directories
- **errors/** (16 files) — Error taxonomy (MEDIUM)
- **intent/** (2 files) — User intent synthesis (MEDIUM)
- **operations/** (3 files) — Agent execution, delivery, security (MEDIUM)
- **research/** (3 files) — Comparative pilots (MEDIUM)
- **risks/** (1 file) — Risk register (HIGH)
- **work/** (3 files) — WBS, scheduling, consumer impact (MEDIUM)

---

## CROSS-REFERENCE: docs-5 vs phenotype-canonicalization

| docs-5 Document | Canonicalization Overlap | Recommendation |
|-----------------|------------------------|----------------|
| adr/ADR-001 through ADR-014 | REPORT.md decisions | Canonicalization is more detailed; ADRs should reference it |
| architecture/DEPENDENCY-ADOPTION.md | Tool adoption decisions | Merge canonicalization's candidate analysis |
| portfolio/ROSTER.md | 46 repo identities | Canonicalization found more repos; merge |
| SSOT_AUTHORITY.md | Authority chain | Canonicalization's G13 finding enriches this |
| prompts/MASTER-COORDINATOR.md | AGENT-HANDOFF.md | Canonicalization's worker roles are more specific |

---

## RECOMMENDATIONS

### HIGH VALUE (preserve as-is)
1. **START-HERE.md** — Clean entrypoint, current
2. **README.md** — Good overview
3. **ROADMAP.md** — Outcome-based, honest
4. **SSOT_AUTHORITY.md** — Clear authority chain
5. **proof/CAPABILITY-COMPOSITION.md** — Key v1.4 concept
6. **federation/README.md** — Clean federation overview
7. **qa/ASSURANCE-CONTRACT.md** — Core QA contract
8. **portfolio/ROSTER.md** — Active roster

### OVERLAPPING (consolidate)
1. **INDEX.md + README.md** — Merge (both are navigation)
2. **portfolio/ROSTER.md + CURRENT-REPO-INDEX.md** — DUPLICATE, delete one
3. **prompts/*.md (11 files)** — Consolidate into 2-3 files
4. **federation/ (17 files)** — Reduce to 5-7 core files
5. **specs/ (16 subdirs)** — Many cover overlapping concerns
6. **CHANGELOG-V1.2/V1.3/V1.4** — Consolidate into single CHANGELOG.md

### STALE
1. **REVISION-1.1.md** — Historical, superseded
2. **VALIDATION-V1.2.md** — Historical, superseded by proof/VALIDATION.md
3. **OWNER-QUICKSTART.md** — Overlaps with START-HERE.md

### MISSING
1. **No unified README for products/** — Each product has dossier but no overview index
2. **No cross-product dependency graph** — Which products depend on which
3. **No automated freshness checker** — Dossiers may go stale silently
4. **No contributor guide** — How to add a new product to the ecosystem

### VOLUME CONCERN
351 markdown files for 24 active repos is ~15 files per repo. This is excessive. The federation/ directory alone has 17 files for a concept that hasn't been implemented yet. Consider a "documentation budget" of 5-7 files per active concept.
