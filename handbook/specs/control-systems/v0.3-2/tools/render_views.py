#!/usr/bin/env python3
"""Regenerate the structured Markdown views from this package's machine records."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
def emit(path,text):
    (ROOT/path).write_text(text.strip()+'\n',encoding='utf-8')
def main():
    data=json.loads((ROOT/'machine/docset.json').read_text(encoding='utf-8'))
    sources=json.loads((ROOT/'machine/sources.json').read_text(encoding='utf-8'))['sources']
    emit('docs/02-audit-findings.md','# Audit findings\n\nP0 blocks closure; it does not establish a production vulnerability. P1 requires qualification before adoption; P2 concerns decision quality.\n\n'+'\n\n'.join(f"## {f['id']} — {f['title']}\n\n**{f['priority']} · {f['verdict']}**\n\n{f['detail']}\n\n**Closure evidence:** {f['closure']}\n\nSources: {', '.join(f['source_ids'])}." for f in data['findings']))
    emit('docs/03-research-register.md','# Source and research register\n\nRepository declarations are not implementation proof; external documentation is not local compatibility evidence. Sources retain explicit limits.\n\n'+'\n\n'.join(f"## {s['id']} — {s['title']}\n\n**Class:** {s['kind']}  \n**Locator:** `{s['locator']}`\n\n"+'\n'.join('- '+c for c in s['claims_supported'])+f"\n\n**Limit:** {s['limitations']}" for s in sources))
    emit('docs/04-functional-requirements.md','# Functional requirements\n\nAll FRs are proposed derived requirements; operational tests have not run. CON-001 through CON-005 separately preserve direct user constraints.\n\n'+'\n\n'.join(f"## {r['id']} — {r['title']}\n\n{r['statement']}\n\n**Owner role:** {r['owner_role']}  \n**Acceptance:** {', '.join(r['acceptance_test_ids'])}  \n**Motivation:** {', '.join(r['finding_ids'])}; sources {', '.join(r['source_ids'])}." for r in data['requirements']))
    emit('docs/11-acceptance-tests.md','# Operational acceptance test catalog\n\nNone of these tests has been run against the user environment. Passing package validation is not passing these tests. Run disruptive cases only on authorized disposable targets. Each result requires pinned inputs, complete relevant output, timestamps and verifier identity.\n\n'+'\n\n'.join(f"## {t['id']} — {t['title']}\n\n**Status:** {t['status']}. **Requirement:** {', '.join(t['requirement_ids'])}.\n\n"+'\n'.join(f'{i+1}. {s}' for i,s in enumerate(t['procedure']))+f"\n\n**Expected:** {t['expected']}\n\n**Evidence required:** "+'; '.join(t['evidence_required']) for t in data['acceptance_tests']))
    for d in data['decisions']:
        emit('adrs/'+d['id']+'.md',f"# {d['id']} — {d['title']}\n\n**Status:** {d['status']}\n\n## Decision\n\n{d['decision']}\n\n## Alternatives tested conceptually\n\n"+'\n'.join('- '+x for x in d['alternatives'])+f"\n\n## Revisit / closure\n\n{d['revisit']}\n\nSources: {', '.join(d['source_ids'])}.\n\nThis record does not authorize mutation. ADR-DEP-001 and ADR-DEP-014 record stated user constraints.")
    print('Regenerated findings, sources, requirements, acceptance-test views and ADRs.')
if __name__=='__main__':main()
