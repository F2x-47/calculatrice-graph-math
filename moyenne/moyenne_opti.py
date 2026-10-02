from casioplot import *
from math import sin,cos,pi
W,H=384,192;HA,BA,GA,DR,OK=14,34,23,25,24;BLANC=(255,255,255);GRIS=(246,247,250);SEP=(222,226,233);NAVY=(28,45,80)
SEL=(45,105,190);FSEL=(226,236,250);TX=(30,35,45);LI=(120,128,140)
VERT,ORANGE,ROUGE=(35,140,80),(205,125,25),(190,55,55)
M=[["Maths",2,[[20,1]]],["Francais",2,[]],["Histoire-Geo",2,[]],["EMC",1,[]],
 ["Anglais",2,[[17,1],[16.5,1]]],["DNL",0.5,[]],["Allemand",2,[]],
 ["Physique-Chimie",2,[[17.25,1]]],["SVT",2,[]],["SES",2,[]],["SISL",0.5,[]],
 ["Eco-Gestion",0.5,[]],["Sport",2,[]]]
def sauver():
 try:
  f=open("notes.txt","w");f.write(repr(M));f.close()
 except:
  pass
def charger():
 global M
 try:
  f=open("notes.txt");M=eval(f.read());f.close()
 except:
  pass
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
def rl():
 n=0
 while n<30:
  if getkey():
   n=0
  else:
   n+=1
def moy(notes):
 s=c=0
 for (n,k) in notes:
  s+=n*k;c+=k
 return s/c if c else None
def generale():
 s=c=0
 for m in M:
  x=moy(m[2])
  if x!=None:
   s+=x*m[1];c+=m[1]
 return s/c if c else None
def fmt(x):
 if x==None:
  return "-"
 s="%.2f"%x
 return s.rstrip("0").rstrip(".")
def couleur(x):
 if x==None:
  return LI
 return VERT if x>=14 else (ORANGE if x>=10 else ROUGE)
def it():
 clear_screen();g=generale();c=couleur(g);cx,cy,R=92,96,46
 for a in range(0,360,3):
  t=a*pi/180;rect(int(cx+R*sin(t))-2,int(cy-R*cos(t))-2,5,5,SEP)
 draw_string(160,58,"MOYENNE",NAVY,"large");draw_string(160,84,"Suivi des notes",LI,"medium");show_screen()
 fin=int(360*(g if g!=None else 0)/20);n=0
 for a in range(0,361,3):
  if a<=fin:
   t=a*pi/180;rect(int(cx+R*sin(t))-2,int(cy-R*cos(t))-2,5,5,c)
  if n<184:
   rect(160+n,110,4,2,SEL);n+=4
  if a%30==0:
   show_screen()
  if getkey():
   break
 draw_string(cx-len(fmt(g))*9,cy-10,fmt(g),c,"large");draw_string(cx-21,cy+12,"/ 20",LI,"small")
 draw_string(160,118,"Graph Math+",LI,"small");draw_string(160,160,"Appuie sur une touche",LI,"small");show_screen()
 rl()
 while not getkey():
  pass
 rl()
def page(titre,val,cval,aide):
 clear_screen();draw_string(10,12,titre,NAVY,"medium");draw_string(W-10-len(val)*18,8,val,cval,"large")
 rect(0,38,W,2,NAVY);rect(0,H-18,W,1,SEP);draw_string(10,H-14,aide,LI,"small")
def ligne(y,item,choisi,neuf=True):
 nom,val,c,x,info=item;rect(0,y,4,19,SEL if choisi else BLANC);rect(0,y+20,W,1,SEL if choisi else SEP)
 draw_string(12,y+3,nom,SEL if choisi else TX,"medium")
 if neuf:
  draw_string(230,y+4,info,LI,"small");draw_string(W-12-len(val)*11,y+3,val,c,"medium")
def liste(titre,val,cval,items,sel,aide):
 n=len(items);haut=-1
 while True:
  h=max(0,min(sel-2,n-6))
  if h!=haut:
   haut=h;page(titre,val,cval,aide)
   for i in range(min(6,n-h)):
    ligne(44+i*21,items[h+i],h+i==sel)
  show_screen();k=touche()
  if k==OK or k==GA:
   return sel,k
  a=sel;sel=(sel+(1 if k==BA else -1 if k==HA else 0))%n
  if max(0,min(sel-2,n-6))==haut:
   ligne(44+(a-haut)*21,items[a],False,False);ligne(44+(sel-haut)*21,items[sel],True,False)
def choix(titre,opts):
 sel,k=liste(titre,"",LI,[(o,"",LI,None,"") for o in opts],0,"^v choisir   OK valider   < annuler")
 return -1 if k==GA else sel
def valeur(titre,v,mini,maxi,pas):
 aide="^v : 1     < > : "+fmt(pas)+"     OK valider"
 while True:
  page(titre,"",LI,aide);draw_string(W//2-len(fmt(v))*9,84,fmt(v),SEL,"large");rect(W//2-50,112,100,2,SEL);show_screen()
  k=touche((HA,BA,GA,DR))
  if k==OK:
   return v
  v+={HA:1,BA:-1,GA:-pas,DR:pas}[k];v=max(mini,min(maxi,v))
def matiere(i):
 sel=0
 while True:
  m=M[i];notes=m[2];items=[]
  for j in range(len(notes)):
   n,c=notes[j];items.append(("Note "+str(j+1),fmt(n),couleur(n),n,"coef "+fmt(c)))
  items.append(("Coef matiere","",LI,None,"coef "+fmt(m[1])));items.append(("Supprimer la matiere","",ROUGE,None,""))
  items.append(("< Retour","",LI,None,""));x=moy(notes);aide="^v choisir   OK ouvrir   < retour"
  sel,k=liste(m[0],fmt(x),couleur(x),items,min(sel,len(items)-1),aide);j=sel-len(notes)
  if k==GA or j==2:
   return
  if j==0:
   m[1]=valeur("Coef de "+m[0],m[1],0.5,10,0.5)
  elif j==1:
   if choix("Supprimer "+m[0]+" ?",["Non","Oui, supprimer"])==1:
    del M[i];sauver()
    return
  else:
   r=choix("Note "+str(sel+1)+" : "+fmt(notes[sel][0]),["Modifier","Supprimer","Annuler"])
   if r==0:
    notes[sel][0]=valeur("Note /20",notes[sel][0],0,20,0.25)
    notes[sel][1]=valeur("Coef de la note",notes[sel][1],0.5,10,0.5)
   elif r==1:
    del notes[sel]
  sauver()
def accueil():
 sel=0
 while True:
  items=[]
  for m in M:
   x=moy(m[2]);items.append((m[0],fmt(x),couleur(x),x,"coef "+fmt(m[1])))
  if not M:
   items.append(("Aucune matiere","",LI,None,""))
  g=generale();aide="^v choisir   OK ouvrir   AC quitter"
  sel,k=liste("MOYENNE GENERALE",fmt(g),couleur(g),items,min(sel,len(items)-1),aide)
  if k==OK and M:
   matiere(sel)
charger();it();accueil()
