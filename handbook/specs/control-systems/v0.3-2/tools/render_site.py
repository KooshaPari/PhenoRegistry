#!/usr/bin/env python3
"""Build REPORT.md and an offline HTML reader; optional dependency: markdown-it-py."""
from pathlib import Path
from html import escape
import re
import json
try:
    from markdown_it import MarkdownIt
except ImportError:
    raise SystemExit('Optional renderer dependency missing: install markdown-it-py in a development environment, or use the already-built HTML.')
ROOT=Path(__file__).resolve().parents[1]

def main():
    records=json.loads((ROOT/'machine/docset.json').read_text(encoding='utf-8'))
    sources=json.loads((ROOT/'machine/sources.json').read_text(encoding='utf-8'))['sources']
    first=[Path('docs/25-cross-system-control-plane.md'),Path('docs/20-local-cloud-and-qualified-node-compute.md'),Path('docs/21-human-agent-automation-interface-tenet.md'),Path('docs/22-assessment-dossier-convergence.md'),Path('docs/23-emergent-garden-status-and-restart.md'),Path('docs/24-review-broker-and-history-reconciliation.md'),Path('docs/26-reference-landscape-and-alternatives.md'),Path('docs/16-full-session-reconciliation.md'),Path('docs/17-lifecycle-and-delivery-profiles.md'),Path('docs/18-api-and-service-binding-contract.md'),Path('docs/19-pilot-repair-and-negative-tests.md')]
    chapters=[Path('README.md'),Path('STATUS.md'),Path('CHANGELOG.md')]+first+[p.relative_to(ROOT) for p in sorted((ROOT/'docs').glob('*.md')) if p.relative_to(ROOT) not in first]+[p.relative_to(ROOT) for p in sorted((ROOT/'adrs').glob('*.md'))]+[Path('evidence/validation.md')]
    # Keep evidence register available, but place it after the design for readable flow.
    reg=Path('docs/03-research-register.md');chapters.remove(reg);chapters.insert(-1,reg)
    md=MarkdownIt('commonmark',{'html':False}).enable('table')
    mapping={str(p):f'chapter-{i:02}' for i,p in enumerate(chapters)}
    nav=[];body=[];report=['# Phenotype deployment & runtime control — consolidated report\n\nVersion 0.3 · Audited design baseline, not production approval.\n']
    for i,p in enumerate(chapters):
        text=(ROOT/p).read_text(encoding='utf-8')
        title=next((x.lstrip('# ').strip() for x in text.splitlines() if x.startswith('# ')),str(p))
        anchor=mapping[str(p)]
        def relink(m):
            label,target=m.group(1),m.group(2)
            if target.startswith(('http:','https:','mailto:','#')):return m.group(0)
            resolved=(ROOT/p.parent/target).resolve()
            try:key=str(resolved.relative_to(ROOT.resolve()))
            except ValueError:return m.group(0)
            if key in mapping:return f'[{label}](#{mapping[key]})'
            if key=='REPORT.md' or key=='site/index.html':return f'[{label}](#chapter-00)'
            return f'[{label}](../{key})'
        html=md.render(re.sub(r'\[([^\]]+)\]\(([^)]+)\)',relink,text))
        # Source identifiers become in-document anchors; no external assets are required.
        if p==reg:
            html=re.sub(r'<h2>(S\d{3}) ',r'<h2 id="\1">\1 ',html)
        html=re.sub(r'(?<![\w"#=/])(S\d{3})(?![\w"=])',r'<a class="source-ref" href="#\1">\1</a>',html)
        nav.append(f'<a href="#{anchor}" data-title="{escape(title.lower())}"><span>{i+1:02}</span>{escape(title)}</a>')
        body.append(f'<section id="{anchor}" class="chapter"><div class="eyebrow">{escape(str(p))}</div>{html}</section>')
        # Adjust ordinary relative Markdown links when merging nested chapter documents.
        def report_link(m):
            label,target=m.group(1),m.group(2)
            if target.startswith(('http:','https:','mailto:','#')):return m.group(0)
            try:key=str((ROOT/p.parent/target).resolve().relative_to(ROOT.resolve()))
            except ValueError:return m.group(0)
            return f'[{label}]({key})'
        report.append('\n---\n\n'+re.sub(r'\[([^\]]+)\]\(([^)]+)\)',report_link,text))
    (ROOT/'REPORT.md').write_text('\n'.join(report),encoding='utf-8')
    css="""
:root{--ink:#162b30;--muted:#5f7176;--line:#d9e4e5;--paper:#f4f7f6;--accent:#176b70;--nav:#102c33;--card:#fff;--warning:#fbf0d7}*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:24px}body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.65 system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}aside{position:fixed;inset:0 auto 0 0;width:292px;background:var(--nav);color:#dcebec;padding:28px 20px;overflow-y:auto}aside .brand{font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:#a8c8c8}aside h1{font-size:25px;line-height:1.18;font-weight:650;margin:10px 0 18px}aside .badge{display:inline-block;border:1px solid #577c7f;border-radius:20px;padding:4px 10px;font-size:12px;margin-bottom:24px}aside input{width:100%;background:#1b3a42;border:1px solid #45636a;border-radius:7px;padding:10px;color:white;font:inherit;font-size:13px}aside input::placeholder{color:#b4c8cc}nav{margin-top:16px;display:grid;gap:3px}nav a{display:flex;gap:10px;color:#dcebec;text-decoration:none;font-size:12px;line-height:1.4;padding:8px;border-radius:5px}nav a:hover,nav a:focus{background:#254b53;color:white}nav a span{color:#8bbab8;font-variant-numeric:tabular-nums;flex:0 0 21px}main{margin-left:292px;padding:38px clamp(22px,4vw,74px);max-width:1560px}.masthead{max-width:1060px;margin-bottom:30px}.masthead .kicker{color:var(--accent);font-size:12px;font-weight:750;letter-spacing:.16em;text-transform:uppercase}.masthead h1{font-size:clamp(34px,4.2vw,60px);line-height:1.08;letter-spacing:-.045em;max-width:900px;margin:14px 0 20px}.masthead p{font-size:19px;line-height:1.5;color:var(--muted);max-width:860px}.stats{display:flex;gap:12px;flex-wrap:wrap;margin:26px 0}.stat{background:white;border:1px solid var(--line);padding:14px 20px;border-radius:9px;min-width:130px}.stat strong{display:block;font-size:28px;line-height:1.1;font-weight:650;color:var(--accent)}.stat small{font-size:12px;color:var(--muted)}.notice{background:var(--warning);border-left:4px solid #a77e24;border-radius:5px;padding:15px 18px;font-size:14px}.chapter{overflow-wrap:anywhere;max-width:1060px;margin:0 0 30px;padding:30px clamp(20px,3vw,44px) 40px;background:var(--card);border:1px solid var(--line);border-radius:11px;box-shadow:0 3px 16px #102c3304}.eyebrow{font:11px/1.4 ui-monospace,monospace;color:var(--muted);letter-spacing:.05em;margin-bottom:10px;overflow-wrap:anywhere}.chapter h1{font-size:31px;line-height:1.2;letter-spacing:-.025em;margin:8px 0 25px}.chapter h2{font-size:22px;line-height:1.35;margin:30px 0 12px;letter-spacing:-.015em}.chapter h3{font-size:18px;margin:25px 0 10px}.chapter p{margin:10px 0 16px}.chapter a{color:var(--accent);text-underline-offset:3px}.chapter a.source-ref{font:11px ui-monospace,monospace;background:#edf5f4;padding:2px 4px;border-radius:4px;text-decoration:none;white-space:nowrap}.chapter table{border-collapse:collapse;width:100%;margin:20px 0;font-size:13px;line-height:1.5;table-layout:auto}.chapter th,.chapter td{border:1px solid var(--line);padding:10px;vertical-align:top;text-align:left;overflow-wrap:anywhere}.chapter th{background:#ecf3f2;font-weight:650}.chapter tbody tr:nth-child(even){background:#fafcfb}.chapter pre{padding:18px;background:#102c33;color:#dcebec;border-radius:7px;overflow:auto;font-size:12px;line-height:1.65;max-width:100%}.chapter code{font-family:ui-monospace,SFMono-Regular,Consolas,monospace;font-size:.87em;overflow-wrap:anywhere}.chapter pre code{font-size:1em;white-space:pre}.chapter ul,.chapter ol{padding-left:24px}.chapter li{margin-bottom:6px}.chapter hr{border:none;border-top:1px solid var(--line);margin:30px 0}footer{color:var(--muted);font-size:12px;margin:30px 0}a:focus-visible,input:focus-visible{outline:3px solid #71bab3;outline-offset:3px}@media(max-width:980px){aside{position:relative;width:auto;max-height:400px;padding:22px}aside h1{font-size:23px}nav{grid-template-columns:repeat(2,minmax(0,1fr))}main{margin-left:0;padding:24px 15px}.chapter{padding:24px 19px}.chapter table{font-size:12px}.chapter th,.chapter td{padding:7px}.masthead h1{font-size:38px}}@media print{aside,.masthead .stats{display:none}body{background:white;font-size:10pt}main{margin:0;padding:0;max-width:none}.chapter{border:0;padding:0;box-shadow:none;break-before:page}.chapter h1{font-size:22pt}.chapter h2{break-after:avoid;font-size:15pt}.chapter table{font-size:8pt}.chapter tr{break-inside:avoid}.chapter pre{white-space:pre-wrap;color:black;background:#f5f5f5}.chapter pre code{white-space:pre-wrap}.masthead h1{font-size:30pt}.notice{background:none;border:1px solid #777}a{color:inherit}}
"""
    page='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Phenotype — Control Systems v0.3</title><meta name="description" content="Evidence-qualified deployment design, runtime selection, approval contract and agent handoff."><style>'+css+'</style></head><body><aside><div class="brand">Phenotype / Engineering</div><h1>Control systems<br>integration</h1><div class="badge">v0.3 · integration baseline</div><label for="filter" style="font-size:12px;display:block;margin-bottom:5px">Find a chapter</label><input id="filter" placeholder="Runtime, approval, evidence…" type="search"><nav>'+''.join(nav)+'</nav></aside><main><header class="masthead"><div class="kicker">Audit · Research · Formalization</div><h1>Four coupled control systems.<br>Not four new products.</h1><p>Evidence-qualified convergence for local cloud lifecycle, assessment dossiers, research corpus continuation and quota-aware review control.</p><div class="stats"><div class="stat"><strong>__FINDINGS__</strong><small>audit findings</small></div><div class="stat"><strong>__REQUIREMENTS__</strong><small>linked requirements</small></div><div class="stat"><strong>__DECISIONS__</strong><small>decision records</small></div><div class="stat"><strong>__SOURCES__</strong><small>source records</small></div></div><div class="notice"><strong>Not production approval.</strong> Validation is limited to the package and its reference functions. All __TESTS__ target-environment acceptance tests remain unrun. No repository, host, cloud or ingress changes were made.</div></header>'+''.join(body)+'<footer>September 12, 2026 · America/Los_Angeles · Internal working document. Original source evidence requires redaction review before publication.</footer></main><script>document.getElementById("filter").addEventListener("input",function(){const q=this.value.trim().toLowerCase();document.querySelectorAll("nav a").forEach(a=>{a.style.display=a.dataset.title.includes(q)?"flex":"none";});});</script></body></html>'
    for key,value in {'FINDINGS':len(records['findings']),'REQUIREMENTS':len(records['requirements']),'DECISIONS':len(records['decisions']),'SOURCES':len(sources),'TESTS':len(records['acceptance_tests'])}.items():
        page=page.replace('__'+key+'__',str(value))
    (ROOT/'site/index.html').write_text(page,encoding='utf-8')
    print(f'Rendered {len(chapters)} chapters to REPORT.md and site/index.html')
if __name__=='__main__':main()
