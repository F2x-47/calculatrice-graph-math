from casioplot import *
from math import sin,cos,pi
W,H=384,192;HA,BA,GA,DR,OK=14,34,23,25,24;BLANC=(255,255,255)
GRIS=(246,247,250);SEP=(222,226,233);NAVY=(28,45,80);SEL=(45,105,190)
FSEL=(226,236,250);TX=(30,35,45);LI=(120,128,140)
VERT,ORANGE,ROUGE=(35,140,80),(205,125,25),(190,55,55)
M=[["Maths",2,[[20,1]]],
 ["Francais",2,[]],
 ["Histoire-Geo",2,[]],
 ["EMC",1,[]],
 ["Anglais",2,[[17,1],[16.5,1]]],
 ["DNL",0.5,[]],
 ["Allemand",2,[]],
 ["Physique-Chimie",2,[[17.25,1]]],
 ["SVT",2,[]],
 ["SES",2,[]],
 ["SISL",0.5,[]],
 ["Management & Gestion",0.5,[]],
 ["Sport",2,[]]]
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
 draw_string(160,58,"MOYENNE",NAVY,"large")
 draw_string(160,84,"Suivi des notes",LI,"medium");show_screen()
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
 draw_string(cx-len(fmt(g))*9,cy-10,fmt(g),c,"large")
 draw_string(cx-21,cy+12,"/ 20",LI,"small")
 draw_string(160,118,"Graph Math+",LI,"small")
 draw_string(160,160,"Appuie sur une touche",LI,"small");show_screen()
 rl()
 while not getkey():
  pass
 rl()
def ligne(y,item,choisi):
 nom,val,c,x,info=item;rect(0,y,W,20,FSEL if choisi else BLANC)
 rect(0,y+20,W,1,SEP)
 if choisi:
  rect(0,y,3,20,SEL)
 draw_string(12,y+3,nom,TX,"medium")
 draw_string(230,y+4,info,LI,"small")
 draw_string(W-12-len(val)*11,y+3,val,c,"medium")
def liste(titre,val,cval,items,sel,aide):
 n=len(items);haut=-1
 while True:
  h=max(0,min(sel-2,n-6))
  if h!=haut:
   if haut==-1:
    clear_screen();rect(0,0,W,40,NAVY)
    draw_string(10,12,titre,BLANC,"medium");lv=len(val)*18+16
    rect(W-10-lv,6,lv,28,BLANC)
    draw_string(W-2-lv,10,val,cval,"large");rect(0,H-18,W,18,GRIS)
    rect(0,H-18,W,1,SEP);draw_string(10,H-14,aide,LI,"small")
   haut=h
   for i in range(6):
    y=46+i*21
    if h+i<n:
     ligne(y,items[h+i],h+i==sel)
    else:
     rect(0,y,W,21,BLANC)
  show_screen();k=touche()
  if k==OK or k==GA:
   return sel,k
  a=sel;sel=(sel+(1 if k==BA else -1 if k==HA else 0))%n
  if max(0,min(sel-2,n-6))==haut:
   ligne(46+(a-haut)*21,items[a],False)
   ligne(46+(sel-haut)*21,items[sel],True)
def boite(titre,h):
 y=(H-h)//2;rect(39,y-1,306,h+2,SEP);rect(40,y,304,h,BLANC)
 rect(40,y,304,24,NAVY);draw_string(50,y+5,titre,BLANC,"medium")
 return y
def choix(titre,opts):
 sel=0;y=boite(titre,34+len(opts)*20)
 while True:
  for i in range(len(opts)):
   rect(48,y+30+i*20,288,18,FSEL if i==sel else BLANC)
   rect(48,y+30+i*20,3,18,SEL if i==sel else BLANC)
   draw_string(56,y+32+i*20,opts[i],TX,"medium")
  show_screen();k=touche()
  if k==OK:
   return sel
  if k==GA:
   return -1
  sel=(sel+(1 if k==BA else -1 if k==HA else 0))%len(opts)
def valeur(titre,v,mini,maxi,pas):
 y=boite(titre,100)
 draw_string(52,y+76,"^v : 1   <> : "+fmt(pas)+"   OK valider",LI,"small")
 while True:
  rect(48,y+32,288,40,BLANC)
  draw_string(W//2-len(fmt(v))*9,y+42,fmt(v),SEL,"large")
  show_screen();k=touche()
  if k==OK:
   return v
  v+={HA:1,BA:-1,GA:-pas,DR:pas}[k];v=max(mini,min(maxi,v))
def matiere(i):
 sel=0
 while True:
  m=M[i];notes=m[2];items=[]
  for j in range(len(notes)):
   n,c=notes[j]
   items.append(("Note "+str(j+1),fmt(n),couleur(n),n,"coef "+fmt(c)))
  items.append(("Coef matiere","",LI,None,"coef "+fmt(m[1])))
  items.append(("Supprimer la matiere","",ROUGE,None,""))
  items.append(("< Retour","",LI,None,""));x=moy(notes)
  aide="^v choisir   OK ouvrir   < retour"
  sel,k=liste(m[0],fmt(x),couleur(x),items,min(sel,len(items)-1),aide)
  j=sel-len(notes)
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
   x=moy(m[2])
   items.append((m[0],fmt(x),couleur(x),x,"coef "+fmt(m[1])))
  if not M:
   items.append(("Aucune matiere","",LI,None,""))
  g=generale();aide="^v choisir   OK ouvrir   AC quitter"
  sel,k=liste("MOYENNE GENERALE",fmt(g),couleur(g),items,min(sel,len(items)-1),aide)
  if k==OK and M:
   matiere(sel)
charger();it();accueil()
