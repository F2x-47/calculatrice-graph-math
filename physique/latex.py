from casioplot import set_pixel
import police
W=384
def rect(x,y,w,h,c):
 for i in range(x,x+w):
  for j in range(y,y+h):
   set_pixel(i,j,c)
def glyphe(c):
 if len(c)>1:
  return len(police.CH)+police.GR.index(c) if c in police.GR else -1
 return police.CH.find(c)
def groupe(s,i):
 if i>=len(s):
  return [],i
 if s[i]=="{":
  return analyse(s,i+1)
 return analyse(s[i],0)[0],i+1
def analyse(s,i=0):
 res=[]
 while i<len(s):
  c=s[i]
  if c=="}":
   return res,i+1
  if c=="\\":
   j=i+1
   while j<len(s) and s[j].isalpha():
    j+=1
   nom=s[i+1:j];i=j
   if i<len(s) and s[i]==" ":
    i+=1
   if nom=="frac":
    a,i=groupe(s,i);b,i=groupe(s,i);res.append(("f",a,b))
   elif nom in ("sqrt","vec"):
    a,i=groupe(s,i);res.append((nom[0],a))
   else:
    res.append(("g",nom))
  elif c in "^_":
   a,i=groupe(s,i+1);res.append((c,a))
  elif c=="{":
   a,i=analyse(s,i+1);res+=a
  elif c==" ":
   res.append((" ",));i+=1
  else:
   res.append(("g",c));i+=1
 return res,i
def mesure(nds,s):
 w=a=d=0
 for n in nds:
  t=n[0]
  if t=="g":
   nw,na,nd=6*s,8*s,2*s
  elif t==" ":
   nw,na,nd=3*s,0,0
  elif t in "^_":
   s2=max(1,s-1);nw,na,nd=mesure(n[1],s2)
   if t=="^":
    na,nd=na+4*s,max(0,nd-4*s)
   else:
    na,nd=max(0,na-3*s),nd+3*s
  elif t=="f":
   w1,a1,d1=mesure(n[1],s);w2,a2,d2=mesure(n[2],s)
   nw,na,nd=max(w1,w2)+4*s,3*s+3+d1+a1,a2+d2+3-3*s
  elif t=="s":
   nw,na,nd=mesure(n[1],s);nw,na=nw+6*s,na+2*s
  else:
   nw,na,nd=mesure(n[1],s);na+=4*s
  w+=nw;a=max(a,na);d=max(d,nd)
 return w,a,d
def dessine(nds,x,y,s,c):
 for n in nds:
  t=n[0]
  if t=="g":
   k=glyphe(n[1])
   if k>=0:
    for r in range(10):
     v=police.A.find(police.D[k*10+r])
     for b in range(6):
      if v>>(5-b)&1:
       rect(x+b*s,y-8*s+r*s,s,s,c)
   x+=6*s
  elif t==" ":
   x+=3*s
  elif t in "^_":
   s2=max(1,s-1);dessine(n[1],x,y-4*s if t=="^" else y+3*s,s2,c)
   x+=mesure(n[1],s2)[0]
  elif t=="f":
   w1,a1,d1=mesure(n[1],s);w2,a2,d2=mesure(n[2],s);w=max(w1,w2)+4*s
   ax=y-3*s;rect(x+s,ax,w-2*s,max(1,s//2+1),c)
   dessine(n[1],x+(w-w1)//2,ax-3-d1,s,c)
   dessine(n[2],x+(w-w2)//2,ax+3+a2,s,c);x+=w
  elif t=="s":
   w,a,d=mesure(n[1],s);rect(x,y-3*s,2*s,s,c)
   rect(x+2*s,y-3*s,s,3*s,c);rect(x+3*s,y-a-2*s,s,a+2*s,c)
   rect(x+3*s,y-a-2*s,w+3*s,s,c);dessine(n[1],x+6*s,y,s,c);x+=w+6*s
  else:
   w,a,d=mesure(n[1],s);rect(x,y-a-2*s,w,s,c)
   rect(x+w-2*s,y-a-3*s,s,3*s,c);dessine(n[1],x,y,s,c);x+=w
def formule(tex,cx,cy,s,c):
 nds=analyse(tex)[0];w,a,d=mesure(nds,s)
 while w>W-20 and s>1:
  s-=1;w,a,d=mesure(nds,s)
 dessine(nds,cx-w//2,cy+(a-d)//2,s,c)
