from casioplot import *
from math import sin,cos,pi
from random import randint
W,H=384,192;HA,BA,GA,DR,OK=14,34,23,25,24;FD=(18,20,40)
BORD=(90,60,160);TX=(255,255,255);LI=(170,170,200);OM=(60,60,90)
CO=((0,200,230),(250,210,0),(240,70,90),(40,200,70),(160,60,220),(255,140,0),(0,200,230),(250,210,0),(240,70,90))
DIR=[(cos(i*pi/16),sin(i*pi/16)) for i in range(32)]
def rect(x,y,w,h,c):
 if x<0:
  w+=x;x=0
 if y<0:
  h+=y;y=0
 w=min(w,W-x);h=min(h,H-y)
 for i in range(x,x+w):
  for j in range(y,y+h):
   set_pixel(i,j,c)
def ln(r):
 return [(dy,int((r*r-dy*dy)**0.5)) for dy in range(-r,r+1)]
L4=ln(4);L5=ln(5)
def disque(x,y,L,c):
 x,y=int(x),int(y)
 for (dy,w) in L:
  rect(x-w,y+dy,2*w+1,1,c)
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
 rl()
 return k
class Serpent:
 def __init__(s,x,y,d,c,n):
  s.c,s.d,s.lg,s.vit=c,d,n,2;s.pts=[(x,y)];s.vivant=True
 def avance(s):
  x,y=s.pts[-1];dx,dy=DIR[s.d];x,y=x+dx*s.vit,y+dy*s.vit
  if len(s.pts)>1:
   disque(s.pts[-1][0],s.pts[-1][1],L4,s.c)
  s.pts.append((x,y))
  while len(s.pts)>s.lg:
   a=s.pts.pop(0);disque(a[0],a[1],L4,FD);b=s.pts[0]
   disque(b[0],b[1],L4,s.c)
  disque(x,y,L4,s.c);ex,ey=DIR[(s.d+8)%32]
  for e in (1,-1):
   rect(int(x+dx*2+ex*e*2),int(y+dy*2+ey*e*2),2,2,TX)
  return x,y
 def efface(s):
  for (x,y) in s.pts:
   disque(x,y,L5,FD)
def touche_corps(x,y,sp,saut):
 for i in range(0,len(sp.pts)-saut,3):
  a,b=sp.pts[i]
  if (a-x)*(a-x)+(b-y)*(b-y)<64:
   return True
 return False
def bouffe(x=None,y=None):
 if x==None:
  x,y=randint(12,W-14),randint(24,H-14)
 return [int(x),int(y),CO[randint(0,8)]]
def dessine_b(b):
 rect(b[0],b[1],3,3,b[2])
def bords():
 rect(0,18,W,2,BORD);rect(0,H-2,W,2,BORD);rect(0,18,2,H-18,BORD)
 rect(W-2,18,2,H-18,BORD)
NV=(("FACILE",CO[3],2,1),("NORMAL",CO[5],3,2),("DIFFICILE",CO[2],4,3))
def ia_nouveau(i):
 c=(CO[2],CO[4],CO[1],CO[5])[i]
 return Serpent(randint(W//2+40,W-40),randint(50,H-30),randint(10,22),c,30)
def pt(niv,record):
 nom,cn,nb,agr=NV[niv];clear_screen();rect(0,0,W,H,FD);bords()
 moi=Serpent(60,100,0,CO[0],40);ias=[ia_nouveau(i) for i in range(nb)]
 nour=[bouffe() for i in range(28)]
 for b in nour:
  dessine_b(b)
 t=0;so=0
 while True:
  t+=1;k=getkey()
  if k==GA:
   moi.d=(moi.d-1)%32
  elif k==DR:
   moi.d=(moi.d+1)%32
  moi.vit=4 if (k==OK and moi.lg>25) else 2
  if moi.vit==4 and t%4==0:
   moi.lg-=1
  x,y=moi.avance()
  if x<6 or x>W-7 or y<24 or y>H-7:
   break
  mort=False
  for ia in ias:
   if not ia.vivant:
    continue
   hx,hy=ia.pts[-1];cible=nour[(t//40+ias.index(ia)*7)%len(nour)]
   if agr>1 and t>150 and t%150<25*(agr-1):
    cible=(x+DIR[moi.d][0]*30,y+DIR[moi.d][1]*30)
   if hx<30 or hx>W-30 or hy<40 or hy>H-26:
    cible=(W//2,H//2)
   a=0;best=9e9
   for d in (-1,0,1):
    dx,dy=DIR[(ia.d+d)%32]
    e=(hx+dx*8-cible[0])**2+(hy+dy*8-cible[1])**2
    if e<best:
     best,a=e,d
   ia.d=(ia.d+a)%32;ax,ay=ia.avance()
   if touche_corps(ax,ay,moi,0) or ax<6 or ax>W-7 or ay<24 or ay>H-7:
    ia.vivant=False;ia.efface()
    for i in range(0,len(ia.pts),5):
     b=bouffe(ia.pts[i][0],ia.pts[i][1]);nour.append(b);dessine_b(b)
    ia.mort=t;bords();continue
   if touche_corps(x,y,ia,0):
    mort=True
   for b in nour:
    if abs(b[0]-ax)<6 and abs(b[1]-ay)<6:
     nour.remove(b);ia.lg+=2
     if len(nour)<28:
      b=bouffe();nour.append(b);dessine_b(b)
     break
  if mort:
   break
  for b in nour:
   if abs(b[0]-x)<7 and abs(b[1]-y)<7:
    nour.remove(b);moi.lg+=3;so+=1
    if len(nour)<28:
     b=bouffe();nour.append(b);dessine_b(b)
    break
  for i in range(nb):
   if not ias[i].vivant and t-ias[i].mort>60:
    ias[i]=ia_nouveau(i)
  if t%10==0:
   for b in nour:
    dessine_b(b)
   rect(0,0,W,18,FD)
   draw_string(6,3,"Longueur "+str(moi.lg),TX,"small")
   draw_string(150,3,"Record "+str(record),LI,"small")
   draw_string(W-70,3,nom,cn,"small")
  show_screen()
 for r in range(3,40,6):
  for i in range(0,32,4):
   rect(int(x+DIR[i][0]*r),int(y+DIR[i][1]*r),4,4,CO[i%9])
  show_screen()
 return moi.lg
LT=(
 ("01111","10000","01110","00001","11110"),
 ("11111","10000","11110","10000","11111"),
 ("11110","10001","11110","10010","10001"),
 ("11110","10001","11110","10000","10000"),
 ("11111","10000","11110","10000","11111"),
 ("10001","11001","10101","10011","10001"),
 ("11111","00100","00100","00100","00100"),
 ("11111","00100","00100","00100","11111"),
 ("10001","11001","10101","10011","10001"))
def it():
 clear_screen();rect(0,0,W,H,FD);s=6;x0=(W-(9*5*s+8*5))//2
 for i in range(9):
  for l in range(5):
   for k in range(5):
    if LT[i][l][k]=="1":
     x,y=x0+i*(5*s+5)+k*s,14+l*s;rect(x+2,y+2,s,s,OM)
     rect(x,y,s,s,CO[i]);rect(x,y,s,2,(255,255,255))
  show_screen()
 draw_string(20,60,"GRAPH MATH+ EDITION",TX,"large")
 rect(20,84,344,3,CO[3])
 draw_string(W//2-62,178,"Appuie pour passer",LI,"small")
 sp=Serpent(20,135,0,CO[3],45);n,base=0,0
 while n<270:
  x,y=sp.pts[-1]
  if x>W-30:
   base=16
  elif x<30:
   base=0
  sp.d=(base+int(3*sin(n/8)))%32;sp.avance();show_screen();n+=1
  if getkey():
   break
 rl()
def mn(sel):
 rl()
 while True:
  clear_screen();rect(0,0,W,H,FD)
  draw_string(W//2-80,12,"DIFFICULTE",TX,"large")
  for i in range(3):
   nom,c=NV[i][:2];y=58+i*36
   if i==sel:
    rect(W//2-100,y-4,200,30,c)
    draw_string(W//2-80,y,"> "+nom,FD,"large")
   else:
    draw_string(W//2-80,y,"  "+nom,c,"large")
  draw_string(W//2-130,172,"Fleches pour choisir, OK pour jouer",LI,"small")
  show_screen();k=at()
  if k==OK:
   return sel
  sel=(sel+(1 if k==BA else -1))%3
def jouer():
 it();sel,record=0,0
 while True:
  sel=mn(sel);lg=pt(sel,record);nw=lg>record;record=max(record,lg)
  rect(50,58,284,76,FD);rect(50,58,284,3,CO[2])
  rect(50,131,284,3,CO[2]);draw_string(110,66,"PERDU !",CO[2],"large")
  draw_string(70,98,("NOUVEAU RECORD : " if nw else "Longueur : ")+str(lg),TX,"medium")
  show_screen();at()
try:
 import sys
 auto='arcade' not in sys.modules
except:
 auto=True
if auto:
 jouer()
