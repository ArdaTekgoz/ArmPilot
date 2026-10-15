"""Generate roadmap Markdown and optionally sync the ArmPilot part of a Sites checkout.

Canonical input: docs/arm-roadmap-r3.json. Does not publish or modify browser progress.
"""
import argparse
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
parser=argparse.ArgumentParser()
parser.add_argument('--site',type=Path,help='Existing Sites source checkout; only its ArmPilot plan is changed.')
args=parser.parse_args()
arm=json.loads((ROOT/'docs/arm-roadmap-r3.json').read_text(encoding='utf-8'))
tasks=arm['tasks']
assert len(tasks)==24 and sum(t['hours'] for t in tasks)==arm['totalHours']
md=['# ArmPilot R3 - Onaylı görev kartları','','15 Ekim 2026. Kullanıcı sekiz revizyonu ve web/PDF eşitlemesini onayladı. ARM-01 R2 tamamlandı; ARM-02 haftaya başlar.','',
 f'24 görev, {arm["totalHours"]} saat geçici ana kapsam; yazılım kapısı ARM-10’a kadar {sum(t["hours"] for t in tasks[:10])} saat. '+arm['estimateNote'],'',
 'Bu plan tamamlanmış uygulama kanıtı değildir. 4 saatlik haftalık kapasite korunur; her görev bir hafta demek değildir.','','## Aşama bütçeleri','','| Aşama | Saat |','| --- | ---: |']
md += [f'| {p["name"]} | {p["hours"]} |' for p in arm['phases']]
for t in tasks:
 md += ['',f'## {t["id"]} - {t["title"]}','',f'**Tahmin:** {t["hours"]} saat | **Ön koşul:** '+(', '.join(t['depends']) or 'Yok')+f' | **Donanım:** {"Gerekir" if t["hardware"] else "Gerekmez"}','',t['objective'],'','**Uygulama:**','']
 md += [f'{i}. {s}' for i,s in enumerate(t['steps'],1)]
 md += ['','**Kabul:**','']+[f'- [ ] {s}' for s in t['acceptance']]
 md += ['','**Kanıt:** '+t['evidence'],'','**Beceri:** '+t['learn'],'','**Takılırsan:** '+t['fallback']]
md += ['','## Kaynaklar','']+[f'- [{s["title"]}]({s["url"]})' for s in arm['sources']]
(ROOT/'docs/arm-gorevleri-r3.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
if args.site:
 path=args.site.resolve()/'dist/data.js'
 plan=json.loads(path.read_text(encoding='utf-8').split('=',1)[1].strip().rstrip(';'))
 assert sum(p['id']=='arm' for p in plan['projects'])==1
 plan['projects']=[arm if p['id']=='arm' else p for p in plan['projects']]
 path.write_text('window.PLAN = '+json.dumps(plan,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
print('Generated Markdown'+(' and synchronized ArmPilot site data.' if args.site else '.'))
