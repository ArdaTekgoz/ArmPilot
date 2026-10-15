"""Render the ARM-01 Markdown contract as a one-page PDF. Documentation helper."""
from pathlib import Path
from xml.sax.saxutils import escape
import re
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer, KeepTogether
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'output/pdf/arm-01-kapsam.pdf'
OUT.parent.mkdir(parents=True,exist_ok=True)
for name,file in [('ArmFont','segoeui.ttf'),('ArmFontBold','segoeuib.ttf')]:
    pdfmetrics.registerFont(TTFont(name,str(Path('C:/Windows/Fonts')/file)))
pdfmetrics.registerFontFamily('ArmFont',normal='ArmFont',bold='ArmFontBold',italic='ArmFont',boldItalic='ArmFontBold')
body=ParagraphStyle('body',fontName='ArmFont',fontSize=9.2,leading=12.2,spaceAfter=5.5,textColor=colors.HexColor('#192f3e'))
small=ParagraphStyle('small',parent=body,fontSize=8.3,leading=11,textColor=colors.HexColor('#526675'))
heading=ParagraphStyle('heading',parent=body,fontName='ArmFontBold',fontSize=10.2,leading=13,spaceBefore=7,spaceAfter=4,textColor=colors.HexColor('#17666e'))
title=ParagraphStyle('title',parent=body,fontName='ArmFontBold',fontSize=16.3,leading=20.2,spaceAfter=7)
cell=ParagraphStyle('cell',parent=body,fontSize=8.7,leading=11.2,spaceAfter=0)

def inline(text):
    text=text.replace('–','-').replace('—','-')
    text=escape(text)
    return re.sub(r'\*\*(.*?)\*\*',r'<b>\1</b>',text)

lines=(ROOT/'docs/arm-01-kapsam.md').read_text(encoding='utf8').splitlines()
story=[]
i=0
while i<len(lines):
    line=lines[i].strip()
    if not line: i+=1; continue
    if line.startswith('# '): story.append(Paragraph(inline(line[2:]),title)); i+=1; continue
    if line.startswith('## '): story.append(Paragraph(inline(line[3:]),heading)); i+=1; continue
    if line.startswith('|'):
        rows=[]
        while i<len(lines) and lines[i].strip().startswith('|'):
            parts=[p.strip() for p in lines[i].strip().strip('|').split('|')]
            if not all(re.fullmatch(r'[:\s-]+',p) for p in parts):
                rows.append([Paragraph(inline(p),cell) for p in parts])
            i+=1
        table=Table(rows,colWidths=[127,A4[0]-72-127],repeatRows=1,hAlign='LEFT')
        table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e6f0f1')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4),('LINEBELOW',(0,0),(-1,0),.5,colors.HexColor('#8faeb2')),('LINEBELOW',(0,1),(-1,-1),.3,colors.HexColor('#d8e1e6'))]))
        story.extend([table,Spacer(1,6)])
        continue
    para=[line]
    i+=1
    while i<len(lines) and lines[i].strip() and not lines[i].startswith(('#','|')):
        para.append(lines[i].strip()); i+=1
    style=small if para[0].startswith('15 Ekim') else body
    story.append(Paragraph(inline(' '.join(para)),style))

def footer(canvas,doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor('#c9d7de'))
    canvas.line(36,29,A4[0]-36,29)
    canvas.setFont('ArmFont',8)
    canvas.setFillColor(colors.HexColor('#526675'))
    canvas.drawString(36,17,'ArmPilot | ARM-01 R2 | Belge kapanışı; fiziksel doğrulama yapılmadı')
    canvas.drawRightString(A4[0]-36,17,str(doc.page))
    canvas.restoreState()

doc=SimpleDocTemplate(str(OUT),pagesize=A4,leftMargin=36,rightMargin=36,topMargin=29,bottomMargin=38,title='ArmPilot ARM-01 - Kapsam ve sürüm sözleşmesi',author='Arda TEKGÖZ / AI danışman desteği')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
reader=PdfReader(OUT)
assert len(reader.pages)==1, f'Expected one page, got {len(reader.pages)}'
content=reader.pages[0].extract_text()
for required in ['400 mm','100 g','10 mm','5°','kapasite garantisi']:
    assert required in content, required
print(f'PASS: one-page PDF and key contract values verified: {OUT}')
