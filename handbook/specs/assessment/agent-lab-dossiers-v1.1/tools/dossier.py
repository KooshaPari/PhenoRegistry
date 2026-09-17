#!/usr/bin/env python3
"""File-first dossier renderer and consistency checker.

Python 3.10+, standard library only. No product commands, APIs, signing keys or
permissions are supplied. The retained PEP 1.0 kernel validates underlying records.
Illustrative premises are never credited as operational product evidence.
"""
from __future__ import annotations
import argparse
import hashlib
import html
import json
import math
from pathlib import Path
import re
import sys
from typing import Any

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'core-v1.0' / 'tools'))
import pep

VERSION = '1.1.0'
GENERATED = {'ASSESSMENT.md', 'ASSESSMENT.html', 'views/assessment.json',
             'views/assessment.yaml', 'views/records.jsonl', 'views/build.json'}

def esc(value: Any) -> str:
    return html.escape(str(value), quote=True)

def md(value: Any) -> str:
    return str(value).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;').replace('|','\\|').replace('\n',' ')

def dumps(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + '\n'

def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    pep.need(not path.is_symlink(), f'refusing symlink output: {path}')
    with path.open('w', encoding='utf-8', newline='\n') as f:
        f.write(text)

def yaml_text(value: Any, indent: int = 0) -> str:
    """Emit a conservative quoted YAML subset; JSON remains canonical input.

    No aliases, tags, anchors, implicit dates, NaN or infinity. Floats use JSON
    spelling. A separate optional parser is used in release tests, not at runtime.
    """
    pad = ' ' * indent
    scalar = lambda x: json.dumps(x, ensure_ascii=False, allow_nan=False)
    if isinstance(value, dict):
        if not value: return pad+'{}\n'
        out = []
        for k,v in value.items():
            if isinstance(v,(dict,list)) and v:
                out.append(pad+scalar(k)+':\n'+yaml_text(v,indent+2))
            else: out.append(pad+scalar(k)+': '+scalar(v)+'\n')
        return ''.join(out)
    if isinstance(value, list):
        if not value: return pad+'[]\n'
        return ''.join(pad+'-\n'+yaml_text(v,indent+2) if isinstance(v,(dict,list)) and v
                       else pad+'- '+scalar(v)+'\n' for v in value)
    return pad+scalar(value)+'\n'

def inputs(base: Path) -> list[dict[str, Any]]:
    rows=[]
    for f in sorted(base.rglob('*')):
        pep.need(not f.is_symlink(), 'symlink inside dossier')
        if not f.is_file(): continue
        rel=f.relative_to(base).as_posix()
        if rel in GENERATED or rel=='MANIFEST.json': continue
        pep.safe_file(base,rel)
        rows.append({'path':rel,'bytes':f.stat().st_size,'digest':pep.file_digest(f)})
    return rows

def load_dossier(base: Path) -> tuple[dict,dict,dict,list,list]:
    d=pep.load_json(pep.safe_file(base,'dossier.json'))
    pep.validate_shape(d,pep.load_json(ROOT/'schemas/dossier.schema.json'))
    b=pep.read_bundle(base)
    a=b['assignment']
    for ev in b['evidence'].values():
        pep.need(not any(c in ev['path'] for c in [':','?','#']), 'evidence path contains URI delimiters')
    if d['record_status']=='OPERATIONAL':
        pep.need(not pep.has_placeholder(d), 'operational dossier contains template placeholders')
    for obfile in (base/'outbox').glob('*.json'):
        ob=pep.load_json(obfile);pep.validate_record(ob)
        pep.need(ob['record_status']==d['record_status'], 'outbox context mismatch')
        if ob['state']=='PENDING':
            pep.need(ob['receipt_ref'] is None, 'pending outbox cannot have a delivery receipt')
        pep.need(ob['payload_digest']==pep.file_digest(base/'assessment.json'), 'outbox payload mismatch')
    pep.need(d['record_status']==a['record_status'],'dossier/core record status mismatch')
    pep.need(d['example_class']!='REAL_ASSESSMENT' or d['record_status']=='OPERATIONAL',
             'real assessment must have OPERATIONAL context')
    if d['example_class'] in ('EXECUTED_FIXTURE','ILLUSTRATIVE_SCENARIO'):
        pep.need(d['record_status']=='EXAMPLE','example class cannot claim operational context')
    subject=pep.load_json(pep.safe_file(base,'subject.json'))
    pep.need(pep.value_digest(subject)==a['subject_digest'],'subject identity digest mismatch')
    if d['example_class']=='EXECUTED_FIXTURE':
        pep.need(subject.get('source_digest')==pep.file_digest(ROOT/'core-v1.0/tools/toy_product.py'),
                 'executed toy source digest mismatch')
    notes=d['row_notes'];pep.unique(notes,'instance_id')
    pep.need({n['instance_id'] for n in notes}=={i['id'] for i in a['instances']},'row notes do not cover exact instance set')
    if d['example_class']=='ILLUSTRATIVE_SCENARIO':
        pep.need(not b['qualifications'],'illustrative scenario cannot fabricate instrument qualification')
        pep.need(all(r['review_status']=='PROPOSED' for r in b['results'].values()),
                 'illustrative results must remain PROPOSED, never ACCEPTED')
        pep.need(all(ev['origin']=='EXTERNAL_REFERENCE' for ev in b['evidence'].values()),
                 'illustrative premises cannot masquerade as executed observations')
        premise=pep.load_json(pep.safe_file(base,'raw/scenario.json'))
        pep.need(premise.get('example_class')=='ILLUSTRATIVE_SCENARIO' and premise.get('product_execution_performed') is False,
                 'missing explicit fictional-premise label')
    findings=[];decisions=[]
    for ids,folder,kind,target in [(d['finding_ids'],'findings','finding',findings),(d['decision_ids'],'decisions','decision',decisions)]:
        recs=pep.index_records(base,ids,folder,kind)
        for rec in recs.values():
            pep.need(rec['record_status']==d['record_status'],'linked record context mismatch')
            for eid in rec['evidence_refs']:
                pep.need(eid in b['evidence'],'unresolved finding/decision evidence reference')
            if kind=='finding':
                pep.need(set(rec['instance_refs']) <= {i['id'] for i in a['instances']},'unknown finding instance')
                pep.need(set(rec['counterevidence_refs'])<=set(b['evidence']),'unknown counterevidence reference')
            target.append(rec)
    return d,b,pep.summarize_bundle(base),findings,decisions

def premise_summary(a:dict,results:dict) -> dict:
    """Pedagogical only: reduce stated scenario premises, not admissible evidence."""
    states={}; rows=[]; counts={k:0 for k in ['PASS','FAIL','UNKNOWN','NOT_APPLICABLE','UNRESOLVED']}
    weights={k:0.0 for k in counts}
    superseded={x for r in results.values() for x in r['supersedes']}
    for i in a['instances']:
        active=[r for r in results.values() if r['instance_id']==i['id'] and r['id'] not in superseded]
        if i['applicability']!='APPLICABLE':state=i['applicability']
        elif len(active)!=1:state='UNKNOWN'
        else:
            r=active[0]
            state=r['verdict'] if r['execution']=='COMPLETED' and r['evidence_state']=='CURRENT' and r['verdict'] in ('PASS','FAIL') else 'UNKNOWN'
        states[i['id']]=state; counts[state]+=1;weights[state]+=i['weight']
    p,f,u=[weights[k] for k in ['PASS','FAIL','UNKNOWN']]
    ratio=lambda x,y:x/y if y else None
    gates=[]
    for g in a['gates']:
        ss=[states[x] for x in g['required_instance_ids']]
        s='FAIL' if 'FAIL' in ss else 'PASS' if all(x=='PASS' for x in ss) else 'BLOCKED'
        gates.append({'id':g['id'],'status':s,'required_instance_ids':g['required_instance_ids']})
    return {'classification':'HYPOTHETICAL_PREMISES_ONLY_NOT_PRODUCT_EVIDENCE',
            'counts':counts,'weights':weights,'assessed_pass_rate':ratio(p,p+f),
            'assessment_coverage':ratio(p+f,p+f+u),'satisfaction':ratio(p,p+f+u),
            'states':states,'gates':gates}

def build_model(base:Path) -> dict:
    d,b,summary,findings,decisions=load_dossier(base)
    notes={n['instance_id']:n for n in d['row_notes']}
    catalog=pep.load_json(pep.ROOT/'catalog/catalog.json')
    cs={c['id']:c for c in catalog['criteria']}; domains={c['id']:c for c in catalog['domains']}
    assumed=premise_summary(b['assignment'],b['results']) if d['example_class']=='ILLUSTRATIVE_SCENARIO' else None
    rows=[]
    for x in summary['instances']:
        iid=x['instance_id']; candidates=[r for r in b['results'].values() if r['instance_id']==iid]
        c=cs[x['criterion_id']]
        row={**x,**notes[iid],'domain':c['domain_id'],'predicate':c['predicate'],
             'display_state':assumed['states'][iid] if assumed else x['state'],
             'result_records':candidates,
             'evidence':[b['evidence'][eid] for r in candidates for eid in r['evidence_ids']]}
        rows.append(row)
    return {'format':'ASSESSMENT_DOSSIER_VIEW_V1_1','dossier':d,'assessment':b['assessment'],
            'assignment':b['assignment'],'evidence_summary':summary,'illustrative_summary':assumed,
            'findings':findings,'decisions':decisions,'rows':rows,'input_files':inputs(base),
            'authority_notice':'A generated view and matching hashes establish neither truthful observations nor permission to publish, merge, spend, or retire.'}

def percent(x: Any) -> str:
    return 'Not defined' if x is None else f'{100*x:.1f}%'

def report_md(m:dict) -> str:
    d=m['dossier'];s=m['evidence_summary'];i=m['illustrative_summary'];a=m['assignment']
    text=[f"# {d['title']}", '',d['subtitle'],'',f"**{d['example_class']} · {d['record_status']}**",'',
          f"> {d['provenance_notice']}",'',
          '## Decision brief','',f"**Next action:** {d['next_action']}",'',
          f"**Stage:** {d['maturity']['scenario_or_scoped_label']}",'',d['maturity']['claim_limit'],'',
          f"**Stop condition:** {d['stop_condition']}",'',
          '## Identity and scope','',
          f"- Dossier: `{d['id']}`; assessment: `{m['assessment']['id']}`; epoch: `{a['epoch_id']}`.",
          f"- Beneficiary: {d['beneficiary']}",f"- Boundary: {d['boundary']}",
          f"- Subject digest: `{a['subject_digest']}`.",
          f"- Assignment byte digest: `{m['assessment']['assignment_digest']}`.",
          f"- Source revision: `{d['subject_identity']['source_revision'] or 'NOT_AVAILABLE — no invented Git SHA'}`.",
          f"- Identity method: {d['subject_identity']['identity_method']}",
          f"- Evidence cutoff: `{m['assessment']['as_of']}`.",
          f"- Registry: `{s['registration_state']}`; signature: **UNSIGNED**.",'',
          d['subject_identity']['limitation'],'',
          '## Scope, coverage, and gates','',
          s['coverage_statement'],'']
    if i:
        text += [f"**Illustrative premises only:** {i['counts']['PASS']} pass / {i['counts']['FAIL']} fail / {i['counts']['UNKNOWN']} unknown / {i['counts']['NOT_APPLICABLE']} not applicable / {i['counts']['UNRESOLVED']} applicability unresolved.",
                 f"Assumed assessed pass rate: {percent(i['assessed_pass_rate'])}; assumed assessment coverage: {percent(i['assessment_coverage'])}.",'',
                 '**These are authored scenario states. They are not executed product results.**','']
    text += [f"**Admissible evidence reduction:** assessed pass rate {percent(s['assessed_pass_rate'])}; assessment coverage {percent(s['assessment_coverage'])}; verified satisfaction within settled applicability {percent(s['verified_satisfaction_within_settled_applicability'])}.",
             f"**Current mandatory gate state:** `{s['mandatory_gate_state']}`. Passing toy gates never implies real-product maturity.",'',
             '| Gate | Scenario premise | Admissible evidence |','|---|---|---|']
    ig={g['id']:g['status'] for g in (i['gates'] if i else [])}
    for g in s['gates']:text.append(f"| {md(g['id'])} | {ig.get(g['id'],'Not an illustrative case')} | {g['status']} |")
    text += ['', '## Intent, genesis, and alternatives','',d['purpose'],'',
             f"**Authorship:** {d['authorship']}. **Intent status:** {d['intent_status']}.",'',
             d['genesis_rationale'],'',f"**Authority:** {d['authority']}",'',
             '**Alternatives:** '+'; '.join(d['alternatives'])+'.','',
             '**Non-goals:** '+'; '.join(d['non_goals'])+'.','',
             '## Inventory and gap map','',
             '| ID | Capability / asset | Declared | Observation or premise | Gap |','|---|---|---|---|---|']
    for x in d['inventory']:text.append('| '+' | '.join(md(x[k]) for k in ['id','item','declared','observed_or_assumed','gap'])+' |')
    text += ['', '## Filled rubric','',
             'Each row is scoped to this assignment. The full catalog is not claimed evaluated. `Display` is illustrative only where the banner says so. `Credit` is the underlying evidence-based reducer result.','',
             '| ID | Criterion / scoped title | Display | Credit | Mandatory | Weight |','|---|---|---|---|---|---|']
    for r in m['rows']:text.append(f"| {r['instance_id']} | {md(r['title'])} (`{r['criterion_id']}`) | {r['display_state']} | {r['state']} | {'Yes' if r['mandatory'] else 'No'} | {r['weight']} |")
    for r in m['rows']:
        text += ['',f"### {r['instance_id']} · {r['title']}",'',f"**Predicate:** {r['predicate']}",'',
                 f"**Interpretation:** {r['interpretation']}",'',f"**Reducer:** {r['state']} — {r['reason']}.",'',
                 f"**Next action:** {r['next_action']}",'']
        for ev in r['evidence']:text.append(f"Evidence: [`{ev['id']}`]({ev['path']}) · `{ev['digest']}` · {ev['summary']}")
        if not r['evidence']:text.append('Evidence: not supplied. This absence is preserved, not converted into a pass.')
    text += ['', '## Findings and bounded decisions','']
    for f in m['findings']:
        text += [f"### {f['id']} · {f['severity']} · {f['class']}",'',f['claim'],'',
                 f"Owner: `{f['owner_ref']}`. Status: `{f['status']}`. Route: `{f['next_action_kind']}`. Wakeup: {f['wakeup_condition'] or 'No external wakeup required.'}",'']
    for x in m['decisions']:
        text += [f"**{x['id']} / {x['disposition']} / {x['status']}:** {x['rationale']}",'',
                 'Alternatives: '+'; '.join(x['alternatives'])+'.','',f"Reversal: {x['reversal_condition']}",'']
    text += ['## Maturity and value','', '| Axis | Scoped status | Basis |','|---|---|---|']
    for x in d['maturity']['axes']:text.append('| '+' | '.join(md(x[k]) for k in ['axis','status','basis'])+' |')
    text += ['',f"**Value evidence:** {d['maturity']['value_evidence']}",'','## Semantic review and contrary cases','']
    for r in d['semantic_reviews']:
        text += [f"### {r['topic']}",'',r['assessment'],'',f"Support: {r['support']}",'',f"Countercase: {r['countercase']}",'',f"Discriminator: {r['discriminator']}",'',f"Confidence basis: {r['confidence_basis']}",'']
    text += ['## Delta and fresh-session handoff','',f"**Change class:** {d['lineage']['change_class']}. {d['lineage']['description']}",'',
             f"**Accepted baseline:** {d['restart_packet']['accepted_baseline']}",'',
             '**Rejected or tested hypotheses:** '+'; '.join(d['restart_packet']['failed_hypotheses'])+'.','',
             f"**Next reproduction:** {d['restart_packet']['next_reproduction']}",'',
             f"**Budget and permissions:** {d['restart_packet']['budget_and_permissions']}",'',
             '## Machine records and integrity','',
             '[Assignment](assignment.json) · [Assessment](assessment.json) · [Dossier context](dossier.json) · [Normalized JSON view](views/assessment.json) · [YAML view](views/assessment.yaml) · [JSONL export](views/records.jsonl) · [Build receipt](views/build.json)','',
             'JSON inputs are authoritative within this dossier. YAML, JSONL, Markdown, and HTML here are generated views. The unsigned manifest detects changed bytes against the supplied baseline; it does not certify observations or authorship.','']
    return '\n'.join(text).replace('<', '&lt;')

CSS='''
:root{--ink:#142b38;--muted:#52636e;--line:#d4dfe3;--bg:#f2f5f6;--paper:#fff;--teal:#367a75;--soft:#e8f3f1;--warn:#805218;--fail:#993b3b;--blue:#315e8a}*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}a{color:#245f83;text-underline-offset:3px}a:focus-visible,button:focus-visible,summary:focus-visible,input:focus-visible{outline:3px solid #805218;outline-offset:4px}h1{font-size:clamp(2rem,4.5vw,3.4rem);line-height:1.12;letter-spacing:-.04em;margin:.6rem 0 1rem}h2{font-size:1.6rem;margin:2.5rem 0 1rem;letter-spacing:-.02em}h3{font-size:1.12rem;margin:1.3rem 0 .5rem}p{margin:.7rem 0 1rem}code{font: .82em/1.6 ui-monospace,SFMono-Regular,Consolas,monospace;overflow-wrap:anywhere}.wrap{max-width:1280px;margin:auto;padding:42px 36px 80px}.eyebrow{text-transform:uppercase;letter-spacing:.14em;font-size:.72rem;font-weight:800;color:var(--teal)}.sub{font-size:1.12rem;max-width:900px;color:var(--muted)}.banner{padding:16px 20px;border-left:5px solid var(--teal);background:var(--soft);margin:24px 0}.banner.illustrative{border-color:var(--warn);background:#fff4e4}.banner strong{display:block;margin-bottom:4px}.card{background:var(--paper);border:1px solid var(--line);border-radius:12px;padding:24px;margin:20px 0;box-shadow:0 4px 12px #172f3a05}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:16px}.metric{border:1px solid var(--line);background:var(--paper);padding:18px 20px;border-radius:10px}.metric span{font-size:.76rem;text-transform:uppercase;letter-spacing:.06em;color:var(--muted);display:block}.metric strong{font-size:1.65rem;display:block;line-height:1.3;margin:8px 0}.metric small{font-size:.8rem;color:var(--muted);display:block}.pill{display:inline-block;padding:3px 9px;border-radius:6px;font-size:.76rem;font-weight:700;background:#edf0f2;letter-spacing:.02em;white-space:nowrap}.PASS{background:#e4f1e9;color:#255e3f}.FAIL{background:#fbe9e7;color:#933b31}.UNKNOWN,.BLOCKED,.UNRESOLVED{background:#fff0d7;color:#7e561d}.NOT_APPLICABLE{background:#ebeff3;color:#52616e}.tablewrap{overflow:auto;border:1px solid var(--line);border-radius:10px;background:#fff}table{border-collapse:collapse;width:100%;text-align:left;font-size:.86rem}th,td{padding:12px 14px;vertical-align:top;border-bottom:1px solid #e3eaed}th{background:#edf2f4;color:#445a67;font-size:.74rem;text-transform:uppercase;letter-spacing:.055em}tr:last-child td{border-bottom:0}td small{display:block;color:var(--muted);line-height:1.5;margin-top:5px}dl{display:grid;grid-template-columns:180px 1fr;gap:8px 20px;margin:0}dt{font-size:.85rem;color:var(--muted);font-weight:600}dd{margin:0;overflow-wrap:anywhere}summary{cursor:pointer;line-height:1.5;font-weight:650;padding:16px 0}details{border-bottom:1px solid var(--line)}details>div{padding:0 0 20px}.dim{color:var(--muted)}.small{font-size:.86rem}.sectionnav{display:flex;flex-wrap:wrap;gap:8px 18px;font-size:.85rem;margin:24px 0}.footer{border-top:1px solid var(--line);margin-top:36px;padding-top:20px;color:var(--muted);font-size:.85rem}.search{padding:12px 16px;width:min(100%,480px);font:inherit;border:1px solid var(--line);border-radius:8px;background:#fff}.dossier-preview{margin:25px 0;padding:0 24px;background:white;border:1px solid var(--line);border-radius:12px}.dossier-preview>summary{font-size:1.2rem}.dossier-preview>div{padding-bottom:32px}.inline-links{display:flex;gap:16px;flex-wrap:wrap}.badge-label{font-size:.75rem;color:var(--muted);margin-left:8px}.break{overflow-wrap:anywhere}.statlabel{font-size:.78rem;color:var(--muted)}@media(max-width:640px){.wrap{padding:24px 16px 50px}.card{padding:18px}dl{grid-template-columns:1fr;gap:0}dd{margin-bottom:12px}.grid{grid-template-columns:1fr 1fr;gap:10px}.metric{padding:14px}.metric strong{font-size:1.25rem}th,td{padding:10px}.dossier-preview{padding:0 14px}.tablewrap{font-size:.82rem}}@media print{body{background:#fff}.wrap{padding:0;max-width:none}.card,.metric,.tablewrap{break-inside:avoid}.search,.sectionnav{display:none}details>div{display:block!important}h2,h3{break-after:avoid}a{color:inherit;text-decoration:none}.dossier-preview{border:0;padding:0;break-before:page}}
'''

def pill(s:str) -> str:
    return f'<span class="pill {esc(s)}">{esc(s)}</span>'

def table(headers:list[str],rows:list[list[str]]) -> str:
    return '<div class="tablewrap"><table><thead><tr>'+''.join('<th scope="col">'+esc(h)+'</th>' for h in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+x+'</td>' for x in r)+'</tr>' for r in rows)+'</tbody></table></div>'

def body_html(m:dict,prefix:str='') -> str:
    d=m['dossier'];s=m['evidence_summary'];i=m['illustrative_summary'];a=m['assignment']
    link=lambda path,label:f'<a href="{esc(prefix+path)}">{esc(label)}</a>'
    cls='illustrative' if i else ''
    out=[f'<div class="eyebrow">Assessment Dossier / {esc(d["id"])}</div>',f'<h1>{esc(d["title"])}</h1>',f'<p class="sub">{esc(d["subtitle"])}</p>',
         f'<div class="banner {cls}"><strong>{esc(d["example_class"])}</strong>{esc(d["provenance_notice"])}</div>',
         '<div class="grid">',
         f'<div class="metric"><span>Current evidence gate</span><strong>{pill(s["mandatory_gate_state"])}</strong><small>Not a publication authorization</small></div>',
         f'<div class="metric"><span>{"Assumed pass rate" if i else "Assessed pass rate"}</span><strong>{percent(i["assessed_pass_rate"] if i else s["assessed_pass_rate"])}</strong><small>{"Scenario premises, not observations" if i else "Within two executed fixture checks"}</small></div>',
         f'<div class="metric"><span>Admissible evidence coverage</span><strong>{percent(s["assessment_coverage"])}</strong><small>Within settled applicability</small></div>',
         f'<div class="metric"><span>Scoped rows</span><strong>{len(m["rows"])}</strong><small>Not the entire 1,080-entry catalog</small></div></div>',
         f'<section class="card"><div class="eyebrow">Decision brief</div><h2 style="margin-top:12px">{esc(d["next_action"])}</h2><p><strong>Stage:</strong> {esc(d["maturity"]["scenario_or_scoped_label"])}</p><p class="dim">{esc(d["maturity"]["claim_limit"])}</p><p><strong>Stop:</strong> {esc(d["stop_condition"])}</p></section>',
         '<h2>Identity and scope</h2><div class="card"><dl>']
    pairs=[('Beneficiary',d['beneficiary']),('Boundary',d['boundary']),('Subject digest',a['subject_digest']),('Assignment digest',m['assessment']['assignment_digest']),('Epoch',a['epoch_id']),('Source revision',d['subject_identity']['source_revision'] or 'Not available — no invented Git SHA'),('Evidence cutoff',m['assessment']['as_of']),('Registry',s['registration_state']),('Signature','UNSIGNED')]
    out += [f'<dt>{esc(k)}</dt><dd>{"<code>"+esc(v)+"</code>" if "digest" in k else esc(v)}</dd>' for k,v in pairs]
    out += ['</dl></div>',f'<p class="small dim">{esc(d["subject_identity"]["identity_method"])} {esc(d["subject_identity"]["limitation"])}</p>',
            '<h2>Intent and repository genesis</h2>',f'<p>{esc(d["purpose"])}</p><p>{esc(d["genesis_rationale"])}</p>',
            f'<p><strong>{esc(d["authorship"])}</strong> · {esc(d["intent_status"])}</p>',
            f'<p><strong>Authority:</strong> {esc(d["authority"])}</p>',
            f'<p><strong>Alternatives:</strong> {esc("; ".join(d["alternatives"]))}</p>',
            f'<p><strong>Non-goals:</strong> {esc("; ".join(d["non_goals"]))}</p>',
            '<h2>Inventory and gap map</h2>',table(['Capability','Declared','Observation / premise','Gap'],[[esc(x['item']),esc(x['declared']),esc(x['observed_or_assumed'])+'<small>'+esc(x['evidence_basis'])+'</small>',esc(x['gap'])] for x in d['inventory']]),
            '<h2>Gates and scope</h2>',f'<p>{esc(s["coverage_statement"])}</p>']
    ig={g['id']:g['status'] for g in (i['gates'] if i else [])}
    out += [table(['Gate','Scenario premise','Admissible evidence'],[[esc(g['id']),pill(ig[g['id']]) if i else 'Executed fixture',pill(g['status'])] for g in s['gates']])]
    if i:out += [f'<p class="small dim">Scenario premise counts: {i["counts"]["PASS"]} pass, {i["counts"]["FAIL"]} fail, {i["counts"]["UNKNOWN"]} unknown, {i["counts"]["NOT_APPLICABLE"]} not applicable, {i["counts"]["UNRESOLVED"]} applicability unresolved. None are credited as executed product evidence.</p>']
    out += ['<h2>Filled rubric</h2><p class="dim">The scorecard is a view over scoped obligations, result records, and evidence. Expand any row below for its interpretation and next action.</p>',
            table(['Row / criterion','Scoped check','Displayed state','Evidence credit','Required'],[[f'<code>{esc(r["instance_id"])}</code><small>{esc(r["criterion_id"])}</small>',esc(r['title']),pill(r['display_state']),pill(r['state']),'Yes' if r['mandatory'] else 'No'] for r in m['rows']]),
            '<h3>Criterion detail and evidence</h3>']
    for r in m['rows']:
        out += [f'<details><summary>{esc(r["instance_id"])} · {esc(r["title"])} <span class="badge-label">{esc(r["display_state"])}</span></summary><div>',
                f'<p><strong>Predicate:</strong> {esc(r["predicate"])}</p><p>{esc(r["interpretation"])}</p>',
                f'<p><strong>Evidence credit:</strong> {pill(r["state"])} · {esc(r["reason"])}</p>',
                f'<p><strong>Next:</strong> {esc(r["next_action"])}</p>']
        for ev in r['evidence']:out.append(f'<p class="small">{link(ev["path"],ev["id"])} · {esc(ev["summary"])}<br><code>{esc(ev["digest"])}</code></p>')
        if not r['evidence']:out.append('<p>No observation evidence supplied.</p>')
        out.append('</div></details>')
    out += ['<h2>Findings and decisions</h2>']
    for f in m['findings']:
        out += [f'<div class="card"><div class="eyebrow">{esc(f["id"])} / {esc(f["severity"])} / {esc(f["class"])}</div><h3>{esc(f["claim"])}</h3><p class="small">Owner: {esc(f["owner_ref"])} · {esc(f["status"])} · Route: {esc(f["next_action_kind"])}</p><p class="small dim">Wakeup: {esc(f["wakeup_condition"] or "No external wakeup required")}</p></div>']
    for x in m['decisions']:
        out += [f'<p><strong>{esc(x["id"])} / {esc(x["disposition"])}</strong> — {esc(x["rationale"])}</p><p class="small dim">Alternatives: {esc("; ".join(x["alternatives"]))}<br>Reversal: {esc(x["reversal_condition"])}</p>']
    out += ['<h2>Maturity and value</h2>',table(['Axis','Scoped status','Basis'],[[esc(x['axis']),esc(x['status']),esc(x['basis'])] for x in d['maturity']['axes']]),f'<p><strong>Value evidence:</strong> {esc(d["maturity"]["value_evidence"])}</p>',
            '<h2>Semantic review and contrary cases</h2>']
    for r in d['semantic_reviews']:
        out += [f'<div class="card"><h3>{esc(r["topic"])}</h3><p>{esc(r["assessment"])}</p><p><strong>Support:</strong> {esc(r["support"])}</p><p><strong>Countercase:</strong> {esc(r["countercase"])}</p><p><strong>Discriminator:</strong> {esc(r["discriminator"])}</p><p class="small dim">{esc(r["confidence_basis"])}</p></div>']
    r=d['restart_packet']
    out += ['<h2>Delta and fresh-session handoff</h2>',f'<p><strong>{esc(d["lineage"]["change_class"])}</strong> — {esc(d["lineage"]["description"])}</p>',
            f'<div class="card"><p><strong>Baseline:</strong> {esc(r["accepted_baseline"])}</p><p><strong>Failed hypotheses:</strong> {esc("; ".join(r["failed_hypotheses"]))}</p><p><strong>Next reproduction:</strong> {esc(r["next_reproduction"])}</p><p><strong>Budget / permission:</strong> {esc(r["budget_and_permissions"])}</p></div>',
            '<h2>Machine views</h2><p class="inline-links">',
            ' '.join(link(p,l) for p,l in [('assignment.json','Assignment JSON'),('assessment.json','Assessment JSON'),('dossier.json','Context JSON'),('views/assessment.json','Full JSON view'),('views/assessment.yaml','YAML view'),('views/records.jsonl','JSONL export'),('views/build.json','Build receipt'),('ASSESSMENT.md','Markdown')]),'</p>',
            '<div class="footer">Canonical inputs → deterministic reduction → Markdown / HTML / YAML / JSONL. Generated views are not editable authorities. SHA-256 manifests are unsigned integrity checks, not certification of observations, identity, authority, or product usefulness.</div>']
    return ''.join(out)

def page(title:str,body:str) -> str:
    return '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light"><title>'+esc(title)+'</title><style>'+CSS+'</style></head><body><main class="wrap">'+body+'</main></body></html>\n'

def expected_views(base:Path) -> dict[str,str]:
    m=build_model(base)
    records=[]
    for f in m['input_files']:
        if f['path'].endswith('.json'):
            records.append(json.dumps({'source_path':f['path'],'source_byte_digest':f['digest'],'record':pep.load_json(base/f['path'])},ensure_ascii=False,separators=(',',':'),allow_nan=False))
    out={'ASSESSMENT.md':report_md(m),'ASSESSMENT.html':page(m['dossier']['title'],body_html(m)),
         'views/assessment.json':dumps(m),'views/assessment.yaml':'# GENERATED VIEW. Edit canonical JSON inputs, then render again.\n'+yaml_text(m),
         'views/records.jsonl':'\n'.join(records)+'\n'}
    receipt={'format':'DOSSIER_RENDER_RECEIPT_V1_1','renderer_version':VERSION,
             'renderer_digest':pep.file_digest(Path(__file__)),
             'core_reducer_digest':pep.file_digest(ROOT/'core-v1.0/tools/pep.py'),
             'schema_digest':pep.file_digest(ROOT/'schemas/dossier.schema.json'),
             'input_manifest_digest':pep.value_digest(m['input_files']),
             'input_digest_profile':'PEP Python JSON digest profile; NOT RFC8785/JCS',
             'inputs':m['input_files'],
             'outputs':[{'path':k,'digest':'sha256:'+hashlib.sha256(v.encode()).hexdigest()} for k,v in sorted(out.items())],
             'generated_build_receipt_is_not_signed':True,
             'source_revision':m['dossier']['subject_identity']['source_revision'],
             'report_commit':None,'registry_commit':None,'registry_state':m['assessment']['registration_state']}
    out['views/build.json']=dumps(receipt)
    return out

def render(base:Path) -> dict:
    for rel,text in expected_views(base).items():write(base/rel,text)
    return {'status':'RENDERED','dossier':str(base),'outputs':sorted(GENERATED)}

def verify(base:Path) -> dict:
    out=expected_views(base)
    for rel,text in out.items():
        f=pep.safe_file(base,rel)
        pep.need(f.read_bytes()==text.encode('utf-8'),f'generated view drift: {rel}')
    d=pep.load_json(base/'dossier.json')
    return {'status':'CONSISTENT','dossier_id':d['id'],'example_class':d['example_class'],'outputs_checked':len(out),
            'claim_limit':'Record, local digest, and rendering consistency only; not independent authentication or real-product acceptance.'}

def case_dirs() -> list[Path]:
    return [p.parent for p in sorted((ROOT/'examples').glob('*/dossier.json'))]

def gallery_text() -> str:
    models=[(p,build_model(p)) for p in case_dirs()]
    rows=[]
    for p,m in models:
        d=m['dossier'];i=m['illustrative_summary'];s=m['evidence_summary']
        detail=p.relative_to(ROOT).as_posix()+'/ASSESSMENT.html'
        rows.append([f'<a href="{esc(detail)}">{esc(d["title"])}</a><small>{esc(d["subtitle"])}</small>',
                     esc(d['example_class']),str(len(m['rows'])),
                     percent(i['assessed_pass_rate'])+'<small>Assumed only</small>' if i else percent(s['assessed_pass_rate'])+'<small>Executed fixture</small>',
                     pill(s['mandatory_gate_state'])])
    intro='''<div class="eyebrow">Agent Lab Evaluation System / Dossier layer 1.1</div><h1>The assessment is a file set.<br>The scorecard is one view.</h1><p class="sub">Reusable Master Assessment Kit → scoped Assignment → completed Assessment Dossier. Machine records retain the evidence; generated reports make the state, uncertainty, and next action readable.</p><div class="banner"><strong>Eight filled dossiers, two evidence classes.</strong>Two reports contain newly executed restoration-fixture measurements. Six contain deliberately authored scenarios, not observations of your repositories. Scenario premises never receive operational acceptance credit.</div><div class="inline-links"><a href="MASTER-ASSESSMENT-KIT.md">Master kit contract</a><a href="README.md">Start and commands</a><a href="docs/FORMAT-AND-INTEGRITY.md">Formats and integrity</a><a href="qualification/VALIDATION-REPORT.md">Validation evidence</a></div><h2>Example overview</h2>'''
    body=[intro,table(['Dossier','Evidence class','Rows','Pass rate','Evidence gate'],rows),
          '<h2>Read the filled examples</h2><p class="dim">Expand a dossier below. Its complete human-readable report is embedded here; no server, external fonts, or network requests are needed. Links to machine records work inside the extracted ZIP.</p>']
    for p,m in models:
        body += [f'<details class="dossier-preview"><summary>{esc(m["dossier"]["title"])} <span class="badge-label">{esc(m["dossier"]["example_class"])}</span></summary><div>',body_html(m,p.relative_to(ROOT).as_posix()+'/'),'</div></details>']
    body += ['<div class="footer">Core 1.0 files are retained unchanged under core-v1.0. Dossier 1.1 adds contextual records, filled examples, generated views, and cross-view consistency checks; it does not replace the grader with a new autonomous platform.</div>']
    return page('Assessment Dossier Gallery', ''.join(body))

def verify_package() -> dict:
    manifest=pep.load_json(ROOT/'MANIFEST.json')
    listed=set()
    for f in manifest['files']:
        pep.need(f['path'] not in listed,'duplicate manifest path');listed.add(f['path'])
        p=pep.safe_file(ROOT,f['path']);pep.need(pep.file_digest(p)==f['digest'],'package digest mismatch: '+f['path'])
        pep.need(p.stat().st_size==f['bytes'],'package size mismatch')
    actual=set()
    for p in ROOT.rglob('*'):
        pep.need(not p.is_symlink(),'package symlink forbidden')
        if p.is_file():
            rel=p.relative_to(ROOT).as_posix()
            if rel=='MANIFEST.json' or '__pycache__' in p.parts or '.local-runs' in p.parts:continue
            actual.add(rel)
    pep.need(actual==listed,'package inventory differs from manifest')
    out=[verify(p) for p in case_dirs()]
    pep.need((ROOT/'OPEN-ME.html').read_text()==gallery_text(),'gallery view drift')
    pep.check_package()
    return {'status':'CONSISTENT','files_checked':len(listed),'dossiers':out,'signature_status':'UNSIGNED'}

def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest='command',required=True)
    for cmd in ['render','verify']:
        q=sub.add_parser(cmd);q.add_argument('dossier',type=Path)
    sub.add_parser('render-all');sub.add_parser('verify-all');sub.add_parser('check-package')
    args=parser.parse_args()
    try:
        if args.command=='render':r=render(args.dossier)
        elif args.command=='verify':r=verify(args.dossier)
        elif args.command=='render-all':
            r=[render(p) for p in case_dirs()];write(ROOT/'OPEN-ME.html',gallery_text())
        elif args.command=='verify-all':r=[verify(p) for p in case_dirs()]
        else:r=verify_package()
        print(dumps(r),end='');return 0
    except (pep.ValidationError,OSError,KeyError,TypeError,ValueError,RecursionError) as exc:
        print(dumps({'status':'ERROR','message':str(exc)}),file=sys.stderr,end='');return 2

if __name__=='__main__':raise SystemExit(main())
