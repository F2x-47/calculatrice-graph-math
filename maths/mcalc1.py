from mbase import *
def stats():
 v=[]
 while True:
  t=saisie("Valeur "+str(len(v)+1)+"  (CALCULER quand c'est fini)","CALCULER")
  if t==None:
   break
  try:
   v.append(float(t))
  except:
   pass
 n=len(v)
 if n==0:
  return
 v.sort();s=0
 for x in v:
  s+=x
 m=s/n;var=0
 for x in v:
  var+=(x-m)**2
 var/=n;med=v[n//2] if n%2 else (v[n//2-1]+v[n//2])/2;q1=v[(n+3)//4-1];q3=v[(3*n+3)//4-1]
 res=(("Effectif N",n),("Somme",s),("Moyenne",m),("Mediane",med),("Minimum",v[0]),("Maximum",v[-1]),
   ("Quartile Q1",q1),("Quartile Q3",q3),("Etendue",v[-1]-v[0]),("Ecart Q3-Q1",q3-q1),
   ("Variance",var),("Ecart type",var**0.5))
 page("STATISTIQUES","OK ou < : retour")
 for i in range(12):
  x,y=10+(i%2)*190,42+(i//2)*21;draw_string(x,y+3,res[i][0],LI,"small")
  draw_string(x+88,y,joli(res[i][1]),SEL if i in (2,11) else TX,"medium")
 pause()
def pgcd(a,b):
 while b:
  a,b=b,a%b
 return a
def frac(n,d):
 if d<0:
  n,d=-n,-d
 g=pgcd(abs(n),d);n,d=n//g,d//g
 if d==1:
  return str(n)
 return ("-" if n<0 else "")+r"\frac{"+str(abs(n))+"}{"+str(d)+"}"
def terme(k,nom,debut):
 if k==0:
  return ""
 s="-" if k<0 else ("" if debut else "+");k=abs(k)
 if k!=1 or not nom:
  s+=joli(k)
 return s+nom
def second():
 a=nombre("Second degre : coefficient a")
 if not a:
  return
 b=nombre("Coefficient b")
 if b==None:
  return
 c=nombre("Coefficient c")
 if c==None:
  return
 d=b*b-4*a*c;page("SECOND DEGRE","OK ou < : retour");t=terme(a,"x^2",True)+terme(b,"x",False)+terme(c,"",False)+"=0"
 formule(t,W//2,50,1,TX);formule(r"\Delta=b^2-4ac="+joli(d),W//2,72,1,NAVY);ent=a==int(a) and b==int(b) and c==int(c)
 if d<0:
  draw_string(60,98,"Pas de solution reelle",ROUGE,"medium")
 elif d==0:
  x=-b/(2*a);t="x_0="+(frac(int(-b),int(2*a)) if ent else joli(x));formule(t,W//2,104,2,SEL)
  draw_string(120,126,"Une solution double",LI,"small")
 else:
  r=d**0.5;x1,x2=(-b-r)/(2*a),(-b+r)/(2*a)
  if ent and int(r+0.5)**2==d:
   r=int(r+0.5);t="x_1="+frac(int(-b)-r,int(2*a))+"   x_2="+frac(int(-b)+r,int(2*a));formule(t,W//2,104,2,SEL)
  elif ent:
   for k in (0,1):
    t="x_"+str(k+1)+r"=\frac{"+str(int(-b))+"-+"[k]+r"\sqrt{"+str(int(d))+"}}{"+str(int(2*a))+"}"
    formule(t,100+k*184,104,1,SEL)
  if not ent or int(r+0.5)**2!=d:
   draw_string(40,124,"x1 = "+joli(x1),TX,"medium");draw_string(210,124,"x2 = "+joli(x2),TX,"medium")
 al=-b/(2*a);be=a*al*al+b*al+c;draw_string(10,146,"Sommet S( "+joli(al)+" ; "+joli(be)+" )",LI,"small")
 draw_string(10,160,("Minimum" if a>0 else "Maximum")+" de la fonction : "+joli(be),LI,"small");pause()
