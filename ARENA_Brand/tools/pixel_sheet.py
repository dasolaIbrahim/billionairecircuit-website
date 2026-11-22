import os, sys, resvg_py
sys.path.insert(0,'.')
import arena_build as A, build_logo as B, pixel as PX
OUT='../04_Directions/D3_Pixel_Scoreboard'
L,I,BN,G,SG='#B8FF2C','#0B0D0E','#F2F5EE','#1B1F21','#FF5A4F'
wd=open(f'{OUT}/build/wordmark.svg').read()
import re
vb=[float(v) for v in re.search(r'viewBox="([^"]+)"',wd).group(1).split()]
wpath=re.search(r' d="([^"]+)"',wd).group(1)
wc=open(f'{OUT}/build/wordmark-colour.svg').read()
wbase_d,wdot_d=re.findall(r' d="([^"]*)"',wc)[:2]
def mark(name,x,y,size,fg,acc=None,face=None):
    s,a=PX.pose(name)
    p=A.build_shapes(s,48); q=A.build_shapes(a,48)
    sc=size/48
    return (f'<g transform="translate({x} {y}) scale({sc})"><path fill="{fg}" d="{B.d_of(p)}"/>'
            f'<path fill="{acc or fg}" d="{B.d_of(q)}"/></g>')
def word(x,y,h,fg,dot):
    # wordmark: font outline in fg; the square full stop drawn in the accent
    sc=h/vb[3]
    return (f'<g transform="translate({x} {y}) scale({sc}) translate({-vb[0]} {-vb[1]})"><path fill="{fg}" d="{wbase_d}"/><path fill="{dot}" d="{wdot_d}"/></g>'
            )
W,H=1560,720
o=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H-72}" viewBox="0 72 {W} {H-72}"><rect width="{W}" height="{H}" fill="#D9D9D9"/>']
for i,(bg,fg) in enumerate([(I,L),(L,I),(BN,I)]):
    cx=143+i*254
    o.append(f'<circle cx="{cx}" cy="206" r="115" fill="{bg}"/>'+mark('idle',cx-66,206-70,140,fg))
for i,(bg,fg,acc) in enumerate([(I,BN,L),(L,I,I),(BN,I,I)]):
    y=92+i*138
    o.append(f'<rect x="790" y="{y}" width="520" height="130" fill="{bg}"/>'+mark('live' if i==1 else 'idle',830,y+15,100,acc if i==0 else fg,acc))
    o.append(word(960,y+42,54,fg,L if i==0 else I))
for i,(n,p) in enumerate(PX.POSES.items()):
    x=28+i*144
    o.append(f'<rect x="{x}" y="525" width="132" height="120" fill="{I}"/>'+mark(n,x+28,535,96,SG if n=="booked" else L,L))
    o.append(f'<text x="{x+66}" y="662" text-anchor="middle" font-family="Martian Mono, JetBrains Mono, monospace" font-size="12" fill="{I}">{n}</text>')
o.append('</svg>')
s=''.join(o)
open(f'{OUT}/D3_system_sheet.svg','w').write(s)
open(f'{OUT}/D3_system_sheet.png','wb').write(bytes(resvg_py.svg_to_bytes(svg_string=s,width=W*2)))
