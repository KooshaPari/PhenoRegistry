"""Validate this dated audit package, not GitHub or any product's acceptance.

The fixed cohort counts belong only to this snapshot. This is not a live
portfolio controller, approval engine, coverage instrument, or deletion tool.
"""
from pathlib import Path
import csv, hashlib, json, re
import sys
from graphlib import TopologicalSorter
ROOT=Path(__file__).resolve().parents[1]
results=[]
def check(name,condition):
 results.append({'check':name,'passed':bool(condition)})
 if not condition:raise AssertionError(name)
def read(p):return json.loads((ROOT/p).read_text())
for p in ROOT.rglob('*.json'):
 if p.name not in ['validation-results.json']:json.loads(p.read_text())
check('all included JSON parses',True)
data=read('records/repository-assessments.json');rows=data['repositories']
check('original snapshot cohort remains 62 unique stable IDs',len(rows)==62==len({r['github_repository_id'] for r in rows}))
check('original active-named cohort remains 30',sum(r['opening_active_cohort'] for r in rows)==30)
close=read('records/closing-inventory.json')
check('closing snapshot has 61 IDs, not a fabricated replacement',len(close)==61 and {x['id'] for x in close}<={r['github_repository_id'] for r in rows})
check('closing snapshot has 29 unprefixed candidates',sum(x['classification_by_name']=='active-named' for x in close)==29)
check('all 62 rows have substantive next-action and acceptance text',all(len(r['next_action'])>40 and len(r['acceptance'])>50 for r in rows))
sources=read('evidence/sources.json');sid={s['id'] for s in sources}
check('source IDs unique',len(sid)==len(sources))
check('repository citations resolve within source registry',all(set(r['source_ids'])<=sid for r in rows))
check('captured blob IDs have valid syntax',all(not s.get('blob_sha') or re.fullmatch(r'[a-f0-9]{40}',s['blob_sha']) for s in sources))
findings=read('records/findings.json');fid={f['id'] for f in findings}
check('findings unique and source-linked',len(fid)==len(findings) and all(set(f['source_ids'])<=sid for f in findings))
work=read('records/next-work.json');wid={w['id'] for w in work}
check('work packages unique, dependencies and findings resolve',len(wid)==len(work) and all(set(w['hard_dependencies'])<=wid and set(w['finding_ids'])<=fid for w in work))
list(TopologicalSorter({w['id']:set(w['hard_dependencies']) for w in work}).static_order())
check('proposed hard-dependency graph is acyclic',True)
check('work is explicitly proposed and grants no new write authority',all(w['status']=='PROPOSED_NOT_CLAIMED' and 'requires existing' in w['write_authority'] for w in work))
changes=read('records/identity-changes.json')
check('nine identity/access changes preserved without inferred permission',len(changes)==9 and all(c['authorization_verified'] is False for c in changes))
check('MobileMcp remains unresolved, not deleted',any(r['github_repository_id']==1273002818 and r['closing_class']=='access-unresolved' for r in rows))
with (ROOT/'records/repository-assessments.csv').open(newline='') as f:csv_rows=list(csv.DictReader(f))
check('CSV projects exactly the same 62 IDs',len(csv_rows)==62 and {int(r['github_repository_id']) for r in csv_rows}=={r['github_repository_id'] for r in rows})
check('audit limitations do not claim product execution or certification',data['coverage']['native_product_tests_run'] is False and data['coverage']['cvps_certified']==0 and data['coverage']['writes_to_github'] is False)
import fitz
pdf=fitz.open(ROOT/'report/PORTFOLIO-EVALUATION.pdf')
texts=[p.get_text() for p in pdf];alltext='\n'.join(texts)
check('PDF contains every original repository and stable ID',all(r['opening_name'] in alltext and str(r['github_repository_id']) in alltext for r in rows))
check('PDF has no text replacement glyphs','\ufffd' not in alltext)
rects=[]
for i,p in enumerate(pdf):
 for b in p.get_text('blocks'):
  if b[0]<35 or b[2]>580 or b[1]<8 or b[3]>778:rects.append(i+1)
check('PDF text bounds stay within page',not rects)
check('no distributed font files',not any(p.suffix.lower() in ('.ttf','.otf','.woff','.woff2') for p in ROOT.rglob('*') if p.is_file()))
check('no HTML dashboard generated',not any(ROOT.rglob('*.html')))
output={'scope':'artifact consistency only; no product test, native installation, runtime coverage or approval authenticated',
        'checks':results,'passed':sum(r['passed'] for r in results),'failed':sum(not r['passed'] for r in results),'pdf_pages':len(pdf)}
(ROOT/'checks/validation-results.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({'passed':output['passed'],'failed':output['failed'],'pdf_pages':len(pdf)},indent=2))
