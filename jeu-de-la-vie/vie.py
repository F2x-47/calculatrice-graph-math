from casioplot import *
from random import randint
W,H=384,192;HA,BA,GA,DR,OK=14,34,23,25,24;FD=(12,12,30);GRIS=(26,26,52);BARRE=(35,35,70);TX=(255,255,255)
LI=(170,170,200);OM=(60,60,90);CO=((0,200,230),(250,210,0),(240,70,90),(40,200,70),(160,60,220),(255,140,0));T=6
NC,NL=64,30;N=NC*NL;g=[0]*N;viv=[];etat=[0,0]
CANON=((24,0),(22,1),(24,1),(12,2),(13,2),(20,2),(21,2),(34,2),(35,2),(11,3),(15,3),(20,3),(21,3),(34,3),(35,3),
   (0,4),(1,4),(10,4),(16,4),(20,4),(21,4),(0,5),(1,5),(10,5),(14,5),(16,5),(17,5),(22,5),(24,5),(10,6),(16,6),
   (24,6),(11,7),(15,7),(12,8),(13,8))
PLANEUR=((1,0),(2,1),(0,2),(1,2),(2,2))
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
def touche():
 rl();k=0
 while k not in (HA,BA,GA,DR,OK):
  k=getkey()
 return k
def cellule(i,curseur=False):
 x,y=(i%NC)*T,(i//NC)*T
 if curseur:
  rect(x,y,T,T,TX);rect(x+1,y+1,T-2,T-2,CO[g[i]-1] if g[i] else FD)
 else:
  rect(x,y,T,T,GRIS);rect(x,y,T-1,T-1,CO[g[i]-1] if g[i] else FD)
def pose(motif,x0,y0,c):
 for (x,y) in motif:
  g[((y0+y)%NL)*NC+(x0+x)%NC]=c
def tout():
 for i in range(N):
  cellule(i)
def sv():
 global viv;cnt={}
 for i in viv:
  x,y=i%NC,i//NC;xg,xd=(x-1)%NC,(x+1)%NC
  for yy in (((y-1)%NL)*NC,y*NC,((y+1)%NL)*NC):
   for j in (yy+xg,yy+x,yy+xd):
    cnt[j]=cnt.get(j,0)+1
 nv=[]
 for j in cnt:
  n=cnt[j]
  if n==3 or (n==4 and g[j]):
   nv.append(j)
 for i in viv:
  n=cnt[i]
  if n!=3 and n!=4:
   g[i]=0;cellule(i)
 c=1+(etat[0]//6)%6
 for j in nv:
  if not g[j]:
   g[j]=c;cellule(j)
 viv=nv;etat[0]+=1
BOUTONS=("LECTURE","1 PAS","EFFACER","MENU")
def barre(sel,marche=False):
 rect(0,180,W,12,BARRE)
 for i in range(4):
  nom="PAUSE" if (i==0 and marche) else BOUTONS[i]
  if i==sel:
   rect(i*62,180,60,12,CO[0])
  draw_string(i*62+4,181,nom,FD if i==sel else TX,"small")
 inf()
def inf():
 rect(250,180,134,12,BARRE);draw_string(254,181,"Gen "+str(etat[0])+"  Pop "+str(len(viv)),LI,"small")
def compte():
 global viv;viv=[i for i in range(N) if g[i]]
def lecture():
 barre(0,True);show_screen();rl()
 while viv:
  sv()
  if etat[0]%3==0:
   inf()
  show_screen()
  if getkey()==OK:
   break
 barre(0)
def simulation(mode):
 global viv
 for i in range(N):
  g[i]=0
 etat[0]=0
 if mode==0:
  for i in range(N):
   if randint(0,3)==0:
    g[i]=randint(1,6)
 elif mode==1:
  pose(CANON,4,3,2)
 elif mode==2:
  for k in range(8):
   pose(PLANEUR,4+k*8,2+(k%3)*9,1+k%6)
 compte();clear_screen();tout();cx,cy,bs=NC//2,NL//2,0;bas=mode!=3
 if bas:
  lecture()
 while True:
  barre(bs if bas else -1)
  if not bas:
   cellule(cy*NC+cx,True)
  show_screen();k=touche()
  if bas:
   if k==OK:
    if bs==0:
     lecture()
    elif bs==1:
     sv()
    elif bs==2:
     for i in viv:
      g[i]=0;cellule(i)
     viv=[];etat[0]=0
    else:
     return
   elif k in (GA,DR):
    bs=(bs+(1 if k==DR else -1))%4
   else:
    bas=False;cy=NL-1 if k==HA else 0
  else:
   i=cy*NC+cx
   if k==OK:
    g[i]=0 if g[i] else 4;compte()
   else:
    cellule(i)
    if k==GA:
     cx=(cx-1)%NC
    elif k==DR:
     cx=(cx+1)%NC
    elif k==HA:
     if cy==0:
      bas=True
     else:
      cy-=1
    elif cy==NL-1:
     bas=True
    else:
     cy+=1
LT=(
 ("10001","10001","10001","01010","00100"),
 ("11111","00100","00100","00100","11111"),
 ("11111","10000","11110","10000","11111"))
def it():
 clear_screen();rect(0,0,W,H,FD);s=8;x0=(W-(3*5*s+2*12))//2
 for i in range(3):
  for l in range(5):
   for k in range(5):
    if LT[i][l][k]=="1":
     x,y=x0+i*(5*s+12)+k*s,12+l*s;rect(x+2,y+2,s,s,OM);rect(x,y,s,s,CO[i*2]);rect(x,y,s,2,(255,255,255))
  show_screen()
 draw_string(20,60,"GRAPH MATH+ EDITION",TX,"large");rect(20,84,344,3,CO[3])
 draw_string(W//2-62,178,"Appuie pour passer",LI,"small");file=[];n=0
 while n<260:
  x,y=randint(3,60)*T,randint(16,27)*T;rect(x,y,T-1,T-1,CO[randint(0,5)]);file.append((x,y))
  if len(file)>45:
   x,y=file.pop(0);rect(x,y,T-1,T-1,FD)
  show_screen();n+=1
  if getkey():
   break
 rl()
MODES=(("ALEATOIRE",CO[0]),("CANON A PLANEURS",CO[1]),("PLANEURS",CO[3]),("DESSIN LIBRE",CO[4]))
def mn(sel):
 while True:
  clear_screen();rect(0,0,W,H,FD);draw_string(W//2-80,8,"DEPART",TX,"large")
  for i in range(4):
   nom,c=MODES[i];y=40+i*32
   if i==sel:
    rect(40,y-4,304,28,c);draw_string(52,y,"> "+nom,FD,"large")
   else:
    draw_string(52,y,"  "+nom,c,"large")
  draw_string(W//2-130,174,"Fleches pour choisir, OK pour lancer",LI,"small");show_screen();k=touche()
  if k==OK:
   rl()
   return sel
  if k in (HA,BA):
   sel=(sel+(1 if k==BA else -1))%4
def jouer():
 it();sel=0
 while True:
  sel=mn(sel);simulation(sel)
try:
 import sys
 auto="arcade" not in sys.modules
except:
 auto=True
if auto:
 jouer()
