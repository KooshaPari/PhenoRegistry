# REVIEW-REPORT.md — docs-5 Product Dossiers

**Reviewer:** Jcode (direct)
**Date:** 2026-09-17
**Products surveyed:** 33

---

## Completeness Summary

| Status | Count | Products |
|--------|-------|----------|
| **COMPLETE (7 files)** | 33 | ALL products (see below) |
| **INCOMPLETE** | 0 | — |
| **TOTAL** | 33 | |

**Dossier repair pass (2026-09-17):** All 10 previously-incomplete dossiers (Agentora-capability, PhenoAI, PhenoGfx, PhenoInfra, PhenoMLX, PhenoTooling, Pine, ResearchLedger, SessionLedger, Substrate) received their 6 missing canonical helper files: START-HERE, STATE, NEXT-ACTIONS, AGENT-PROMPT, FEDERATION, PROOF-AND-GRADE. All 10 carry the "v1.2 historical/capability context, not a current owner assignment" header, so the generated content records obligations without dispatching a new owner chat. Format parity achieved; substantive review and ownership resolution remain sponsor/owner-driven. No grade is implied by file-shape parity.

Each complete dossier contains:
- `AGENT-PROMPT.md` — Agent instructions
- `DOSSIER.md` — Product identity
- `FEDERATION.md` — Ecosystem participation
- `NEXT-ACTIONS.md` — What's next
- `PROOF-AND-GRADE.md` — Quality proof
- `START-HERE.md` — Entrypoint
- `STATE.md` — Current state

---

## Complete Dossiers (21 products)

### Primary repos (ACTIVE, well-documented)

| Product | Role | Dossier Quality | Notes |
|---------|------|----------------|-------|
| **Melosviz** | Music-to-visual toolkit | COMPLETE | Active development, v0.1.0 shipped |
| **OmniRoute** | AI model routing proxy | COMPLETE | 40+ providers, active |
| **PhenoMLX** | ML inference engine | INCOMPLETE (1 file) | Should be complete given activity |
| **HeliosLab** | Research lab | COMPLETE | Active |
| **Portage** | Python tooling | COMPLETE | Active |
| **PhenoShared** | Shared infrastructure | COMPLETE | Core ecosystem repo |
| **Tracera** | Persistent graph model | COMPLETE | Active |
| **PhenoRegistry** | Registry/catalog | COMPLETE | Active |

### Secondary repos (complete dossiers)

| Product | Dossier Quality | Notes |
|---------|----------------|-------|
| AgilePlus | COMPLETE | Agile tooling |
| BytePort | COMPLETE | Data portability |
| CivicWarfare | COMPLETE | Game |
| Civis | COMPLETE | Civic engagement |
| Dino | COMPLETE | Unknown purpose |
| HeliosCLI | COMPLETE | CLI tools |
| HeliosLite | COMPLETE | Lightweight variant |
| KCode | COMPLETE | Code tooling |
| Khostty | COMPLETE | Unknown purpose |
| KooshaPari | COMPLETE | Account meta |
| PhenoApps | COMPLETE | App extraction |
| PhenoDesign | COMPLETE | Design system |
| PhenoFabric | COMPLETE | Fabric/textile |
| PhenoLab | COMPLETE | Lab environment |
| ShareCLI | COMPLETE | Sharing CLI |
| WorldSphereMod | COMPLETE | 3D world |

---

## Incomplete Dossiers (10 products)

These have only DOSSIER.md, missing STATE, FEDERATION, PROOF-AND-GRADE, etc:

| Product | Has DOSSIER | Missing | Priority |
|---------|------------|---------|----------|
| **PhenoMLX** | YES | STATE, FED, PROOF, NEXT, AGENT, START | HIGH - active repo |
| **Substrate** | YES | STATE, FED, PROOF, NEXT, AGENT, START | HIGH - core infra |
| **PhenoAI** | YES | STATE, FED, PROOF, NEXT, AGENT, START | MEDIUM - renamed to PhenoShared |
| **PhenoInfra** | YES | STATE, FED, PROOF, NEXT, AGENT, START | MEDIUM - infrastructure |
| **PhenoTooling** | YES | STATE, FED, PROOF, NEXT, AGENT, START | MEDIUM - tooling |
| **Agentora-capability** | YES | STATE, FED, PROOF, NEXT, AGENT, START | LOW - capability only |
| **PhenoGfx** | YES | STATE, FED, PROOF, NEXT, AGENT, START | LOW - graphics |
| **Pine** | YES | STATE, FED, PROOF, NEXT, AGENT, START | LOW - possibly retired |
| **ResearchLedger** | YES | STATE, FED, PROOF, NEXT, AGENT, START | LOW - possibly retired |
| **SessionLedger** | YES | STATE, FED, PROOF, NEXT, AGENT, START | LOW - possibly retired |

---

## Product Overlap Analysis

| Overlap Group | Products | Recommendation |
|---------------|----------|----------------|
| **HeliosCLI / HeliosLite / HeliosLab** | Three Helios products | Clarify: CLI = tooling, Lite = lightweight variant, Lab = research |
| **PhenoAI / PhenoShared** | PhenoAI renamed to PhenoShared | PhenoAI dossier is stale, should reference PhenoShared |
| **PhenoTooling / PhenoRegistry** | Both handle tooling/registry | Clarify boundaries |
| **ResearchLedger / SessionLedger** | Both are ledger products | Consider merging or retiring |
| **Pine / Substrate** | Both are infrastructure | Clarify: Pine = ?, Substrate = compute mesh |
| **KCode / Khostty** | Both start with K | Unclear relationship |

---

## RECOMMENDATIONS

### IMMEDIATE
1. **Complete PhenoMLX dossier** — It's an active repo with only 1 file
2. **Complete Substrate dossier** — Core infrastructure, needs full dossier
3. **Mark retired products** — Pine, ResearchLedger, SessionLedger may be retired; add STATE.md saying so

### SOON
4. **Complete PhenoInfra and PhenoTooling** — Active infrastructure repos
5. **Update PhenoAI** — Redirect to PhenoShared or mark as historical
6. **Clarify Helios family** — Three products need clear boundaries

### DOCUMENTATION QUALITY
7. **All 21 complete dossiers follow the same template** — Good consistency
8. **DOSSIER.md files are well-written** — Each has clear identity, role, and current state
9. **FEDERATION.md files are mostly boilerplate** — Could be more product-specific
10. **NEXT-ACTIONS.md varies in quality** — Some are detailed, some are vague

### VOLUME
33 products x 7 files = 231 product-specific files. This is reasonable for a 24-repo ecosystem. The incomplete products (10) need attention, not the complete ones.
