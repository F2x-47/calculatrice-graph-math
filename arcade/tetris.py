from casioplot import *
from random import randint
W,H=384,192;C=9;BW,BH=10,20;X0=(W-BW*C)//2;Y0=(H-BH*C)//2
HA,BA,GA,DR,OK=14,34,23,25,24;VITESSE=28;BG=(255,255,255)
FD=(20,20,45);GR=(35,35,70);TX=(30,30,80);LI=(170,170,190)
OM=(60,60,90)
CO=(None,(0,200,230),(250,210,0),(160,60,220),(40,200,70),(235,40,50),(30,90,230),(255,140,0))
FM=(
 None,
 ((0,1),(1,1),(2,1),(3,1)),
 ((1,0),(2,0),(1,1),(2,1)),
 ((1,0),(0,1),(1,1),(2,1)),
 ((1,0),(2,0),(0,1),(1,1)),
 ((0,0),(1,0),(1,1),(2,1)),
 ((0,0),(0,1),(1,1),(2,1)),
 ((2,0),(0,1),(1,1),(2,1)))
def rots(t):
 f=FM[t]
 if t==2:
  return (f,)
 n=4 if t==1 else 3;res=[f]
 for _ in range(3):
  f=tuple((n-1-y,x) for (x,y) in f);res.append(f)
 return tuple(res)
ROT=[None]+[rots(t) for t in range(1,8)]
def rect(x,y,w,h,c):
 for i in range(x,x+w):
  for j in range(y,y+h):
   set_pixel(i,j,c)
def cl(c,d):
 return (min(255,c[0]+d),min(255,c[1]+d),min(255,c[2]+d))
def fo(c,d):
 return (max(0,c[0]-d),max(0,c[1]-d),max(0,c[2]-d))
def bk(px,py,c):
 rect(px,py,C-1,C-1,c);rect(px,py,C-1,1,cl(c,90))
 rect(px,py,1,C-1,cl(c,60));rect(px,py+C-2,C-1,1,fo(c,70))
 rect(px+C-2,py,1,C-1,fo(c,50))
def cs(x,y,t):
 px,py=X0+x*C,Y0+y*C
 if t:
  bk(px,py,CO[t])
 else:
  rect(px,py,C,C,FD);set_pixel(px+C-1,py+C-1,GR)
def rl():
 n=0
 while n<30:
  if getkey():
   n=0
  else:
   n+=1
def at():
 rl();k=0
 while not k:
  k=getkey()
 rl()
 return k
LT=(
 ("111","010","010","010","010"),
 ("111","100","110","100","111"),
 ("111","010","010","010","010"),
 ("110","101","110","101","101"),
 ("111","010","010","010","111"),
 ("011","100","010","001","110"))
try:
 from time import monotonic as hz
except:
 hz=None
def le(motif,x,y,s,c):
 for l in range(5):
  for k in range(3):
   if motif[l][k]=="1":
    rect(x+k*s+3,y+l*s+3,s,s,OM);b2(x+k*s,y+l*s,s,c)
def b2(px,py,s,c):
 rect(px,py,s,s,c);rect(px,py,s,2,cl(c,90))
 rect(px,py+s-2,s,2,fo(c,70))
def it(du=15):
 clear_screen();rect(0,0,W,H,FD);show_screen();s=10;lg=6*3*s+5*8
 x0=(W-lg)//2
 for i in range(6):
  le(LT[i],x0+i*(3*s+8),14,s,CO[1+i]);show_screen()
 draw_string(20,78,"GRAPH MATH+ EDITION",(255,255,255),"large")
 rect(20,102,344,3,CO[7])
 draw_string(W//2-62,176,"Appuie pour passer",LI,"small")
 show_screen();pz=[]
 for i in range(6):
  pz.append([14+i*62,randint(1,7),108-randint(0,80),randint(1,3)])
 t0=hz() if hz else 0;n=0
 while True:
  for p in pz:
   bx,t,y,v=p
   for (a,b) in FM[t]:
    yy=y+b*8
    if 108<=yy<=H-28:
     rect(bx+a*8,yy,8,8,FD)
   y+=v
   if y>H:
    y=100-randint(0,60);v=randint(1,3);t=randint(1,7)
   for (a,b) in FM[t]:
    yy=y+b*8
    if 108<=yy<=H-28:
     b2(bx+a*8,yy,8,CO[t])
   p[1],p[2],p[3]=t,y,v
  show_screen();n+=1
  if getkey():
   break
  if hz:
   if hz()-t0>=du:
    break
  elif n>=270:
   break
 rl()
NV=(("FACILE",CO[4],1),("MOYEN",CO[7],4),("DIFFICILE",CO[5],8))
def mn(sel):
 rl()
 while True:
  clear_screen();rect(0,0,W,H,FD)
  draw_string(W//2-80,12,"DIFFICULTE",(255,255,255),"large")
  for i in range(3):
   n=NV[i];y=58+i*36
   if i==sel:
    rect(W//2-100,y-4,200,30,n[1])
    draw_string(W//2-80,y,"> "+n[0],FD,"large")
   else:
    draw_string(W//2-80,y,"  "+n[0],n[1],"large")
  draw_string(W//2-100,172,"Fleches pour choisir, OK pour valider",LI,"small")
  show_screen();k=at()
  if k==HA:
   sel=(sel-1)%3
  elif k==BA:
   sel=(sel+1)%3
  elif k==OK:
   return sel
def inf(so,ln,niv,mx):
 rect(4,20,X0-12,150,FD);draw_string(8,24,"SCORE",LI,"small")
 draw_string(8,38,str(so),(255,255,255),"medium")
 draw_string(8,66,"LIGNES",LI,"small")
 draw_string(8,80,str(ln),(255,255,255),"medium")
 draw_string(8,108,"NIVEAU",LI,"small")
 draw_string(8,122,str(niv),CO[2],"medium")
 draw_string(8,150,"RECORD "+str(mx),CO[1],"small")
def sv(t):
 bx=X0+BW*C+20;draw_string(bx,24,"SUIVANTE",LI,"small")
 rect(bx,42,44,30,FD)
 for (a,b) in FM[t]:
  b2(bx+2+a*10,46+b*10,10,CO[t])
def cd():
 clear_screen();rect(0,0,W,H,FD);rect(X0-3,Y0-3,BW*C+6,BH*C+6,CO[1])
 rect(X0-2,Y0-2,BW*C+4,BH*C+4,CO[3]);rect(X0-1,Y0-1,BW*C+2,BH*C+2,FD)
 for y in range(BH):
  for x in range(BW):
   cs(x,y,0)
 bx=X0+BW*C+20;draw_string(bx,120,"^ tourner",LI,"small")
 draw_string(bx,140,"OK chute",LI,"small")
def lb(g,t,r,x,y):
 for (a,b) in ROT[t][r]:
  i,j=x+a,y+b
  if i<0 or i>=BW or j>=BH:
   return False
  if j>=0 and g[j][i]:
   return False
 return True
def dw(t,r,x,y,v):
 for (a,b) in ROT[t][r]:
  if y+b>=0:
   cs(x+a,y+b,v)
def pt(niv0,mx):
 g=[[0]*BW for _ in range(BH)];so=ln=0;niv=niv0;cd();inf(so,ln,niv,mx)
 t=randint(1,7);nt=randint(1,7);sv(nt)
 while True:
  r,x,y=0,3,-1
  if not lb(g,t,r,x,y):
   return so
  dw(t,r,x,y,t);show_screen();ch=max(3,VITESSE-3*(niv-1));cpt=0;prev=0
  rep=0;pose=False
  while not pose:
   k=getkey();nx,ny,nr=x,y,r;dur=False
   if k!=prev:
    rep=0
    if k==GA:
     nx-=1
    elif k==DR:
     nx+=1
    elif k==HA:
     nr=(r+1)%len(ROT[t])
    elif k==OK:
     while lb(g,t,r,x,ny+1):
      ny+=1
     so+=2*(ny-y);dur=True
    elif k==BA:
     ny+=1
   else:
    rep+=1
    if k in (GA,DR) and rep>8 and rep%3==0:
     nx+=1 if k==DR else -1
    elif k==BA and rep%2==0:
     ny+=1
   prev=k;cpt+=1
   if cpt>=ch:
    cpt=0;ny+=1 if ny==y else 0
   if nr!=r:
    ok=False
    for d in (0,-1,1,-2,2):
     if lb(g,t,nr,x+d,y):
      nx=x+d;ok=True
      break
    if not ok:
     nr=r
   if (nx,nr)!=(x,r) and not lb(g,t,nr,nx,y):
    nx,nr=x,r
   if ny!=y and not lb(g,t,nr,nx,ny):
    ny=y
    if cpt==0 or k==BA:
     pose=True
   if (nx,ny,nr)!=(x,y,r):
    dw(t,r,x,y,0);x,y,r=nx,ny,nr;dw(t,r,x,y,t)
   if dur:
    pose=True
   show_screen()
  for (a,b) in ROT[t][r]:
   if y+b<0:
    return so
   g[y+b][x+a]=t
  pl=[j for j in range(BH) if 0 not in g[j]]
  if pl:
   for _ in range(2):
    for j in pl:
     rect(X0,Y0+j*C,BW*C,C,(255,255,255))
    show_screen()
    for j in pl:
     for i in range(BW):
      cs(i,j,g[j][i])
    show_screen()
   for j in pl:
    del g[j];g.insert(0,[0]*BW)
   for j in range(max(pl)+1):
    for i in range(BW):
     cs(i,j,g[j][i])
   n=len(pl);so+=(0,100,300,500,800)[n]*niv;ln+=n
   niv=max(niv,niv0+ln//10);inf(so,ln,niv,max(mx,so))
  t=nt;nt=randint(1,7);sv(nt)
def jouer():
 it();sel=0;mx=0
 while True:
  sel=mn(sel);sc=pt(NV[sel][2],mx);nw=sc>mx;mx=max(mx,sc)
  rect(X0-10,70,BW*C+20,56,FD);rect(X0-10,70,BW*C+20,2,CO[5])
  rect(X0-10,124,BW*C+20,2,CO[5])
  draw_string(X0+2,76,"GAME OVER",CO[5],"large")
  draw_string(X0+4,102,("RECORD ! " if nw else "Score : ")+str(sc),(255,255,255),"small")
  show_screen();at()
try:
 import sys
 auto='arcade' not in sys.modules
except:
 auto=True
if auto:
 jouer()
