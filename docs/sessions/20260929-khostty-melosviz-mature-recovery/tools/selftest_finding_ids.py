#!/usr/bin/env python3
import json,tempfile
from pathlib import Path
from validate_finding_ids import validate

def main():
  with tempfile.TemporaryDirectory() as td:
    r=Path(td)
    (r/"good.md").write_text("## X-F01 — a\n## X-F02 — b\n")
    (r/"good.json").write_text(json.dumps({"blocking_findings":["X-F01","X-F02","other"]}))
    a=validate(r/"good.md",r/"good.json","X-F")
    (r/"dup.md").write_text("## X-F01 — a\n## X-F01 — b\n")
    b=validate(r/"dup.md",r/"good.json","X-F")
    (r/"missing.json").write_text(json.dumps({"blocking_findings":["X-F03"]}))
    c=validate(r/"good.md",r/"missing.json","X-F")
    checks={"good_passes":a["pass"],"duplicate_fails":not b["pass"] and b["duplicates"]==["X-F01"],"missing_ref_fails":not c["pass"] and c["missing_blocking_refs"]==["X-F03"]}
    print(json.dumps({"subject":"FINDING_ID_VALIDATOR_SELFTEST","checks":checks,"all_passed":all(checks.values())},indent=2))
    return 0 if all(checks.values()) else 1
if __name__=="__main__":raise SystemExit(main())
