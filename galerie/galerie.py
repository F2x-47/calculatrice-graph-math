from casioplot import *
W,H=384,192;HA,BA,GA,DR,OK=14,34,23,25,24
CODE="HBGD"
A="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/";FD=(20,20,45);TX=(255,255,255);LI=(170,170,200)
OM=(60,60,90);CO=((0,200,230),(250,210,0),(240,70,90),(40,200,70),(160,60,220),(255,140,0),(0,200,230));MAXI=30
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
def oublie(nom):
 try:
  import sys,gc
  if nom in sys.modules:
   del sys.modules[nom]
  gc.collect()
 except:
  pass
def charge(n):
 nom="image"+str(n)
 try:
  return __import__(nom)
 except ImportError:
  return None
def afficher(m):
 clear_screen();L,Hh,S=m.L,m.H,m.S;x0=(W-L*S)//2;y0=(H-Hh*S)//2;P=m.P;x=y=0;d=m.D
 for i in range(0,len(d),2):
  c=P[A.find(d[i])];n=A.find(d[i+1])+1
  while n>0:
   k=min(n,L-x);rect(x0+x*S,y0+y*S,k*S,S,c);x+=k;n-=k
   if x>=L:
    x=0;y+=1
  if i%400==0:
   show_screen()
 show_screen()
def legende(m,n,nb):
 rect(0,H-22,W,22,FD);draw_string(8,H-17,str(n)+"/"+str(nb)+"  "+m.NOM[:30],TX,"small")
 draw_string(W-150,H-17,"< > changer   ^ albums",LI,"small");show_screen()
LT=(
 ("01111","10000","10011","10001","01110"),
 ("01110","10001","11111","10001","10001"),
 ("10000","10000","10000","10000","11111"),
 ("11111","10000","11110","10000","11111"),
 ("11110","10001","11110","10010","10001"),
 ("11111","00100","00100","00100","11111"),
 ("11111","10000","11110","10000","11111"))
def it(nb):
 clear_screen();rect(0,0,W,H,FD);s=7;x0=(W-(7*5*s+6*6))//2
 for i in range(7):
  for l in range(5):
   for k in range(5):
    if LT[i][l][k]=="1":
     x,y=x0+i*(5*s+6)+k*s,16+l*s;rect(x+2,y+2,s,s,OM);rect(x,y,s,s,CO[i]);rect(x,y,s,2,(255,255,255))
  show_screen()
 draw_string(20,62,"GRAPH MATH+ EDITION",TX,"large");rect(20,86,344,3,CO[0])
 if nb:
  draw_string(40,110,str(nb)+" image"+("s" if nb>1 else "")+" trouvee"+("s" if nb>1 else ""),TX,"medium")
  draw_string(40,170,"OK pour ouvrir les albums",LI,"small")
 else:
  draw_string(40,104,"Aucune image trouvee.",CO[2],"medium")
  draw_string(40,126,"Cree des fichiers image1.py, image2.py...",LI,"small")
  draw_string(40,140,"avec le convertisseur, puis copie-les",LI,"small")
  draw_string(40,154,"a cote de galerie.py.",LI,"small")
 show_screen()
 while touche()!=OK:
  pass
def cadenas(x,y,c):
 rect(x+3,y,6,2,c);rect(x+2,y+1,2,5,c);rect(x+8,y+1,2,5,c);rect(x,y+6,12,8,c);rect(x+5,y+9,2,3,FD)
def albums(noms,alb,sel):
 while True:
  clear_screen();rect(0,0,W,H,FD);rect(0,0,W,26,OM);draw_string(10,5,"ALBUMS",TX,"medium")
  h=max(0,min(sel-2,len(noms)-6))
  for i in range(h,min(len(noms),h+6)):
   y=32+(i-h)*23;t,v=alb[noms[i]]
   if i==sel:
    rect(8,y,W-16,21,CO[i%6])
   c=FD if i==sel else TX
   if v:
    cadenas(15,y+3,c if i==sel else CO[2])
   else:
    rect(14,y+4,13,13,c if i==sel else CO[i%6])
   draw_string(36,y+3,noms[i][:20],c,"medium")
   draw_string(W-90,y+5,"masque" if v else str(len(t))+" photo"+("s" if len(t)>1 else ""),c if i==sel else LI,"small")
  draw_string(10,H-16,"^ v : choisir     OK : ouvrir     AC : quitter",LI,"small");show_screen();k=touche()
  if k==OK:
   return sel
  if k in (HA,BA):
   sel=(sel+(1 if k==BA else -1))%len(noms)
def code(nom):
 rect(52,56,280,80,OM);rect(52,56,280,3,CO[2]);cadenas(64,68,CO[1]);draw_string(84,66,"Album masque",TX,"medium")
 draw_string(64,112,"Tape le code : 4 fleches",LI,"small");t=""
 for i in range(4):
  rect(150+i*24,90,16,4,LI);show_screen();k=touche()
  if k==OK:
   return False
  t+={HA:"H",BA:"B",GA:"G",DR:"D"}[k];rect(150+i*24,82,16,12,CO[1])
 show_screen()
 if t==CODE:
  return True
 rect(60,108,264,20,OM);draw_string(64,112,"Code incorrect. OK : retour",CO[2],"small");show_screen()
 while touche()!=OK:
  pass
 return False
def voir(nums):
 i=0
 while True:
  n=nums[i];m=charge(n);afficher(m);legende(m,i+1,len(nums));vu=True
  while True:
   k=touche()
   if k==OK:
    vu=not vu
    if vu:
     legende(m,i+1,len(nums))
    else:
     afficher(m)
   else:
    break
  del m;oublie("image"+str(n))
  if k in (HA,BA):
   return
  i=(i+(1 if k==DR else -1))%len(nums)
def galerie():
 noms=[];alb={};nb=0
 for n in range(1,MAXI+1):
  m=charge(n)
  if m:
   nb+=1;a=getattr(m,"ALB","Photos")
   if a not in alb:
    noms.append(a);alb[a]=[[],0]
   alb[a][0].append(n)
   if getattr(m,"V",0):
    alb[a][1]=1
   del m;oublie("image"+str(n))
 it(nb)
 if not nb:
  return
 noms=[a for a in noms if not alb[a][1]]+[a for a in noms if alb[a][1]];sel=0
 while True:
  sel=albums(noms,alb,sel);t,v=alb[noms[sel]]
  if not v or code(noms[sel]):
   voir(t)
galerie()
