from casioplot import *
from random import randint
W,H=384,192;HA,BA,GA,DR,OK=14,34,23,25,24;FD=(20,20,45)
TX=(255,255,255);LI=(170,170,200);OM=(60,60,90)
CO=((0,200,230),(250,210,0),(240,70,90),(40,200,70),(160,60,220),(255,140,0),(0,200,230))
C=20;X0,Y0=6,6;CASE=(246,244,236);CASE2=(232,228,214)
SELC=(150,210,240);MEME=(210,230,245);DONNE=(28,30,60)
JOUE=(40,100,200);FAUX=(220,50,60)
CH=((14,17,19,21,25,17,14),(4,12,4,4,4,4,14),(14,17,1,2,4,8,31),(31,2,4,2,1,17,14),(2,6,10,18,31,2,2),
  (31,16,30,1,1,17,14),(6,8,16,30,17,17,14),(31,1,2,4,8,8,8),(14,17,17,14,17,17,14),(14,17,17,15,1,2,12))
def rect(x,y,w,h,c):
 for i in range(x,x+w):
  for j in range(y,y+h):
   set_pixel(i,j,c)
def chiffre(n,x,y,c,s=2):
 for r in range(7):
  v=CH[n][r]
  for k in range(5):
   if v>>(4-k)&1:
    rect(x+k*s,y+r*s,s,s,c)
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
def melange(l):
 for i in range(len(l)-1,0,-1):
  j=randint(0,i);l[i],l[j]=l[j],l[i]
 return l
def solution():
 b=[[(r*3+r//3+c)%9+1 for c in range(9)] for r in range(9)];rows=[]
 for bd in melange([0,1,2]):
  rows+=[bd*3+i for i in melange([0,1,2])]
 cols=[]
 for st in melange([0,1,2]):
  cols+=[st*3+i for i in melange([0,1,2])]
 p=melange(list(range(1,10)))
 return [[p[b[r][c]-1] for c in cols] for r in rows]
def conflit(g,r,c):
 v=g[r][c]
 if not v:
  return False
 for i in range(9):
  if (i!=c and g[r][i]==v) or (i!=r and g[i][c]==v):
   return True
 br,bc=r//3*3,c//3*3
 for i in range(br,br+3):
  for j in range(bc,bc+3):
   if (i,j)!=(r,c) and g[i][j]==v:
    return True
 return False
def cs(g,fixe,r,c,sel):
 x,y=X0+c*C,Y0+r*C;v=g[r][c]
 fondc=CASE if ((r//3+c//3)%2==0) else CASE2
 if (r,c)==sel:
  fondc=SELC
 elif v and g[sel[0]][sel[1]]==v:
  fondc=MEME
 rect(x+1,y+1,C-1,C-1,fondc)
 if v:
  chiffre(v,x+6,y+4,FAUX if conflit(g,r,c) else (DONNE if fixe[r][c] else JOUE))
def grille(g,fixe,sel):
 rect(X0,Y0,9*C+1,9*C+1,(150,150,170))
 for i in range(0,10,3):
  rect(X0+i*C-1,Y0-1,2,9*C+2,DONNE);rect(X0-1,Y0+i*C-1,9*C+2,2,DONNE)
 for r in range(9):
  for c in range(9):
   cs(g,fixe,r,c,sel)
def panneau(nom,coul,vides,msg):
 x=X0+9*C+14;rect(x,0,W-x,H,FD)
 draw_string(x,8,"SUDOKU",CO[1],"large")
 draw_string(x,34,nom,coul,"small")
 draw_string(x,52,"Cases vides : "+str(vides),TX,"small")
 if msg:
  draw_string(x,74,msg,CO[2],"small")
 draw_string(x,150,"Fleches : deplacer",LI,"small")
 draw_string(x,166,"OK : ecrire un chiffre",LI,"small")
def choisir(x0,y0):
 i=4
 while True:
  rect(x0,y0,120,108,OM)
  for k in range(10):
   x,y=x0+6+(k%3)*38,y0+6+(k//3)*25;w=110 if k==9 else 34
   rect(x,y,w,21,CO[0] if k==i else (40,40,80))
   if k<9:
    chiffre(k+1,x+12,y+3,TX)
   else:
    draw_string(x+28,y+3,"Effacer",TX,"small")
  show_screen();k=touche()
  if k==OK:
   return 0 if i==9 else i+1
  if k==GA:
   i=(i-1)%10
  elif k==DR:
   i=(i+1)%10
  elif k==HA:
   i=7 if i==9 else (i-3 if i>2 else 9)
  else:
   i=1 if i==9 else (i+3 if i<6 else 9)
def pt(niv):
 nom,coul,trous=NV[niv];sol=solution();g=[l[:] for l in sol];n=0
 while n<trous:
  r,c=randint(0,8),randint(0,8)
  if g[r][c]:
   g[r][c]=0;n+=1
 fixe=[[v!=0 for v in l] for l in g];sel=(4,4);clear_screen()
 rect(0,0,W,H,FD);grille(g,fixe,sel)
 while True:
  vides=sum(l.count(0) for l in g)
  faux=any(conflit(g,r,c) for r in range(9) for c in range(9))
  panneau(nom,coul,vides,"Il y a une erreur" if faux else "")
  if vides==0 and not faux:
   show_screen()
   return
  show_screen();k=touche();r,c=sel
  if k==OK:
   if not fixe[r][c]:
    v=choisir(X0+9*C+12,40)
    if v!=None:
     g[r][c]=v
    grille(g,fixe,sel)
   continue
  a=sel
  sel=((r+(1 if k==BA else -1 if k==HA else 0))%9,(c+(1 if k==DR else -1 if k==GA else 0))%9)
  vo=g[a[0]][a[1]];vn=g[sel[0]][sel[1]]
  for i in range(9):
   for j in range(9):
    if (i,j) in (a,sel) or (g[i][j] and g[i][j] in (vo,vn)):
     cs(g,fixe,i,j,sel)
NV=(("FACILE",CO[3],36),("MOYEN",CO[5],46),("DIFFICILE",CO[2],53))
LT=(
 ("01111","10000","01110","00001","11110"),
 ("10001","10001","10001","10001","01110"),
 ("11110","10001","10001","10001","11110"),
 ("01110","10001","10001","10001","01110"),
 ("10001","10010","11100","10010","10001"),
 ("10001","10001","10001","10001","01110"))
def it():
 clear_screen();rect(0,0,W,H,FD);s=7;x0=(W-(6*5*s+5*7))//2
 for i in range(6):
  for l in range(5):
   for k in range(5):
    if LT[i][l][k]=="1":
     x,y=x0+i*(5*s+7)+k*s,14+l*s;rect(x+2,y+2,s,s,OM)
     rect(x,y,s,s,CO[i]);rect(x,y,s,2,(255,255,255))
  show_screen()
 draw_string(20,60,"GRAPH MATH+ EDITION",TX,"large")
 rect(20,84,344,3,CO[3])
 for i in range(9):
  rect(57+i*30,108,28,28,CASE)
 for i,v in enumerate((5,3,9,1,7,2,8,6,4)):
  chiffre(v,66+i*30,115,JOUE);show_screen()
 draw_string(W//2-62,170,"Appuie sur une touche",LI,"small")
 show_screen();touche()
def mn(sel):
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
  show_screen();k=touche()
  if k==OK:
   return sel
  if k in (HA,BA):
    sel=(sel+(1 if k==BA else -1))%3
def jouer():
 #it();sel=0
 sel=0
 while True:
  sel=mn(sel);pt(sel);rect(60,64,264,64,FD);rect(60,64,264,3,CO[3])
  rect(60,125,264,3,CO[3]);draw_string(110,72,"BRAVO !",CO[3],"large")
  draw_string(80,102,"Grille terminee",TX,"medium");show_screen();rl()
  while getkey()!=OK:
   pass
try:
 import sys
 auto='arcade' not in sys.modules
except:
 auto=True
if auto:
 jouer()
