from casioplot import *
from random import randint
import vignettes
W,H=384,192;GA,DR,OK=23,25,24;FD=(20,20,45);BARRE=(35,35,70);TX=(255,255,255);LI=(170,170,190);OM=(60,60,90)
SEL=(0,200,255);CO=((40,200,70),(235,40,50),(30,90,230),(250,210,0),(160,60,220),(255,140,0),(0,200,230))
JEUX=(("PONG","pong",(0,160,255)),
   ("TETRIS","tetris",(160,60,220)),
   ("SIMON","simon",(40,200,70)),
   ("SERPENTIN","serpent",(0,200,230)),
   ("CUBE RUSH","cube",(255,200,0)),
   ("SUDOKU","sudoku",(250,210,0)),
   ("INVASION","invasion",(240,70,90)),
   ("ENVOL","envol",(160,80,220)),
   ("BATAILLE NAVALE","naval",(0,200,230)))
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
 rect(px,py,s,s,c);rect(px,py,s,2,(min(255,c[0]+90),min(255,c[1]+90),min(255,c[2]+90)));rect(px,py+s-2,s,2,terne(c))
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
 clear_screen();rect(0,0,W,H,FD);show_screen();s=8;x0=(W-(6*5*s+5*8))//2
 for i in range(6):
  for l in range(5):
   for k in range(5):
    if LT[i][l][k]=="1":
     x,y=x0+i*(5*s+8)+k*s,18+l*s;rect(x+3,y+3,s,s,OM);bk(x,y,s,CO[i])
  show_screen()
 draw_string(20,78,"GRAPH MATH+ EDITION",TX,"large");rect(20,102,344,3,SEL)
 draw_string(W//2-62,176,"Appuie pour passer",LI,"small");rect(92,140,200,14,BARRE);t0=hz() if hz else 0;n=0
 while n<196:
  rect(94+n,142,4,10,CO[(n//28)%7]);show_screen();n+=4
  if getkey():
   break
 rl()
TX0,TY,TW,TH,GAP=20,36,100,100,22
def position(i):
 return TX0+(i%3)*(TW+GAP),TY
def cd(i,c):
 x,y=position(i);rect(x-6,y-6,TW+12,4,c);rect(x-6,y+TH+2,TW+12,4,c);rect(x-6,y-6,4,TH+12,c);rect(x+TW+2,y-6,4,TH+12,c)
def accueil(page):
 clear_screen();rect(0,0,W,H,FD);rect(0,0,W,22,BARRE);draw_string(8,4,"GRAPH ARCADE",TX,"small")
 for i in range(4):
  rect(330+i*8,7,6,8,CO[i])
 rect(0,H-18,W,18,BARRE);draw_string(8,H-15,"< > choisir     OK jouer     AC quitter un jeu",LI,"small")
 for i in range(page*3,min(len(JEUX),page*3+3)):
  x,y=position(i);nom,f,c=JEUX[i]
  if f in vignettes.DESSINS:
   vignettes.DESSINS[f](x,y)
  else:
   vignettes.vignette_autre(x,y,c)
 if len(JEUX)>3:
  draw_string(W-40,H-15,str(page+1)+"/"+str((len(JEUX)+2)//3),TX,"small")
def titre(i):
 rect(0,TY+TH+8,W,24,FD);nom=JEUX[i][0];draw_string(W//2-len(nom)*9,TY+TH+10,nom,JEUX[i][2],"large")
def lancer(f):
 clear_screen();rect(0,0,W,H,FD);draw_string(W//2-60,H//2-10,"Chargement...",TX,"large");show_screen()
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
  elif f=="sudoku":
   import sudoku as m
  elif f=="invasion":
   import invasion as m
  elif f=="envol":
   import envol as m
  elif f=="naval":
   import naval as m
  else:
   m=__import__(f)
  m.jouer()
 except KeyboardInterrupt:
  pass
 except Exception as e:
  clear_screen();rect(0,0,W,H,FD);draw_string(20,60,"Erreur dans "+f+".py",(235,40,50),"large")
  draw_string(20,100,str(e)[:40],TX,"small");draw_string(20,150,"OK pour revenir",LI,"small");show_screen();rl()
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
