from casioplot import *
W,H=384,192;GA,DR,OK=23,25,24
A="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"
FD=(20,20,45);TX=(255,255,255);LI=(170,170,200);OM=(60,60,90)
CO=((0,200,230),(250,210,0),(240,70,90),(40,200,70),(160,60,220),(255,140,0),(0,200,230))
MAXI=30
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
 clear_screen();L,Hh,S=m.L,m.H,m.S;x0=(W-L*S)//2;y0=(H-Hh*S)//2;P=m.P
 x=y=0;d=m.D
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
 rect(0,H-22,W,22,FD)
 draw_string(8,H-17,str(n)+"/"+str(nb)+"  "+m.NOM[:30],TX,"small")
 draw_string(W-110,H-17,"< > changer",LI,"small");show_screen()
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
     x,y=x0+i*(5*s+6)+k*s,16+l*s;rect(x+2,y+2,s,s,OM)
     rect(x,y,s,s,CO[i]);rect(x,y,s,2,(255,255,255))
  show_screen()
 draw_string(20,62,"GRAPH MATH+ EDITION",TX,"large")
 rect(20,86,344,3,CO[0])
 if nb:
  draw_string(40,110,str(nb)+" image"+("s" if nb>1 else "")+" trouvee"+("s" if nb>1 else ""),TX,"medium")
  draw_string(40,170,"OK pour ouvrir la galerie",LI,"small")
 else:
  draw_string(40,104,"Aucune image trouvee.",CO[2],"medium")
  draw_string(40,126,"Cree des fichiers image1.py, image2.py...",LI,"small")
  draw_string(40,140,"avec le convertisseur, puis copie-les",LI,"small")
  draw_string(40,154,"a cote de galerie.py.",LI,"small")
 show_screen()
 while touche()!=OK:
  pass
def galerie():
 nums=[]
 for n in range(1,MAXI+1):
  m=charge(n)
  if m:
   nums.append(n);del m;oublie("image"+str(n))
 it(len(nums))
 if not nums:
  return
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
  del m;oublie("image"+str(n));i=(i+(1 if k==DR else -1))%len(nums)
galerie()
