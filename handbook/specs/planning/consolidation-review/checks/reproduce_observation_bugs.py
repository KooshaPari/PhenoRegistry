#!/usr/bin/env python3
"""Reproduce two log-observed JSON interpretation errors, without any remote calls.

Requires jq on PATH. Only invokes jq with constant filters and synthetic stdin.
Never invokes gh, git, a shell, a network client, or repository mutations.
"""
from __future__ import annotations
import json
import shutil
import subprocess
import sys

def main() -> int:
    jq = shutil.which('jq')
    if jq is None:
        print(json.dumps({'status': 'BLOCKED', 'reason': 'jq is not installed'}))
        return 2
    cases = [
        ('existing-unarchived', {'id': 1, 'archived': False}, '.archived // "DELETED"', 'DELETED'),
        ('existing-archived', {'id': 1, 'archived': True}, '.archived // "DELETED"', True),
        ('missing-field', {'id': 1}, '.archived // "DELETED"', 'DELETED'),
        ('rest-fork-field', {'fork': True, 'parent': {'full_name': 'upstream/example'}}, '{isFork,parent:.parent.full_name}', {'isFork': None, 'parent': 'upstream/example'}),
    ]
    records=[]
    for name, payload, expression, expected in cases:
        run=subprocess.run([jq,expression],input=json.dumps(payload),text=True,capture_output=True,timeout=5,check=False)
        try: actual=json.loads(run.stdout)
        except json.JSONDecodeError: actual={'unparsed':run.stdout}
        records.append({'id':name,'input':payload,'expression':expression,'exit_code':run.returncode,'output':actual,'expected_bug_behavior':expected,'reproduced':run.returncode==0 and actual==expected})
    verdict=all(r['reproduced'] for r in records)
    print(json.dumps({'status':'REPRODUCED' if verdict else 'FAILED','scope':'Four inert fixtures; observed erroneous behavior, NOT a validated replacement observer','jq_version':subprocess.check_output([jq,'--version'],text=True,timeout=5).strip(),'remote_actions':0,'cases':records},indent=2))
    return 0 if verdict else 1
if __name__=='__main__':
    raise SystemExit(main())
