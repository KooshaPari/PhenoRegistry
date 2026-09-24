# Frontend / 3D Agent Kit

An open-source kit that gives coding agents the design judgment, local asset workflow, interaction architecture, and verification loop needed to build ambitious 3D product pages.

**Not a template. Not a CDN dependency. Not a landing page generator.**

This kit provides 18 original agent skills, a working offline demo with real procedural geometry, Blender build scripts, material/export guides, quality gates, machine-readable contracts, and a validated source catalog of 36 annotated primary references.

## Quick start

**1. Open the searchable catalog** -- `index.html` (no dependencies, works offline).

**2. Open the interactive demo** -- `demo-standalone.html` (no CDN, no npm, no network required). Or serve locally if your browser blocks file navigation:

```bash
python -m http.server --bind 127.0.0.1 8080
# Then open http://127.0.0.1:8080/
```

**3. Explore the editable multi-file demo** -- `demo/index.html` with `demo/viewer.js`, `demo/style.css`, and `demo/mesh-data.js`.

**4. Run the diagnostics:**

```bash
python scripts/doctor.py             # Check local environment
python scripts/audit_asset.py        # Audit the included GLB
python -m unittest discover -s tests -p 'test_*.py' -v
```

## What is included

| Area | Contents |
|---|---|
| Agent skills | 18 original `fd3d-*` SKILL.md modules plus one verified upstream Anthropic frontend-design skill |
| Resource catalog | 36 annotated primary-source entries with selection rationale, caveats, and evidence status |
| Local asset creation | Procedural concept trainer generator, real GLB, structured mesh source, manifest, headless Blender scripts |
| Working demo | Scroll-linked 3D story, real mesh rotation, layer separation, material accents, drag/keyboard controls, responsive layout, static fallback |
| Integration reference | A separate Three.js + GSAP implementation sketch (dependencies not installed here) |
| Operating guides | Materials/export, local generation, Blender isolation, harness setup, quality gates, recipes |
| Contracts | Machine-readable JSON schemas for asset metadata, design tokens, and quality budgets |
| Verification | 25 unit tests, 21 browser checks, real screenshots, validation report, checksum manifest |

## What is not included

No Blender binaries, no npm dependencies, no model weights, no fonts, no branded commercial models, no paid course text, no active MCP server configuration. Unzipping does not install anything. See `THIRD-PARTY-NOTICES.md` for attribution boundaries.

## For agents

Read `AGENT-HANDOFF.md` first. Then selectively load skills from `skills/` as needed for the task. The kit root must remain at a stable path because synced skill copies reference it back. Use `scripts/sync_skills.py` to install selected skills into a project without overwriting existing rules:

```bash
python scripts/sync_skills.py --project /path/to/project --harness codex --skills fd3d-art-direction fd3d-scroll-story fd3d-visual-qa
# Review the dry-run output, then repeat with --apply.
```

See `AGENTS.md` for the full agent behavior contract within this kit.

## Project structure

```
frontend-3d-agent-kit/
  START-HERE.md          -- Routing document (open first)
  AGENT-HANDOFF.md       -- Agent workflow instructions
  AGENTS.md              -- Agent behavior contract for this kit
  index.html             -- Searchable offline resource catalog
  demo-standalone.html   -- Self-contained interactive demo
  demo/                  -- Editable multi-file demo source
  assets/                -- GLB, mesh source, manifest
  blender/               -- Blender build script
  contracts/             -- JSON schemas (asset, tokens, quality, story)
  evidence/              -- Validation report, screenshots, test results
  integrations/          -- Three.js + GSAP reference implementation
  recipes/               -- Implementation recipes (sneaker story, 2-5D, glass dial, active props)
  resources/             -- Guides, source catalog, stack rationale, quality gates
  scripts/               -- Doctor, audit, build, package, skill sync, verify
  skills/                -- 18 fd3d-* skill modules
  tests/                 -- Unit tests and browser smoke tests
  upstream/              -- Verified upstream skill snapshots with licenses
```

## Quality and verification

The included validation report (`evidence/VALIDATION.md`) separates what was actually tested from what was not. The demo was validated through a CPU triangle preview (WebGL was not available in the test environment). Browser interaction, DOM structure, scroll behavior, keyboard controls, fallback states, and responsive layout were tested with Playwright.

Not yet validated: native Blender build and Cycles rendering, WebGL2 shader compilation, Three.js + GSAP runtime, Khronos glTF validator, real touch devices, GPU benchmarks. These are documented in `evidence/VALIDATION.md`.

## Documentation guide

| Document | Purpose |
|---|---|
| `START-HERE.md` | Where to begin; routing for humans and agents |
| `AGENT-HANDOFF.md` | Step-by-step agent workflow |
| `AGENTS.md` | Agent behavior contract for this kit |
| `INVENTORY.md` | File-by-file inventory with byte sizes |
| `THIRD-PARTY-NOTICES.md` | Attribution and license boundaries |
| `resources/SOURCES.md` | Annotated source catalog (36 entries) |
| `resources/STACK-CHOICES.md` | Technology selection rationale |
| `resources/QUALITY-GATES.md` | Pass/fail acceptance criteria |
| `resources/HARNESS-SETUP.md` | Non-destructive skill installation |
| `resources/BLENDER-AUTONOMY.md` | Headless Blender execution guide |
| `resources/MATERIALS-AND-EXPORT.md` | Material families and browser export |
| `resources/LOCAL-GENERATION.md` | Local image-to-3D evaluation |
| `resources/UPSTREAM-SKILLS.md` | Third-party skill candidates |
| `skills/README.md` | Skill router and descriptions |
| `evidence/VALIDATION.md` | Test results and verification boundary |

## License

MIT License. See `LICENSE` for the full text. Covers original kit material only. The included Anthropic frontend-design skill is licensed separately under Apache 2.0 (see `upstream/anthropic/frontend-design/LICENSE.txt`). All other referenced resources are links, not redistributions. See `THIRD-PARTY-NOTICES.md`.

## References

Built 15 September 2026. The reference product is an original unbranded concept trainer. Apple/Nike references describe the requested ambition, not copied artwork, an affiliation, or a claim of equivalent production polish.
