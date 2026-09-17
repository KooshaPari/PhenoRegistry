# Phenotype Docs Cross-Packet Synthesis

**Date:** 2026-09-17
**Scope:** `/Users/kooshapari/Downloads/docs-5` vs `/Users/kooshapari/Downloads/phenotype-canonicalization`
**Author:** Jcode (cross-review agent)

---

## 1. What Each Packet Is Authoritative For

### docs-5 (live governing corpus at `~/CodeProjects/docs/docs-5/`)
**Authoritative for:** Per-product truth — current identity, status, test counts, artifact hashes, atlas concerns, and bounded next actions for each Phenotype product/lab.

The `~/Downloads/docs-5` copy is **incomplete** — it contains only the Melosviz product dossier (3 files, 127 lines). The live corpus at `~/CodeProjects/docs/docs-5/` has 30+ product dossiers, federation docs, qa/ metrics, and architecture contracts.

**Melosviz-specific authority (from docs-5):**
- GitHub ID 1262466303, default branch `main`, release tag `v0.1.0`
- Web tests 243/246 passing (3 skipped spec-first); backend 1448/1450
- Head commit `f082aa5`, artifacts with sha256 prefixes
- Status: v0.1.0 released; live render backend is placeholder only, not product-proven

### docs-3 (archived corpus at `~/CodeProjects/docs/_archive/docs-3/`)
**Authoritative for:** Planning cohort structure (30-item roster, 54 session seats), quality gates (85% coverage floors, negative controls, assurance matrix), Atlas questions, carry-forward items, advantage hypotheses, cross-ecosystem acceptance rules, Phase A-D roadmap, and the 20-risk register.

docs-3 is **archived 2026-09** per AGENTS.md; its per-product dossiers are historical snapshots, not current truth. The Melosviz dossier in docs-3 is pre-release (has PILOT.json, no post-release STATE.md/NEXT-ACTIONS.md).

### phenotype-canonicalization (research/handoff packet)
**Authoritative for:** Decision inventory, tool selection profiles, pattern matrices, decision trees, audit findings (F01-F14), and proposed operationalization of canonical engineering. It is explicitly "proposed operationalization, not deployed policy" — it does NOT grant permissions, certify products, or supersede existing user decisions.

**What it observed:** 46 repository identities via connected discovery; source files read in 9 repos (PhenoShared, PhenoRegistry, PhenoInfra, Tracera, AgilePlus, HeliosLab, OmniRoute, PhenoDesign, Portage); local verification of packet structure (VALID), 40/40 unit tests (98.2% statement coverage on 3 reference Python tools only).

**What it did NOT verify:** Product qualification, installed consumer tests, production benchmarks — all three are `NOT_RUN`.

---

## 2. Overlaps and Contradictions

### Overlaps (same concern, multiple packets)
| Concern | docs-3 | docs-5 | canonicalization |
|---------|--------|--------|------------------|
| Melosviz identity/release | DOSSIER.md (pre-release) | DOSSIER.md + STATE.md + NEXT-ACTIONS.md (post-release v0.1.0) | Not observed |
| Quality gates / coverage floors | ASSURANCE-CONTRACT.md, METRICS.md | (in live corpus, not in ~/Downloads copy) | References G04-G05 gates but doesn't define them |
| Authority chain | SSOT_AUTHORITY.md | (in live corpus) | D01 extends handbook/registry roles |
| Shared component boundaries | ECOSYSTEM-FIRST-EVOLUTION.md | (in live corpus) | F01/F08/F10/F12 address Shared boundaries |
| Migration/work packages | (none) | (none in ~/Downloads copy) | migration/work-packages.json |

### Contradictions
1. **Melosviz release state:** docs-3's Melosviz DOSSIER.md is pre-release; docs-5's STATE.md says v0.1.0 released 2026-09-17T03:00:57Z. docs-3 is stale for Melosviz.
2. **Authority date:** The canonicalization packet references "September 16 handbook" and audit sources dated 2026-09-16, but docs-5's Melosviz STATE.md has observation date September 17 — the packet's snapshot is one day behind the live product state.
3. **Coverage claims:** docs-3's METRICS.md declares 85% coverage floors; the canonicalization packet's verification achieved 98.2% on reference tools only — this is NOT product coverage and the packet explicitly says so ("Three reference Python tools only; this is not product coverage").
4. **Scope of "canonical":** docs-3/SSOT_AUTHORITY.md says "No competing writable copies" and that a "document calling itself canonical is an observation; authority comes from the accepted mandate and ownership chain." The canonicalization packet calls itself "canonical engineering" research but is not an accepted mandate — this is a self-declared research packet, not an authority document.
5. **Repo count:** docs-3 ROSTER lists 30 planning cohort items; the canonicalization packet observed 46 repos. 16 repos are not in the planning cohort — their lifecycle authority is "unresolved; discovery is not an activity or mutation decision."

### Stale References
- docs-3's Melosviz DOSSIER.md references pre-release state; superseded by docs-5's post-release STATE.md and NEXT-ACTIONS.md
- The canonicalization packet's audit sources are dated 2026-09-16; Melosviz released 2026-09-17 — the packet doesn't cover Melosviz at all
- AGENTS.md references docs-3 as "ARCHIVED 2026-09" but the ~/Downloads/docs-5 copy is incomplete (only Melosviz), so the archived-to-live migration is not fully verifiable from this copy alone

### Scope Drift
- The canonicalization packet drifted from "audit findings" into "proposed operationalization" without a clear boundary between observation and prescription. D01-Dxx are proposals, not deployed policy, but the packet's structure (decisions.json, profiles.json, pattern-matrix.json) implies enforceability that doesn't exist yet.
- docs-5's Melosviz NEXT-ACTIONS.md includes post-release outcomes (install/smoke on clean machine) that the canonicalization packet doesn't address — the packet's scope is tooling/architecture, not product release qualification.

---

## 3. Document Classification: Retain / Merge / Supersede

### Retain (authoritative, still in force)
| Document | Role |
|----------|------|
| docs-3/SSOT_AUTHORITY.md | Authority/writer chain; no competing writable copies rule |
| docs-3/qa/ASSURANCE-CONTRACT.md | Quality gate contract definition |
| docs-3/qa/METRICS.md | 27 measurement families, 85% floor |
| docs-3/qa/NEGATIVE-CONTROLS.md | Instrument qualification |
| docs-3/architecture/ECOSYSTEM-FIRST-EVOLUTION.md | Consumer-driven evolution rules |
| docs-3/architecture/APPLET-CONTRACT.md | Recursive applet boundaries |
| docs-3/risks/RISK-REGISTER.md | 20 risks with controls |
| docs-5/products/Melosviz/STATE.md | Current Melosviz state (post-release) |
| docs-5/products/Melosviz/NEXT-ACTIONS.md | Bounded next outcomes with acceptance criteria |
| canonicalization/decisions.json | Proposed decision inventory (status: proposed, not deployed) |
| canonicalization/profiles.json | Tool selection profiles (status: proposed) |
| canonicalization/pattern-matrix.json | Branching rules for canonical selections |

### Merge (combine into unified authority)
| Source | Target | Reason |
|--------|--------|--------|
| docs-3/products/Melosviz/DOSSIER.md | docs-5/products/Melosviz/ (supersede) | Pre-release; docs-5 has post-release evidence |
| docs-3/portfolio/ROSTER.md | docs-5/ (as planning reference) | 30-item cohort definition; still valid as planning input |
| docs-3/portfolio/TAXONOMY.md | docs-5/ (as reference) | Topic/lifecycle taxonomy |
| canonicalization/audit/findings.json | docs-5/qa/ (as evidence input) | F01-F14 are audit evidence, not quality gates |
| canonicalization/migration/work-packages.json | docs-5/ (as execution plan) | Bounded work packages, not governance |

### Supersede (archived, replaced by newer evidence)
| Document | Replaced By | Evidence |
|----------|-------------|----------|
| docs-3/products/Melosviz/DOSSIER.md | docs-5/products/Melosviz/STATE.md + NEXT-ACTIONS.md | v0.1.0 release, new test counts, post-release outcomes |
| docs-3/products/Melosviz/PILOT.json | docs-5/products/Melosviz/STATE.md | PILOT.json is pre-release pilot; STATE.md has actual release data |
| docs-3/products/* (all other product dossiers) | docs-5/products/* (live corpus) | docs-3 is archived; docs-5 is the live governing corpus |
| docs-3 (entire corpus as authority) | docs-5 + canonicalization (proposed) | docs-3 explicitly archived 2026-09 |

---

## 4. Proposed Canonical Documentation Map

```
Phenotype Documentation Authority Map
======================================

LAYER 1: AUTHORITY (who writes what, who owns releases)
  docs-5/.../SSOT_AUTHORITY.md          ← immutable repo IDs, writer/release authority
  docs-5/.../OWNER-MATRIX.md            ← federation owner matrix (live corpus)

LAYER 2: PRODUCT TRUTH (current state per product)
  docs-5/products/<name>/DOSSIER.md     ← identity, status, atlas concerns
  docs-5/products/<name>/STATE.md       ← current observation, test counts, commits
  docs-5/products/<name>/NEXT-ACTIONS.md ← bounded outcomes with acceptance criteria
  docs-5/products/<name>/PILOT.json     ← pilot data (where exists)

LAYER 3: QUALITY GATES (independent verification)
  docs-5/qa/ASSURANCE-CONTRACT.md       ← 85% coverage floors, negative controls
  docs-5/qa/METRICS.md                  ← 27 measurement families
  docs-5/qa/NEGATIVE-CONTROLS.md        ← instrument qualification
  docs-5/qa/DOCUMENTATION-COVERAGE.md   ← doc coverage tracking

LAYER 4: ARCHITECTURE (ecosystem contracts)
  docs-5/architecture/ECOSYSTEM-FIRST-EVOLUTION.md  ← consumer-driven evolution
  docs-5/architecture/APPLET-CONTRACT.md            ← recursive applet boundaries
  docs-5/architecture/DEPENDENCY-ADOPTION.md        ← dependency patterns
  docs-5/architecture/INCREMENTAL-STATE.md          ← state management
  docs-5/adr/                                       ← architecture decision records (14 ADRs)

LAYER 5: FEDERATION (cross-product contracts)
  docs-5/federation/README.md
  docs-5/federation/PRODUCT-CONTRACT.md
  docs-5/federation/ACCEPTANCE.md
  docs-5/federation/EXPERIENCE-CONTRACT.md
  docs-5/federation/SECURITY-AND-DATA.md
  docs-5/federation/work-packages.json
  docs-5/federation/requirements.json
  docs-5/federation/sources.json

LAYER 6: DECISION INVENTORY (proposed, not deployed)
  phenotype-canonicalization/decisions.json    ← D01-Dxx proposed selections
  phenotype-canonicalization/profiles.json     ← tool profiles
  phenotype-canonicalization/pattern-matrix.json ← branching rules
  phenotype-canonicalization/decision-trees.json ← decision trees
  STATUS: proposed operationalization — NOT deployed policy

LAYER 7: AUDIT EVIDENCE (observations, not authority)
  phenotype-canonicalization/audit/findings.json  ← F01-F14 findings
  phenotype-canonicalization/audit/sources.json   ← source evidence
  phenotype-canonicalization/audit/repositories.json ← 46 repo observations
  phenotype-canonicalization/coverage.json        ← reference tool coverage only
  STATUS: audit evidence — requires product qualification before enforcement

LAYER 8: RESEARCH (experiments, not decisions)
  phenotype-canonicalization/research/EXPERIMENT-PROTOCOL.md
  phenotype-canonicalization/research/candidates.json
  STATUS: research input — not implementation guidance
```

**Key principle:** Layers 1-5 are normative (in force). Layers 6-8 are proposals/evidence (not in force until product-qualified and deployed). The canonicalization packet must complete product qualification (E01, W05, W10) before its decisions become authoritative.

---

## 5. Top 10 Concrete Next Actions (ordered by impact)

| # | Action | Owner | Impact | Evidence |
|---|--------|-------|--------|----------|
| **1** | **Verify Melosviz in canonicalization's 46-repo observation set** — check `repositories.json` for GitHub ID 1262466303; if absent, Melosviz is unaudited and needs a source observation | Canonicalization owner | High — Melosviz v0.1.0 is released but may have unobserved identity/auth issues | repositories.json (46 entries, Melosviz not confirmed in visible excerpt) |
| **2** | **Resolve docs-5 ~/Downloads copy incompleteness** — the ~/Downloads/docs-5 only has Melosviz; the live corpus at ~/CodeProjects/docs/docs-5/ has 30+ products. Confirm which copy is the true governing corpus and sync if needed | Docs steward | High — authority chain depends on knowing which docs are current | AGENTS.md says live corpus is ~/CodeProjects/docs/docs-5/ |
| **3** | **Execute E01: Tracera typecheck canary on actual pinned compiler** — the packet found a coverage hazard (six `-p` flags, TypeScript 5.8.3 fixture reproduced last-project selection); run the canary with Tracera's actual compiler | Tracera frontend owner | High — false-confidence typechecking undermines G04/G05 gates | F02, G04, E01 in findings.json |
| **4** | **Resolve F01: PhenoShared conflicting identities** — README describes PhenoMLX/OMLX, npm manifest names `phenodocs`, Cargo identifies substrate workspace. Establish one accurate root map with distinct component manifests | Shared integration owner | High — entry-point ambiguity sends agents to wrong surfaces | F01, G01-G03 |
| **5** | **Resolve F07: Python version conflation** — AgilePlus declares >=3.14 while Ruff targets py312; Portage uses uv/Ruff/ty with >=3.12. Separate interpreter selection, lint target, and runtime GIL state | AgilePlus/Portage owners | Medium — minimum supported Python, lint syntax, and runtime are independent facts | F07, G09, G10 |
| **6** | **Resolve F09: CI workflow 404** — AgilePlus calls `phenotype-tooling/.github/workflows/sbom-monthly.yml@main`; old provider name returns 404. Resolve stable provider identity and workflow location | AgilePlus CI owner | Medium — 404 doesn't distinguish deletion, access restriction, or rename path | F09, G15, G23 |
| **7** | **Execute product qualification for Melosviz live render backend** — docs-5 STATE.md says live render is placeholder only; NEXT-ACTIONS.md A1-A3 require real creative output, installation smoke, and comparison. Run actual licensed audio through the pipeline | Melosviz owner | High — v0.1.0 is released but the shipped path is rehearsal, not production proof | docs-5 STATE.md, NEXT-ACTIONS.md CUR-1262466303-A1/A2/A3 |
| **8** | **Merge docs-3 Melosviz dossier into docs-5 with explicit supersession** — docs-3's Melosviz DOSSIER.md is pre-release; add a supersession marker linking to docs-5's STATE.md | Docs steward | Medium — prevents stale pre-release info from being read as current | docs-3 vs docs-5 Melosviz state mismatch |
| **9** | **Complete W05: Python 3.14t qualification** — if free-threaded Python is the target, verify actual GIL-disabled imports, dependency thread-safety, and time/memory behavior under intended workload patterns | AgilePlus owner | Medium — 3.14t means more than an interpreter suffix; failed import must not become a no-op stub | F07, W05 in REPORT.md |
| **10** | **Deploy decision model with consumer proof** — D01-Dxx decisions are proposed, not deployed. Require exact use, actual behavior, and exit criteria before treating any canonical selection as enforced | Canonicalization owner | High — "it might be needed" is not a permanent exception; require exact use + exit criterion | D01 enforcement_status: not_deployed, mutation_authority: false |

---

## 6. Open Questions

1. **Is the ~/Downloads/docs-5 copy a deliberate subset or an incomplete archive?** The live corpus at ~/CodeProjects/docs/docs-5/ has 30+ products; the Downloads copy has only Melosviz. This affects whether the cross-review can assess the full ecosystem from these two packets alone.

2. **Does the canonicalization packet's 46-repo observation include Melosviz (GitHub ID 1262466303)?** The visible repositories.json excerpt shows BytePort and zz-pause-* repos but Melosviz is not confirmed. If Melosviz was not observed, its F-findings are missing from the audit.

3. **Who owns the decision model deployment?** D01 says "Extend the current handbook and registry roles" but the current handbook's authority chain (docs-3 SSOT_AUTHORITY.md) says authority comes from "accepted mandate and ownership chain." The packet is not an accepted mandate — deployment requires explicit authority.

4. **What is the superseded-state handling for docs-3 product dossiers?** The AGENTS.md says docs-3 is archived, but the ROSTER still references docs-3 dossier paths (e.g., `../products/Tracera/DOSSIER.md`). Are these paths still resolvable, or do they point to stale pre-release dossiers?

---

## 7. Evidence Sources

| Packet | Path | Lines | Key Contents |
|--------|------|-------|--------------|
| docs-5 (Downloads copy) | `products/Melosviz/DOSSIER.md` | 41 | Melosviz identity, v0.1.0 release, atlas concerns |
| docs-5 (Downloads copy) | `products/Melosviz/NEXT-ACTIONS.md` | 26 | Bounded next outcomes, carry-forward items |
| docs-5 (Downloads copy) | `products/Melosviz/STATE.md` | 60 | Current observation, test counts, build status |
| docs-3 (archive) | `ROSTER.md` | 30+ | 30-item planning cohort, 54 session seats |
| docs-3 (archive) | `SSOT_AUTHORITY.md` | 21 | Authority/writer chain, no competing copies |
| docs-3 (archive) | `START-HERE.md` | 17 | Reading order, rev 1.1 direction |
| docs-3 (archive) | `products/Melosviz/DOSSIER.md` + `PILOT.json` | — | Pre-release Melosviz dossier |
| canonicalization | `REPORT.md` | 310 | Diagnosis, decisions, canonical tooling selections |
| canonicalization | `AGENT-HANDOFF.md` | 71 | Agent mandate, authority recovery steps |
| canonicalization | `decisions.json` | 514 | D01-Dxx proposed decisions |
| canonicalization | `profiles.json` | 231 | Tool selection profiles |
| canonicalization | `audit/findings.json` | 44 | F01-F14 findings with evidence |
| canonicalization | `audit/repositories.json` | 626 | 46 repo observations |
| canonicalization | `verification/summary.json` | 37 | Local verification results (40/40 tests, 98.2% coverage on reference tools only) |
| canonicalization | `verification/packet-validation.json` | 6 | Packet structure VALID, product_qualification NOT_EVALUATED |
