import sys, resvg_py
sys.path.insert(0,'.')
import arena_build as A, letters as T, build_logo as B
from functools import partial
SK='/tmp/claude-0/-home-user-billionairecircuit-website/1f5040fb-3d73-5c1d-8813-8783f8070ea5/scratchpad/sk/'
def render(groups, name):
    p=A.build_shapes(groups,100)
    open(SK+name+'.svg','w').write(B.svg(B.d_of(p),p.bounds,pad=12))
    open(SK+name+'.png','wb').write(bytes(resvg_py.svg_to_bytes(svg_string=open(SK+name+'.svg').read(),width=900,background='#ffffff')))
g,_=T.word([T.d1_A,T.d1_R,T.d1_E,T.d1_N,T.d1_A],[5,11,15,4]); render(g,'d1')
g,_=T.word([T.d2_A,T.d2_R,T.d2_E,T.d2_N,T.d2_A],[6,6,7,6]); render(g,'d2')
g,_=T.word([T.d5_A,T.d5_R,T.d5_E,T.d5_N,partial(T.d5_A,counter='o')],[6,9,12,6]); render(g,'d5')
