#!/usr/bin/env python3
"""Validate stable finding IDs and blocking references for a recovery dossier.

Usage:
  python validate_finding_ids.py --findings FINDINGS.md --state CURRENT-STATE.json --prefix K-F
  python validate_finding_ids.py --findings FINDINGS.md --state CURRENT-STATE.json --prefix M-F

This validates identifier integrity only, not semantic correctness or product acceptance.
"""
from __future__ import annotations
import argparse, json, re
from pathlib import Path

def validate(findings: Path, state: Path, prefix: str) -> dict:
    text=findings.read_text(encoding="utf-8")
    pattern=re.compile(r"^## ("+re.escape(prefix)+r"\d+)\b",re.M)
    ids=pattern.findall(text)
    seen=set();duplicates=[]
    for x in ids:
        if x in seen and x not in duplicates: duplicates.append(x)
        seen.add(x)
    payload=json.loads(state.read_text(encoding="utf-8"))
    refs=[x for x in payload.get("blocking_findings",[]) if re.fullmatch(re.escape(prefix)+r"\d+",str(x))]
    missing=[x for x in refs if x not in seen]
    malformed=[x for x in payload.get("blocking_findings",[]) if isinstance(x,str) and x.startswith(prefix) and x not in refs]
    return {
      "prefix":prefix,
      "finding_count":len(ids),
      "unique_count":len(seen),
      "duplicates":duplicates,
      "blocking_refs":refs,
      "missing_blocking_refs":missing,
      "malformed_prefixed_refs":malformed,
      "pass":not duplicates and not missing and not malformed,
      "scope":"identifier integrity only; no semantic/product acceptance"
    }

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--findings",type=Path,required=True)
    p.add_argument("--state",type=Path,required=True)
    p.add_argument("--prefix",required=True)
    p.add_argument("--out",type=Path)
    a=p.parse_args()
    r=validate(a.findings,a.state,a.prefix)
    out=json.dumps(r,indent=2)+"\n"
    if a.out:
        a.out.parent.mkdir(parents=True,exist_ok=True)
        with a.out.open("x") as f:f.write(out)
    print(out,end="")
    raise SystemExit(0 if r["pass"] else 1)
if __name__=="__main__":main()
