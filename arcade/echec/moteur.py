from random import randint
VAL={"P":100,"N":320,"B":330,"R":500,"Q":900,"K":20000}
DIRS={"N":(-21,-19,-12,-8,8,12,19,21),"B":(-11,-9,9,11),"R":(-10,-1,1,10),
   "Q":(-11,-10,-9,-1,1,9,10,11),"K":(-11,-10,-9,-1,1,9,10,11)}
GLISSE="BRQ"
def depart():
 b=[" "]*120
 rang=("rnbqkbnr","pppppppp","........","........","........","........","PPPPPPPP","RNBQKBNR")
 for l in range(8):
  for c in range(8):
   b[21+10*l+c]=rang[l][c]
 return [b,"w","KQkq",0]
def blanc(p):
 return p.isupper()
def a_moi(p,cote):
 return p not in " ." and (p.isupper()==(cote=="w"))
def attaque(b,s,cote):
 for d in DIRS["N"]:
  p=b[s+d]
  if p in "Nn" and a_moi(p,cote):
   return True
 for d in DIRS["K"]:
  p=b[s+d]
  if p in "Kk" and a_moi(p,cote):
   return True
 for (ds,ty) in (((-11,-9,9,11),"BQ"),((-10,-1,1,10),"RQ")):
  for d in ds:
   x=s+d
   while b[x]==".":
    x+=d
   p=b[x]
   if p!=" " and a_moi(p,cote) and p.upper() in ty:
    return True
 pion="P" if cote=="w" else "p";r=10 if cote=="w" else -10
 return b[s+r-1]==pion or b[s+r+1]==pion
def roi(b,cote):
 return b.index("K" if cote=="w" else "k")
def coups(pos):
 b,cote,roq,ep=pos;res=[]
 for s in range(21,99):
  p=b[s]
  if not a_moi(p,cote):
   continue
  t=p.upper()
  if t=="P":
   av=-10 if cote=="w" else 10
   if b[s+av]==".":
    res.append((s,s+av,0))
    if (s//10==8 and cote=="w") or (s//10==3 and cote=="b"):
     if b[s+2*av]==".":
      res.append((s,s+2*av,0))
   for d in (av-1,av+1):
    q=b[s+d]
    if q not in " ." and not a_moi(q,cote):
     res.append((s,s+d,0))
    elif s+d==ep:
     res.append((s,s+d,1))
  else:
   for d in DIRS[t]:
    x=s+d
    while b[x]!=" ":
     q=b[x]
     if q==".":
      res.append((s,x,0))
     else:
      if not a_moi(q,cote):
       res.append((s,x,0))
      break
     if t not in GLISSE:
      break
     x+=d
 adv="b" if cote=="w" else "w"
 if cote=="w":
  if "K" in roq and b[96]==b[97]=="." and not attaque(b,95,adv) and not attaque(b,96,adv) and not attaque(b,97,adv):
   res.append((95,97,2))
  if "Q" in roq and b[94]==b[93]==b[92]=="." and not attaque(b,95,adv) and not attaque(b,94,adv) and not attaque(b,93,adv):
   res.append((95,93,2))
 else:
  if "k" in roq and b[26]==b[27]=="." and not attaque(b,25,adv) and not attaque(b,26,adv) and not attaque(b,27,adv):
   res.append((25,27,2))
  if "q" in roq and b[24]==b[23]==b[22]=="." and not attaque(b,25,adv) and not attaque(b,24,adv) and not attaque(b,23,adv):
   res.append((25,23,2))
 return res
def joue(pos,m):
 b,cote,roq,ep=pos;b=b[:];s,x,sp=m;p=b[s];b[x]=p;b[s]=".";nep=0
 if sp==1:
  b[x+(10 if cote=="w" else -10)]="."
 elif sp==2:
  if x==97: b[98],b[96]=".","R"
  if x==93: b[91],b[94]=".","R"
  if x==27: b[28],b[26]=".","r"
  if x==23: b[21],b[24]=".","r"
 if p in "Pp":
  if abs(x-s)==20:
   nep=(s+x)//2
  if x<29 or x>90:
   b[x]="Q" if p=="P" else "q"
 for (c,l) in ((95,"KQ"),(25,"kq"),(98,"K"),(91,"Q"),(28,"k"),(21,"q")):
  if s==c or x==c:
   for ch in l:
    roq=roq.replace(ch,"")
 return [b,"b" if cote=="w" else "w",roq,nep]
def legaux(pos):
 res=[]
 for m in coups(pos):
  n=joue(pos,m)
  if not attaque(n[0],roi(n[0],pos[1]),n[1]):
   res.append(m)
 return res
def echec(pos):
 return attaque(pos[0],roi(pos[0],pos[1]),"b" if pos[1]=="w" else "w")
CENTRE=(0,1,2,3,3,2,1,0)
def evalue(b):
 sc=0
 for s in range(21,99):
  p=b[s]
  if p in " .":
   continue
  t=p.upper();v=VAL[t];l,c=s//10-2,s%10-1
  if t in "NB":
   v+=4*(CENTRE[l]+CENTRE[c])
  elif t=="P":
   v+=(6-l if p=="P" else l-1)*6+(4 if 2<c<5 else 0)
  sc+=v if blanc(p) else -v
 return sc
def recherche(pos,prof,a,bt):
 if prof==0:
  e=evalue(pos[0])
  return e if pos[1]=="w" else -e
 ms=coups(pos);ms.sort(key=lambda m:-VAL.get(pos[0][m[1]].upper(),0))
 mx=-99999
 for m in ms:
  if pos[0][m[1]] in "Kk":
   return 50000
  v=-recherche(joue(pos,m),prof-1,-bt,-a)
  if v>mx:
   mx=v
  if v>a:
   a=v
  if a>=bt:
   break
 return mx
def ordi(pos,niveau):
 ms=legaux(pos);prof=(1,2,3)[niveau];best,choix=-999999,[]
 for m in ms:
  v=-recherche(joue(pos,m),prof-1,-999999,999999)+(randint(0,30) if niveau==0 else randint(0,4))
  if v>best:
   best,choix=v,m
 return choix
