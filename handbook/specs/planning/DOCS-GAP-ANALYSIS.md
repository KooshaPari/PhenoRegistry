# Docs Gap Analysis - 2026-09-17

## Per-Repo Status

| Repo | README | ARCHITECTURE | CONTRIBUTING | API_REF | Dossiers | Key Gaps |
|------|--------|-------------|-------------|---------|----------|----------|
| **PhenoMLX** | Rewritten (153 lines) | exists | MISSING | MISSING | exists (docs/dossiers/) | CONTRIBUTING.md, API_REFERENCE.md |
| **HeliosLab** | Rewritten (136 lines) | exists (docs/) | exists | MISSING | none | API_REFERENCE.md, dossiers |
| **PhenoShared** | Updated (133 lines) | exists (docs/) | exists | exists (docs/) | exists (docs/dossiers/) | Relatively complete |
| **Portage** | Good (153 lines, upstream Harbor) | exists (docs/) | exists | MISSING | none | API_REFERENCE.md, dossiers |

## Per-Repo Detail

### PhenoMLX
- `docs/` has: ARCHITECTURE.md, ADRs (6+), BENCHMARK_REPORT.md, GLOBAL_HANDBOOK.md, boundary docs, session docs
- `docs/dossiers/` has: DOSSIER.md, ATLAS_EXTRACTION.md, HANDOFF.md
- README: REWRITTEN (was 180 lines of sladge badges, now 153 lines comprehensive)
- **Missing:** CONTRIBUTING.md, docs/API_REFERENCE.md

### HeliosLab
- `docs/` has: ADRs (7+), demo docs, research docs, governance docs
- README: REWRITTEN (was 82 lines, now 136 lines comprehensive)
- Has: ARCHITECTURE.md (docs/), CONTRIBUTING.md
- **Missing:** docs/API_REFERENCE.md, product dossiers

### PhenoShared
- `docs/` has: ARCHITECTURE.md, API_REFERENCE.md, GARDEN_LOOP.md, research docs (8+), governance docs
- README: Updated (133 lines, was overwritten by worker then restored)
- Has: CONTRIBUTING.md, ARCHITECTURE.md, API_REFERENCE.md
- **Most complete** of the four repos

### Portage
- `docs/` has: ARCHITECTURE_GUIDE.md, DATA_MODEL.md, ADRs (6+), getting-started.md, governance docs
- README: Good from upstream Harbor (153 lines with badges)
- Has: CONTRIBUTING.md
- **Missing:** docs/API_REFERENCE.md, product dossiers

## Priority Actions (Top 5)

1. **PhenoMLX: Create CONTRIBUTING.md** -- Guidelines for contributing to the fork, test requirements, PR process
2. **PhenoMLX: Create docs/API_REFERENCE.md** -- Document OpenAI-compatible endpoints, TurboQuant+ config, CLI commands
3. **HeliosLab: Create docs/API_REFERENCE.md** -- Document phenoctl CLI, crate APIs, FFI interfaces
4. **Portage: Create docs/API_REFERENCE.md** -- Document Harbor evaluation endpoints, CLI commands
5. **PhenoMLX/HeliosLab/Portage: Create product dossiers** -- Follow PhenoShared pattern in docs/dossiers/
