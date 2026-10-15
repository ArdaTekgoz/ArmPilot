"""AI-authored teaching figure, not ArmPilot FK implementation or learner evidence.

UR5 ideal URDF transforms transcribed from the vendor's rolling description:
https://github.com/UniversalRobots/Universal_Robots_ROS2_Description/blob/rolling/config/ur5/default_kinematics.yaml
https://github.com/UniversalRobots/Universal_Robots_ROS2_Description/blob/rolling/urdf/ur_macro.xacro
Checked 2026-10-15. Simplified link silhouettes; joint axes calculated from transforms.
"""
from pathlib import Path
import math
import html
import json
import argparse
from PIL import Image, ImageDraw, ImageFont

parser=argparse.ArgumentParser()
parser.add_argument('--model',choices=['ur5','wer24'],default='ur5')
MODEL=parser.parse_args().model
OUT = Path(__file__).resolve().parent
W, H, SS = 2000, 1350, 2
COLORS = ['#be4b30', '#226a9c', '#407c49', '#7b4ea8', '#bc6517', '#087e87']
INK, MUTED, LIGHT, BODY = '#182c3c', '#536778', '#dae3e9', '#92a7b5'
im = Image.new('RGB', (W*SS, H*SS), '#fafcfd')
draw = ImageDraw.Draw(im)
svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">', f'<rect width="{W}" height="{H}" fill="#fafcfd"/>']
fonts = {}

def font(size, bold=False):
    key = (size, bold)
    if key not in fonts:
        name = 'segoeuib.ttf' if bold else 'segoeui.ttf'
        fonts[key] = ImageFont.truetype(str(Path('C:/Windows/Fonts') / name), round(size*SS))
    return fonts[key]

def text(p, value, size=25, color=INK, bold=False):
    draw.text((p[0]*SS, p[1]*SS), value, fill=color, font=font(size,bold))
    svg.append(f'<text x="{p[0]:.2f}" y="{p[1]+size:.2f}" font-family="Segoe UI,Arial,sans-serif" font-size="{size}" font-weight="{600 if bold else 400}" fill="{color}">{html.escape(value)}</text>')

def line(points, color=INK, width=2, dashed=False):
    if dashed:
        for a,b in zip(points,points[1:]):
            dist = math.dist(a,b)
            for s in range(0, math.ceil(dist), 13):
                t1, t2 = s/dist, min(s+7,dist)/dist
                line([tuple(a[k]+(b[k]-a[k])*t1 for k in range(2)), tuple(a[k]+(b[k]-a[k])*t2 for k in range(2))],color,width)
        return
    pts = [(x*SS,y*SS) for x,y in points]
    draw.line(pts,fill=color,width=round(width*SS),joint='curve')
    if width > 6:
        r=width*SS/2
        for x,y in [pts[0],pts[-1]]:
            draw.ellipse((x-r,y-r,x+r,y+r),fill=color)
    svg.append(f'<polyline points="{" ".join(f"{x:.3f},{y:.3f}" for x,y in points)}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round"/>')

def circle(p,r,fill,stroke=None,width=2):
    x,y=p
    draw.ellipse(((x-r)*SS,(y-r)*SS,(x+r)*SS,(y+r)*SS),fill=fill,outline=stroke,width=round(width*SS))
    svg.append(f'<circle cx="{x:.3f}" cy="{y:.3f}" r="{r}" fill="{fill}" stroke="{stroke or fill}" stroke-width="{width}"/>')

def arrow(points,color,width=3,head=12):
    line(points,color,width)
    a,b=points[-2:]
    d=math.dist(a,b)
    if d < 1e-8: return
    u=((b[0]-a[0])/d,(b[1]-a[1])/d)
    v=(-u[1],u[0])
    pts=[b,(b[0]-head*u[0]+.48*head*v[0],b[1]-head*u[1]+.48*head*v[1]),(b[0]-head*u[0]-.48*head*v[0],b[1]-head*u[1]-.48*head*v[1])]
    draw.polygon([(x*SS,y*SS) for x,y in pts],fill=color)
    svg.append(f'<polygon points="{" ".join(f"{x:.3f},{y:.3f}" for x,y in pts)}" fill="{color}"/>')

def add(a,b): return [x+y for x,y in zip(a,b)]
def mul(a,k): return [x*k for x in a]
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b): return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def norm(a): return mul(a,1/math.sqrt(dot(a,a)))
def mm(a,b): return [[sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
def mv(a,b): return [dot(row,b) for row in a]
def rx(t): return [[1,0,0],[0,math.cos(t),-math.sin(t)],[0,math.sin(t),math.cos(t)]]
def ry(t): return [[math.cos(t),0,math.sin(t)],[0,1,0],[-math.sin(t),0,math.cos(t)]]
def rz(t): return [[math.cos(t),-math.sin(t),0],[math.sin(t),math.cos(t),0],[0,0,1]]
def rpy(r,p,y): return mm(mm(rz(y),ry(p)),rx(r))

# Each joint rotates about its OWN local +Z, after the fixed origin transform.
pi=math.pi
origins=[([0,0,.089159],[0,0,0]),([0,0,0],[pi/2,0,0]),([-.425,0,0],[0,0,0]),([-.39225,0,.10915],[0,0,0]),([0,-.09465,-1.941303950897609e-11],[1.570796327,0,0]),([0,.0823,-1.688001216681175e-11],[1.570796326589793,pi,pi])]
qdeg=[0,-45,-120,-15,55,0]
R,p=rz(pi),[0,0,0]
if MODEL=='wer24':
    origins=[([0,0,.10693],[0,0,0]),([.01163,0,.05732],[1.57079,0,1.57079]),([0,.2032,-.04911],[0,0,1.57079]),([.1778,0,.0103],[0,0,0]),([.03095,0,.02667],[-1.57079,0,-1.57079]),([0,-.04546,.02683],[1.57079,0,0])]
    qdeg=[0,-60,-120,0,55,0]
    R=rz(0)
positions,axes=[],[]
for (xyz,rot),angle in zip(origins,qdeg):
    p=add(p,mv(R,xyz))
    R=mm(R,rpy(*rot))
    positions.append(p[:]); axes.append(mv(R,[0,0,1]))
    R=mm(R,rz(math.radians(angle)))

# UR5 structural facts, independent of displayed joint angles.
assert abs(abs(dot(axes[1],axes[2]))-1)<2e-5
assert abs(abs(dot(axes[2],axes[3]))-1)<2e-5
assert abs(dot(axes[3],axes[4]))<2e-5
assert abs(dot(axes[4],axes[5]))<2e-5

n=norm([1.5,-2,1.1]); right=norm(cross([0,0,1],n)); up=cross(n,right)
def project(p): return [dot(p,right),-dot(p,up)]
def fit(points,rect,pad=90):
    projected=[project(p) for p in points]
    lo=[min(p[k] for p in projected) for k in range(2)]
    hi=[max(p[k] for p in projected) for k in range(2)]
    x,y,w,h=rect
    scale=min((w-2*pad)/(hi[0]-lo[0]),(h-2*pad)/(hi[1]-lo[1]))
    c=[(lo[k]+hi[k])/2 for k in range(2)]
    return lambda p: [x+w/2+(project(p)[0]-c[0])*scale,y+h/2+(project(p)[1]-c[1])*scale]

def extent(points,axes,length):
    return [add(p,mul(a,s*length)) for p,a in zip(points,axes) for s in [-1,1]]

def render_robot(P,center_points,joint_indices,zoom=False):
    if not zoom:
        # The J1 shaft is vertical; its label is placed lower along that same line.
        foot=[positions[0][0],positions[0][1],0]
        line([P(foot),P(positions[1])],LIGHT,66)
        circle(P(foot),42,LIGHT, BODY,3)
        path=[positions[1],positions[2],positions[3],positions[4],positions[5]]
    else:
        stub=add(positions[3],mul(norm(add(positions[2],mul(positions[3],-1))),.07))
        path=[stub]+positions[3:]
    for a,b in zip(path,path[1:]):
        line([P(a),P(b)],BODY,50 if not zoom else 44)
        line([P(a),P(b)],LIGHT,34 if not zoom else 29)
    for index in joint_indices:
        point=center_points[index]
        axis=axes[index]
        col=COLORS[index]
        circle(P(point),18 if not zoom else 24,'#f5f8fa',BODY,3)
        length=.070 if not zoom else .065
        a=P(add(point,mul(axis,-length))); b=P(add(point,mul(axis,length)))
        line([a,b],col,3,True)
        arrow([P(add(point,mul(axis,.044))),b],col,3,11)
        helper=[0,0,1] if abs(axis[2])<.8 else [1,0,0]
        u=norm(cross(axis,helper)); v=cross(axis,u)
        radius=.038 if not zoom else .027
        points=[P(add(point,add(mul(u,radius*math.cos(t)),mul(v,radius*math.sin(t))))) for t in [math.radians(20+k*4) for k in range(68)]]
        arrow(points,col,3,11)
        circle(P(point),5,col)
        if zoom: text((b[0]+8,b[1]-19),'+',22,col,True)

title='UR5 tipi kol: J1–J6 eksenleri ve dönüşleri' if MODEL=='ur5' else 'WE-R2.4 referansı: J1–J6 eksenleri ve dönüşleri'
subtitle='Resmî UR5 ideal eklem dönüşümlerinden hesaplanmış eğitim şeması • ArmPilot ölçüleri henüz seçilmedi' if MODEL=='ur5' else 'Yayımlanmış WE-R2.4 ROS modelinden hesaplandı • Senin CAD montajınla boyutsal eşleştirme yapılmadı'
text((72,42),title,45,INK,True)
text((74,107),subtitle,25,MUTED)
line([(70,164),(1930,164)],LIGHT,2)
text((80,190),'KOLUN TAMAMI',24,MUTED,True)
text((1160,190),'BİLEK AYRINTISI · J4 / J5 / J6',24,MUTED,True)

centers=[p[:] for p in positions]
centers[0]=[0,0,.025]
mainP=fit(extent(centers,axes,.09)+[[0,0,0]],(210,250,830,660),72)
render_robot(mainP,centers,list(range(6)))
zoomP=fit(extent(positions[3:],axes[3:],.08),(1150,250,750,570),90)
render_robot(zoomP,positions,[3,4,5],True)

main_labels=[(95,854),(93,708),(815,566),(93,448),(93,337),(515,238)]
if MODEL=='wer24':
    main_labels=[(95,854),(93,600),(855,275),(855,480),(855,645),(855,800)]
main_names=['Taban','Omuz','Dirsek','Bilek 1','Bilek 2','Bilek 3']
for i,(label,name) in enumerate(zip(main_labels,main_names)):
    target=mainP(centers[i]); x,y=label
    label_width=draw.textlength(name,font=font(25,True))/SS
    endpoint=[x+54+label_width+16,y+22] if target[0]-x>200 else [x+22,y+22]
    line([target,endpoint],COLORS[i],1.5)
    circle((x+22,y+22),22,COLORS[i])
    text((x+5,y+5),f'J{i+1}',21,'#ffffff',True)
    text((x+54,y+5),name,25,INK,True)

zoom_labels=[(1165,710),(1410,265),(1700,365)] if MODEL=='ur5' else [(1165,280),(1720,480),(1695,735)]
for i,label in zip([3,4,5],zoom_labels):
    target=zoomP(positions[i]); x,y=label
    caption=f'J{i+1} · Bilek {i-2}'
    label_width=draw.textlength(caption,font=font(27,True))/SS
    endpoint=(x+label_width+14,y+20) if i==3 else ((x+90,y+42) if i==4 else (x-14,y+20))
    if MODEL=='wer24':
        endpoint=(x+label_width+14,y+25) if i==3 else (x-14,y+20)
    line([target,endpoint],COLORS[i],2)
    text((x,y),f'J{i+1} · Bilek {i-2}',27,COLORS[i],True)

# Tool/flange reference aligned with J6 shaft, not a calibrated TCP for ArmPilot.
tip=add(positions[5],mul(axes[5],.045))
circle(zoomP(tip),7,COLORS[5])
text((1170,826),'J4 ekseni J2 ve J3’e paraleldir.',28,COLORS[3],True)
text((1170,875),'J5 ekseni J4’e; J6 ekseni J5’e diktir.',26,INK)

line([(70,967),(1930,967)],LIGHT,2)
text((80,993),'ÇİZGİ VE OKLAR',22,MUTED,True)
line([(87,1060),(198,1060)],COLORS[3],3,True)
arrow([(172,1060),(198,1060)],COLORS[3],3,10)
text((220,1039),'Kesikli çizgi: eklem ekseni · düz ok: pozitif eksen yönü',25)
text((87,1090),'Kavisli ok: eksen çevresinde pozitif dönüş (sağ el kuralı). Oklar hareket limiti değildir.',25)
text((87,1140),'J4, uzun önkolun boyuna ekseninde dönmez. J6, uç flanşını kendi ekseninde döndürür.',25,INK,True)
text((87,1191),'J5 hareket ettikçe J6 ekseni yön değiştirir; J4 ile J6 her duruşta paralel değildir.',24,MUTED)
source='Kaynak: UniversalRobots / Universal_Robots_ROS2_Description · ur_macro.xacro + config/ur5/default_kinematics.yaml' if MODEL=='ur5' else 'Kaynak: RobinWolf / diy_robotarm_wer24_description · default_kinematics.yaml + diy_robotarm_macro.urdf.xacro'
text((87,1250),source,20,MUTED)
text((87,1284),'AI tarafından hazırlanmış açıklayıcı şema • Fiziksel ölçüm veya Arda’nın elle çizimi değildir • 15 Ekim 2026',20,MUTED)

svg.append('</svg>')
OUT.mkdir(parents=True,exist_ok=True)
prefix='ur5' if MODEL=='ur5' else 'wer24'
(OUT/f'{prefix}-joint-axes-reference.svg').write_text('\n'.join(svg),encoding='utf-8')
im.resize((W,H),Image.Resampling.LANCZOS).save(OUT/f'{prefix}-joint-axes-reference.png')
data={'pose_degrees':qdeg,'joint_origins_m':positions,'joint_axes_in_base':axes,'source':source,'note':'Reference model; not dimensionally matched to the user CAD assembly.'}
(OUT/f'{prefix}-joint-axes-reference.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
print('Generated PNG, SVG and axis data; parallel/perpendicular assertions passed.')
print('Main projected centers:',[list(map(lambda v:round(v,1),mainP(p))) for p in centers])
print('Wrist projected centers:',[list(map(lambda v:round(v,1),zoomP(p))) for p in positions[3:]])
