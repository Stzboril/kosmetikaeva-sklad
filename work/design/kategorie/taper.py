# Štětcová (zužující se) linka: z cesty M…C… udělá vyplněný tvar s proměnnou šířkou
import re, math
def _segs(d):
    t=[float(x) for x in re.findall(r'-?\d*\.?\d+',d)]
    assert d.strip()[0]=='M'
    x,y=t[0],t[1]; i=2; segs=[]
    while i+5<len(t)+0 and i<len(t):
        c=t[i:i+6]; segs.append(((x,y),(c[0],c[1]),(c[2],c[3]),(c[4],c[5]))); x,y=c[4],c[5]; i+=6
    return segs
def _pt(s,u):
    (x0,y0),(x1,y1),(x2,y2),(x3,y3)=s; a=1-u
    return (a**3*x0+3*a*a*u*x1+3*a*u*u*x2+u**3*x3, a**3*y0+3*a*a*u*y1+3*a*u*u*y2+u**3*y3)
def brush(d, w=1.6, n=14, start=.15, end=.15, fill='url(#gold)', minw=.18):
    segs=_segs(d); pts=[]
    for k,s in enumerate(segs):
        for j in range(n+ (1 if k==len(segs)-1 else 0)):
            pts.append(_pt(s,j/n))
    # délky
    L=[0]
    for i in range(1,len(pts)): L.append(L[-1]+math.dist(pts[i-1],pts[i]))
    T=L[-1] or 1
    left=[];right=[]
    for i,p in enumerate(pts):
        a=pts[max(i-1,0)]; b=pts[min(i+1,len(pts)-1)]
        dx,dy=b[0]-a[0],b[1]-a[1]; l=math.hypot(dx,dy) or 1; nx,ny=-dy/l,dx/l
        t=L[i]/T
        f=1.0
        if start>0 and t<start: f=math.sin(math.pi/2*t/start)
        if end>0 and t>1-end: f=min(f, math.sin(math.pi/2*(1-t)/end))
        ww=max(minw, w*f)/2
        left.append((p[0]+nx*ww,p[1]+ny*ww)); right.append((p[0]-nx*ww,p[1]-ny*ww))
    poly=left+right[::-1]
    return '<path d="M'+' L'.join(f'{x:.2f} {y:.2f}' for x,y in poly)+f'Z" fill="{fill}"/>'
