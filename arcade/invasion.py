from casioplot import *
from random import randint
W,H=384,192;HA,BA,GA,DR,OK=14,34,23,25,24;FD=(10,10,30)
TX=(255,255,255);LI=(170,170,200);OM=(60,60,90)
CO=((0,200,230),(250,210,0),(240,70,90),(40,200,70),(160,60,220),(255,140,0),(0,200,230),(250,210,0))
VAIS=(0,220,160)
AL=(((192,480,876,2046,3579,2313,408,0),(192,480,876,2046,3579,2313,516,0)),
  ((516,264,1020,1782,4095,3069,2565,408),(516,2313,3069,3831,4095,2046,516,1026)),
  ((240,2046,4095,3687,4095,408,876,3075),(240,2046,4095,3687,4095,924,1638,780)))
NAVIRE=(96,96,240,1020,2046,2047,2047)
def rect(x,y,w,h,c):
 if x<0:
  w+=x;x=0
 w=min(w,W-x)
 for i in range(x,x+w):
  for j in range(y,y+h):
   set_pixel(i,j,c)
def sprite(d,x,y,c,lg=12):
 for r in range(len(d)):
  v=d[r]
  for k in range(lg):
   if v>>(lg-1-k)&1 and 0<=x+k<W:
    set_pixel(x+k,y+r,c)
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
NV=(("FACILE",CO[3],60,24),("NORMAL",CO[5],35,18),("DIFFICILE",CO[2],20,14))
def vague(n,vies,so,niv):
 nom,cn,tir,vit0=NV[niv];clear_screen();rect(0,0,W,H,FD)
 for i in range(30):
  set_pixel(randint(0,W-1),randint(16,H-20),(80,80,120))
 rect(0,H-12,W,1,(60,200,120))
 al=[[20+c*26,24+r*16+min(n,4)*4,r//2 if r<4 else 2,True] for r in range(5) for c in range(9)]
 sens,pose=4,0;px=W//2;bal=None;bombes=[];t=0
 def hud():
  rect(0,0,W,14,FD);draw_string(6,1,"Score "+str(so),TX,"small")
  draw_string(150,1,"Vague "+str(n),LI,"small")
  draw_string(W-80,1,"Vies "+str(vies),CO[2],"small")
 hud()
 while True:
  t+=1;vivants=[a for a in al if a[3]]
  if not vivants:
   return vies,so,True
  k=getkey()
  if k in (GA,DR):
   rect(px-6,H-22,12,7,FD)
   px=max(10,min(W-10,px+(5 if k==DR else -5)))
  sprite(NAVIRE,px-6,H-22,VAIS,11)
  if k in (OK,HA) and not bal:
   bal=[px,H-24]
  if bal:
   rect(bal[0],bal[1],2,6,FD);bal[1]-=7;touche=False
   for a in vivants:
    if a[0]-1<=bal[0]<=a[0]+12 and a[1]<=bal[1]<=a[1]+8:
     a[3]=False;rect(a[0],a[1],12,8,CO[1]);so+=(30,20,10)[a[2]]
     touche=True;hud()
     break
   if touche or bal[1]<16:
    bal=None
   else:
    rect(bal[0],bal[1],2,6,TX)
  if t%max(2,vit0*len(vivants)//45)==0:
   bord=any(a[0]+sens<4 or a[0]+12+sens>W-4 for a in vivants)
   pose=1-pose
   for a in al:
    rect(a[0],a[1],12,8,FD)
   for a in vivants:
    if bord:
     a[1]+=6
    else:
     a[0]+=sens
    sprite(AL[a[2]][pose],a[0],a[1],CO[[2,4,0][a[2]]])
    if a[1]+8>=H-24:
     return 0,so,False
   if bord:
    sens=-sens
  if randint(0,tir)==0:
   a=vivants[randint(0,len(vivants)-1)];bombes.append([a[0]+5,a[1]+9])
  for b in bombes[:]:
   rect(b[0],b[1],2,5,FD);b[1]+=4
   if b[1]>H-18:
    bombes.remove(b)
   elif abs(b[0]-px)<7 and b[1]>H-24:
    bombes.remove(b);vies-=1
    for r in range(2,24,4):
     rect(px-r//2,H-20-r//3,r,2,CO[r%8]);show_screen()
    rect(0,H-30,W,18,FD)
    if vies<=0:
     return 0,so,False
    hud()
   else:
    rect(b[0],b[1],2,5,CO[5])
  show_screen()
def pt(niv,record):
 vies,so,n=3,0,1
 while True:
  vies,so,ok=vague(n,vies,so,niv)
  if not ok:
   return so
  rect(110,80,164,30,FD)
  draw_string(120,86,"Vague "+str(n)+" terminee !",CO[3],"medium")
  show_screen()
  for i in range(40):
   show_screen()
  n+=1
LT=(
 ("11111","00100","00100","00100","11111"),
 ("10001","11001","10101","10011","10001"),
 ("10001","10001","10001","01010","00100"),
 ("01110","10001","11111","10001","10001"),
 ("01111","10000","01110","00001","11110"),
 ("11111","00100","00100","00100","11111"),
 ("01110","10001","10001","10001","01110"),
 ("10001","11001","10101","10011","10001"))
def it():
 clear_screen();rect(0,0,W,H,FD);s=6;x0=(W-(8*5*s+7*6))//2
 for i in range(8):
  for l in range(5):
   for k in range(5):
    if LT[i][l][k]=="1":
     x,y=x0+i*(5*s+6)+k*s,14+l*s;rect(x+2,y+2,s,s,OM)
     rect(x,y,s,s,CO[i]);rect(x,y,s,2,(255,255,255))
  show_screen()
 draw_string(20,60,"GRAPH MATH+ EDITION",TX,"large")
 rect(20,84,344,3,CO[4])
 draw_string(W//2-62,178,"Appuie pour passer",LI,"small");n=0
 while n<200:
  x=(n*3)%(W+60)-40
  for i in range(3):
   rect(x-3+i*40,104+i*18,16,8,FD)
   sprite(AL[i][(n//6)%2],x+i*40,104+i*18,CO[[2,4,0][i]])
  show_screen();n+=1
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
  sel=mn(sel);sc=pt(sel,record);nw=sc>record;record=max(record,sc)
  rect(50,58,284,76,FD);rect(50,58,284,3,CO[2])
  rect(50,131,284,3,CO[2])
  draw_string(100,66,"GAME OVER",CO[2],"large")
  draw_string(70,98,("NOUVEAU RECORD : " if nw else "Score : ")+str(sc),TX,"medium")
  show_screen();at()
try:
 import sys
 auto='arcade' not in sys.modules
except:
 auto=True
if auto:
 jouer()
