print()
print("Choisir une formule :")
print("(1) masse volumique")
print("(2) vitesse")
print("(3) loi d'ohm")
print("(4) ")
formule = input("formule : ")
if formule == "1":
  print()
  print("(1) normale")
  print("(2) masse")
  print("(3) volume")
  quoi = input(" - ")
  if quoi == "1":
    print()
    masse = float(input("masse : "))
    print("(1) gramme (g)")
    print("(2) kilogramme (kg)")
    print("(3) tonne (t)")
    print("(4) milligramme (mg)")
    mesure_masse = input(" - ")
    print()
    volume = float(input("volume : "))
    print("(1) litre (L)")
    print("(2) millilitre (mL)")
    print("(3) centilitre (cL)")
    print("(4) metre-cube (m^3)")
    mesure_volume = input(" - ")
    if mesure_masse == "1" and mesure_volume == "1":
      mesure_choisie = "g/L"
    elif mesure_masse == "1" and mesure_volume == "2":
      mesure_choisie = "g/mL"
    elif mesure_masse == "1" and mesure_volume == "3":
      mesure_choisie = "g/cL"
    elif mesure_masse == "1" and mesure_volume == "4":
      mesure_choisie = "g/m^3"
    elif mesure_masse == "2" and mesure_volume == "1":
      mesure_choisie = "kg/L"
    elif mesure_masse == "2" and mesure_volume == "2":
      mesure_choisie = "kg/mL"
    rho = print(masse / volume, " ", mesure_choisie)
  elif quoi == "2":
    print()
    rho = float(input("rho : "))
    print("(1) g/L")
    print("(2) g/mL")
    print("(3) kg/L")
    print("(4) g/cL")
    mesure_rho = input(" - ")
    volume = float(input("volume : "))
    print("(1) litre (L)")
    print("(2) millilitre (mL)")
    print("(3) centilitre (cL)")
    print("(4) metre-cube (m^3)")
    mesure_volume = input(" - ")
    if mesure_rho == "1" and mesure_volume == "1":
      mesure_choisie = "g"
    elif mesure_rho == "1" and mesure_volume == "2":
      mesure_choisie = "erreur de mesure"
    elif mesure_rho == "1" and mesure_volume == "3":
      mesure_choisie = "erreur de mesure"
    elif mesure_rho == "1" and mesure_volume == "4":
      mesure_choisie = "erreur de mesure"
    masse = print(rho * volume, mesure_choisie)
elif formule == "2":
  # vitesse
  print()
elif formule == "3":
  # loi d'ohm
  print()
  print("(1) tension")
  print("(2) resistance")
  print("(3) intensite")
  quoi = input(" - ")
  if quoi == "1":
    print()
    resistance = float(input("resistance : "))
    intensite = float(input("intensite : "))
    print(resistance * intensite, "ohm")
  if quoi == "2":
    print()
    tension = float(input("tension : "))
    intensite = float(input("intensite : "))
    print(tension / intensite, "ohm")