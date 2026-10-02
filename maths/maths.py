from mbase import *
from math import sin
import mform1
import mform2
CAT=mform1.CAT+mform2.CAT
def fiches(F,i):
 while True:
  f=F[i];page(f[0],"^v : formule suivante   < : retour");formule(f[1],W//2,78,2,NAVY);rect(10,116,W-20,1,SEP)
  lg=f[2].split("|")
  for j in range(len(lg)):
   draw_string(14,122+j*16,lg[j],TX,"small")
  show_screen();k=touche()
  if k in (GA,OK):
   return i
  i=(i+(1 if k==BA else -1 if k==HA else 0))%len(F)
def menu_formules():
 sc=0
 while True:
  sc,k=liste("FORMULES",CAT,sc)
  if k==GA:
   return
  n1=len(mform1.CAT);F=mform1.F[sc] if sc<n1 else mform2.F[sc-n1];sf=0
  while True:
   sf,k=liste(CAT[sc].upper(),[f[0] for f in F],sf,"OK : voir la formule   < : retour")
   if k==GA:
    break
   sf=fiches(F,sf)
def it():
 clear_screen();rect(20,96,120,1,LI);rect(80,40,1,112,LI);draw_string(160,52,"MATHS",NAVY,"large")
 draw_string(160,78,"Formules et outils de calcul",LI,"small")
 for x in range(118):
  y=96-int(34*sin((x-59)/15));rect(21+x,y,2,2,SEL)
  if x<92:
   rect(160+x*2,96,2,2,SEL)
  if x%8==0:
   show_screen()
  if getkey():
   break
 formule(r"\Sigma x_i   \bar{x}   \sigma   \Delta   \pi",252,124,1,NAVY);draw_string(160,146,"Graph Math+",LI,"small")
 draw_string(160,160,"Appuie sur une touche",LI,"small");show_screen()
 while getkey():
  pass
 while not getkey():
  pass
def accueil():
 it();sel=0
 mn=["Formules","Statistiques d'une serie","Second degre","PGCD, PPCM, facteurs premiers",
    "Suites","Tables de valeurs"]
 while True:
  sel,k=liste("MATHS",mn,sel,"^v : choisir   OK : ouvrir   AC : quitter")
  if k==OK:
   if sel==0:
    menu_formules()
   elif sel<3:
    import mcalc1
    if sel==1:
     mcalc1.stats()
    else:
     mcalc1.second()
   else:
    import mcalc2
    if sel==3:
     mcalc2.arith()
    elif sel==4:
     mcalc2.suites()
    else:
     mcalc2.tables()
accueil()
