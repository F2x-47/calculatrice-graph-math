from casioplot import set_pixel,draw_string
from math import sin
TW,TH=100,100;LI=(170,170,190);CO=((40,200,70),(235,40,50),(30,90,230),(250,210,0),(160,60,220),(255,140,0),(0,200,230))
def rect(x,y,w,h,c):
 for i in range(x,x+w):
  for j in range(y,y+h):
   set_pixel(i,j,c)
def terne(c):
 return (c[0]//3,c[1]//3,c[2]//3)
def bk(px,py,s,c):
 rect(px,py,s,s,c);rect(px,py,s,2,(min(255,c[0]+90),min(255,c[1]+90),min(255,c[2]+90)));rect(px,py+s-2,s,2,terne(c))
def vignette_pong(x,y):
 rect(x,y,TW,TH,(10,10,30))
 for j in range(y+6,y+TH-6,10):
  rect(x+49,j,2,5,LI)
 rect(x+8,y+30,5,28,(0,160,255));rect(x+TW-13,y+50,5,28,(230,0,120));rect(x+64,y+40,6,6,(255,140,0))
 draw_string(x+30,y+8,"3",(0,160,255),"medium");draw_string(x+60,y+8,"2",(230,0,120),"medium")
def vignette_tetris(x,y):
 rect(x,y,TW,TH,(10,10,30));s=10
 pile=((0,8,5),(1,8,5),(2,8,1),(3,8,1),(4,8,1),(5,8,1),(6,8,2),(7,8,2),(8,8,4),(9,8,4),
    (0,7,5),(1,7,6),(2,7,6),(3,7,6),(6,7,2),(7,7,2),(8,7,4),(9,7,3),
    (0,6,5),(3,6,6),(8,6,3),(9,6,3),
    (4,2,0),(4,3,0),(5,3,0),(5,4,0))
 for (a,b,c) in pile:
  bk(x+a*s,y+b*s+8,s,CO[c])
def zones(R,r,g):
 res=[]
 for d in range(g,R+1):
  b=min(int((R*R-d*d)**0.5),d-g);a=int((r*r-d*d)**0.5) if d<r else 0
  if b>a:
   res.append((d,a,b))
 return res
def disque(cx,cy,R,c):
 for dy in range(-R,R+1):
  w=int((R*R-dy*dy)**0.5);rect(cx-w,cy+dy,2*w+1,1,c)
def vignette_simon(x,y):
 rect(x,y,TW,TH,(10,10,30));cx,cy=x+50,y+50;disque(cx,cy,42,(70,70,110));disque(cx,cy,40,(10,10,25))
 vif=((40,220,70),(240,40,50),(40,110,255),(255,215,0))
 for (d,a,b) in zones(38,12,3):
  rect(cx-b,cy-d,b-a+1,1,vif[0]);rect(cx+a,cy-d,b-a+1,1,vif[0])
  rect(cx-b,cy+d,b-a+1,1,terne(vif[2]));rect(cx+a,cy+d,b-a+1,1,terne(vif[2]))
  rect(cx+d,cy-b,1,b-a+1,terne(vif[1]));rect(cx+d,cy+a,1,b-a+1,terne(vif[1]))
  rect(cx-d,cy-b,1,b-a+1,terne(vif[3]));rect(cx-d,cy+a,1,b-a+1,terne(vif[3]))
 disque(cx,cy,10,(70,70,110))
def vignette_serpent(x,y):
 rect(x,y,TW,TH,(18,20,40))
 for (a,b,c) in ((10,20,0),(30,70,5),(70,15,3),(85,60,1),(55,85,4),(15,85,6)):
  rect(x+a,y+b,3,3,CO[c])
 for i in range(40):
  px=x+12+i*2;py=y+50+int(10*sin(i/5.0));rect(px-3,py-3,7,7,(0,200,230))
 rect(x+90,py-2,2,2,(255,255,255));rect(x+90,py+1,2,2,(255,255,255))
 for i in range(14):
  rect(x+40+i*3,y+22+i,6,6,(240,70,90))
def vignette_cube(x,y):
 rect(x,y,TW,TH,(28,22,70));rect(x,y+76,TW,24,(10,70,120));rect(x,y+76,TW,2,(20,140,200))
 for i in range(0,TW,16):
  rect(x+i,y+78,8,22,(15,100,160))
 rect(x+20,y+40,14,14,(255,200,0));rect(x+20,y+40,14,2,(255,240,150));rect(x+23,y+44,3,3,(40,30,0))
 rect(x+28,y+44,3,3,(40,30,0));rect(x+23,y+49,8,2,(40,30,0))
 for (a,h) in ((50,16),(66,16)):
  for r in range(h):
   rect(x+a+8-r//2,y+60+r,2*(r//2)+1,1,(240,240,255))
 rect(x+80,y+58,18,18,(110,60,220));rect(x+80,y+58,18,2,(170,130,255));rect(x+85,y+63,8,8,(70,30,160))
def vignette_autre(x,y,c):
 rect(x,y,TW,TH,(10,10,30));rect(x+30,y+30,40,40,c)
def vignette_sudoku(x,y):
 rect(x,y,TW,TH,(20,20,45));rect(x+5,y+5,90,90,(28,30,60))
 for i in range(9):
  for j in range(9):
   rect(x+6+j*10,y+6+i*10,9,9,(246,244,236) if (i//3+j//3)%2==0 else (232,228,214))
 for (i,j,c) in ((0,1,(28,30,60)),(1,4,(28,30,60)),(2,7,(40,100,200)),(4,2,(40,100,200)),(4,4,(28,30,60)),(6,6,(28,30,60)),(7,1,(40,100,200)),(8,8,(28,30,60)),(3,6,(28,30,60)),(5,0,(40,100,200))):
  rect(x+9+j*10,y+8+i*10,3,5,c)
 rect(x+46,y+46,9,9,(150,210,240))
def vignette_invasion(x,y):
 rect(x,y,TW,TH,(10,10,30))
 for r,c in ((0,(240,70,90)),(1,(160,60,220)),(2,(0,200,230))):
  for k in range(4):
   ax,ay=x+12+k*22,y+14+r*16;rect(ax+2,ay,8,2,c);rect(ax,ay+2,12,4,c);rect(ax+2,ay+6,2,2,c);rect(ax+8,ay+6,2,2,c)
 rect(x+48,y+66,2,6,(255,255,255));rect(x+44,y+84,12,6,(0,220,160));rect(x+48,y+80,4,4,(0,220,160))
 rect(x,y+93,TW,1,(60,200,120))
def vignette_envol(x,y):
 for j in range(80):
  rect(x,y+j,TW,1,(70+j,140+j*2//3,215))
 for k in range(TW):
  m=58-abs((k*3)%60-30)*2//3;rect(x+k,y+m,1,80-m,(110,120,185))
 rect(x,y+80,TW,4,(90,200,90));rect(x,y+84,TW,16,(150,105,60))
 for (cx,h0,h1) in ((14,0,26),(14,58,80),(66,0,40),(66,72,80)):
  rect(x+cx,y+h0,16,h1-h0,(225,210,185));rect(x+cx+3,y+h0,3,h1-h0,(250,242,225))
  rect(x+cx+12,y+h0,3,h1-h0,(170,150,125))
 for (cx,cy) in ((14,24),(14,56),(66,38),(66,70)):
  rect(x+cx-2,y+cy,20,3,(90,70,60))
 rect(x+42,y+40,12,9,(160,80,220));rect(x+38,y+44,6,4,(220,170,255));rect(x+49,y+42,3,3,(255,255,255))
 rect(x+54,y+45,5,3,(255,150,40))
def vignette_naval(x,y):
 rect(x,y,TW,TH,(30,95,175))
 for k in range(0,TW,20):
  rect(x+k,y,1,TH,(18,60,125));rect(x,y+k,TW,1,(18,60,125))
 rect(x+21,y+21,59,19,(150,160,175));rect(x+61,y+61,19,39,(150,160,175));rect(x+41,y+21,19,19,(235,60,50))
 rect(x+47,y+27,7,7,(255,200,60))
 for (a,b) in ((0,3),(2,2),(4,0),(1,4),(4,3)):
  rect(x+a*20+8,y+b*20+8,5,5,(255,255,255))
DESSINS={"pong":vignette_pong,"tetris":vignette_tetris,"simon":vignette_simon,"serpent":vignette_serpent,"cube":vignette_cube,
    "sudoku":vignette_sudoku,"invasion":vignette_invasion,"envol":vignette_envol,"naval":vignette_naval}
