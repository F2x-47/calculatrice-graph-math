from casioplot import *
from random import choice

# Pong pour Casio Graph Math+ (casioplot + getkey)
W,H=384,192
PW,PH,B=4,32,5
VJ=3  # vitesse des raquettes des joueurs (pixels par image)
XJ,XC=6,W-10
BG=(255,255,255)
J1=(0,160,255)
J2=(230,0,120)
BA=(255,140,0)
LI=(190,190,190)
TX=(30,30,80)

def rect(x,y,w,h,c):
  for i in range(x,x+w):
    for j in range(y,y+h):
      set_pixel(i,j,c)

def relache():
  n=0
  while n<30:
    if getkey():
      n=0
    else:
      n+=1

def touche(msg,info=""):
  relache()
  clear_screen()
  draw_string(40,70,msg,TX,"large")
  if info:
    draw_string(40,110,info,LI,"medium")
  show_screen()
  k=0
  while not k:
    k=getkey()
  clear_screen()
  draw_string(40,70,"Code touche : "+str(k),TX,"large")
  show_screen()
  relache()
  return k

def filet():
  for y in range(0,H,12):
    rect(W//2-1,y,2,6,LI)

def score(s1,s2):
  rect(W//2-42,4,20,22,BG)
  rect(W//2+22,4,20,22,BG)
  draw_string(W//2-40,4,str(s1),J1,"large")
  draw_string(W//2+26,4,str(s2),J2,"large")

# nom, couleur, vitesse ordi, vitesse balle depart, vitesse max, taille raquette joueur, zone de reaction ordi
NIVEAUX=(
  ("FACILE",(0,190,90),2,2,6,44,W//2),
  ("MOYEN",(255,140,0),3,3,8,32,W//3),
  ("DIFFICILE",(230,0,120),5,4,10,26,0))

def service(sens,v):
  return W//2-2,H//2,v*sens,choice((-2,-1,1,2))

def menu(HAUT,BAS,sel,titre,opts):
  relache()
  nb=len(opts)
  while True:
    clear_screen()
    rect(0,0,W,4,J1)
    rect(0,H-4,W,4,J2)
    draw_string(W//2-80,14,titre,TX,"large")
    for i in range(nb):
      n=opts[i]
      y=60+i*36
      if i==sel:
        rect(W//2-100,y-4,200,30,n[1])
        draw_string(W//2-80,y,"> "+n[0],BG,"large")
      else:
        draw_string(W//2-80,y,"  "+n[0],n[1],"large")
    draw_string(W//2-100,172,"Fleches pour choisir, OK pour valider",LI,"small")
    show_screen()
    k=0
    while not k:
      k=getkey()
    relache()
    if k==HAUT:
      sel=(sel-1)%nb
    elif k==BAS:
      sel=(sel+1)%nb
    else:
      return sel

MODES=(("1 JOUEUR",J1),("2 JOUEURS",J2))

def partie(T,niv,deux):
  nom,coul,VC,V0,VM,PJ,ZONE=NIVEAUX[niv]
  PC=PJ if deux else PH
  s1=s2=0
  py=(H-PJ)//2
  cy=(H-PC)//2
  clear_screen()
  filet()
  rect(XJ,py,PW,PJ,J1)
  rect(XC,cy,PW,PC,J2)
  draw_string(W//2+60,H-14,nom,coul,"small")
  score(s1,s2)
  bx,by,dx,dy=service(1,V0)
  while s1<5 and s2<5:
    # Clavier : plusieurs lectures, mais 1 seul pas par raquette et par image
    m1=m2=0
    for _ in range(4 if deux else 2):
      k=getkey()
      if k==T[0]:
        m1=-1
      elif k==T[1]:
        m1=1
      elif deux and k==T[2]:
        m2=-1
      elif deux and k==T[3]:
        m2=1
    ny=max(0,min(H-PJ,py+m1*VJ))
    if ny!=py:
      rect(XJ,py,PW,PJ,BG)
      py=ny
      rect(XJ,py,PW,PJ,J1)
    if deux:
      ny=max(0,min(H-PC,cy+m2*VJ))
    else:
      # Ordinateur : ne suit la balle que si elle vient vers lui et a passe sa zone
      if dx>0 and bx>ZONE:
        d=by-(cy+PC//2)
      else:
        d=(H-PC)//2-cy
      ny=max(0,min(H-PC,cy+max(-VC,min(VC,d))))
    if ny!=cy:
      rect(XC,cy,PW,PC,BG)
      cy=ny
      rect(XC,cy,PW,PC,J2)
    # Balle
    rect(bx,by,B,B,BG)
    bx+=dx
    by+=dy
    if by<=0 or by>=H-B:
      dy=-dy
      by=max(0,min(H-B,by))
    if dx<0 and XJ-B<=bx<=XJ+PW and py-B<by<py+PJ:
      bx=XJ+PW
      dx=min(-dx+1,VM)
      dy=(by+B//2-py-PJ//2)//5 or choice((-1,1))
    if dx>0 and XC-B<=bx<=XC+PW and cy-B<by<cy+PC:
      bx=XC-B
      dx=max(-dx-1,-VM)
      dy=(by+B//2-cy-PC//2)//5 or choice((-1,1))
    if bx<0 or bx>W-B:
      if bx<0:
        s2+=1
        bx,by,dx,dy=service(1,V0)
      else:
        s1+=1
        bx,by,dx,dy=service(-1,V0)
      score(s1,s2)
    if abs(bx-W//2)<B+4:
      filet()
    if by<28:
      score(s1,s2)
    if by>H-24:
      draw_string(W//2+60,H-14,nom,coul,"small")
    rect(bx,by,B,B,BA)
    show_screen()
  return s1>s2

VE=(0,190,90)
OM=(60,60,90)
LETTRES=(
  ("1110","1001","1110","1000","1000"),
  ("0110","1001","1001","1001","0110"),
  ("1001","1101","1011","1001","1001"),
  ("0111","1000","1011","1001","0111"))

try:
  from time import monotonic as horloge
except:
  horloge=None

def lettre(motif,x,y,s,c):
  for l in range(5):
    for k in range(4):
      if motif[l][k]=="1":
        rect(x+k*s+3,y+l*s+3,s,s,OM)
        rect(x+k*s,y+l*s,s,s,c)

def intro(duree=15):
  clear_screen()
  rect(0,0,W,4,J1)
  rect(0,4,W,4,J2)
  rect(0,H-8,W,4,J2)
  rect(0,H-4,W,4,J1)
  show_screen()
  couleurs=(J1,J2,BA,VE)
  s=9
  x0=(W-(4*4*s+3*12))//2
  for i in range(4):
    lettre(LETTRES[i],x0+i*(4*s+12),22,s,couleurs[i])
    show_screen()
  draw_string(W//2-70,76,"Graph Math+ Edition",TX,"medium")
  draw_string(W//2-62,160,"Appuie pour passer",LI,"small")
  # mini partie animee
  gx,dx=W//2-60,W//2+56
  rect(gx,110,3,20,J1)
  rect(dx,110,3,20,J2)
  bx,by,vx,vy=W//2,118,5,2
  t0=horloge() if horloge else 0
  n=0
  while True:
    rect(bx,by,4,4,BG)
    bx+=vx
    by+=vy
    if bx<=gx+3 or bx>=dx-4:
      vx=-vx
    if by<=106 or by>=130:
      vy=-vy
    rect(bx,by,4,4,couleurs[n//6%4])
    show_screen()
    n+=1
    if getkey():
      break
    if horloge:
      if horloge()-t0>=duree:
        break
    elif n>=270:
      break
  relache()

def jouer():
 intro()
 def choisir(msg,info,prises):
   k=touche(msg,info)
   while k in prises:
     k=touche("Deja prise ! "+msg[:12],info)
   prises.append(k)
   return k

 # Fleches de la calculatrice : haut = 14, bas = 34
 HAUT,BAS=14,34
 T=[HAUT,BAS]
 mode=0
 niv=1
 while True:
   mode=menu(HAUT,BAS,mode,"MODE",MODES)
   deux=mode==1
   if deux and len(T)<4:
     choisir("J2 : touche MONTER","(une touche a droite)",T)
     choisir("J2 : touche DESCENDRE","(une touche a droite)",T)
   niv=menu(HAUT,BAS,niv,"DIFFICULTE",NIVEAUX)
   gagne=partie(T,niv,deux)
   if deux:
     touche("JOUEUR "+("1" if gagne else "2")+" GAGNE !","Touche pour continuer")
   elif gagne:
     touche("GAGNE ! Rejouer ?")
   else:
     touche("PERDU... Rejouer ?")
try:
 import sys
 auto='arcade' not in sys.modules
except:
 auto=True
if auto:
 jouer()
