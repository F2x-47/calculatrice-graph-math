from casioplot import *
from random import randint
W,H=384,192;HA,BA,GA,DR,OK=14,34,23,25,24;RYTHME=40;FD=(20,20,45)
TX=(255,255,255);LI=(170,170,190);OM=(60,60,90)
VIF=((40,220,70),(240,40,50),(40,110,255),(255,215,0))
TOUCHES=(HA,DR,BA,GA);CX,CY=192,96
def zones(R,r,g):
 res=[]
 for d in range(g,R+1):
  b=min(int((R*R-d*d)**0.5),d-g);a=int((r*r-d*d)**0.5) if d<r else 0
  if b>a:
   res.append((d,a,b))
 return res
GRAND=zones(86,32,4);PETIT=zones(28,9,2)
try:
 from time import monotonic as hz
except:
 hz=None
def rect(x,y,w,h,c):
 for i in range(x,x+w):
  for j in range(y,y+h):
   set_pixel(i,j,c)
def terne(c):
 return (c[0]//3,c[1]//3,c[2]//3)
def pause(t):
 if hz:
  t0=hz()
  while hz()-t0<t:
   getkey()
 else:
  for _ in range(int(t*RYTHME)):
   show_screen()
def rl():
 n=0
 while n<30:
  if getkey():
   n=0
  else:
   n+=1
def quartier(i,c,cx,cy,zs):
 for (d,a,b) in zs:
  if i==0 or i==2:
   y=cy-d if i==0 else cy+d;rect(cx-b,y,b-a+1,1,c)
   rect(cx+a,y,b-a+1,1,c)
  else:
   x=cx+d if i==1 else cx-d;rect(x,cy-b,1,b-a+1,c)
   rect(x,cy+a,1,b-a+1,c)
def pad(i,allume):
 quartier(i,VIF[i] if allume else terne(VIF[i]),CX,CY,GRAND)
def disque(cx,cy,R,c):
 for dy in range(-R,R+1):
  w=int((R*R-dy*dy)**0.5);rect(cx-w,cy+dy,2*w+1,1,c)
def centre(txt,c):
 disque(CX,CY,30,(40,40,75))
 draw_string(CX-len(txt)*9,CY-10,txt,c,"large")
def inf(so,record):
 rect(0,0,78,60,FD);draw_string(4,4,"SCORE",LI,"small")
 draw_string(4,18,str(so),TX,"large");rect(306,0,78,60,FD)
 draw_string(310,4,"RECORD",LI,"small")
 draw_string(310,18,str(record),VIF[3],"large")
def plateau(so,record):
 clear_screen();rect(0,0,W,H,FD);disque(CX,CY,92,(70,70,110))
 disque(CX,CY,89,(10,10,25))
 for i in range(4):
  pad(i,False)
 disque(CX,CY,33,(70,70,110));centre("",TX);inf(so,record)
 show_screen()
def flash(i,t):
 pad(i,True);show_screen();pause(t);pad(i,False);show_screen()
LT=(
 ("01111","10000","01110","00001","11110"),
 ("11111","00100","00100","00100","11111"),
 ("10001","11011","10101","10001","10001"),
 ("01110","10001","10001","10001","01110"),
 ("10001","11001","10101","10011","10001"))
def bk(px,py,s,c):
 rect(px,py,s,s,c)
 rect(px,py,s,2,(min(255,c[0]+90),min(255,c[1]+90),min(255,c[2]+90)))
 rect(px,py+s-2,s,2,terne(c))
def it(du=15):
 clear_screen();rect(0,0,W,H,FD);s=9;x0=(W-(5*5*s+4*10))//2
 cols=(VIF[0],VIF[1],VIF[2],VIF[3],(160,60,220))
 for i in range(5):
  for l in range(5):
   for k in range(5):
    if LT[i][l][k]=="1":
     x,y=x0+i*(5*s+10)+k*s,14+l*s;rect(x+3,y+3,s,s,OM)
     bk(x,y,s,cols[i])
  show_screen()
 draw_string(20,78,"GRAPH MATH+ EDITION",TX,"large")
 rect(20,102,344,3,VIF[1])
 draw_string(W//2-62,176,"Appuie pour passer",LI,"small")
 disque(192,142,31,(70,70,110));disque(192,142,29,(10,10,25))
 for d in range(4):
  quartier(d,terne(VIF[d]),192,142,PETIT)
 disque(192,142,7,(70,70,110))
 etoiles=[[randint(8,120) if k%2 else randint(264,376),randint(112,170),randint(0,3)] for k in range(10)]
 t0=hz() if hz else 0;n=0;der=0
 while True:
  if n%6==0:
   quartier(der,terne(VIF[der]),192,142,PETIT)
   der=(der+1)%4 if n<120 else randint(0,3)
   quartier(der,VIF[der],192,142,PETIT);e=etoiles[(n//6)%10]
   rect(e[0],e[1],4,4,FD)
   e[0]=randint(8,120) if n%12 else randint(264,376)
   e[1]=randint(112,170);e[2]=der;rect(e[0],e[1],4,4,VIF[der])
  show_screen();n+=1
  if getkey():
   break
  if hz:
   if hz()-t0>=du:
    break
  elif n>=270:
   break
 rl()
def pt(record):
 seq=[];plateau(0,record);centre("OK",TX);show_screen();rl()
 while getkey()!=OK:
  pass
 rl()
 while True:
  seq.append(randint(0,3));centre(str(len(seq)),TX);show_screen()
  pause(0.6);t=max(0.2,0.6-len(seq)*0.03)
  for i in seq:
   flash(i,t);pause(t/2)
  centre("?",VIF[3]);show_screen()
  for i in seq:
   k=0
   while k not in TOUCHES:
    k=getkey()
   j=TOUCHES.index(k);pad(j,True);show_screen();rl();pad(j,False)
   show_screen()
   if j!=i:
    for _ in range(3):
     for p in range(4):
      pad(p,True)
     show_screen();pause(0.15)
     for p in range(4):
      pad(p,False)
     show_screen();pause(0.15)
    return len(seq)-1
  centre(":)",VIF[0]);inf(len(seq),max(record,len(seq)));show_screen()
  pause(0.4)
def jouer():
 it();record=0
 while True:
  sc=pt(record);nw=sc>record;record=max(record,sc)
  rect(40,62,304,66,FD);rect(40,62,304,3,VIF[1])
  rect(40,125,304,3,VIF[1])
  draw_string(129,70,"PERDU !",VIF[1],"large")
  draw_string(60,100,("NOUVEAU RECORD : " if nw else "Score : ")+str(sc),TX,"medium")
  show_screen();rl()
  while getkey()!=OK:
   pass
  rl()
try:
 import sys
 auto='arcade' not in sys.modules
except:
 auto=True
if auto:
 jouer()
