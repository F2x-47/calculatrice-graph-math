from casioplot import *
from latex import formule
W,H=384,192;HA,BA,GA,DR,OK=14,34,23,25,24;BLANC=(255,255,255);SEP=(222,226,233);NAVY=(28,45,80);SEL=(45,105,190)
TX=(30,35,45);LI=(120,128,140);ROUGE=(190,55,55)
def rect(x,y,w,h,c):
 for i in range(x,x+w):
  for j in range(y,y+h):
   set_pixel(i,j,c)
try:
 from time import monotonic as hz
except:
 hz=None
dern=[0,0,0]
def touche(rep=(HA,BA)):
 z=0
 while True:
  k=getkey()
  if k in (HA,BA,GA,DR,OK):
   z=0
   if k!=dern[0]:
    dern[0]=k;dern[1]=0;dern[2]=hz()+0.4 if hz else 0
    return k
   if k in rep:
    dern[1]+=1
    if hz:
     if hz()>=dern[2]:
      dern[2]=hz()+0.07
      return k
    elif dern[1]>150:
     dern[1]=125
     return k
  else:
   z+=1
   if z>3:
    dern[0]=0
def page(titre,aide):
 clear_screen();draw_string(10,10,titre,NAVY,"medium");rect(0,34,W,2,NAVY);rect(0,H-18,W,1,SEP)
 draw_string(10,H-14,aide,LI,"small")
def ligne(y,nom,choisi):
 rect(0,y,4,17,SEL if choisi else BLANC);rect(0,y+18,W,1,SEL if choisi else SEP)
 draw_string(12,y+2,nom,SEL if choisi else TX,"medium")
def liste(titre,noms,sel,aide="^v : choisir   OK : ouvrir   < : retour"):
 n=len(noms);haut=-1
 while True:
  h=max(0,min(sel-3,n-7))
  if h!=haut:
   haut=h;page(titre,aide)
   for i in range(min(7,n-h)):
    ligne(40+i*19,noms[h+i],h+i==sel)
  show_screen();k=touche()
  if k==OK or k==GA:
   return sel,k
  if k==DR:
   continue
  a=sel;sel=(sel+(1 if k==BA else -1))%n
  if max(0,min(sel-3,n-7))==haut:
   ligne(40+(a-haut)*19,noms[a],False);ligne(40+(sel-haut)*19,noms[sel],True)
def joli(x):
 if abs(x-round(x))<1e-9 and abs(x)<1e12:
  return str(int(round(x)))
 return "%.6g"%x
CLAV=("789<","456C","123-","0.")
def saisie(titre,fin="RETOUR"):
 t="";r=c=0
 while True:
  page(titre,"fleches : choisir une touche   OK : appuyer");draw_string(24,44,t+"_",SEL,"large")
  for i in range(4):
   for j in range(4):
    if i==3 and j>1:
     nom=(fin,"VALIDER")[j-2]
    else:
     nom={"<":"EFF","C":"VIDER","-":"+/-"}.get(CLAV[i][j],CLAV[i][j])
    x,y=24+j*88,74+i*24;draw_string(x+6,y+3,nom,ROUGE if (i==3 and j==2) else TX,"medium")
    if i==r and j==c:
     rect(x,y,82,2,SEL);rect(x,y+20,82,2,SEL);rect(x,y,2,22,SEL);rect(x+80,y,2,22,SEL)
  show_screen();k=touche((HA,BA,GA,DR))
  if k==HA:
   r=(r-1)%4
  elif k==BA:
   r=(r+1)%4
  elif k==GA:
   c=(c-1)%4
  elif k==DR:
   c=(c+1)%4
  elif r==3 and c==2:
   return None
  elif r==3 and c==3:
   if t not in ("","-","."):
    return t
  else:
   ch=CLAV[r][c]
   if ch=="<":
    t=t[:-1]
   elif ch=="C":
    t=""
   elif ch=="-":
    t=t[1:] if t[:1]=="-" else "-"+t
   elif ch!="." or "." not in t:
    if len(t)<12:
     t+=ch
def nombre(titre,entier=False):
 while True:
  t=saisie(titre)
  if t==None:
   return None
  try:
   v=float(t)
   if entier:
    if v!=int(v) or v<1:
     continue
    return int(v)
   return v
  except:
   pass
def pause():
 show_screen();k=0
 while k not in (OK,GA):
  k=touche()
