# Package validation — not product verification

All **22 artifact-consistency checks passed**. The PDF has **45 pages**.

Validated: JSON syntax, 62 stable-ID cohort preservation, original 30 active-candidate membership, the 61-ID closing observation, nine recorded identity/access changes, per-repository next actions and acceptance criteria, source references, SHA syntax, finding/work references, acyclic hard dependencies, explicit non-authorization, unresolved-not-deleted MobileMcp classification, CSV identity parity, truthful execution limitations, all original names/IDs in the PDF, absence of replacement glyphs, page text bounds, and no distributed font binaries or HTML dashboard.

Rendering: the initial PDF was rendered through Poppler. All initial pages were inspected as contact sheets; a sparse release spill page and source-label separation were corrected. The final PDF was rendered through PyMuPDF and changed page groups were visually inspected. Final text bounds remain within page margins. The final layout check is in `pdf-layout.json`.

This validates this artifact set only. No native project tests, actual suite coverage, deployment, privacy penetration test, live credential probe, graphical installation, SOTA pilot, full Git history or preservation restore was executed. No external linked URL was exhaustively revalidated after the snapshot. Source observations and release metadata have their own stated limits.

Run `python checks/validate_package.py` to reproduce the package-consistency checks. Fixed 62/30/61/29 counts apply only to this immutable observation, not to future live inventory validation.
