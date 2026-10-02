from casioplot import *
from random import randint
W,H=384,192;HA,BA,GA,DR,OK=14,34,23,25,24;FD=(14,18,44);TX=(255,255,255);LI=(170,170,200);OM=(60,60,90)
CO=((0,200,230),(250,210,0),(240,70,90),(40,200,70),(160,60,220),(255,140,0));MER=(30,95,175);TRAIT=(18,60,125)
COQUE=(150,160,175);FEU=(235,60,50);EPAVE=(110,25,35);C=15;GX=(14,220);GY=20;TAILLES=(5,4,3,3,2);fl=[None,None]
tir=[None,None];pv=[None,None];montre=[0]
def rect(x,y,w,h,c):
 for i in range(x,x+w):
  for j in range(y,y+h):
   set_pixel(i,j,c)
def rl():
 n=0
 while n<30:
  if getkey():
   n=0
  else:
   n+=1
def at():
 rl();k=0
 while k not in (HA,BA,GA,DR,OK):
  k=getkey()
 return k
def placer():
 g=[0]*100
 for n in range(5):
  t=TAILLES[n]
  while True:
   h=randint(0,1);x=randint(0,9-(t-1)*h);y=randint(0,9-(t-1)*(1-h));cases=[(y+k*(1-h))*10+x+k*h for k in range(t)]
   ok=True
   for i in cases:
    if g[i]:
     ok=False
   if ok:
    for i in cases:
     g[i]=n+1
    break
 return g
def dcase(cote,i,curseur=False):
 x,y=GX[cote]+(i%10)*C,GY+(i//10)*C;s=tir[cote][i]
 if s==3:
  c=EPAVE
 elif s==2:
  c=FEU
 elif fl[cote][i] and (cote==0 or montre[0]):
  c=COQUE
 else:
  c=MER
 if curseur:
  rect(x,y,C+1,C+1,CO[1]);rect(x+2,y+2,C-3,C-3,c)
 else:
  rect(x,y,C+1,C+1,TRAIT);rect(x+1,y+1,C-1,C-1,c)
 if s==1:
  rect(x+6,y+6,4,4,TX)
 elif s==2:
  rect(x+5,y+5,6,6,(255,200,60))
 elif s==3:
  rect(x+5,y+5,6,6,(30,10,15))
def grille(cote):
 for i in range(100):
  dcase(cote,i)
def flottes():
 rect(168,GY,49,150,FD)
 for n in range(5):
  t=TAILLES[n]*8;rect(214-t,GY+6+n*12,t,8,CO[0] if pv[1][n] else (60,60,85))
  rect(170,GY+86+n*12,t,8,COQUE if pv[0][n] else EPAVE)
def msg(texte,c=TX):
 rect(0,174,W,18,FD);draw_string(14,177,texte,c,"small")
def tire(cote,i):
 n=fl[cote][i]
 if not n:
  tir[cote][i]=1
  return 1
 tir[cote][i]=2;pv[cote][n-1]-=1
 if pv[cote][n-1]==0:
  for j in range(100):
   if fl[cote][j]==n:
    tir[cote][j]=3;dcase(cote,j)
  return 3
 return 2
def choix(niv):
 t=tir[0];libres=[i for i in range(100) if t[i]==0]
 if niv>0:
  best=[];bs=0
  for i in libres:
   x,y=i%10,i//10;s=0
   for (dx,dy) in ((1,0),(-1,0),(0,1),(0,-1)):
    k=1
    while 0<=x+dx*k<10 and 0<=y+dy*k<10 and t[(y+dy*k)*10+x+dx*k]==2:
     k+=1
    if k>1:
     s=max(s,k if niv==2 else 2)
   if s>bs:
    best=[i];bs=s
   elif s==bs and s:
    best.append(i)
  if best:
   return best[randint(0,len(best)-1)]
  if niv==2:
   p=[i for i in libres if (i%10+i//10)%2==0]
   if p:
    libres=p
 return libres[randint(0,len(libres)-1)]
RES=("","Dans l'eau.","Touche !","Coule !")
def pt(niv):
 montre[0]=0;clear_screen();rect(0,0,W,H,FD);draw_string(GX[0],3,"TA FLOTTE",COQUE,"small")
 draw_string(GX[1],3,"MER ENNEMIE",CO[0],"small")
 for k in (0,1):
  tir[k]=[0]*100;pv[k]=list(TAILLES)
 fl[1]=placer();grille(1)
 while True:
  fl[0]=placer();grille(0);flottes();msg("< > : autre placement      OK : valider",LI);show_screen()
  if at()==OK:
   break
 cur=44;tirs=0
 while True:
  msg("A toi : fleches pour viser, OK pour tirer",LI)
  while True:
   dcase(1,cur,True);show_screen();k=at()
   if k==OK:
    if tir[1][cur]==0:
     break
   else:
    dcase(1,cur);x,y=cur%10,cur//10
    if k==GA:
     x=(x-1)%10
    elif k==DR:
     x=(x+1)%10
    elif k==HA:
     y=(y-1)%10
    else:
     y=(y+1)%10
    cur=y*10+x
  r=tire(1,cur);tirs+=1;dcase(1,cur,True);flottes();msg("Ton tir : "+RES[r],CO[r]);show_screen()
  if max(pv[1])==0:
   return True,tirs
  i=choix(niv);r2=tire(0,i)
  for k in range(6):
   dcase(0,i,k%2==0);show_screen()
  flottes();msg("Ton tir : "+RES[r]+"   Ennemi : "+RES[r2],TX);show_screen()
  if max(pv[0])==0:
   montre[0]=1;grille(1)
   return False,tirs
  rl()
LT=(
 ("10001","11001","10101","10011","10001"),
 ("01110","10001","11111","10001","10001"),
 ("10001","10001","10001","01010","00100"),
 ("01110","10001","11111","10001","10001"),
 ("10000","10000","10000","10000","11111"))
def bateau(x,y):
 rect(x,y+8,40,7,COQUE);rect(x+4,y+15,32,3,(100,110,125));rect(x+12,y+2,14,6,(200,205,215));rect(x+17,y-4,4,6,CO[2])
 rect(x+28,y+5,10,2,(90,95,110))
def it():
 clear_screen();rect(0,0,W,H,FD);s=8;x0=(W-(5*5*s+4*8))//2
 for i in range(5):
  for l in range(5):
   for k in range(5):
    if LT[i][l][k]=="1":
     x,y=x0+i*(5*s+8)+k*s,12+l*s;rect(x+2,y+2,s,s,OM);rect(x,y,s,s,CO[i]);rect(x,y,s,2,(255,255,255))
  show_screen()
 draw_string(20,60,"GRAPH MATH+ EDITION",TX,"large");rect(20,84,344,3,CO[0]);rect(0,132,W,40,MER)
 for i in range(0,W,12):
  rect(i,140+(i//12)%3*9,6,2,(90,160,230))
 draw_string(W//2-62,178,"Appuie pour passer",LI,"small");n=0
 while n<170:
  x=n*2;rect(max(0,x-2),106,2,26,FD);rect(max(0,x-2),132,2,3,MER)
  if x<W-40:
   bateau(x,114)
  show_screen();n+=1
  if getkey():
   break
 rl()
NV=(("FACILE",CO[3]),("NORMAL",CO[5]),("DIFFICILE",CO[2]))
def mn(sel):
 while True:
  clear_screen();rect(0,0,W,H,FD);draw_string(W//2-80,12,"DIFFICULTE",TX,"large")
  for i in range(3):
   nom,c=NV[i];y=58+i*36
   if i==sel:
    rect(W//2-100,y-4,200,30,c);draw_string(W//2-80,y,"> "+nom,FD,"large")
   else:
    draw_string(W//2-80,y,"  "+nom,c,"large")
  draw_string(W//2-130,172,"Fleches pour choisir, OK pour jouer",LI,"small");show_screen();k=at()
  if k==OK:
   return sel
  if k in (HA,BA):
   sel=(sel+(1 if k==BA else -1))%3
def jouer():
 it();sel=0
 while True:
  sel=mn(sel);gagne,tirs=pt(sel);c=CO[3] if gagne else CO[2];rect(82,66,220,60,FD);rect(82,66,220,3,c)
  rect(82,123,220,3,c);draw_string(110,74,"VICTOIRE !" if gagne else "DEFAITE...",c,"large")
  draw_string(110,102,"en "+str(tirs)+" tirs    OK : rejouer",TX,"small");show_screen();rl()
  while getkey()!=OK:
   pass
try:
 import sys
 auto="arcade" not in sys.modules
except:
 auto=True
if auto:
 jouer()
