from casioplot import *
W,H=384,192;GA,DR,OK=23,25,24
A="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"
FD=(20,20,45);NOIR=(0,0,0);TX=(255,255,255);LI=(170,170,200)
OM=(60,60,90)
CO=((240,70,90),(250,210,0),(40,200,70),(0,200,230),(160,60,220))
MAXI=20
try:
 from time import monotonic as hz
except:
 hz=None
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
 while k not in (GA,DR,OK):
  k=getkey()
 return k
def charge_ok(nom):
 m=charge(nom);oublie(nom)
 return m!=None
def oublie(nom):
 try:
  import sys,gc
  if nom in sys.modules:
   del sys.modules[nom]
  gc.collect()
 except:
  pass
def charge(nom):
 try:
  return __import__(nom)
 except ImportError:
  return None
def image(f,m,x0,y0):
 L,S,P=m.L,m.S,m.P;pos=0
 for i in range(0,len(f),3):
  a,b,c=A.find(f[i]),A.find(f[i+1]),A.find(f[i+2])
  if c==63:
   pos+=a*64+b+1;continue
  pos+=a;n=b+1;col=P[c]
  while n>0:
   x,y=pos%L,pos//L;k=min(n,L-x);rect(x0+x*S,y0+y*S,k*S,S,col);pos+=k
   n-=k
def lire(num):
 m=charge("video"+str(num)+"_0");L,H2,S,FPS,NB=m.L,m.H,m.S,m.FPS,m.NB
 x0,y0=(W-L*S)//2,(H-H2*S)//2;clear_screen();rect(0,0,W,H,NOIR)
 for p in range(NB):
  if p:
   oublie("video"+str(num)+"_"+str(p-1))
   m2=charge("video"+str(num)+"_"+str(p))
   if not m2:
    manque("video"+str(num)+"_"+str(p)+".py")
    return
  else:
   m2=m
  for f in m2.F:
   t0=hz() if hz else 0;image(f,m,x0,y0);show_screen();k=getkey()
   if k==OK:
    icone=x0>=36 or y0>=22
    if icone:
     rect(4,4,8,14,TX);rect(16,4,8,14,TX);show_screen()
    rl()
    while getkey()!=OK:
     pass
    rl()
    if icone:
     rect(4,4,20,14,NOIR)
   elif k==GA:
    oublie("video"+str(num)+"_"+str(p))
    return
   if hz:
    while hz()-t0<1/FPS:
     pass
 oublie("video"+str(num)+"_"+str(NB-1));oublie("video"+str(num)+"_0")
def manque(nom):
 rect(40,60,304,72,FD);rect(40,60,304,3,CO[0])
 draw_string(52,70,"Fichier manquant :",CO[0],"medium")
 draw_string(52,92,nom,TX,"medium")
 draw_string(52,114,"Copie-le sur la calculatrice. OK : retour",LI,"small")
 show_screen();rl()
 while getkey()!=OK:
  pass
LT=(
 ("10001","10001","10001","01010","00100"),
 ("11111","00100","00100","00100","11111"),
 ("11110","10001","10001","10001","11110"),
 ("11111","10000","11110","10000","11111"),
 ("01110","10001","10001","10001","01110"))
def it():
 clear_screen();rect(0,0,W,H,FD);s=8;x0=(W-(5*5*s+4*8))//2
 for i in range(5):
  for l in range(5):
   for k in range(5):
    if LT[i][l][k]=="1":
     x,y=x0+i*(5*s+8)+k*s,12+l*s;rect(x+2,y+2,s,s,OM)
     rect(x,y,s,s,CO[i]);rect(x,y,s,2,(255,255,255))
  show_screen()
 draw_string(20,60,"GRAPH MATH+ EDITION",TX,"large")
 rect(20,84,344,3,CO[0]);show_screen()
def liste(vids,sel):
 rect(0,96,W,96,FD)
 if not vids:
  draw_string(30,104,"Aucune video trouvee.",CO[0],"medium")
  draw_string(30,126,"Cree des fichiers video1_0.py ... avec le",LI,"small")
  draw_string(30,140,"convertisseur, puis copie-les a cote de",LI,"small")
  draw_string(30,154,"video.py.",LI,"small");show_screen()
  return
 for i in range(len(vids)):
  if i<sel-2 or i>sel+2:
   continue
  y=100+(i-sel+2)*16;n,nom,du=vids[i]
  if i==sel:
   rect(20,y-2,344,16,CO[0])
  draw_string(30,y,str(n)+". "+nom[:26]+"  ("+du+")",FD if i==sel else TX,"small")
 draw_string(30,178,"OK : lire   < > : choisir   < pendant la video : stop",LI,"small")
 show_screen()
def lecteur():
 it();vids=[]
 for n in range(1,MAXI+1):
  m=charge("video"+str(n)+"_0")
  if m:
   ok=all(charge_ok("video"+str(n)+"_"+str(p)) for p in range(1,m.NB))
   vids.append((n,m.NOM,str(int(m.DUREE+0.5))+" s"+("" if ok else ", INCOMPLETE")))
   del m;oublie("video"+str(n)+"_0")
 sel=0
 while True:
  liste(vids,sel);k=touche()
  if not vids:
   continue
  if k==OK:
   lire(vids[sel][0]);it()
  else:
   sel=(sel+(1 if k==DR else -1))%len(vids)
lecteur()
