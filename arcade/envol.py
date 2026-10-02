from casioplot import *
from random import randint
W,H=384,192;HA,BA,GA,DR,OK=14,34,23,25,24;SOL=176;TX=(255,255,255);LI=(170,170,200);OM=(60,60,90);FD=(20,20,45)
CO=((0,200,230),(250,210,0),(240,70,90),(40,200,70),(160,60,220),(255,140,0));CORPS=(0,170,190);BANDE=(150,245,240)
BORD=(0,90,110);from math import sin;CIEL=[(70+y*90//SOL,140+y*70//SOL,210+y*30//SOL) for y in range(H)]
MONT=[int(124-abs((x*3+40)%140-70)*0.7-7*sin(x/23)) for x in range(W)]
COLL=[int(150+5*sin(x/21)+3*sin(x/7)) for x in range(W)];NUAGE=[]
for x in range(W):
 t,b=-1,-1
 for (cx,cy,r) in ((50,38,16),(72,42,12),(30,44,10),(210,30,18),(236,36,13),(190,38,11),(330,46,15),(352,50,10)):
  if abs(x-cx)<r:
   h=int((r*r-(x-cx)**2)**0.5*0.6);t=cy-h if t<0 else min(t,cy-h);b=max(b,cy+3)
 NUAGE.append((t,b))
def bgc(x,y):
 if y>=COLL[x]:
  return (60,150,110) if (x+y)%7 else (50,135,100)
 if y>=MONT[x]:
  return (230,235,250) if y<MONT[x]+3 and MONT[x]<96 else (110,120,185)
 t,b=NUAGE[x]
 if t<=y<=b:
  return (250,252,255) if y>t+1 else (220,230,250)
 return CIEL[y]
def ciel(x,y,w,h):
 if x<0:
  w+=x;x=0
 w=min(w,W-x)
 for j in range(max(0,y),min(SOL,y+h)):
  for i in range(x,x+w):
   set_pixel(i,j,bgc(i,j))
OIS=(("....11111.....","..111111111...",".11111113311..",".1111111343...","111111111444..","22211111144444",
   "222211111444..","1222211111....",".11111111111..","..111111111...","....11111.....","..............",),
  ("....11111.....","..111111111...",".11111113311..","22211111343...","222211111444..","12221111144444",
   "111111111444..","11111111111...",".11111111111..","..111111111...","....11111.....","..............",))
PAL={"1":(160,80,220),"2":(220,170,255),"3":(255,255,255),"4":(255,150,40)}
def rect(x,y,w,h,c):
 if x<0:
  w+=x;x=0
 w=min(w,W-x)
 for i in range(x,x+w):
  for j in range(y,y+h):
   set_pixel(i,j,c)
def oiseau(x,y,pose):
 d=OIS[pose]
 for r in range(12):
  for k in range(14):
   ch=d[r][k]
   if ch!=".":
    set_pixel(x+k,y+r,PAL[ch])
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
LC=26;ECART=62;NC=(90,70,60)
FUT=((0,2,NC),(2,5,(250,242,225)),(5,6,(185,165,140)),(6,10,(235,222,200)),(10,11,(170,150,125)),(11,15,(215,200,175)),
  (15,16,(150,130,110)),(16,20,(195,178,152)),(20,21,(135,115,98)),(21,24,(170,150,125)),(24,26,NC))
JOINT=((0,26,(120,100,85)),);ECH=((-2,0,NC),(0,6,(245,235,215)),(6,18,(215,200,175)),(18,26,(170,150,125)),(26,28,NC))
ABA=((-4,-2,NC),(-2,4,(255,250,235)),(4,20,(225,210,185)),(20,28,(180,160,135)),(28,30,NC));TRAIT=((-4,30,NC),)
def bandes(haut):
 g=haut+ECART;r=[];y=haut-9
 while y>0:
  r+=[(max(0,y-22),y-1,FUT),(y-1,y,JOINT)];y-=23
 r+=[(haut-9,haut-5,ECH),(haut-5,haut-1,ABA),(haut-1,haut,TRAIT),(g,g+1,TRAIT),(g+1,g+5,ABA),(g+5,g+9,ECH)];y=g+9
 while y<SOL:
  r+=[(y,y+1,JOINT),(y+1,min(SOL,y+23),FUT)];y+=23
 return r
def colonne(x,haut,v=0):
 for (y0,y1,segs) in bandes(haut):
  if y1<=y0:
   continue
  for (a,b,c) in segs:
   rect(x+a,y0,(b-a) if v==0 else min(v,b-a),y1-y0,c)
  if v:
   ciel(x+segs[-1][1],y0,v,y1-y0)
def decor():
 ciel(0,0,W,SOL);rect(0,SOL,W,H-SOL,(150,105,60));rect(0,SOL,W,4,(90,200,90));rect(0,SOL+4,W,2,(60,150,70))
 for i in range(0,W,8):
  rect(i,SOL,3,2,(140,230,120))
 for i in range(0,W,16):
  rect(i+4,SOL+9,6,3,(125,85,45));rect(i+12,SOL+13,4,2,(175,125,75))
def pt(record):
 decor();bx,by,vy=80,80,0.0;cols=[[W+40+i*150,randint(30,SOL-ECART-30),False] for i in range(3)];so=0;pose=0;v=3;t=0
 while True:
  ciel(bx,by-3,14,18);yy=by+int(4*((t//6)%2));oiseau(bx,yy,(t//6)%2);rect(118,74,150,18,FD)
  draw_string(126,76,"OK pour voler",TX,"small");show_screen();t+=1
  if getkey() in (OK,HA):
   break
 ciel(118,74,150,18);avant=OK
 while True:
  k=getkey()
  if k in (OK,HA) and avant not in (OK,HA):
   vy=-5.2
  avant=k;vy=min(vy+0.45,7);ancien=by;by=int(by+vy)
  for c in cols:
   c[0]-=v
   if c[0]<W and c[0]+LC+8>=0:
    colonne(c[0],c[1],v)
   if c[0]<W and c[0]+LC+4+v>W:
    colonne(c[0],c[1])
   if not c[2] and c[0]+LC<bx:
    c[2]=True;so+=1
   if c[0]<-LC-6:
    c[0]=max(cc[0] for cc in cols)+150;c[1]=randint(24,SOL-ECART-24);c[2]=False
  ciel(bx,ancien,14,12);pose=1 if vy<0 else 0;oiseau(bx,max(0,by),pose);rect(4,4,64,20,FD)
  draw_string(10,6,str(so),TX,"medium");show_screen();mort=by<0 or by+11>=SOL
  for c in cols:
   if c[0]<bx+12 and c[0]+LC>bx+2 and (by+1<c[1] or by+10>c[1]+ECART):
    mort=True
  if mort:
   for r in range(3,30,5):
    for (a,b) in ((-1,-1),(1,-1),(-1,1),(1,1),(0,-1),(1,0),(0,1),(-1,0)):
     rect(bx+7+a*r,max(0,min(H-4,by+6+b*r)),4,4,CO[r%6])
    show_screen()
   return so
LT=(
 ("11111","10000","11110","10000","11111"),
 ("10001","11001","10101","10011","10001"),
 ("10001","10001","10001","01010","00100"),
 ("01110","10001","10001","10001","01110"),
 ("10000","10000","10000","10000","11111"))
def it():
 clear_screen();rect(0,0,W,H,FD);s=8;x0=(W-(5*5*s+4*8))//2
 for i in range(5):
  for l in range(5):
   for k in range(5):
    if LT[i][l][k]=="1":
     x,y=x0+i*(5*s+8)+k*s,12+l*s;rect(x+2,y+2,s,s,OM);rect(x,y,s,s,CO[i]);rect(x,y,s,2,(255,255,255))
  show_screen()
 draw_string(20,60,"GRAPH MATH+ EDITION",TX,"large");rect(20,84,344,3,CO[0])
 draw_string(W//2-62,178,"Appuie pour passer",LI,"small");n=0;oy=130
 while n<220:
  x=(n*3)%(W+40)-20;y=130+int(14*((n%40)-20)*((n%40)-20)/400)-7;rect(max(0,x-4),oy,20,12,FD)
  if 0<=x<W-14:
   oiseau(x,y,(n//4)%2)
  oy=y;show_screen();n+=1
  if getkey():
   break
 rl()
def jouer():
 it();record=0
 while True:
  sc=pt(record);nw=sc>record;record=max(record,sc);rect(60,52,264,86,FD);rect(60,52,264,3,CO[2])
  rect(60,135,264,3,CO[2]);draw_string(110,60,"GAME OVER",CO[2],"large")
  draw_string(80,90,("NOUVEAU RECORD : " if nw else "Score : ")+str(sc),TX,"medium")
  draw_string(80,114,"Record : "+str(record)+"   OK : rejouer",LI,"small");show_screen();at()
try:
 import sys
 auto='arcade' not in sys.modules
except:
 auto=True
if auto:
 jouer()
