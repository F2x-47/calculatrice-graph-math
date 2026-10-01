from casioplot import *
from ecran import *
import reponses
VIOLET=(90,70,200);LIEN=(40,70,180);BULLE=(232,228,252)
LOGO=((95,60,205),(80,90,210),(60,120,205),(45,150,190),(40,170,165),(55,185,135))
LT=(
 ("01111","10000","10011","10001","01110"),
 ("01110","10001","10001","10001","01110"),
 ("01111","10000","10011","10001","01110"),
 ("01110","10001","10001","10001","01110"),
 ("10000","10000","10000","10000","11111"),
 ("11111","10000","11110","10000","11111"))
try:
 from time import monotonic as hz
except:
 hz=None
def pause(t):
 if hz:
  t0=hz()
  while hz()-t0<t:
   pass
 else:
  for _ in range(int(t*40)):
   show_screen()
def logo(x,y,s):
 for i in range(6):
  for l in range(5):
   for k in range(5):
    if LT[i][l][k]=="1":
     rect(x+i*(5*s+s)+k*s,y+l*s,s,s,LOGO[i])
def loupe(x,y,c):
 for (a,b) in ((2,0),(3,0),(4,0),(1,1),(5,1),(0,2),(6,2),(0,3),(6,3),(0,4),(6,4),(1,5),(5,5),(2,6),(3,6),(4,6),(6,6),(7,7),(8,8)):
  rect(x+a,y+b,1,1,c)
def icone(x,y,s):
 arrondi(x,y,s,s,VIOLET);arrondi(x+s//5,y+s//4,s*3//5,s*2//5,BLANC)
 rect(x+s//3,y+s*13//20,s//8+1,s//8+1,BLANC)
def chargement():
 for i in range(0,W,24):
  rect(0,0,i,3,LOGO[(i//24)%6]);show_screen()
 rect(0,0,W,3,BLANC)
def accueil():
 sel=0
 while True:
  clear_screen();texte("Images   Actus   Apps",W-136,8,LI)
  logo(W//2-102,30,6)
  for i in range(2):
   cs=(70,90,200) if sel==i else SEP
   if i==0:
    arrondi(51,85,282,24,cs);arrondi(52,86,280,22,BLANC)
    loupe(62,93,LI);texte("Rechercher sur Gogole",80,93,LI)
   else:
    arrondi(W//2-24,120,48,48,cs if sel==1 else BLANC)
    icone(W//2-18,124,36);texte("Claudette",W//2-27,172,TX)
  rect(0,H-1,W,1,SEP);show_screen();k=touche()
  if k in (HA,BA):
   sel=1-sel
  elif k==OK:
   if sel==1:
    claudette()
   else:
    q=clavier("Rechercher")
    if q.strip():
     resultats(q.strip())
def resultats(q):
 chargement();res=[]
 for (m,l) in reponses.S:
  if m in q.lower():
   res=l
   break
 if not res:
  res=[(q+" : definition et explications","encyclo-libre.fr/"+q.replace(" ","_"),"Tout savoir sur "+q+" : definition, exemples et explications detaillees."),
    ("Questions frequentes sur "+q,"forum-entraide.fr","Les reponses de la communaute a vos questions sur "+q+"."),
    (q[0].upper()+q[1:]+" - Cours et exercices","cours-en-ligne.fr","Fiches de revision et exercices corriges.")]
 sel=0
 while True:
  clear_screen();logo(8,8,2);arrondi(84,4,292,18,SEP)
  arrondi(85,5,290,16,BLANC);texte(q[:44],92,8,TX)
  texte("Tous",12,28,VIOLET);rect(10,39,28,2,VIOLET)
  texte("Images   Actus   Videos",56,28,LI);rect(0,41,W,1,SEP)
  texte("Environ "+str(len(q)*137+2104)+" 000 resultats",12,46,LI)
  for i in range(len(res)):
   t,u,e=res[i];y=60+i*42
   if i==sel:
    rect(4,y-2,W-8,40,GRIS)
   texte(u[:58],12,y,LI);texte(t[:58],12,y+11,LIEN)
   if i==sel:
    rect(12,y+21,len(t[:58])*6,1,LIEN)
   texte(e if len(e)<59 else e[:55]+"...",12,y+24,TX)
  show_screen();k=touche()
  if k==GA:
   return
  if k in (HA,BA):
   sel=(sel+(1 if k==BA else -1))%len(res)
  elif k==OK and "claudette" in res[sel][1]:
   claudette()
   return
def entete():
 clear_screen();icone(8,5,20);texte("Claudette",34,6,TX)
 texte("Assistant",34,16,LI);rect(0,29,W,1,SEP)
def bas(focus,ch):
 rect(0,150,W,42,BLANC);x=8
 for i in range(len(reponses.SUGG)):
  m=reponses.SUGG[i];w=len(m)*6+14;s=(focus==1 and ch==i)
  arrondi(x,152,w,15,(70,90,200) if s else SEP)
  arrondi(x+1,153,w-2,13,(70,90,200) if s else BLANC)
  texte(m,x+7,155,BLANC if s else TX);x+=w+6
 arrondi(8,171,W-16,18,(70,90,200) if focus==2 else SEP)
 arrondi(9,172,W-18,16,GRIS)
 texte("Ecris un message a Claudette...",16,176,LI)
 rect(W-30,174,12,12,VIOLET);texte("^",W-27,176,BLANC)
def conversation(ln,deb):
 rect(0,30,W,120,BLANC);y=34
 for i in range(deb,len(ln)):
  t,l=ln[i];h=haut_ligne(l) if t=="a" else 14
  if y+h>148:
   return True
  if t=="u":
   w=len(l)*6+12;arrondi(W-10-w,y-1,w,14,BULLE);texte(l,W-4-w,y+2,TX)
  else:
   ligne(l,12,y,TX,W-24)
  y+=h
 return False
def reponse(q):
 q=q.lower()
 for (m,r) in reponses.R:
  if m in q:
   return r
 return reponses.DEFAUT
def claudette():
 rect(0,0,W,H,BLANC);icone(W//2-24,60,48)
 texte("Claudette",W//2-27,118,TX);show_screen();pause(0.8);ln=[]
 deb=0;plus=False;focus,ch=1,0;entete()
 texte("Bonjour ! Comment puis-je t'aider ?",W//2-105,80,TX)
 while True:
  bas(focus,ch);show_screen();k=touche();msg=""
  if k==GA and focus==1:
   if ch==0:
    return
   ch-=1
  elif k==DR and focus==1:
   ch=min(ch+1,len(reponses.SUGG)-1)
  elif k==BA:
   if focus==0 and plus:
    deb+=1;plus=conversation(ln,deb)
   else:
    focus=min(2,focus+1)
  elif k==HA:
   if focus==0 and deb>0:
    deb-=1;plus=conversation(ln,deb)
   elif ln:
    focus=max(0,focus-1)
   else:
    focus=1
  elif k==OK:
   if focus==1:
    msg=reponses.SUGG[ch]
   elif focus==2:
    msg=clavier("Message");entete();conversation(ln,deb)
  if msg.strip():
   ln=[("u",l) for l in decoupe(msg,50)];entete();conversation(ln,0)
   for n in range(9):
    for j in range(3):
     rect(14+j*10,54,6,6,VIOLET if j==n%3 else SEP)
    show_screen();pause(0.15)
   rect(10,50,40,14,BLANC)
   for l in decoupe(reponse(msg),58):
    ln.append(("a",l));plus=conversation(ln,0);show_screen()
    pause(0.12)
   deb=0;focus=0 if plus else 1;plus=conversation(ln,deb)
accueil()
