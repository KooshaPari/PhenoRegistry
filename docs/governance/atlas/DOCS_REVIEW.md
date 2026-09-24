# DOCS_REVIEW.md — docs-5 (Phenotype Atlas & Assurance Program v1.4)

**Reviewer:** Jcode
**Date:** 2026-09-17
**Scope:** Full structural review of docs-5 corpus

---

## Overall Accuracy Score: 72/100

The documentation corpus is mature, well-structured, and transparent about its limitations. The core authority model, specifications, and design documents are accurate and consistent. The primary problems are **stale numerical claims in the README**, a **version mismatch in the README title**, and the inherent tension between the documented 24-repo allocation and the 33 product directories that include historical/incomplete entries.

---

## Per-Section Assessment

### 1. README.md — Accuracy: 55/100

**CRITICAL issues found:**

| Issue | Detail | Location |
|-------|--------|----------|
| Version mismatch | Title says "v1.3" but package is v1.4 | README.md:1 |
| Stale requirement count | Claims "166 proposed program requirements" but package-summary.json says 204 | README.md:14 |
| Stale work package count | Claims "132 planned work packages" but package-summary.json says 140 | README.md:14 |
| Stale test count | Claims "238 passing tests" but package-summary.json says 393 | README.md:14 |

**Evidence:**
- `records/package-summary.json`: `"program_requirements": 204`, `"proposed_work_packages": 140`, `"reference_tests_passed": 393`
- README.md:1: `# Phenotype atlas and assurance program — v1.3`
- README.md:14: `**166 proposed program requirements and 132 planned work packages**`

The README appears to have been carried forward from v1.3 without updating numerical claims for v1.4.

**What IS accurate in README:**
- The primary navigation links are valid (all referenced files exist)
- The federation amendment description is accurate
- The interpretation section correctly states this is not product certification
- All PDF and cross-references resolve to real files

### 2. START-HERE.md — Accuracy: 90/100

The entrypoint is current and accurate at v1.4. All 13 referenced priority documents exist. The one-chat-per-repository model is consistently described. Minor concern: "24 such repositories" claim in line 5 matches the owner index exactly.

**One note:** The START-HERE references `report/STATE-AND-OWNER-HANDOFF-2026-09-16.pdf` and `federation/RECIPROCAL-APPLICATION-FEDERATION.pdf` — both exist and are byte-identical as claimed.

### 3. SSOT_AUTHORITY.md — Accuracy: 95/100

Excellent. The authority table clearly distinguishes writer vs consumer for each entity type. The "no competing writable copies" policy is well-articulated. The v1.1 ecosystem evolution and v1.3 federation revisions are properly attributed with forward references. No fabricated authority claims.

### 4. PRD.md — Accuracy: 90/100

Accurate problem statement and scope definition. The "23 product/lab candidates, four pooled foundation homes and three supporting surfaces" claim in scope matches `records/products.json` (23 products) and the package-summary.json (23 dossiers). The "10 seats focus on distinct Tracera workstreams" is historical context (now superseded by one-chat-per-repo).

### 5. REQUIREMENTS.md — Accuracy: 95/100

Contains 98 `## REQ-xx-xx` headers in the markdown file. The full machine source is `records/requirements.json` (204 requirements). The markdown is an interpretation of the JSON, not the complete list. Each requirement has proper status, source, and acceptance criteria. No fabricated product-level requirements — all are clearly marked `PROPOSED_PROGRAM_REQUIREMENT`.

### 6. SPECIFICATION.md — Accuracy: 90/100

Well-structured normative specification with clear section delineation. References `records/requirements.json` as machine source. Correctly notes that AgilePlus-shaped specs are provisional. The "16 spec subdirectories" under `specs/` actually exist (001 through 016 plus FORMAT-ADAPTER.md).

### 7. ROADMAP.md — Accuracy: 95/100

Explicitly states "There is no fabricated duration." Phase A-D outcomes are described without calendar promises. The null-estimate claim is verifiable. This is one of the most honest roadmap documents in the corpus — it resists the common anti-pattern of inventing timelines.

### 8. HLD.md — Accuracy: 90/100

Five cooperating planes (Acquisition, Model, Analysis, Work, Presentation) are clearly defined. Local-first strategy is reasonable. Fault behavior and integration witness are well-specified. Correctly does not claim that the runtime exists.

### 9. ALD.md — Accuracy: 90/100

Six abstraction layers (L0-L5) are well-defined. ALD is explicitly labeled as "Abstraction-Layer Design" (not a standard AgilePlus acronym). Recursive composition section is clear. All cross-references to ecosystem evolution and federation are valid.

### 10. LLD.md — Accuracy: 90/100

Detailed contracts for entity identity, stores, incremental processing, and assurance measurement. The 7-step incremental processing model is concrete and actionable. Error/lifecycle model (NO_DATA through VERIFIED) is comprehensive.

### 11. TRACEABILITY.md — Accuracy: 85/100

Correctly states machine source is `records/traceability.json`. The INT-003 delta is properly linked. However, the claim "Product test/evidence edges are intentionally empty" is an important caveat that should be more prominent.

### 12. portfolio/ — Accuracy: 85/100

- **CURRENT-REPO-INDEX.md**: Lists 24 repos with IDs, branches, and owner chats. Matches owner-map.json claims.
- **ROSTER.md**: Contains the same data as CURRENT-REPO-INDEX.md (confirmed duplicate — ROSTER.md has the full index embedded).
- **TAXONOMY.md**: Topic taxonomy with 30 proposals.
- **live-inventory-2026-09-16.json**: Raw inventory data.

**Issue:** ROSTER.md and CURRENT-REPO-INDEX.md contain the same table. This is a documented duplicate (ROSTER.md line 1 says "The active roster is CURRENT-REPO-INDEX").

### 13. products/ — Accuracy: 80/100

33 product directories exist. 21 have complete dossiers (7 files each). 10 have incomplete dossiers (DOSSIER.md only). 2 directories (Agentora-capability, PhenoMLX) have incomplete structures.

**Issue:** The owner index lists 24 repos but products/ has 33 directories. The 9 extra directories are historical/incomplete (Pine, ResearchLedger, SessionLedger, Substrate, PhenoAI, PhenoGfx, PhenoInfra, PhenoTooling, Agentora-capability). The docs correctly note these are historical but having them without clear "SUPERSEDED" labels creates confusion.

### 14. qa/ — Accuracy: 90/100

- **ASSURANCE-CONTRACT.md**: Clear QA/QC/QE definitions with 85% coverage floors
- **METRICS.md**: 27 measurement families documented
- **NEGATIVE-CONTROLS.md**: Instrument qualification procedures

All referenced from SPECIFICATION.md. The 85% floor is consistently applied.

### 15. federation/ — Accuracy: 85/100

30 files total (17 markdown, 8 JSON, 2 Python, 2 schemas, 1 PDF). The v1.3 amendment is well-documented. FED-01-01 through FED-07-08 requirements are referenced consistently. The `VALIDATION.md` correctly states "no live consumer checks executed."

### 16. proof/ — Accuracy: 90/100

v1.4 capability/design/proof/grading amendment. The reference grader (`grade.py`) exists. Validation results in `proof/validation/` show test logs. The `OWNER-MATRIX.md` covers all 24 owners. Synthetic fixtures are correctly distinguished from product results.

### 17. adr/ — Accuracy: 95/100

15 ADRs (ADR-001 through ADR-014 plus 016-capability-proof-numeric-grading.md). Well-structured decision records. All referenced from SPECIFICATION.md and other docs.

### 18. schemas/ — Accuracy: 90/100

10 JSON Schema files plus README. All referenced in MANIFEST.json. Examples in `examples/` directory match the schemas.

### 19. MANIFEST.json + SHA256SUMS — Accuracy: 95/100

- MANIFEST.json: 615 files tracked, SHA256SUMS: 615 entries — **counts match**
- Schema version 1.4 matches package version
- Kind field correctly states "artifact-integrity-not-product-qualification"
- Hashes are present for all tracked files

### 20. records/ — Accuracy: 90/100

10 JSON files including package-summary.json, requirements.json, traceability.json, products.json. All machine-readable sources referenced from markdown docs. The `package-summary.json` is the canonical source of truth for counts.

---

## Specific Issues Found

### Critical (must fix)

1. **README.md:1** — Title says "v1.3" but package is v1.4. This is the first thing anyone reads.
2. **README.md:14** — "166 proposed program requirements and 132 planned work packages" are v1.3 numbers. Current: 204 requirements, 140 work packages (per `records/package-summary.json`).
3. **README.md:14** — "238 passing tests" is stale. Current: 393 (per `records/package-summary.json`).

### Moderate (should fix)

4. **portfolio/ROSTER.md** — Contains the same table as CURRENT-REPO-INDEX.md. The document correctly says "The active roster is CURRENT-REPO-INDEX" on line 1 but the rest is redundant content.
5. **products/REVIEW-REPORT.md** — This file is inside the products/ directory rather than at repo root. It reviews products/ but was placed in the wrong location.
6. **33 product directories vs 24-owner index** — Historical/incomplete directories (Pine, ResearchLedger, SessionLedger, Substrate, PhenoAI, PhenoGfx, PhenoInfra, PhenoTooling) lack clear SUPERSEDED/ARCHIVED labels. New readers may assume they are active.
7. **Prior REVIEW-REPORT.md** (at root) — Claims "~351 .md files" but actual count is 355. Minor but worth noting for precision.
8. **16 spec subdirectories** — Heavy process overhead for 24 repos. Many specs overlap (identity, intent, atlas, specification, assurance).

### Low (nice to have)

9. **CHANGELOG-V1.4.md** exists but is only 802 bytes — very terse for a major amendment.
10. **DOMAIN_MODEL.md** (3,501 bytes) and **INDEX.md** (15,639 bytes) overlap with README.md navigation.
11. **SROC/CDP remain unresolved** — This is correctly documented as unresolved but could benefit from a clear "known unknowns" section.

---

## Cross-Reference Verification

| Reference | Status | Notes |
|-----------|--------|-------|
| README -> START-HERE.md | ✓ | Exists |
| README -> proof/README.md | ✓ | Exists |
| README -> federation/README.md | ✓ | Exists |
| README -> CHANGELOG-V1.3.md | ✓ | Exists |
| START-HERE -> prompts/ONE-CHAT-PER-REPOSITORY.md | ✓ | Exists |
| START-HERE -> report/STATE-AND-OWNER-HANDOFF-2026-09-16.pdf | ✓ | Exists |
| START-HERE -> portfolio/CURRENT-REPO-INDEX.md | ✓ | Exists |
| START-HERE -> proof/README.md | ✓ | Exists |
| START-HERE -> prompts/MASTER-COORDINATOR.md | ✓ | Exists |
| SPECIFICATION -> records/requirements.json | ✓ | Exists (204 reqs) |
| HLD -> architecture/ECOSYSTEM-FIRST-EVOLUTION.md | ✓ | Exists |
| HLD -> federation/README.md | ✓ | Exists |
| README -> schemas/ecosystem-impact.schema.json | ✓ | Exists |
| proof/VALIDATION.md -> proof/validation/results.json | ✓ | Exists |
| MANIFEST.json -> SHA256SUMS | ✓ | 615 entries each |
| CURRENT-REPO-INDEX -> products/*/AGENT-PROMPT.md | ✓ | All 24 exist |
| CURRENT-REPO-INDEX -> products/*/STATE.md | ✓ | All 24 exist |
| package-summary.json product count -> products.json | ✓ | 23 = 23 |
| package-summary.json ADR count -> adr/ dir | ✓ | 15 = 15 |
| package-summary.json spec count -> specs/ dir | ✓ | 16 = 16 |

---

## What the Repo Description Claims vs Reality

| Claim | Status | Evidence |
|-------|--------|----------|
| "Phenotype atlas and assurance program" | ✓ Accurate | All content aligns |
| "166 proposed program requirements" | ✗ Stale | Current: 204 |
| "132 planned work packages" | ✗ Stale | Current: 140 |
| "238 passing tests" | ✗ Stale | Current: 393 |
| "24-owner September 16 snapshot" | ✓ Accurate | Matches owner index |
| "No product is certified" | ✓ Accurate | Consistently stated |
| "No fabricated duration" | ✓ Accurate | ROADMAP.md is honest |
| "SROC/CDP undefined" | ✓ Accurate | Correctly unresolved |
| "Reference validator never grants approval" | ✓ Accurate | Stated in SSOT_AUTHORITY |
| "File count: 617" (package-summary) | ~ Accurate | Actual: 615 files tracked |

---

## Recommendations

### Immediate (P0)
1. **Update README.md title** from "v1.3" to "v1.4"
2. **Update README.md numerical claims** to match `records/package-summary.json`: 204 requirements, 140 work packages, 393 tests

### Short-term (P1)
3. **Add SUPERSEDED labels** to historical product directories (Pine, ResearchLedger, SessionLedger, Substrate, PhenoAI, PhenoGfx, PhenoInfra)
4. **Move products/REVIEW-REPORT.md** to repo root or `report/` directory
5. **Deduplicate ROSTER.md** — either remove or add unique value (e.g., historical context)

### Medium-term (P2)
6. **Consolidate overlapping specs** — 16 specs for 24 repos is heavy; consider merging identity/intent/atlas
7. **Add a "Known Unknowns" section** to START-HERE.md covering SROC/CDP, unverified product tests, stale dates
8. **Consolidate DOMAIN_MODEL.md and INDEX.md** into README.md or remove them

---

## Summary

docs-5 is a well-structured, honest documentation corpus. Its greatest strength is its transparency about limitations: "not product qualification," "no fabricated duration," "reference validator never grants approval." The v1.4 amendment for capability/design/proof/grading is properly integrated.

The primary risk is the **stale README** — it is the entrypoint for all readers and currently presents v1.3 numbers while the package is at v1.4. Fixing the three numerical claims in README.md:14 and the version title in README.md:1 would immediately raise the overall score to ~82/100.

The documentation corpus covers the full lifecycle: identity → requirements → specification → design (HLD/LLD/ALD) → assurance → work → federation → grading → validation. Cross-references are overwhelmingly valid. No placeholder content or fabricated product tests were found.
