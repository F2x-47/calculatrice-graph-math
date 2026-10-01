from casioplot import *
from random import randint
from math import sin
W,H=384,192;GA,DR,OK=23,25,24;FD=(20,20,45);BARRE=(35,35,70)
TX=(255,255,255);LI=(170,170,190);OM=(60,60,90);SEL=(0,200,255)
CO=((40,200,70),(235,40,50),(30,90,230),(250,210,0),(160,60,220),(255,140,0),(0,200,230))
JEUX=(("PONG","pong",(0,160,255)),
   ("TETRIS","tetris",(160,60,220)),
   ("SIMON","simon",(40,200,70)),
   ("SERPENTIN","serpent",(0,200,230)),
   ("CUBE RUSH","cube",(255,200,0)))
try:
 from time import monotonic as hz
except:
 hz=None
def rect(x,y,w,h,c):
 for i in range(x,x+w):
  for j in range(y,y+h):
   set_pixel(i,j,c)
def terne(c):
 return (c[0]//3,c[1]//3,c[2]//3)
def bk(px,py,s,c):
 rect(px,py,s,s,c)
 rect(px,py,s,2,(min(255,c[0]+90),min(255,c[1]+90),min(255,c[2]+90)))
 rect(px,py+s-2,s,2,terne(c))
def rl():
 n=0
 while n<30:
  if getkey():
   n=0
  else:
   n+=1
LT=(
 ("01110","10001","11111","10001","10001"),
 ("11110","10001","11110","10010","10001"),
 ("01111","10000","10000","10000","01111"),
 ("01110","10001","11111","10001","10001"),
 ("11110","10001","10001","10001","11110"),
 ("11111","10000","11110","10000","11111"))
def demarrage():
 clear_screen();rect(0,0,W,H,FD);show_screen();s=8
 x0=(W-(6*5*s+5*8))//2
 for i in range(6):
  for l in range(5):
   for k in range(5):
    if LT[i][l][k]=="1":
     x,y=x0+i*(5*s+8)+k*s,18+l*s;rect(x+3,y+3,s,s,OM);bk(x,y,s,CO[i])
  show_screen()
 draw_string(20,78,"GRAPH MATH+ EDITION",TX,"large")
 rect(20,102,344,3,SEL)
 draw_string(W//2-62,176,"Appuie pour passer",LI,"small")
 rect(92,140,200,14,BARRE);t0=hz() if hz else 0;n=0
 while n<196:
  rect(94+n,142,4,10,CO[(n//28)%7]);show_screen();n+=4
  if getkey():
   break
 rl()
TX0,TY,TW,TH,GAP=20,36,100,100,22
def vignette_pong(x,y):
 rect(x,y,TW,TH,(10,10,30))
 for j in range(y+6,y+TH-6,10):
  rect(x+49,j,2,5,LI)
 rect(x+8,y+30,5,28,(0,160,255));rect(x+TW-13,y+50,5,28,(230,0,120))
 rect(x+64,y+40,6,6,(255,140,0))
 draw_string(x+30,y+8,"3",(0,160,255),"medium")
 draw_string(x+60,y+8,"2",(230,0,120),"medium")
def vignette_tetris(x,y):
 rect(x,y,TW,TH,(10,10,30));s=10
 pile=((0,8,5),(1,8,5),(2,8,1),(3,8,1),(4,8,1),(5,8,1),(6,8,2),(7,8,2),(8,8,4),(9,8,4),
    (0,7,5),(1,7,6),(2,7,6),(3,7,6),(6,7,2),(7,7,2),(8,7,4),(9,7,3),
    (0,6,5),(3,6,6),(8,6,3),(9,6,3),
    (4,2,0),(4,3,0),(5,3,0),(5,4,0))
 for (a,b,c) in pile:
  bk(x+a*s,y+b*s+8,s,CO[c])
def zones(R,r,g):
 res=[]
 for d in range(g,R+1):
  b=min(int((R*R-d*d)**0.5),d-g);a=int((r*r-d*d)**0.5) if d<r else 0
  if b>a:
   res.append((d,a,b))
 return res
def disque(cx,cy,R,c):
 for dy in range(-R,R+1):
  w=int((R*R-dy*dy)**0.5);rect(cx-w,cy+dy,2*w+1,1,c)
def vignette_simon(x,y):
 rect(x,y,TW,TH,(10,10,30));cx,cy=x+50,y+50
 disque(cx,cy,42,(70,70,110));disque(cx,cy,40,(10,10,25))
 vif=((40,220,70),(240,40,50),(40,110,255),(255,215,0))
 for (d,a,b) in zones(38,12,3):
  rect(cx-b,cy-d,b-a+1,1,vif[0]);rect(cx+a,cy-d,b-a+1,1,vif[0])
  rect(cx-b,cy+d,b-a+1,1,terne(vif[2]));rect(cx+a,cy+d,b-a+1,1,terne(vif[2]))
  rect(cx+d,cy-b,1,b-a+1,terne(vif[1]));rect(cx+d,cy+a,1,b-a+1,terne(vif[1]))
  rect(cx-d,cy-b,1,b-a+1,terne(vif[3]));rect(cx-d,cy+a,1,b-a+1,terne(vif[3]))
 disque(cx,cy,10,(70,70,110))
def vignette_serpent(x,y):
 rect(x,y,TW,TH,(18,20,40))
 for (a,b,c) in ((10,20,0),(30,70,5),(70,15,3),(85,60,1),(55,85,4),(15,85,6)):
  rect(x+a,y+b,3,3,CO[c])
 for i in range(40):
  px=x+12+i*2;py=y+50+int(10*sin(i/5.0))
  rect(px-3,py-3,7,7,(0,200,230))
 rect(x+90,py-2,2,2,(255,255,255));rect(x+90,py+1,2,2,(255,255,255))
 for i in range(14):
  rect(x+40+i*3,y+22+i,6,6,(240,70,90))
def vignette_cube(x,y):
 rect(x,y,TW,TH,(28,22,70));rect(x,y+76,TW,24,(10,70,120))
 rect(x,y+76,TW,2,(20,140,200))
 for i in range(0,TW,16):
  rect(x+i,y+78,8,22,(15,100,160))
 rect(x+20,y+40,14,14,(255,200,0));rect(x+20,y+40,14,2,(255,240,150))
 rect(x+23,y+44,3,3,(40,30,0));rect(x+28,y+44,3,3,(40,30,0))
 rect(x+23,y+49,8,2,(40,30,0))
 for (a,h) in ((50,16),(66,16)):
  for r in range(h):
   rect(x+a+8-r//2,y+60+r,2*(r//2)+1,1,(240,240,255))
 rect(x+80,y+58,18,18,(110,60,220));rect(x+80,y+58,18,2,(170,130,255))
 rect(x+85,y+63,8,8,(70,30,160))
def vignette_autre(x,y,c):
 rect(x,y,TW,TH,(10,10,30));rect(x+30,y+30,40,40,c)
DESSINS={"pong":vignette_pong,"tetris":vignette_tetris,"simon":vignette_simon,"serpent":vignette_serpent,"cube":vignette_cube}
def position(i):
 return TX0+(i%3)*(TW+GAP),TY
def cd(i,c):
 x,y=position(i);rect(x-6,y-6,TW+12,4,c);rect(x-6,y+TH+2,TW+12,4,c)
 rect(x-6,y-6,4,TH+12,c);rect(x+TW+2,y-6,4,TH+12,c)
def accueil(page):
 clear_screen();rect(0,0,W,H,FD);rect(0,0,W,22,BARRE)
 draw_string(8,4,"GRAPH ARCADE",TX,"small")
 for i in range(4):
  rect(330+i*8,7,6,8,CO[i])
 rect(0,H-18,W,18,BARRE)
 draw_string(8,H-15,"< > choisir     OK jouer     AC quitter un jeu",LI,"small")
 for i in range(page*3,min(len(JEUX),page*3+3)):
  x,y=position(i);nom,f,c=JEUX[i]
  if f in DESSINS:
   DESSINS[f](x,y)
  else:
   vignette_autre(x,y,c)
 if len(JEUX)>3:
  draw_string(W-40,H-15,str(page+1)+"/"+str((len(JEUX)+2)//3),TX,"small")
def titre(i):
 rect(0,TY+TH+8,W,24,FD);nom=JEUX[i][0]
 draw_string(W//2-len(nom)*9,TY+TH+10,nom,JEUX[i][2],"large")
def lancer(f):
 clear_screen();rect(0,0,W,H,FD)
 draw_string(W//2-60,H//2-10,"Chargement...",TX,"large");show_screen()
 try:
  if f=="pong":
   import pong as m
  elif f=="tetris":
   import tetris as m
  elif f=="simon":
   import simon as m
  elif f=="serpent":
   import serpent as m
  elif f=="cube":
   import cube as m
  else:
   m=__import__(f)
  m.jouer()
 except KeyboardInterrupt:
  pass
 except Exception as e:
  clear_screen();rect(0,0,W,H,FD)
  draw_string(20,60,"Erreur dans "+f+".py",(235,40,50),"large")
  draw_string(20,100,str(e)[:40],TX,"small")
  draw_string(20,150,"OK pour revenir",LI,"small");show_screen();rl()
  while getkey()!=OK:
   pass
 try:
  import sys,gc
  if f in sys.modules:
   del sys.modules[f]
  gc.collect()
 except:
  pass
 rl()
def console():
 demarrage();sel=0
 while True:
  page=sel//3;accueil(page);cd(sel,SEL);titre(sel);show_screen()
  while True:
   k=0
   while k not in (GA,DR,OK):
    k=getkey()
   rl()
   if k==OK:
    lancer(JEUX[sel][1])
    break
   n=(sel+(1 if k==DR else -1))%len(JEUX)
   if n//3!=page:
    sel=n
    break
   cd(sel,FD);sel=n;cd(sel,SEL);titre(sel);show_screen()
console()
