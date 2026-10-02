from mbase import *
def facteurs(n):
 r=[];p=2
 while p*p<=n:
  e=0
  while n%p==0:
   n//=p;e+=1
  if e:
   r.append(str(p)+("^{"+str(e)+"}" if e>1 else ""))
  p+=1 if p==2 else 2
 if n>1 or not r:
  r.append(str(n))
 return r"\times ".join(r)
def arith():
 a=nombre("Premier nombre entier",True)
 if a==None:
  return
 b=nombre("Deuxieme nombre entier",True)
 if b==None:
  return
 x,y=a,b
 while y:
  x,y=y,x%y
 page("ARITHMETIQUE","OK ou < : retour");draw_string(10,44,"PGCD("+str(a)+" ; "+str(b)+") = "+str(x),SEL,"medium")
 draw_string(10,64,"PPCM("+str(a)+" ; "+str(b)+") = "+str(a*b//x),SEL,"medium");t=r"\frac{"+str(a)+"}{"+str(b)+"}="
 t+=r"\frac{"+str(a//x)+"}{"+str(b//x)+"}" if b//x>1 else str(a//x);formule(t,300,62,1,NAVY);rect(10,88,W-20,1,SEP)
 draw_string(10,94,"Facteurs premiers",LI,"small");formule(str(a)+"="+facteurs(a),W//2,122,1,TX)
 formule(str(b)+"="+facteurs(b),W//2,152,1,TX);pause()
def suites():
 g,k=liste("SUITES",["Suite arithmetique","Suite geometrique"],0)
 if k==GA:
  return
 u0=nombre("Premier terme u0")
 if u0==None:
  return
 q=nombre("Raison q" if g else "Raison r")
 if q==None:
  return
 n=nombre("Rang n",True)
 if n==None:
  return
 page("SUITE "+("GEOMETRIQUE" if g else "ARITHMETIQUE"),"OK ou < : retour")
 if g:
  un=u0*q**n;s=u0*(n+1) if q==1 else u0*(1-q**(n+1))/(1-q);formule(r"u_n=u_0\times q^n",100,58,1,NAVY)
  formule(r"S=u_0\times\frac{1-q^{n+1}}{1-q}",280,58,1,NAVY)
 else:
  un=u0+n*q;s=(n+1)*(u0+un)/2;formule(r"u_n=u_0+n\times r",100,58,1,NAVY)
  formule(r"S=(n+1)\times\frac{u_0+u_n}{2}",280,58,1,NAVY)
 rect(10,84,W-20,1,SEP);draw_string(10,94,"u0 = "+joli(u0)+"    raison = "+joli(q)+"    n = "+str(n),LI,"small")
 draw_string(10,114,"u"+str(n)+" = "+joli(un),SEL,"medium")
 draw_string(10,138,"u0 + u1 + ... + u"+str(n)+" = "+joli(s),SEL,"medium");pause()
def grille(titre,cols,lg,p):
 page(titre,"^v : page suivante   < : retour");w=(W-20)//len(cols)
 for j in range(len(cols)):
  draw_string(14+j*w,40,cols[j],NAVY,"small")
 rect(10,53,W-20,1,NAVY)
 for i in range(10):
  if p*10+i<len(lg):
   for j in range(len(cols)):
    draw_string(14+j*w,57+i*11,lg[p*10+i][j],TX,"small")
def carres():
 lg=[(str(n),str(n*n),str(n**3),"%.4f"%n**0.5,"%.4f"%(1/n)) for n in range(1,31)];p=0
 while True:
  grille("CARRES, CUBES, RACINES",("n","n au carre","n au cube","racine de n","1/n"),lg,p);show_screen();k=touche()
  if k in (GA,OK):
   return
  p=(p+(1 if k==BA else -1 if k==HA else 0))%3
TRIGO=(("x",r"0",r"\frac{\pi}{6}",r"\frac{\pi}{4}",r"\frac{\pi}{3}",r"\frac{\pi}{2}"),
   ("deg","0","30","45","60","90"),
   ("sin x","0",r"\frac{1}{2}",r"\frac{\sqrt{2}}{2}",r"\frac{\sqrt{3}}{2}","1"),
   ("cos x","1",r"\frac{\sqrt{3}}{2}",r"\frac{\sqrt{2}}{2}",r"\frac{1}{2}","0"),
   ("tan x","0",r"\frac{\sqrt{3}}{3}","1",r"\sqrt{3}","-"))
def trigo():
 page("VALEURS REMARQUABLES","OK ou < : retour")
 for i in range(5):
  y=52+i*27
  if i:
   rect(10,y-14,W-20,1,SEP)
  for j in range(6):
   formule(TRIGO[i][j],40+j*62,y,1,NAVY if (i==0 or j==0) else TX)
 rect(74,38,1,134,SEP);pause()
def premiers():
 t=[];s=""
 for n in range(2,500):
  p=n>1;d=2
  while d*d<=n:
   if n%d==0:
    p=False
    break
   d+=1
  if p:
   if len(s)+len(str(n))>50:
    t.append(s);s=""
   s+=str(n)+"  "
 t.append(s);page("NOMBRES PREMIERS < 500","OK ou < : retour")
 for i in range(len(t)):
  draw_string(10,42+i*13,t[i],TX,"small")
 pause()
def tables():
 s=0
 while True:
  s,k=liste("TABLES",["Carres, cubes, racines","Valeurs trigonometriques","Nombres premiers"],s)
  if k==GA:
   return
  (carres,trigo,premiers)[s]()
