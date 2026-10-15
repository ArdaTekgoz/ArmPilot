"""Render the approved R3 planning source. Documentation tooling, not robot code."""
import json
from html import escape
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak

ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads((ROOT/'docs/arm-roadmap-r3.json').read_text(encoding='utf-8'))
OUT = ROOT/'output/pdf/arm-rapor-r3.pdf'
pdfmetrics.registerFont(TTFont('Segoe', 'C:/Windows/Fonts/segoeui.ttf'))
pdfmetrics.registerFont(TTFont('SegoeBold', 'C:/Windows/Fonts/segoeuib.ttf'))
pdfmetrics.registerFontFamily('Segoe', normal='Segoe', bold='SegoeBold')
ink = colors.HexColor('#163b3c')
gold = colors.HexColor('#946726')
muted = colors.HexColor('#586b70')
body = ParagraphStyle('body', fontName='Segoe', fontSize=10, leading=14.5, textColor=ink, spaceAfter=7)
small = ParagraphStyle('small', parent=body, fontSize=8.8, leading=12)
title = ParagraphStyle('title', parent=body, fontName='SegoeBold', fontSize=27, leading=32, spaceAfter=16)
h1 = ParagraphStyle('h1', parent=title, fontSize=19, leading=24, spaceAfter=12)
h2 = ParagraphStyle('h2', parent=body, fontName='SegoeBold', fontSize=11, leading=15, textColor=gold, spaceBefore=9, spaceAfter=6)
eyebrow = ParagraphStyle('eyebrow', parent=small, fontName='SegoeBold', textColor=gold, spaceAfter=10)
story=[]

def clean(s):
    return str(s).replace('—','-').replace('–','-').replace('\u2011','-')
def p(s, style=body):
    return Paragraph(escape(clean(s)), style)
def add(s, style=body):
    story.append(p(s,style))
def heading(s): add(s,h2)
def bullets(items, numbered=False):
    for i,s in enumerate(items,1):
        add((f'{i}. ' if numbered else '• ')+s)
def table(rows, widths, header=True):
    tb=Table([[p(v,small) for v in row] for row in rows], colWidths=widths, hAlign='LEFT')
    styles=[('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),('LINEBELOW',(0,0),(-1,-1),.35,colors.HexColor('#dce5e2'))]
    if header: styles += [('BACKGROUND',(0,0),(-1,0),colors.HexColor('#eef3ed'))]
    tb.setStyle(TableStyle(styles));story.append(tb)
def page(): story.append(PageBreak())

add('ARMPILOT / PROJE RAPORU VE YOL HARİTASI',eyebrow)
add('Altı eksenli kol için\nmasaüstü kontrol uygulaması',title)
add('R3 • 15 Ekim 2026 • Kullanıcı onaylı plan revizyonu',h2)
add('Proje sahibi: Arda TEKGÖZ. Amaç: projeyi yaparken robotik, yazılım ve sistem doğrulama yetkinliklerini öğrenmek. Bu rapor planı ve bugün gerçekten tamamlanan belge çalışmasını ayırır.')
heading('Ürün sözleşmesi')
add(DATA['vision'])
bullets(DATA['scope'][1:])
heading('Sürüm sınırları')
bullets(DATA['definitionOfDone'][:3])
heading('Bugünkü durum')
add('ARM-01 R2 belge aşaması tamamlandı (Git: 65142f1). Kapsam sözleşmesi, CAD montaj görüntüsü, kaynaklı AI eklem şeması ve katkı kaydı var. Kullanıcının aktif çalışma tahmini 3 saat; ölçülmüş süre değildir. Çalışır uygulama, fiziksel kol ve ölçüm sonucu henüz yok. ARM-02 haftaya başlayacak.')
add('Başlangıçtaki 3 eklem / yalnız XYZ planı ile 138 saat tahmini tarihsel kaynaktır. Bu R3 planı onların yerini alır; kullanıcının eski PDF’i arşiv olarak korunur.',small)
page()

add('PLAN / KAPASİTE VE BAĞIMLILIKLAR',eyebrow)
add('24 görev, geçici 242 saat',h1)
add(DATA['estimateNote'])
table([['Aşama','Görevler','Saat']]+[[ph['name'],ph['taskIds'][0]+' - '+ph['taskIds'][-1],str(ph['hours'])] for ph in DATA['phases']], [84*mm,62*mm,20*mm])
heading('Takvim varsayımı')
add('ArmPilot haftada 4 saat: 242 saat yaklaşık 61 haftalık nominal kapasitedir. %25 payla yaklaşık 76 hafta senaryosu oluşur. Bunlar öğrenme hızı, tedarik ve yeniden çalışma bilinmeden verilen takvim taahhütleri değildir. ARM-10’a kadar geçici yazılım bütçesi 112 saattir. ARM-01’in 4 saat tahmini ile gerçekleşen 3 saat kaydı ayrı tutulur.')
heading('Kapılar ve kritik sıra')
bullets(['ARM-01 → ARM-02 (A/B alt oturumları) → ARM-03–06 (kendi model/kinematik) → ARM-07–09 (kendi arayüz + plan + mock) → ARM-10 v0.1.',
 'ARM-11 yük/bütçe kararı → ARM-12 CAD/baskı ve ARM-13 güç/protokol tasarımı. ARM-12 ile ARM-13 bağımsız ilerleyebilir.',
 'ARM-09 + ARM-13 → ARM-14 gerçek protokol emülatörü. ARM-12 + ARM-14 → ARM-15–16 tek eklem kapısı → ARM-17–18 tüm kol/model ve kalibrasyon.',
 'ARM-10 + ARM-14 + ARM-18 → ARM-19 gerçek yürütme → ARM-20 ölçüm → ARM-21 iyileştirme → ARM-22–24 rapor/demo/v1.0 kapanışı.'])
add('Her kartın ön koşulu ayrıca yazılıdır. Görev kodları korunmuştur; ARM-09’daki erken mock denemesi ARM-14’ü beklemez. Donanım beklenirken bağımsız iş yapılabilir, fiziksel kabul kutusu kapatılamaz.',small)
page()

add('MİMARİ / ÖĞRENME VE SINIRLAR',eyebrow)
add('Kendi uygulaman, doğrulanan altyapı',h1)
table([['Katman','Sorumluluk'],['ArmPilot','Kendi masaüstü penceren, 3B görünüm, XYZ+yönelim, durum ve Planla / Önizle / Yürüt akışı.'],['ROS 2 + MoveIt 2','Robot modeli/SRDF, IK, sabit planlama sahnesi, yol ve zamanlı yörünge. OS/dağıtım/sürüm seçimi ARM-02’de.'],['Kontrolcü + köprü','FollowJointTrajectory → ros2_control donanım arayüzü veya gerekçeli eşdeğer → STM32 → altı sürücü. Hazır uyum varsayılmaz.'],['Durum geri dönüşü','joint_states ve eylem sonucu. Ölçülen, komutlanan ve tahmin edilen alanlar görünür biçimde ayrılır.'],['RViz','Geliştirme karşılaştırması; ArmPilot’un kendi ürün penceresinin yerine geçmez.']], [43*mm,123*mm])
heading('Arda’nın uygulayacağı öğrenme çekirdeği')
add('Birim dönüşümleri, 2R FK/analitik IK ve tek eklem kübik zaman ölçekleme küçük kişisel örneklerdir. Altı eksenli ürün çözücüsü ve planlayıcı kütüphanesi kullanılabilir. AI doküman/iskelet/açıklama/hata incelemesi sağlar; Arda’nın yazmadığı kod veya CAD onun özgün katkısı diye sunulmaz.')
heading('Henüz doğrulanmamış tasarım varsayımları')
add('WE-R2.4 hazır baskı adayı; yaklaşık 400 mm flanş erişimi. Aday görev kutusu: X150–250, Y−100–100, Z150–250 mm; her yönelim için erişim garantisi yok. Toplam harici uç kütlesi 100 g (takım+nesne), ağırlık merkezi yaklaşık 30 mm. İlk profil 5°/s ve 10°/s²; tek eklem ilk denemeleri yaklaşık 1°/s. ARM-03/11/20’de gözden geçirilecek. Bunlar üretici kapasitesi veya ölçülmüş sonuç değildir.')
heading('Sonraki sürüm listesi')
bullets(DATA['outOfScope'][:3])
page()

for t in DATA['tasks']:
    add('ARMPILOT R3 / '+t['id'],eyebrow)
    add(t['title'],h1)
    add(t['phase']+f' • {t["hours"]} saat geçici tahmin • '+('Donanım gerekir' if t['hardware'] else 'Donanım gerekmez'),small)
    add('Ön koşul: '+(', '.join(t['depends']) or 'Yok'),small)
    heading('Amaç')
    add(t['objective'])
    heading('Uygulama adımları')
    bullets(t['steps'],True)
    heading('Tamamlanma ölçütleri')
    bullets(t['acceptance'])
    heading('Kanıt ve öğrenme')
    add('Kanıt: '+t['evidence'])
    add('Beceri: '+t['learn'])
    heading('Takılırsan / donanım bekliyorsan')
    add(t['fallback'],small)
    page()

add('R3 / KARAR VE KAYNAK KAYDI',eyebrow)
add('Onaylanan sekiz düzeltme',h1)
bullets(['ARM-02 iki alt oturum: Python/birim disiplini ve ROS/MoveIt ortam denemesi.',
 'ARM-03–06 kendi WE-R2.4 geometrisi, altı eklem/TCP, URDF/SRDF ve planlama yapılandırması.',
 'ARM-07 kendi masaüstü 3B görünümünün açık teslimatı.',
 'ARM-08 XYZ+yönelim, simülasyon/fiziksel mod ve Planla / Önizle / Yürüt durumları.',
 'ARM-09 sabit modellenmiş sahnede planlama ve zamanlı yörünge; kişisel kübik örneği ayrı.',
 'ARM-09’da erken mock kontrolcü; ARM-14’te gerçek protokol hata testleri; v0.1 öncesi bağımlılık döngüsü kaldırıldı.',
 'ARM-13–20 somut altı eklemli donanım köprüsü, durum kaynağı, kalibrasyon ve konum/yönelim ölçümü.',
 'Tahmin/ön koşul yenileme; repo, bu PDF ve web kartlarının aynı R3 verisiyle eşleştirilmesi.'],True)
heading('Katkı ve revizyon durumu')
add('Kullanıcı ürün hedefini ve sekiz revizyonu onayladı; canlı çalışma haritası ile raporun birlikte güncellenmesini istedi. AI bu planın görev/kabul/bağımlılık metinlerini, rapor üretimini ve site entegrasyonunu hazırladı. Bugün ARM-02 kodu veya ortam kurulumu yapılmadı. Bu plan güncellemesinin ek insan çalışma süresi ölçülmedi; önceki 3 saate ek süre uydurulmadı.',small)
heading('Resmî ve birincil başvuru kaynakları')
for s in DATA['sources']:
    story.append(Paragraph('<link href="'+escape(s['url'],quote=True)+'" color="#236a73">'+escape(clean(s['title']))+'</link>',small))
add('Kaynak tasarım LoboCNC’ye aittir. MoveIt/ROS belgeleri mimari dayanağıdır; yerel CAD ölçüsü veya donanım yeterliliği yerine geçmez. Çalışma raporunun sürekli kaynağı docs/rapor.md; ayrıntılı görev verisi docs/arm-roadmap-r3.json dosyasıdır.',small)

def frame(c,doc):
    c.setStrokeColor(colors.HexColor('#dce5e2'));c.line(22*mm,282*mm,188*mm,282*mm)
    c.setFont('Segoe',8);c.setFillColor(muted)
    c.drawString(22*mm,286*mm,'ARMPILOT • ARDA TEKGÖZ')
    c.drawRightString(188*mm,286*mm,'R3 / 15 EKİM 2026')
    c.line(22*mm,16*mm,188*mm,16*mm)
    c.drawString(22*mm,11*mm,'Onaylı plan • Uygulama ve ölçüm kanıtı ayrı kaydedilir')
    c.drawRightString(188*mm,11*mm,str(doc.page))

OUT.parent.mkdir(parents=True,exist_ok=True)
doc=SimpleDocTemplate(str(OUT),pagesize=(210*mm,297*mm),leftMargin=22*mm,rightMargin=22*mm,topMargin=23*mm,bottomMargin=23*mm,title='ArmPilot R3 - Proje Raporu ve Yol Haritası',author='Arda TEKGÖZ; AI danışman desteği')
doc.build(story,onFirstPage=frame,onLaterPages=frame)
print(OUT)
