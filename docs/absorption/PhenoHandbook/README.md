# PhenoHandbook — Absorbed into phenotype-registry

**Absorption date:** 2026-09-12
**Source repo:** [KooshaPari/PhenoHandbook](https://github.com/KooshaPari/PhenoHandbook)
**Status:** PhenoHandbook is archived. All portable content migrated here.

## What was migrated

| Category | Files | Notes |
|----------|-------|-------|
| **ADRs** | 10 | Architecture decision records (001–008) |
| **Patterns** | 31 | Architecture, async, auth, caching, observability, testing, CI, delegation, governance, methodology, tooling, traceability |
| **Anti-patterns** | 3 | Language-bucket SDK, mirror-to-empty-repo, README index |
| **Governance** | 8 | Stacked PRs (5-part series), journey traceability, overview, happy-path checklist |
| **Security** | 2 | Retention policy, threat model |
| **Operations** | 3 | Iconography spec, journey traceability, SLOs |
| **Guides** | 5 | Architecture, getting started, AGENTS.md generator, full-turn delivery, tooling |
| **Root docs** | 14 | ADR.md, CHARTER.md, CONTRIBUTING.md, SPEC.md, PRD.md, SOTA.md, etc. |
| **Sessions** | 10 | Historical session logs (2026-02, 2026-04) |
| **Historical** | 9 | Phase 2–8 completion summaries, BLUEPRINT, SOTA |
| **Tooling** | 4 | Legacy enforcement scanner, happy-path scripts, rules.yaml |
| **CI workflows** | 18 | GitHub Actions configs, CircleCI, Mergify, Dependabot |
| **Reference** | 3 | API reference, CODE_ENTITY_MAP, FR_TRACKER, validation-rules.py |

**Total: 127 files**

## Overlap with existing registry

| Content | Overlap | Action |
|---------|---------|--------|
| SECURITY.md | Registry already has SECURITY.md | PhenoHandbook version preserved as historical reference |
| CONTRIBUTING.md | Registry already has CONTRIBUTING.md | PhenoHandbook version preserved as historical reference |
| AGENTS.md | Registry already has AGENTS.md | PhenoHandbook version preserved as historical reference |
| CLAUDE.md | Registry already has CLAUDE.md | PhenoHandbook version preserved as historical reference |
| ADRs | Registry has `docs/adr/` and `docs/adrs/` | PhenoHandbook ADRs are separate (different numbering); no conflict |
| Operations | Registry has `docs/operations/` | Absorbed into PhenoHandbook subdirectory to avoid clobbering |
| Sessions | Registry has `docs/sessions/` | Absorbed into PhenoHandbook subdirectory |

## Directory structure

```
docs/absorption/PhenoHandbook/
  adrs/                    # Architecture decision records
  anti-patterns/           # Anti-pattern catalog
  ci-workflows/            # CI/GitHub Actions configs (reference)
  docs-patterns/           # Detailed pattern docs from docs/patterns/
  governance/              # Governance docs (stacked PRs, traceability)
  guides/                  # Guide documents
  historical/              # Phase completion summaries
  operations/              # SLOs, iconography, journey traceability
  patterns/                # Top-level pattern catalog
  security/                # Threat model, retention policy
  sessions/                # Historical session logs
  tooling/                 # Legacy enforcement scanner, scripts
  *.md                     # Root docs (CHARTER, SPEC, PRD, etc.)
```

## Source of truth

This directory is the canonical location for PhenoHandbook content. The original [PhenoHandbook repo](https://github.com/KooshaPari/PhenoHandbook) is tombstoned — do not make changes there.
