# Editing and rendering

The Markdown report and JSON/CSV records are editable outputs. `build_audit.py` contains the normalized observations and authored assessments; `render_report.py` generates the PDF from those definitions. Regenerating overwrites the derived report/record files in this package directory. It does not contact or modify GitHub.

For source-based regeneration, install ReportLab and PyMuPDF in an isolated Python environment, then run:

```sh
python render_report.py
python checks/validate_package.py
```

See `records/package-environment.json` for the actual rendering library versions used. Font paths in the renderer reference local DejaVu Sans installations; install them locally or choose locally available licensed fonts. No font binaries are supplied. Final output needs fresh visual review after edits. Refresh checksums after any change.

Do not confuse the generated package validators with a product coverage or lifecycle-approval engine. No source history, native binaries or full raw API export is included.
