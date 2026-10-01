from casioplot import *
import latex
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
def tex(t,x,y,c,s=1,centre=False):
 n=latex.analyse(t)[0]
 if centre:
  x-=latex.mesure(n,s)[0]//2
 latex.dessine(n,x,y+8*s,s,c)
U=[
("Longueur",[("km",1e3),("m",1),("dm",0.1),("cm",0.01),("mm",1e-3),("um",1e-6),("nm",1e-9),("UA",1.496e11),("al",9.461e15)]),
("Masse",[("t",1e3),("kg",1),("g",1e-3),("mg",1e-6),("ug",1e-9)]),
("Volume",[("m^3",1e3),("dm^3",1),("L",1),("dL",0.1),("cL",0.01),("mL",1e-3),("cm^3",1e-3)]),
("Temps",[("an",31557600),("j",86400),("h",3600),("min",60),("s",1),("ms",1e-3),("us",1e-6)]),
("Vitesse",[("m/s",1),("km/h",1/3.6),("km/s",1e3)]),
("Energie",[("J",1),("kJ",1e3),("Wh",3600),("kWh",3.6e6),("eV",1.602e-19),("cal",4.184),("kcal",4184)]),
("Puissance",[("W",1),("kW",1e3),("MW",1e6),("mW",1e-3)]),
("Pression",[("Pa",1),("hPa",100),("kPa",1e3),("bar",1e5),("atm",101325),("mmHg",133.3)]),
("Temperature",[("C",0),("K",0),("F",0)]),
("Concentration",[("mol/L",1),("mmol/L",1e-3),("mol/m^3",1e-3)]),
("Angle",[("deg",1),("rad",57.29578),("tr",360)]),
]
def vers_base(v,cat,u):
 if cat=="Temperature":
  return (v-32)*5/9+273.15 if u=="F" else (v+273.15 if u=="C" else v)
 return v*dict(U_cat(cat))[u]
def depuis_base(v,cat,u):
 if cat=="Temperature":
  return (v-273.15)*9/5+32 if u=="F" else (v-273.15 if u=="C" else v)
 return v/dict(U_cat(cat))[u]
def U_cat(cat):
 for (c,l) in U:
  if c==cat:
   return l
def joli(x):
 if x==0:
  return "0"
 s="%.6g"%x
 if "e" in s:
  m,e=s.split("e")
  return m+r"\times10^{"+str(int(e))+"}"
 return s
CLAV=(("7","8","9","DEL"),("4","5","6","-"),("1","2","3","EXP"),("0",".","C","OK"))
def saisie(t):
 r,c=0,0
 while True:
  rect(80,36,224,134,GRIS);rect(80,36,224,1,SEP)
  rect(88,42,208,20,BLANC)
  tex((t.replace("e","E")+"|")[-32:],94,47,TX)
  for i in range(4):
   for j in range(4):
    x,y=88+j*53,68+i*25;s=(i==r and j==c)
    rect(x,y,49,21,SEL if s else BLANC);k=CLAV[i][j]
    tex(k,x+24,y+6,BLANC if s else TX,1,True)
  show_screen();k=touche()
  if k==HA: r=(r-1)%4
  elif k==BA: r=(r+1)%4
  elif k==GA: c=(c-1)%4
  elif k==DR: c=(c+1)%4
  else:
   ch=CLAV[r][c]
   if ch=="OK":
    return t
   if ch=="DEL":
    t=t[:-1]
   elif ch=="C":
    t=""
   elif ch=="EXP":
    if "e" not in t and t:
     t+="e"
   else:
    t+=ch
def convertisseur(liste):
 sc=0
 while True:
  sc,k=liste("CONVERTISSEUR",[c for (c,l) in U],sc,"^v : choisir   OK : ouvrir   < : retour")
  if k==GA:
   return
  cat,us=U[sc];v="1";a,b=0,1;champ=0
  while True:
   entete(cat.upper(),"^v : champ   <> : unite   OK : saisir")
   noms=("Valeur","De","Vers");vals=(v,us[a][0],us[b][0])
   for i in range(3):
    y=40+i*28;rect(10,y,W-20,24,FSEL if champ==i else BLANC)
    if champ==i:
     rect(10,y,3,24,SEL)
    draw_string(20,y+5,noms[i],LI,"small")
    tex(("< " if i and champ==i else "")+vals[i].replace("e","E")+(" >" if i and champ==i else ""),110,y+7,TX)
   try:
    r=depuis_base(vers_base(float(v),cat,us[a][0]),cat,us[b][0])
    res=joli(float(v))+" "+us[a][0]+"="+joli(r)+" "+us[b][0]
   except:
    res="Valeur invalide"
   rect(10,128,W-20,40,GRIS)
   tex(res,W//2,140,NAVY,2 if len(res)<26 else 1,True);show_screen()
   k=touche()
   if k==HA:
    champ=(champ-1)%3
   elif k==BA:
    champ=(champ+1)%3
   elif k in (GA,DR):
    if champ==0:
     if k==GA:
      break
    else:
     d=1 if k==DR else -1
     if champ==1:
      a=(a+d)%len(us)
     else:
      b=(b+d)%len(us)
   elif k==OK:
    if champ==0:
     v=saisie(v) or "0"
    else:
     a,b=b,a
PREF=(("Tera","T","10^{12}"),("Giga","G","10^9"),("Mega","M","10^6"),("kilo","k","10^3"),("hecto","h","10^2"),("deca","da","10"),
   ("deci","d","10^{-1}"),("centi","c","10^{-2}"),("milli","m","10^{-3}"),("micro","u","10^{-6}"),("nano","n","10^{-9}"),("pico","p","10^{-12}"))
EQUIV=(r"1 h=3600 s",r"1 m/s=3,6 km/h",r"T(K)=T(C)+273,15",r"1 L=1 dm^3     1 mL=1 cm^3",r"1 kWh=3,6\times10^6 J",
   r"1 eV=1,602\times10^{-19} J",r"1 bar=10^5 Pa",r"1 atm=1013 hPa",r"1 cal=4,184 J",r"1 al=9,461\times10^{15} m",r"1 UA=1,496\times10^{11} m")
TABLES=["Prefixes","Longueurs","Masses","Volumes et capacites","Equivalences utiles"]
def grille(titre,cols,ln,note):
 n=len(cols);w=(W-20)//n
 for j in range(n):
  x=10+j*w;rect(x,40,w-2,22,SEL);tex(cols[j],x+w//2,46,BLANC,1,True)
  for i in range(len(ln)):
   rect(x,64+i*24,w-2,22,FSEL if i%2==0 else BLANC)
   tex(ln[i][j],x+w//2,70+i*24,TX,1,True)
 tex(note,10,64+len(ln)*24+8,LI)
def table(i):
 t=TABLES[i];entete(t.upper(),"^v : tableau suivant   < : retour")
 if i==0:
  for k in range(12):
   p=PREF[k];x,y=10+(k//6)*184,36+(k%6)*22
   rect(x,y,180,20,FSEL if k%2==0 else BLANC);tex(p[0],x+6,y+5,TX)
   tex(p[1],x+70,y+5,SEL);tex(p[2],x+110,y+5,TX)
 elif i==1:
  grille(t,["km","hm","dam","m","dm","cm","mm"],[["1","0","0","0","","",""],["","","","1","0","0","0"]],"Chaque colonne = x10 vers la droite. 1 km = 1000 m")
 elif i==2:
  grille(t,["t","q","","kg","hg","dag","g","dg","cg","mg"],[["1","0","0","0","","","","","",""],["","","","1","0","0","0","","",""],["","","","","","","1","0","0","0"]],"1 t = 1000 kg     1 kg = 1000 g     1 g = 1000 mg")
 elif i==3:
  grille(t,["kL","hL","daL","L","dL","cL","mL"],[["m^3","","","dm^3","","","cm^3"],["1","0","0","0","","",""],["","","","1","0","0","0"]],"1 m^3 = 1000 L     1 dm^3 = 1 L     1 cm^3 = 1 mL")
 else:
  for k in range(len(EQUIV)):
   x,y=10+(k%2)*184,36+(k//2)*22
   rect(x,y,180,20,FSEL if (k//2)%2==0 else BLANC)
   tex(EQUIV[k],x+6,y+6,TX)
 show_screen()
def tableaux(liste):
 sel=0
 while True:
  sel,k=liste("TABLEAUX DE CONVERSION",TABLES,sel,"^v : choisir   OK : ouvrir   < : retour")
  if k==GA:
   return
  i=sel
  while True:
   table(i);k=touche()
   if k in (GA,OK):
    break
   i=(i+(1 if k==BA else -1 if k==HA else 0))%len(TABLES)
