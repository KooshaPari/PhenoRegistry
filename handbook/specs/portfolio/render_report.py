from pathlib import Path
import runpy, re
from xml.sax.saxutils import escape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import letter
R=Path(__file__).resolve().parent
D=runpy.run_path(str(R/'build_audit.py'))
for var in ['RECORDS','FINDINGS','SOURCES','WORK','RELEASES','CHANGES','METHOD','SUMMARY','INTERPRETATION','ACCEPTANCE','ORDER']:
 globals()[var]=D[var]
FONT='/usr/share/fonts/truetype/dejavu/'
for name,file in [('DV','DejaVuSans.ttf'),('DVB','DejaVuSans-Bold.ttf'),('DVI','DejaVuSans-Oblique.ttf'),('DVM','DejaVuSansMono.ttf')]:
 pdfmetrics.registerFont(TTFont(name,FONT+file))
pdfmetrics.registerFontFamily('DV',normal='DV',bold='DVB',italic='DVI',boldItalic='DVB')
NAVY=colors.HexColor('#172B3A');TEAL=colors.HexColor('#145C61');GRAY=colors.HexColor('#516371');LIGHT=colors.HexColor('#EFF4F6')
styles={
 'title':ParagraphStyle('Title',fontName='DVB',fontSize=29,leading=34,textColor=NAVY,spaceAfter=18),
 'subtitle':ParagraphStyle('Subtitle',fontName='DV',fontSize=14,leading=20,textColor=GRAY,spaceAfter=14),
 'h1':ParagraphStyle('Heading1',fontName='DVB',fontSize=20,leading=25,textColor=NAVY,spaceAfter=13),
 'h2':ParagraphStyle('Heading2',fontName='DVB',fontSize=12.3,leading=16,textColor=TEAL,spaceBefore=10,spaceAfter=7),
 'body':ParagraphStyle('Body',fontName='DV',fontSize=10,leading=14.4,textColor=NAVY,spaceAfter=9),
 'card':ParagraphStyle('CardBody',fontName='DV',fontSize=10,leading=14,textColor=NAVY,spaceAfter=6),
 'small':ParagraphStyle('Small',fontName='DV',fontSize=8.0,leading=10.7,textColor=GRAY,spaceAfter=5),
 'tiny':ParagraphStyle('Tiny',fontName='DV',fontSize=7.2,leading=9.6,textColor=GRAY,spaceAfter=4),
 'cell':ParagraphStyle('Cell',fontName='DV',fontSize=8.5,leading=11.6,textColor=NAVY),
 'cellhead':ParagraphStyle('CellHead',fontName='DVB',fontSize=8.5,leading=11.6,textColor=colors.white),
 'call':ParagraphStyle('Call',fontName='DVB',fontSize=11,leading=15.4,textColor=TEAL,spaceAfter=8)
}
P=lambda text,style='body':Paragraph(escape(text).replace('\n','<br/>'),styles[style])
S=[]
def text(t,style='body'):
 for p in t.split('\n\n'):
  if p.strip():S.append(P(p,style))
def section(title,breakpage=True):
 if breakpage:S.append(PageBreak())
 S.append(P(title,'h1'))
def source_line(ids):
 links=[]
 for sid in ids:
  src=SOURCES[sid]
  links.append(f'<link href="{escape(src["url"], {chr(34):"&quot;"})}" color="#145C61">{sid}</link>')
 return Paragraph('Evidence: '+', '.join(links),styles['small'])
def table(headers,rows,widths):
 data=[[P(str(x),'cellhead') for x in headers]]+[[P(str(x),'cell') for x in row] for row in rows]
 t=Table(data,colWidths=widths,repeatRows=1,hAlign='LEFT')
 t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),NAVY),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,LIGHT]),('LINEBELOW',(0,0),(-1,0),0.6,NAVY)]))
 S.append(t);S.append(Spacer(1,10))

S.append(Spacer(1,24));S.append(P('PHENOTYPE\nPORTFOLIO EVALUATION','title'))
S.append(P('The 62-repository cohort\nand 30 active-named projects','subtitle'))
S.append(P('Read-only audit  |  September 15, 2026','call'))
S.append(Spacer(1,12))
text('The count is smaller. The remaining challenge is trustworthy ownership, verification and installed-product closure.','call')
text(SUMMARY)
table(['Opening observation','Closing observation'],[['62 repository IDs','61 currently listed IDs'],['30 unprefixed active candidates','29 unprefixed names; original cohort retained'],['0 platform-archived repositories','0 platform-archived repositories'],['Names are an organizational hint','Not lifecycle approval or evidence of preservation']], [264,264])
text('No repository mutation, product build, native installation or lifecycle certification was performed. Source facts, metadata observations, policy conflicts and proposed work are distinguished throughout.','small')

section('1 / Scope, limits and how to use this report')
text(METHOD)
text(INTERPRETATION)
text('Reading order: inventory changes; portfolio-level findings; release observations; the 30 active-candidate cards; the 32 retained/reference cards; acceptance and execution plan; source index. The adjacent Markdown/JSON/CSV are editable projections of the same records.','small')

section('2 / The denominator changed during the pass')
text('The opening census matched the request. A closing read returned one fewer accessible ID and multiple renamed categories. This report does not silently change the requested cohort or infer successful deletion from that difference.')
table(['Category by observed name','Opening','Closing'],[['Unprefixed active candidate',30,29],['Dependency',10,10],['Paused (non-reference)',11,4],['Paused reference',7,7],['Incubation-like name',0,7],['Target undecided',4,4],['Listed total',62,61]], [334,97,97])
table(['Stable ID','Opening name','Closing name'],[[c['repository_id'],c['opening_name'],c['closing_name'] or 'Not resolved'] for c in CHANGES],[95,216,217])
text('Refreshed VibeKanban, AGSLAG and SessionLedger README blobs still say pause/no development after the zz-inc renames. A new name is not an accepted scope/permission supersession. MobileMcp remains access-unresolved; other absent old URLs similarly do not prove deletion.','small')
S.append(source_line(['OBS-OPEN','OBS-CLOSE','S318','S319','S320','W01']))

section('3 / Portfolio-level findings')
for f in FINDINGS:
 block=[P(f"{f['id']}  {f['title']}",'h2'),P(f"{f['severity']}  |  {f['evidence_status']}",'small'),P(f['detail']),P('Impact: '+f['impact']),P('Next: '+f['next_action']),source_line(f['source_ids']),Spacer(1,7)]
 S.append(KeepTogether(block))

section('4 / Release presence is not CVP acceptance')
text('These are six sampled latest-release endpoint responses, not an exhaustive distribution-channel audit. Files were not downloaded, installed or run. A tag or auto-generated source archive is not the same artifact as a native app, CLI binary or deployable service.')
table(['Repository / release / date (UTC)','Observed attached assets','Acceptance gap'],[
 [x['repo']+' / '+x['tag']+'\n'+x['published_utc'][:10]+' ['+x['source']+']',x['assets'],x['gap']] for x in RELEASES],[145,175,208])
text('PhenoFabric latest-stable release endpoint returned 404. That is not evidence that no prerelease, package, local build or alternate channel exists. Those remain to be inspected by the owner.','small')

active_records=[r for r in RECORDS if r['opening_active_cohort']]
for idx,r in enumerate(active_records):
 if idx%2==0:
  section('5 / Active-candidate assessments' if idx==0 else '5 / Active candidates, continued')
  if idx==0:text('All original 30 unprefixed names remain in this section. AirLock transitioned to dependency status during the pass. Each card is an evidence-grounded next acceptance contract, not an assigned completion percentage.','small')
 card=[P(f"{idx+1:02d}  {r['opening_name']}",'h2'),P(f"ID {r['github_repository_id']}  |  {r['priority']}  |  {r['assessment']}",'small'),
       P('Role: '+r['role'],'card'),P('Observed: '+r['observed'],'card'),P('Next useful outcome: '+r['next_action'],'card'),
       P('Acceptance proof: '+r['acceptance'],'card'),P('Next comparison (not executed): '+r['comparison_next'],'small'),source_line(r['source_ids']),Spacer(1,10)]
 S.append(KeepTogether(card))

held_records=[r for r in RECORDS if not r['opening_active_cohort']]
for idx,r in enumerate(held_records):
 if idx%3==0:
  section('6 / Retained, held and reference repositories' if idx==0 else '6 / Retained scope, continued')
  if idx==0:text('32 original cohort entries. Their finish line is an explicit maintained dependency, accepted incubation, deliberate hold or verified custody state—not a universal requirement to ship a new application.','small')
 closing='; closing: '+str(r['closing_name'] or 'ACCESS UNRESOLVED') if r['opening_name']!=r['closing_name'] else ''
 card=[P(f"{idx+1:02d}  {r['opening_name']}",'h2'),P(f"ID {r['github_repository_id']}  |  {r['priority']}{closing}",'small'),P(r['assessment'],'call'),
       P('Observed: '+r['observed'],'card'),P('Next: '+r['next_action'],'card'),P('Acceptance: '+r['acceptance'],'card'),source_line(r['source_ids']),Spacer(1,6)]
 S.append(KeepTogether(card))

section('7 / The acceptance contract still applies')
text(ACCEPTANCE)
section('8 / Convert current work into installed outcomes')
text(ORDER)
text('Do not translate this into a one-agent-per-repository rule. Several workers may contribute to one product through bounded capability slices. Shared destination manifests, lockfiles, migrations and releases need an integration owner and non-overlapping or coordinated writes.','call')

section('9 / Proposed next work; not new permissions')
text('These are bounded proposed packages for existing owners. Only WP07 has an explicit hard dependency on WP02. Priority, shared-resource exclusion and work-in-progress admission are separate from technical dependencies. No speculative calendar or effort totals are presented.','small')
for w in WORK:
 S.append(KeepTogether([P(f"{w['id']}  {w['title']}",'h2'),P('Owner: '+w['owner_role'],'small'),P('Scope: '+w['scope']),P('Acceptance: '+w['acceptance']),P('Hard prerequisites: '+(', '.join(w['hard_dependencies']) or 'None specified beyond local preflight/authority')+'  |  Findings: '+', '.join(w['finding_ids']),'small'),Spacer(1,6)]))

section('10 / Source index and reproducibility')
text('Each evidence label links to the inspected source location. Metadata and selected file hashes are preserved in evidence/sources.json. Raw connector responses and complete repository trees are not included. Branch names may advance; use the captured blob/commit or re-resolve the current head when executing. Official docs explain platform/tool behavior, not the state of your private machines.','small')
for sid,s in SOURCES.items():
 title=(s.get('observed_repository','')+' / '+s.get('path','')).strip(' /') or s['kind']
 url=escape(s['url'],{chr(34):'&quot;'})
 item_title=Paragraph(f'<b>{sid}</b> · <link href="{url}" color="#145C61">{escape(title)}</link>',styles['small'])
 ident=''
 if s.get('ref'):ident+='ref: '+str(s['ref'])+'; '
 if s.get('blob_sha'):ident+='blob: '+s['blob_sha']+'; '
 S.append(KeepTogether([item_title,P(ident+s.get('coverage',''),'tiny')]))

class Report(SimpleDocTemplate):
 def afterFlowable(self,flowable):
  if isinstance(flowable,Paragraph) and flowable.style.name=='Heading1':
   text=flowable.getPlainText();key='s'+str(self.page)+'-'+re.sub('[^a-zA-Z0-9]','',text)[:40]
   self.canv.bookmarkPage(key);self.canv.addOutlineEntry(text,key,level=0,closed=False)

def page(c,d):
 w,h=letter;c.saveState()
 if d.page>1:
  c.setFont('DVB',8);c.setFillColor(TEAL);c.drawString(42,h-25,'PHENOTYPE  /  PORTFOLIO 62-ID COHORT')
  c.setStrokeColor(colors.HexColor('#CCD7DD'));c.setLineWidth(.5);c.line(42,h-31,w-42,h-31)
 c.setFont('DV',7.4);c.setFillColor(GRAY)
 c.drawString(42,23,'September 15, 2026  |  Read-only, bounded evaluation  |  No lifecycle approval')
 c.drawRightString(w-42,23,str(d.page));c.restoreState()
path=R/'report/PORTFOLIO-EVALUATION.pdf'
doc=Report(str(path),pagesize=letter,rightMargin=42,leftMargin=42,topMargin=46,bottomMargin=40,title='Phenotype Portfolio Evaluation — 62-ID Cohort / 30 Active Candidates',author='Portfolio audit',subject='Evidence-grounded repository evaluation, CVP acceptance and post-consolidation risks')
doc.build(S,onFirstPage=page,onLaterPages=page)
print(path)
