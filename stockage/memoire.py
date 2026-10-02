from casioplot import *

# Memoire disponible pour Python sur Casio Graph Math+
W,H=384,192
NAVY=(28,45,80)
GRIS=(222,226,233)
LI=(120,128,140)
VERT,ORANGE,ROUGE=(35,140,80),(205,125,25),(190,55,55)

def rect(x,y,w,h,c):
  for i in range(x,x+w):
    for j in range(y,y+h):
      set_pixel(i,j,c)

def ko(n):
  return str(n//1024)+" Ko" if n<1048576 else str(n*10//1048576/10)+" Mo"

def mesure():
  # renvoie (libre, total) en octets ; total = 0 si la calculatrice ne le donne pas
  try:
    import gc
    gc.collect()
    l=gc.mem_free()
    return l,l+gc.mem_alloc()
  except:
    pass
  # methode de secours : on remplit la memoire par blocs de 1 Ko jusqu'a ce qu'elle soit pleine
  t=[]
  n=0
  try:
    while True:
      t.append("x"*1000+str(n))
      n+=1
  except MemoryError:
    pass
  t=None
  return n*1024,0

clear_screen()
draw_string(10,10,"MEMOIRE PYTHON",NAVY,"medium")
rect(0,34,W,2,NAVY)
draw_string(10,60,"Mesure en cours...",LI,"medium")
show_screen()
libre,total=mesure()
rect(0,50,W,40,(255,255,255))
draw_string(20,50,"Libre : "+ko(libre),NAVY,"large")
if total:
  pris=total-libre
  p=pris*100//total
  c=VERT if p<60 else (ORANGE if p<85 else ROUGE)
  # barre de progression qui se remplit
  rect(20,90,344,24,GRIS)
  for x in range(0,340*p//100,4):
    rect(22+x,92,4,20,c)
    show_screen()
  draw_string(20,122,"Utilise : "+ko(pris)+" sur "+ko(total)+"  ("+str(p)+" %)",c,"medium")
else:
  draw_string(20,96,"(total inconnu sur cette calculatrice)",LI,"small")
draw_string(10,150,"C'est la memoire de travail de Python,",LI,"small")
draw_string(10,164,"pas l'espace de stockage des fichiers.",LI,"small")
show_screen()
while not getkey():
  pass
