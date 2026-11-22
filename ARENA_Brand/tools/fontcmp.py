import sys, os, resvg_py, subprocess
sys.path.insert(0,'.')
import arena_build as A, build_logo as B, fonts as F, pathops
from fontTools.varLib import instancer
from fontTools.ttLib import TTFont
from fontTools.pens.transformPen import TransformPen
SK='/tmp/claude-0/-home-user-billionairecircuit-website/1f5040fb-3d73-5c1d-8813-8783f8070ea5/scratchpad/fc/'; os.makedirs(SK,exist_ok=True)
def load(fam, axes):
    info=F.fetch(fam,A.FONTS)
    for p in info['files']:
        f=TTFont(p)
        if 'fvar' in f:
            ax={a.axisTag:a for a in f['fvar'].axes}
            loc={t:max(ax[t].minValue,min(ax[t].maxValue,v)) for t,v in axes.items() if t in ax}
            for t,a in ax.items(): loc.setdefault(t,a.defaultValue)
            return instancer.instantiateVariableFont(f,loc)
    return F.load(info, axes.get('wght',400))
C=[('Unbounded',{'wght':900}),('Krona One',{}),('Archivo',{'wght':900,'wdth':125}),('Anybody',{'wght':900,'wdth':150}),
   ('Syne',{'wght':800}),('Lexend Zetta',{'wght':800}),('Dela Gothic One',{}),('Michroma',{}),('Hanken Grotesk',{'wght':900}),('Bricolage Grotesque',{'wght':800,'wdth':100})]
outs=[]
for fam,ax in C:
    try:
        t=F.set_text(load(fam,ax),'boring pays twice.',-20)
    except SystemExit as e:
        print('skip',fam,e); continue
    p=pathops.Path(); t['pen'].replay(TransformPen(p.getPen(),(1,0,0,-1,0,0)))
    s=B.svg(B.d_of(p),p.bounds,pad=60)
    f=SK+fam.replace(' ','_')+'.png'
    open(f,'wb').write(bytes(resvg_py.svg_to_bytes(svg_string=s,height=110,background='#EDE6DB')))
    subprocess.run(['convert',f,'-gravity','west','-background','#EDE6DB','-extent','1100x120','-fill','#c0392b','-pointsize','16','-annotate','+880+0',fam+' '+str(ax),f])
    outs.append(f)
subprocess.run(['convert',*outs,'-append',SK+'cmp.png'])
