# phenotype-registry

[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/KooshaPari/pheno-registry/badge)](https://securityscorecards.dev/viewer/?uri=github.com/KooshaPari/pheno-registry)
[![CII Best Practices](https://www.bestpractices.dev/projects/11735/badge)](https://www.bestpractices.dev/projects/11735)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache-2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![AI-DD-Slop](https://img.shields.io/badge/AI--DD--Slop%20Expected-orange?style=flat-square)]

## Description

Organization registry: master index connecting specs, patterns, and templates across the Phenotype ecosystem. This repo owns the **INDEX** role in the four-repo governance spine, maintaining the canonical [`ECOSYSTEM_MAP.md`](./ECOSYSTEM_MAP.md) and dependency graph. It provides the authoritative mapping of repo roles (INDEX, ADRs/contracts, conventions, enforcement) and cross-references `docs/intent/<repo>.md`, `docs/boundary/<repo>.md`, and `_bindings.json` for provenance. The Python SDK (`pheno-registry-python`) provides PyO3-bound access to registry data.

## Quick Start

### Clone

```bash
git clone --recurse-submodules https://github.com/KooshaPari/phenotype-registry.git
cd phenotype-registry
```

### Build and Install

```bash
# Rust crate
cargo build --release

# Python SDK (PyO3)
uv venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
```

### Lint and Check

```bash
cargo check --workspace
cargo clippy --workspace
ruff check src/
mypy src/
```

### Test

```bash
cargo test --workspace
pytest tests/
```

## Repository Structure

```
├── crates/                  # Rust workspace crates
│   ├── phenotype-dag-core/  # DAG foundation for compute/infra automation
│   └── pheno-registry-python/  # Python SDK via PyO3
├── docs/                    # SSOT, boundary, intent files
│   ├── SSOT.md              # Single source of truth for capability & intent
│   ├── ECOSYSTEM_MAP.md     # Canonical ecosystem index
│   └── intent/              # Per-repo intent statements
├── ADR.md                   # Architecture Decision Records
├── RATIONALIZATION_PLAN.md  # Rationalization roadmap
├── ECOSYSTEM_MAP.md         # Repo role classification + dependency graph
├── CHANGELOG.md
├── CONTRIBUTING.md
├── PRD.md
├── PLAN.md
├── SPEC.md
├── tests/                   # Test suite
├── benches/                 # Benchmarks
├── scripts/                 # Render and propagation scripts
│   ├── render-per-repo.py
│   ├── propagate-intent-to-repos.py
│   └── regen-ecosystem-map.py
└── Cargo.toml / pyproject.toml
```

## 4-Role Governance Spine

| Repo | Role | Owns |
|------|------|------|
| **phenotype-registry** | **INDEX** | ECOSYSTEM_MAP.md + dependency graph |
| **PhenoSpecs** | **ADRs / contracts** | Architecture Decision Records, API contracts |
| **PhenoHandbook** | **CONVENTIONS** | Patterns, methodologies |
| **phenotype-org-governance** | **ENFORCEMENT** | Policy workflows, deny.toml, license baseline |

## GitHub

- **GitHub:** [KooshaPari/PhenoRegistry](https://github.com/KooshaPari/PhenoRegistry)
- **Description:** Organization registry: master index connecting specs, patterns, and templates
- **Topics:** devtools, docs, maintained, meta
- **License:** MIT + Apache-2.0
- **Language:** Rust (primary), Python (SDK)

## Authority

See [`docs/SSOT.md`](docs/SSOT.md) for the Capability & Intent SSOT — when any other doc contradicts this section, SSOT wins. Per [RATIONALIZATION_PLAN.md](./RATIONALIZATION_PLAN.md), PhenoHandbook is collapsed into this registry via index link.