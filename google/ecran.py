from casioplot import *
import latex
W,H=384,192;HA,BA,GA,DR,OK=14,34,23,25,24;BLANC=(255,255,255)
GRIS=(244,245,248);SEP=(220,224,232);TX=(32,33,36);LI=(110,115,125)
def rect(x,y,w,h,c):
 for i in range(x,x+w):
  for j in range(y,y+h):
   set_pixel(i,j,c)
def arrondi(x,y,w,h,c):
 rect(x+3,y,w-6,h,c);rect(x+1,y+1,2,h-2,c);rect(x+w-3,y+1,2,h-2,c)
 rect(x,y+3,1,h-6,c);rect(x+w-1,y+3,1,h-6,c)
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
def texte(t,x,y,c,s=1):
 latex.dessine([("g",ch if ch!=" " else "~") for ch in t],x,y+8*s,s,c)
def decoupe(t,n):
 res=[]
 for par in t.split("|"):
  if par[:2]=="$$":
   res.append(par);continue
  l=""
  for m in par.split(" "):
   if l and len(l)+1+len(m)>n:
    res.append(l);l=m
   else:
    l=(l+" "+m) if l else m
  res.append(l)
 return res
def haut_ligne(l):
 if l[:2]=="$$":
  w,a,d=latex.mesure(latex.analyse(l[2:])[0],1)
  return a+d+6
 return 12
def ligne(l,x,y,c,lg):
 if l[:2]=="$$":
  w,a,d=latex.mesure(latex.analyse(l[2:])[0],1)
  latex.dessine(latex.analyse(l[2:])[0],x+(lg-w)//2,y+3+a,1,c)
 else:
  texte(l,x,y,c)
LIG=("azertyuiop","qsdfghjklm","wxcvbn'-?<"," ")
def clavier(titre,t=""):
 r,c=0,0
 while True:
  rect(0,84,W,108,GRIS);rect(0,84,W,1,SEP);arrondi(8,90,W-16,18,BLANC)
  texte((t+"_")[-58:],14,95,TX)
  for i in range(3):
   for j in range(10):
    x,y=10+j*37,114+i*19;sel=(i==r and j==c)
    arrondi(x,y,34,17,(70,90,200) if sel else BLANC);ch=LIG[i][j]
    texte("DEL" if ch=="<" else ch,x+(14 if ch!="<" else 8),y+4,BLANC if sel else TX)
  for j,(nom,x,w) in enumerate((("espace",10,232),("Envoyer",250,124))):
   sel=(r==3 and j==c)
   arrondi(x,171,w,17,(70,90,200) if sel else BLANC)
   texte(nom,x+w//2-len(nom)*3,175,BLANC if sel else TX)
  show_screen();k=touche()
  if k==HA:
   r=(r-1)%4
  elif k==BA:
   r=(r+1)%4
  elif k==GA:
   c=(c-1)%(2 if r==3 else 10)
  elif k==DR:
   c=(c+1)%(2 if r==3 else 10)
  else:
   if r==3:
    if c==1:
     return t
    t+=" "
   else:
    ch=LIG[r][c];t=t[:-1] if ch=="<" else t+ch
  if r==3:
   c=min(c,1)
