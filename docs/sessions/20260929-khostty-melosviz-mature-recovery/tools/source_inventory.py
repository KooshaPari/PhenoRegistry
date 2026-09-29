#!/usr/bin/env python3
"""Inventory a FULL pinned Git tree without checking out/running product code.
This closes only the tracked-file enumeration, NOT semantic source coverage.
Deleted baseline paths are preserved as historical rows. No zero-result search
or file-open count becomes a requirement or a product-completion percentage.
"""
from __future__ import annotations
import argparse, hashlib, json, re, subprocess
from pathlib import Path

CHECKS=("meaning_understood","contradictions_disposed","obligations_dispositioned",
        "implementation_surfaces_identified","stage_journey_considered","verification_considered")

def git(repo: Path, *args: str) -> bytes:
    r=subprocess.run(["git","-C",str(repo),*args],capture_output=True,timeout=30,check=False)
    if r.returncode: raise ValueError(r.stderr.decode(errors="replace"))
    return r.stdout

def tree(repo:Path, rev:str)->dict:
    if not re.fullmatch(r"[a-f0-9]{40}",rev): raise ValueError("supply exact 40-character commit, not a moving ref")
    if git(repo,"rev-parse",f"{rev}^{{commit}}").decode().strip()!=rev: raise ValueError("revision is not that commit")
    records={}
    for entry in git(repo,"ls-tree","-rz","--full-tree",rev).split(b"\0"):
        if not entry:continue
        meta,path=entry.split(b"\t",1);mode,kind,oid=meta.decode().split()
        name=path.decode("utf-8","surrogateescape")
        if name in records:raise ValueError("duplicate tree path")
        records[name]=dict(path=name,mode=mode,kind=kind,object_id=oid)
    return records

def inventory(repo:Path,product:str,source:str,baseline:str|None=None)->dict:
    current=tree(repo,source);old=tree(repo,baseline) if baseline else {}
    rows=[]
    for path in sorted(set(current)|set(old)):
        now,prior=current.get(path),old.get(path)
        status="removed" if now is None else "added" if prior is None and baseline else "not_compared" if not baseline else "unchanged" if now==prior else "modified"
        rows.append(dict(id="SRC-"+hashlib.sha256((product+"\0"+path).encode("utf-8","surrogateescape")).hexdigest()[:20],
            **(now or prior),source_snapshot=source,current=now is not None,baseline_snapshot=baseline,
            baseline_object_id=prior["object_id"] if prior else None,delta=status,
            source_family="UNCLASSIFIED",authority="UNCLASSIFIED",semantic_resolution="OPEN",
            resolution_checks={c:False for c in CHECKS},obligations=[],journeys=[],evidence=[]))
    # Immutable Git objects are inventoried, not mutable worktree contents.
    return dict(schema_version=1,product=product,source_snapshot=source,baseline=baseline,
        enumeration="COMPLETE_TRACKED_TREE",tracked_source_entries=len(current),baseline_removed_entries=len(set(old)-set(current)),
        semantic_source_denominator="OPEN",semantic_resolved=0,rows=rows,
        limitations=["Untracked/local files, deleted remote repos, PRs, conversations and external standards not included",
                    "Rename lineage not inferred; reviewers must record explicit supersession",
                    "An inventoried file is not a semantically resolved source"])

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("--repo",type=Path,required=True)
    p.add_argument("--product",required=True);p.add_argument("--source",required=True);p.add_argument("--baseline")
    p.add_argument("--out",type=Path,required=True);a=p.parse_args()
    if a.out.resolve().is_relative_to(a.repo.resolve()):
        raise ValueError("write evidence outside candidate checkout")
    r=inventory(a.repo,a.product,a.source,a.baseline);a.out.parent.mkdir(parents=True,exist_ok=True)
    # Exclusive creation: a new receipt cannot overwrite a prior observation.
    with a.out.open("x") as f: json.dump(r,f,indent=2);f.write("\n")
    print(json.dumps({k:v for k,v in r.items() if k!="rows"},indent=2))

if __name__=="__main__":main()
