import os, sys, json, resvg_py, subprocess
R='04_Directions'; T='/tmp/claude-0/-home-user-billionairecircuit-website/1f5040fb-3d73-5c1d-8813-8783f8070ea5/scratchpad/ov/'; os.makedirs(T,exist_ok=True)
rows=[]
for d in sorted(x for x in os.listdir(R) if os.path.isdir(f'{R}/{x}')):
    b=f'{R}/{d}/build'; p=json.load(open(f'{b}/build.json'))['palette']
    for f,w,bg in [('lockup-colour.svg',700,p['paper']),('mark-colour.svg',220,p['paper']),('mark.svg',220,'#ffffff')]:
        s=open(f'{b}/{f}').read()
        if f=='mark.svg': s=s.replace('#151515',p['paper']); bg=p['ink']
        out=f'{T}{d}_{f}.png'
        open(out,'wb').write(bytes(resvg_py.svg_to_bytes(svg_string=s,width=w,background=bg)))
        subprocess.run(['convert',out,'-gravity','center','-background',bg,'-resize',f'{w+60}x240>','-extent',f'{w+80}x260',out])
    subprocess.run(['convert',f'{T}{d}_lockup-colour.svg.png',f'{T}{d}_mark-colour.svg.png',f'{T}{d}_mark.svg.png','+append',f'{T}row_{d}.png'])
    rows.append(f'{T}row_{d}.png')
subprocess.run(['convert',*rows,'-append',sys.argv[1]])
