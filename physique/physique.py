from casioplot import *
from math import sin,cos,pi
from latex import formule
import elements
import formules
W,H=384,192;HA,BA,GA,DR,OK=14,34,23,25,24;BLANC=(255,255,255)
GRIS=(246,247,250);SEP=(222,226,233);NAVY=(28,45,80);SEL=(45,105,190)
FSEL=(226,236,250);TX=(30,35,45);LI=(120,128,140)
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
def entete(titre,aide):
 clear_screen();rect(0,0,W,30,NAVY)
 draw_string(10,8,titre,BLANC,"medium");rect(0,H-18,W,18,GRIS)
 rect(0,H-18,W,1,SEP);draw_string(10,H-14,aide,LI,"small")
def liste(titre,noms,sel,aide):
 n=len(noms);haut=-1
 while True:
  h=max(0,min(sel-3,n-7))
  if h!=haut:
   if haut==-1:
    entete(titre,aide)
   haut=h
   for i in range(7):
    ligne(h+i,noms,sel,haut)
  show_screen();k=touche()
  if k in (OK,GA,DR):
   return sel,k
  a=sel;sel=(sel+(1 if k==BA else -1))%n
  if max(0,min(sel-3,n-7))==haut:
   ligne(a,noms,sel,haut);ligne(sel,noms,sel,haut)
def ligne(i,noms,sel,haut):
 y=34+(i-haut)*20;rect(0,y,W,19,FSEL if i==sel else BLANC)
 rect(0,y+19,W,1,SEP)
 if i<len(noms):
  if i==sel:
   rect(0,y,3,19,SEL)
  draw_string(12,y+3,noms[i],TX,"medium")
FAM={"a":("Metaux alcalins",(244,170,160)),"t":("Alcalino-terreux",(246,206,150)),
  "m":("Metaux de transition",(240,195,210)),"p":("Metaux pauvres",(190,215,232)),
  "s":("Metalloides",(200,225,180)),"n":("Non-metaux",(175,222,200)),
  "h":("Halogenes",(238,232,150)),"g":("Gaz nobles",(205,192,238)),
  "l":("Lanthanides",(200,232,240)),"c":("Actinides",(232,214,190))}
EL=[e.split(",") for e in elements.E.split(";")]
CW,CH0,X0,Y0=20,15,12,33
def place(z):
 if z==1:
  return 0,0
 if z==2:
  return 0,17
 for p,d in ((1,3),(2,11),(3,19),(4,37),(5,55),(6,87)):
  if z<d+(8 if p<3 else 18 if p<5 else 32):
   i=z-d
   break
 if p<3:
  return p,(i if i<2 else i+10)
 if p<5:
  return p,i
 if 2<=i<=16:
  return p+2,i+1
 return p,(i if i<2 else i-14)
POS={}
for z in range(1,119):
 POS[place(z)]=z
def config(z):
 if z>36:
  return ""
 if z==24:
  return r"1s^2 2s^2 2p^6 3s^2 3p^6 4s^1 3d^5"
 if z==29:
  return r"1s^2 2s^2 2p^6 3s^2 3p^6 4s^1 3d^{10}"
 r=[]
 for (o,m) in (("1s",2),("2s",2),("2p",6),("3s",2),("3p",6),("4s",2),("3d",10),("4p",6)):
  if z<=0:
   break
  r.append(o+"^{"+str(min(m,z))+"}");z-=m
 return " ".join(r)
def cs(z,choisi):
 l,c=place(z);x,y=X0+c*CW,Y0+l*CH0+(4 if l>6 else 0);e=EL[z-1]
 rect(x,y,CW-1,CH0-1,SEL if choisi else FAM[e[3]][1])
 draw_string(x+2,y+2,e[0],BLANC if choisi else TX,"small")
def info(z):
 e=EL[z-1];x,y=X0+2*CW+4,Y0+1;rect(x,y,10*CW-8,3*CH0-2,BLANC)
 rect(x,y,38,38,FAM[e[3]][1]);draw_string(x+4,y+2,str(z),TX,"small")
 draw_string(x+19-len(e[0])*9,y+14,e[0],TX,"large")
 draw_string(x+46,y+2,e[1],TX,"medium")
 draw_string(x+46,y+18,"M = "+e[2]+" g/mol",LI,"small")
 draw_string(x+46,y+30,FAM[e[3]][0],LI,"small")
def tableau():
 z=1
 while True:
  z=tableau_z(z)
  if not z:
   return
  detail(z)
def tableau_z(z):
 entete("TABLEAU PERIODIQUE","fleches : deplacer   OK : details   < au bord : retour")
 for k in range(1,119):
  cs(k,False)
 while True:
  cs(z,True);info(z);show_screen();k=touche();l,c=place(z)
  if k==GA and c==0:
   return 0
  dl,dc={HA:(-1,0),BA:(1,0),GA:(0,-1),DR:(0,1),OK:(0,0)}[k]
  if k==OK:
   return z
  nz=0
  while not nz:
   l+=dl;c+=dc
   if l<0 or l>8 or c<0 or c>17:
    break
   nz=POS.get((l,c),0)
   if dl and not nz:
    for e in range(1,18):
     nz=POS.get((l,c-e),0) or POS.get((l,c+e),0)
     if nz:
      break
  if nz:
   cs(z,False);z=nz
def detail(z):
 e=EL[z-1];l,c=place(z);entete(e[1].upper(),"< ou OK : retour")
 rect(14,40,92,92,FAM[e[3]][1]);draw_string(20,44,str(z),TX,"medium")
 draw_string(60-len(e[0])*9,74,e[0],TX,"large")
 draw_string(20,112,e[2],TX,"small");x=120
 ln=(("Numero atomique","Z = "+str(z)),("Masse molaire",e[2]+" g/mol"),("Famille",FAM[e[3]][0]),
     ("Periode",str(l+1 if l<7 else l-1)),("Groupe",str(c+1) if l<7 else "3 (bloc f)"))
 for i in range(5):
  draw_string(x,40+i*16,ln[i][0],LI,"small")
  draw_string(x+120,40+i*16,ln[i][1],TX,"small")
 cf=config(z)
 if cf:
  draw_string(x,124,"Configuration electronique",LI,"small")
  formule(cf,(x+W)//2,150,1,SEL)
 show_screen();k=0
 while k not in (OK,GA):
  k=touche()
def fiche(i):
 while True:
  f=formules.F[i];entete(f[1],"^v : formule suivante   < : retour")
  rect(10,38,W-20,78,GRIS);formule(f[2],W//2,77,2,NAVY)
  lg=f[3].split("|")
  for j in range(len(lg)):
   draw_string(14,122+j*16,lg[j],TX,"small")
  show_screen();k=touche()
  if k in (GA,OK):
   return
  i=(i+(1 if k==BA else -1 if k==HA else 0))%len(formules.F)
def menu_formules():
 sc=0
 while True:
  sc,k=liste("FORMULES",formules.CAT,sc,"^v : choisir   OK : ouvrir   < : retour")
  if k==GA:
   return
  idx=[i for i in range(len(formules.F)) if formules.F[i][0]==sc];sf=0
  while True:
   sf,k=liste(formules.CAT[sc].upper(),[formules.F[i][1] for i in idx],sf,"OK : voir la formule   < : retour")
   if k==GA:
    break
   fiche(idx[sf])
def it():
 clear_screen();cx,cy=80,96;rect(cx-6,cy-6,13,13,SEL)
 draw_string(150,52,"PHYSIQUE",NAVY,"large")
 draw_string(150,76,"CHIMIE",NAVY,"large")
 draw_string(150,102,"Tableau periodique et formules",LI,"small")
 for a in range(0,360,4):
  t=a*pi/180
  for o in range(3):
   p=o*pi/3;x,y=52*cos(t),18*sin(t)
   rect(int(cx+x*cos(p)-y*sin(p)),int(cy+x*sin(p)+y*cos(p)),2,2,NAVY)
  if a<=184:
   rect(150+a,118,4,2,SEL)
  if a%40==0:
   show_screen()
 for o in range(3):
  p=o*pi/3+0.6
  rect(int(cx+52*cos(p)*cos(o*pi/3)-18*sin(p)*sin(o*pi/3))-3,int(cy+52*cos(p)*sin(o*pi/3)+18*sin(p)*cos(o*pi/3))-3,7,7,(190,55,55))
 draw_string(150,126,"Graph Math+",LI,"small")
 draw_string(150,160,"Appuie sur une touche",LI,"small");show_screen()
 rl()
 while not getkey():
  pass
def accueil():
 it();sel=0
 while True:
  mn=["Tableau periodique","Formules","Tableaux de conversion","Convertisseur d'unites"]
  sel,k=liste("PHYSIQUE-CHIMIE",mn,sel,"^v : choisir   OK : ouvrir   AC : quitter")
  if k==OK:
   if sel==0:
    tableau()
   elif sel==1:
    menu_formules()
   else:
    import conversion
    if sel==2:
     conversion.tableaux(liste)
    else:
     conversion.convertisseur(liste)
accueil()
