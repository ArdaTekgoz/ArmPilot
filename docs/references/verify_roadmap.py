"""Validate documentation consistency; does not run robot software or change progress."""
import argparse
import json
import subprocess
from pathlib import Path
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[2]
parser=argparse.ArgumentParser()
parser.add_argument('--site',type=Path,help='Optional existing Sites checkout for source/PDF and other-project comparison.')
args=parser.parse_args()
arm=json.loads((ROOT/'docs/arm-roadmap-r3.json').read_text(encoding='utf-8'))
tasks=arm['tasks']
assert [t['id'] for t in tasks]==[f'ARM-{i:02}' for i in range(1,25)]
seen=set()
for t in tasks:
 assert set(t['depends'])<=seen,(t['id'],t['depends'])
 assert t['acceptance'] and t['steps'] and t['evidence']
 seen.add(t['id'])
assert sum(t['hours'] for t in tasks)==sum(p['hours'] for p in arm['phases'])==arm['totalHours']==242
assert 'ARM-09' in tasks[9]['depends'] and 'ARM-14' not in tasks[9]['depends']
md=(ROOT/'docs/arm-gorevleri-r3.md').read_text(encoding='utf-8')
pdf=ROOT/'output/pdf/arm-rapor-r3.pdf'
pages=PdfReader(pdf).pages
assert len(pages)==28
for i,t in enumerate(tasks,3):
 text=pages[i].extract_text()
 assert t['id'] in text and 'Tamamlanma ölçütleri' in text
 assert t['title'] in md and all(a in md for a in t['acceptance'])
if args.site:
 site=args.site.resolve()
 parse=lambda s:json.loads(s.split('=',1)[1].strip().rstrip(';'))
 plan=parse((site/'dist/data.js').read_text(encoding='utf-8'))
 original_sha='e33880af128cd6800e24e7312301dd403d45b38c'
 before=parse(subprocess.check_output(['git','show',original_sha+':dist/data.js'],cwd=site).decode('utf-8'))
 assert next(p for p in plan['projects'] if p['id']=='arm')==arm
 for a,b in zip(before['projects'],plan['projects']):
  if a['id']!='arm':assert a==b,a['id']
 for name in ['amr','automation']:
  original=subprocess.check_output(['git','show',original_sha+f':dist/reports/{name}-rapor.pdf'],cwd=site)
  assert original==(site/f'dist/reports/{name}-rapor.pdf').read_bytes()
 assert pdf.read_bytes()==(site/'dist/reports/arm-rapor.pdf').read_bytes()
print('PASS: 24 tasks, dependency DAG, 242h, early mock gate, Markdown and 28 PDF pages'+('; site parity and unchanged other projects/reports.' if args.site else '.'))
