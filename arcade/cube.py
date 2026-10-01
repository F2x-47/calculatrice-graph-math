from casioplot import *
W,H=384,192;HA,BA,OK=14,34,24;FD=(28,22,70);SOL=(20,140,200)
SOL2=(10,70,120);TX=(255,255,255);LI=(170,170,200);OM=(60,60,90)
CUBE=(255,200,0);PIC=(240,240,255);BLOC=(110,60,220)
CO=((0,200,230),(250,210,0),(240,70,90),(40,200,70),(160,60,220),(255,140,0),(0,200,230),(250,210,0),(240,70,90))
GY=150;CX=70;G,J=0.9,8.6
def rect(x,y,w,h,c):
 if x<0:
  w+=x;x=0
 if x+w>W:
  w=W-x
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
def at():
 rl();k=0
 while k not in (HA,BA,OK):
  k=getkey()
 rl()
 return k
def pic(x,y,c):
 for r in range(16):
  h=r//2;rect(x+8-h,y+r,2*h+1,1,c)
def bk(x,y):
 rect(x,y,18,18,BLOC);rect(x,y,18,2,(170,130,255))
 rect(x+5,y+5,8,8,(70,30,160))
def cube(x,y,c):
 rect(x,y,14,14,c)
 if c!=FD:
  rect(x,y,14,2,(255,240,150));rect(x+3,y+4,3,3,(40,30,0))
  rect(x+8,y+4,3,3,(40,30,0));rect(x+3,y+9,8,2,(40,30,0))
def objet(o,dist,c=None):
 x=o[0]-dist
 if o[1]=="s":
  if c:
   rect(x,GY-16,17,16,c)
  else:
   pic(x,GY-16,PIC)
 else:
  if c:
   rect(x,o[2],18,18,c)
  else:
   bk(x,o[2])
def decor():
 clear_screen();rect(0,0,W,GY,FD)
 for i in range(0,W,48):
  rect(i+10,26+(i*7)%40,3,3,(60,50,120))
 rect(0,GY,W,H-GY,SOL2);rect(0,GY,W,3,SOL)
 for i in range(0,W,32):
  rect(i,GY+3,16,H-GY-3,(15,100,160))
NV=(("FACILE",CO[3],4,2400,150),("NORMAL",CO[5],5,3000,115),("DIFFICILE",CO[2],6,3600,90))
MOTIFS=(("s",0),("s",0,"s",17),("b",0,"s",60),("s",0,"s",17,"s",34),("b",0,"b",50,"bb",50),("b",0,"b",18,"s",36))
def niveau(n):
 nom,c,v,lg,ecart=NV[n];obs=[];x=500;r=7+n
 while x<lg:
  r=(r*1103+12345)%32768;m=MOTIFS[r%(3,5,6)[n]]
  for i in range(0,len(m),2):
   t=m[i]
   if t=="bb":
    obs.append([x+m[i+1],"b",GY-36])
   else:
    obs.append([x+m[i+1],t,GY-18])
  x+=ecart+(r%60)+m[-1]
 return obs,v,lg
def essai(n,num):
 obs,v,lg=niveau(n);decor()
 draw_string(8,4,"Essai "+str(num),TX,"small");rect(100,8,184,6,OM)
 dist=0;y,vy=GY-14,0;vu=[];oy=y
 while True:
  k=getkey();dist+=v;sol=GY
  for o in obs:
   x=o[0]-dist
   if o[1]=="b" and x<CX+14 and x+18>CX and oy+14<=o[2]+2:
    sol=min(sol,o[2])
  if y+14>=sol and vy>=0:
   y,vy=sol-14,0
   if k in (HA,OK):
    vy=-J
  else:
   vy+=G
  y=int(y+vy)
  if y+14>sol and vy>=0:
   y,vy=sol-14,0
  mort=False
  for o in obs:
   x=o[0]-dist
   if x>CX+20:
    break
   if x+18<CX:
    continue
   if o[1]=="s":
    if x+4<CX+12 and x+13>CX+2 and y+14>GY-10:
     mort=True
   elif x<CX+12 and x+18>CX+2 and y+14>o[2]+3 and y<o[2]+18:
    mort=True
  for o in vu:
   objet(o,dist-v,FD)
  cube(CX,oy,FD);vu=[o for o in obs if -20<o[0]-dist<W]
  for o in vu:
   objet(o,dist)
  cube(CX,y,CUBE);oy=y;rect(100,8,min(184,184*dist//lg),6,CO[0])
  show_screen()
  if mort:
   for r in range(2,30,4):
    for (a,b) in ((-1,-1),(1,-1),(-1,1),(1,1),(0,-1),(1,0),(0,1),(-1,0)):
     rect(CX+7+a*r,y+7+b*r,4,4,CO[r%9])
    show_screen()
   return False
  if dist>=lg:
   return True
def pt(n):
 num=1
 while not essai(n,num):
  num+=1
 rect(60,60,264,70,FD);rect(60,60,264,3,CO[3])
 rect(60,127,264,3,CO[3])
 draw_string(80,70,"NIVEAU TERMINE !",CO[1],"large")
 draw_string(80,104,"En "+str(num)+" essai"+("s" if num>1 else ""),TX,"medium")
 show_screen();at()
LT=(
 ("01111","10000","10000","10000","01111"),
 ("10001","10001","10001","10001","01110"),
 ("11110","10001","11110","10001","11110"),
 ("11111","10000","11110","10000","11111"),
 None,
 ("11110","10001","11110","10010","10001"),
 ("10001","10001","10001","10001","01110"),
 ("01111","10000","01110","00001","11110"),
 ("10001","10001","11111","10001","10001"))
def it():
 clear_screen();rect(0,0,W,H,FD);s=6;x0=(W-(9*5*s+8*6))//2
 for i in range(9):
  if LT[i]:
   for l in range(5):
    for k in range(5):
     if LT[i][l][k]=="1":
      x,y=x0+i*(5*s+6)+k*s,14+l*s;rect(x+2,y+2,s,s,OM)
      rect(x,y,s,s,CO[i]);rect(x,y,s,2,(255,255,255))
  show_screen()
 draw_string(20,60,"GRAPH MATH+ EDITION",TX,"large")
 rect(20,84,344,3,CO[0])
 draw_string(W//2-62,178,"Appuie pour passer",LI,"small")
 rect(0,150,W,2,SOL);y,vy,n=136,0,0
 while n<270:
  xs=W-(n*4)%(W+60);pic(xs+4,134,FD);pic(xs,134,PIC);cube(180,y,FD)
  if y>=136 and xs<230 and xs>190:
   vy=-7
  vy+=0.8;y=min(136,int(y+vy));cube(180,y,CUBE);show_screen();n+=1
  if getkey():
   break
 rl()
def mn(sel):
 rl()
 while True:
  clear_screen();rect(0,0,W,H,FD)
  draw_string(W//2-80,12,"DIFFICULTE",TX,"large")
  for i in range(3):
   nom,c=NV[i][:2];y=58+i*36
   if i==sel:
    rect(W//2-100,y-4,200,30,c)
    draw_string(W//2-80,y,"> "+nom,FD,"large")
   else:
    draw_string(W//2-80,y,"  "+nom,c,"large")
  draw_string(W//2-130,172,"Fleches pour choisir, OK pour jouer",LI,"small")
  show_screen();k=at()
  if k==OK:
   return sel
  sel=(sel+(1 if k==BA else -1))%3
def jouer():
 it();sel=0
 while True:
  sel=mn(sel);pt(sel)
try:
 import sys
 auto='arcade' not in sys.modules
except:
 auto=True
if auto:
 jouer()
