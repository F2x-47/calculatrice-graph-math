from casioplot import *
import cours
W,H=384,192;HA,BA,GA,DR,OK=14,34,23,25,24;BLANC=(255,255,255);SEP=(222,226,233);NAVY=(28,45,80);SEL=(45,105,190)
TX=(30,35,45);LI=(120,128,140)
PAL=((45,105,190),(205,125,25),(35,140,80),(190,55,55),(130,70,190),(0,150,160),(200,80,140),
  (110,130,30),(90,90,200),(170,100,50),(60,60,70),(0,120,200),(210,60,100))
ABR=("Lun","Mar","Mer","Jeu","Ven","Sam");NOMS=("Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi");C=cours.COURS
ND=5;HMIN,HMAX=24,0;MAT=[]
for c in C:
 if c[0]=="Sam":
  ND=6
 HMIN=min(HMIN,int(c[1]));HMAX=max(HMAX,int(c[2]+0.99))
 if c[3] not in MAT:
  MAT.append(c[3])
X0=26;CW=(W-X0)//ND;RH=min(18,(H-30)//max(1,HMAX-HMIN))
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
def heure(h):
 m=int((h-int(h))*60+0.5)
 return str(int(h))+"h"+("0" if m<10 else "")+str(m)
def du_jour(j,s):
 r=[]
 for c in C:
  if c[0]==ABR[j] and c[5] in ("",s):
   i=len(r)
   while i>0 and r[i-1][1]>c[1]:
    i-=1
   r.insert(i,c)
 return r
def semaine(j,s):
 clear_screen();draw_string(3,1,"S."+s,SEL,"small")
 for d in range(ND):
  x=X0+d*CW
  if d==j:
   rect(x,0,CW-2,14,SEL)
  draw_string(x+(CW-26)//2,1,ABR[d],BLANC if d==j else NAVY,"small")
 rect(0,15,W,1,NAVY)
 for h in range(HMIN,HMAX):
  y=17+(h-HMIN)*RH;draw_string(1,y,str(h)+"h",LI,"small")
  for x in range(X0,W,4):
   set_pixel(x,y,SEP)
 for d in range(ND):
  x=X0+d*CW
  for c in du_jour(d,s):
   y=17+int((c[1]-HMIN)*RH);h=int((c[2]-c[1])*RH);rect(x,y+1,4,h-2,PAL[MAT.index(c[3])%13]);rect(x+4,y+h-1,CW-8,1,SEP)
   draw_string(x+7,y+2,c[3][:(CW-9)//7],TX if d==j else LI,"small")
   if c[5]:
    rect(x+CW-5,y+2,2,5,SEL)
 draw_string(3,H-12,"< > : jour     ^ v : semaine A / B     OK : detail du jour",LI,"small");show_screen()
def jour(j,s):
 clear_screen();draw_string(10,8,NOMS[j],NAVY,"medium");draw_string(W-110,6,"Semaine "+s,SEL,"medium")
 rect(0,30,W,2,NAVY);t=du_jour(j,s)
 if not t:
  draw_string(10,50,"Pas de cours",LI,"medium")
 n=len(t);p=min(19,136//max(1,n))
 for i in range(n):
  c=t[i];y=36+i*p;rect(104,y,4,p-3,PAL[MAT.index(c[3])%13]);draw_string(8,y+2,heure(c[1])+" - "+heure(c[2]),LI,"small")
  draw_string(114,y,c[3],TX,"medium");draw_string(290,y+2,c[4],LI,"small")
  if c[5]:
   draw_string(W-22,y+2,c[5],SEL,"small")
 rect(0,H-17,W,1,SEP);draw_string(3,H-12,"< > : jour     ^ v : semaine A / B     OK : semaine entiere",LI,"small")
 show_screen()
def edt():
 j,s,detail=0,"A",False
 while True:
  if detail:
   jour(j,s)
  else:
   semaine(j,s)
  k=touche()
  if k==OK:
   detail=not detail
  elif k in (HA,BA):
   s="B" if s=="A" else "A"
  else:
   j=(j+(1 if k==DR else -1))%ND
edt()
