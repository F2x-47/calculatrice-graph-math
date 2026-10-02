from casioplot import *
import moteur
W,H=384,192;HA,BA,GA,DR,OK=14,34,23,25,24;FD=(20,20,45);TX=(255,255,255);LI=(170,170,200);OM=(60,60,90)
CLAIR=(236,214,176);SOMBRE=(176,128,86);SELC=(120,180,90);DERN=(214,200,90);CURS=(0,200,230)
CO=((0,200,230),(250,210,0),(240,70,90),(40,200,70),(160,60,220),(255,140,0),(0,200,230));C=22;X0,Y0=8,8
DESSIN={"P":(0,0,0,192,480,480,192,480,1008,480,480,1008,2040,4092,0,0),
"R":(0,0,3510,4092,4092,2040,1008,1008,1008,1008,1008,2040,4092,4092,0,0),
"N":(0,128,480,1008,2040,3964,4088,248,496,992,1008,2040,4092,4092,0,0),
"B":(0,192,480,944,880,1008,480,192,480,480,1008,2040,4092,4092,0,0),
"Q":(0,2340,2340,3510,4092,2040,1008,1008,1008,480,1008,2040,4092,4092,0,0),
"K":(192,1008,192,1008,2040,4092,4092,2040,1008,480,1008,2040,4092,4092,0,0)}
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
def piece(x,y,p):
 d=DESSIN[p.upper()];rempl,bord=((250,248,240),(30,30,40)) if p.isupper() else ((45,40,50),(225,220,210))
 for r in range(16):
  v=d[r];a=(d[r-1] if r>0 else 0)|(d[r+1] if r<15 else 0)|(v<<1)|(v>>1)
  for c in range(14):
   b=1<<(13-c)
   if v&b:
    set_pixel(x+c,y+r,rempl)
   elif a&b:
    set_pixel(x+c,y+r,bord)
def cs(pos,l,c,marque=None,point=False,curseur=False):
 x,y=X0+c*C,Y0+l*C;rect(x,y,C,C,marque if marque else (CLAIR if (l+c)%2==0 else SOMBRE));p=pos[0][21+10*l+c]
 if p!=".":
  piece(x+4,y+3,p)
 if point:
  rect(x+8,y+8,6,6,(70,110,60))
 if curseur:
  rect(x,y,C,2,CURS);rect(x,y+C-2,C,2,CURS);rect(x,y,2,C,CURS);rect(x+C-2,y,2,C,CURS)
def nom_case(s):
 return "abcdefgh"[s%10-1]+str(10-s//10)
def panneau(pos,msg,mode,dernier):
 x=X0+8*C+12;rect(x,0,W-x,H,FD);draw_string(x,10,"ECHECS",CO[1],"large")
 draw_string(x,36,("Ordinateur : "+("Facile","Moyen","Difficile")[mode-1]) if mode else "2 joueurs",LI,"small")
 tour="Trait aux blancs" if pos[1]=="w" else "Trait aux noirs"
 rect(x,58,12,12,(250,248,240) if pos[1]=="w" else (45,40,50));rect(x,58,12,1,LI);draw_string(x+18,58,tour,TX,"small")
 if dernier:
  draw_string(x,80,"Dernier coup : "+nom_case(dernier[0])+"-"+nom_case(dernier[1]),LI,"small")
 e=moteur.evalue(pos[0]);draw_string(x,98,"Materiel : "+("+" if e>=0 else "")+str(e//100),LI,"small")
 if msg:
  draw_string(x,124,msg,CO[2],"medium")
 draw_string(x,160,"Fleches : deplacer",LI,"small");draw_string(x,174,"OK : choisir / jouer",LI,"small")
def plateau(pos,dernier):
 rect(0,0,X0+8*C+12,H,FD)
 for l in range(8):
  for c in range(8):
   cs(pos,l,c,DERN if dernier and 21+10*l+c in dernier[:2] else None)
 for i in range(8):
  draw_string(X0+8*C+2,Y0+i*C+6,str(8-i),LI,"small")
def pt(mode):
 pos=moteur.depart();l,c=6,4;sel=None;cibles=[];dernier=None;msg="";plateau(pos,dernier)
 while True:
  legal=moteur.legaux(pos)
  if not legal:
   msg="ECHEC ET MAT !" if moteur.echec(pos) else "PAT : nulle"
  elif moteur.echec(pos):
   msg="Echec !"
  panneau(pos,msg,mode,dernier)
  if not legal:
   show_screen();fin(msg,pos[1])
   return
  msg=""
  if mode and pos[1]=="b":
   draw_string(X0+8*C+12,124,"Je reflechis...",CO[1],"medium");show_screen();m=moteur.ordi(pos,mode-1)
   pos=moteur.joue(pos,m);dernier=m;plateau(pos,dernier);continue
  cs(pos,l,c,curseur=True);show_screen();k=touche();s=21+10*l+c
  if k==OK:
   if sel and s in [m[1] for m in cibles]:
    m=[m for m in cibles if m[1]==s][0];pos=moteur.joue(pos,m);dernier=m;sel=None;cibles=[];plateau(pos,dernier)
    continue
   ancien=cibles+([(0,sel,0)] if sel else [])
   if moteur.a_moi(pos[0][s],pos[1]) and s!=sel:
    sel=s;cibles=[m for m in legal if m[0]==s]
   else:
    sel=None;cibles=[]
   for m in ancien:
    q=m[1];cs(pos,q//10-2,q%10-1,DERN if dernier and q in dernier[:2] else None)
   if sel:
    cs(pos,l,c,SELC)
    for m in cibles:
     q=m[1];cs(pos,q//10-2,q%10-1,point=True)
   continue
  q=s;cs(pos,l,c,SELC if s==sel else (DERN if dernier and s in dernier[:2] else None),point=s in [m[1] for m in cibles])
  l=(l+(1 if k==BA else -1 if k==HA else 0))%8;c=(c+(1 if k==DR else -1 if k==GA else 0))%8
def fin(msg,perdant):
 rect(60,64,264,64,FD);rect(60,64,264,3,CO[1]);rect(60,125,264,3,CO[1]);draw_string(80,72,msg,CO[1],"large")
 if "MAT" in msg:
  draw_string(80,102,("Les noirs" if perdant=="w" else "Les blancs")+" gagnent",TX,"medium")
 show_screen();rl()
 while getkey()!=OK:
  pass
LT=(
 ("11111","10000","11110","10000","11111"),
 ("01111","10000","10000","10000","01111"),
 ("10001","10001","11111","10001","10001"),
 ("11111","10000","11110","10000","11111"),
 ("01111","10000","10000","10000","01111"),
 ("01111","10000","01110","00001","11110"))
def it():
 clear_screen();rect(0,0,W,H,FD);s=7;x0=(W-(6*5*s+5*7))//2
 for i in range(6):
  for li in range(5):
   for k in range(5):
    if LT[i][li][k]=="1":
     x,y=x0+i*(5*s+7)+k*s,14+li*s;rect(x+2,y+2,s,s,OM);rect(x,y,s,s,CO[i]);rect(x,y,s,2,(255,255,255))
  show_screen()
 draw_string(20,60,"GRAPH MATH+ EDITION",TX,"large");rect(20,84,344,3,CO[1])
 for i in range(8):
  rect(56+i*34,104,34,34,CLAIR if i%2==0 else SOMBRE)
 for i in range(8):
  piece(66+i*34,113,"rNbQkBnR"[i]);show_screen()
 draw_string(W//2-62,170,"Appuie sur une touche",LI,"small");show_screen();touche()
def mn(sel):
 opts=(("2 JOUEURS",CO[0]),("ORDI FACILE",CO[3]),("ORDI MOYEN",CO[5]),("ORDI DIFFICILE",CO[2]))
 while True:
  clear_screen();rect(0,0,W,H,FD);draw_string(W//2-60,8,"MODE",TX,"large")
  for i in range(4):
   nom,c=opts[i];y=44+i*30
   if i==sel:
    rect(W//2-130,y-4,260,26,c);draw_string(W//2-110,y,"> "+nom,FD,"large")
   else:
    draw_string(W//2-110,y,"  "+nom,c,"large")
  draw_string(W//2-130,172,"Fleches pour choisir, OK pour jouer",LI,"small");show_screen();k=touche()
  if k==OK:
   return sel
  if k in (HA,BA):
   sel=(sel+(1 if k==BA else -1))%4
def jouer():
 it();sel=0
 while True:
  sel=mn(sel);pt(sel)
try:
 import sys
 auto='arcade' not in sys.modules
except:
 auto=True
if auto:
 jouer()
