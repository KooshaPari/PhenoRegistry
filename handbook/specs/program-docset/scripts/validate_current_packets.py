#!/usr/bin/env python3
"""Validate current owner packets, not product correctness or chat activity."""
from __future__ import annotations
import argparse,json,re
from pathlib import Path

REQUIRED=('START-HERE.md','STATE.md','NEXT-ACTIONS.md','AGENT-PROMPT.md','CURRENT-STATE.json','WORKER-RECEIPT.template.json','DOSSIER.md','PILOT.json')

def validate_records(inventory,index,states,root):
    errors=[]
    observed={str(r['repository_id']):r for r in inventory['repositories'] if not r['name'].casefold().startswith('zz')}
    entries=index['entries']; ids=[str(e['repository_id']) for e in entries]
    if len(ids)!=len(set(ids)): errors.append('duplicate owner repository')
    if set(ids)!=set(observed): errors.append('current cohort mismatch')
    if index['expected_count']!=len(observed): errors.append('wrong current count')
    state_ids=[str(s['repository_id']) for s in states]
    if len(state_ids)!=len(set(state_ids)) or set(state_ids)!=set(observed): errors.append('state cohort mismatch')
    sd={str(s['repository_id']):s for s in states}
    for e in entries:
        rid=str(e['repository_id']);obs=observed.get(rid);s=sd.get(rid)
        if obs is None or s is None: continue
        if e['name']!=obs['name'] or s['name']!=obs['name']:errors.append('stale name')
        if e['default_branch']!=obs['default_branch'] or s['default_branch']!=obs['default_branch']:errors.append('wrong branch')
        if e['owner_chats']!=1 or s['owner_chat_count']!=1:errors.append('wrong owner allocation')
        if e['actual_chat_receipt'] is not None or s['owner_chat_id'] is not None:errors.append('invented session receipt')
        if s['owner_chat_evidence']!='USER_REPORTED_NOT_INDEPENDENTLY_OBSERVED':errors.append('invented session observation')
        if any(s.get(k) is not False for k in ('native_tests_run_by_this_audit','installed_product_qualified','new_authority_granted')):errors.append('unsupported audit claim')
        if s['repository_completion']!='NOT_CERTIFIED':errors.append('unsupported completion')
        if not re.fullmatch('[0-9a-f]{40}',s['sampled_commit']):errors.append('invalid source sha')
        if not s['sources'] or not s['concerns'] or not s['parent_acceptance']:errors.append('missing basis or acceptance')
        if not s['next_actions']:errors.append('missing next actions')
        for a in s['next_actions']:
            if a['status']!='PROPOSED_NOT_EXECUTED' or a['cross_repo_writes_authorized'] is not False:errors.append('invented execution authority')
            if not a['acceptance'] or not a['work']:errors.append('empty action contract')
        folder=root/e['folder']
        if e['folder']!='products/'+obs['name'] or not folder.resolve().is_relative_to(root.resolve()):errors.append('bad subject path');continue
        for f in REQUIRED:
            if not (folder/f).is_file():errors.append('missing '+f+' '+obs['name'])
        if (folder/'CURRENT-STATE.json').is_file():
            if json.loads((folder/'CURRENT-STATE.json').read_text())!=s:errors.append('state projection drift')
    return errors

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('root',type=Path,nargs='?',default=Path(__file__).resolve().parents[1]);a=p.parse_args();r=a.root
    try:
        load=lambda f:json.loads((r/f).read_text())
        errors=validate_records(load('portfolio/live-inventory-2026-09-16.json'),load('portfolio/CURRENT-REPO-INDEX.json'),load('records/current-repository-state.json'),r)
        print(json.dumps({'status':'PASS' if not errors else 'FAIL','errors':errors,'scope':'Current set and packet consistency only','native_product_qualification':False,'actual_sessions_observed':False},indent=2));return int(bool(errors))
    except Exception as ex:
        print(json.dumps({'status':'INPUT_ERROR','error':str(ex),'native_product_qualification':False}));return 2
if __name__=='__main__':raise SystemExit(main())
