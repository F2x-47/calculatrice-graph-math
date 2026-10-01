# moyenne claude

notes_maths = [20]
notes_francais = []
notes_histoire_geo = []
notes_emc = []
notes_anglais = [17, 16.5]
notes_dnl = []
notes_allemand = []
notes_physique_chimie = [17.25]
notes_svt = []
notes_ses = []
notes_sisl = []
notes_management_gestion = []
notes_sport = []

coef_notes_maths = [1]
coef_notes_francais = []
coef_notes_histoire_geo = []
coef_notes_emc = []
coef_notes_anglais = [1, 1]
coef_notes_dnl = []
coef_notes_allemand = []
coef_notes_physique_chimie = [1]
coef_notes_svt = []
coef_notes_ses = []
coef_notes_sisl = []
coef_notes_management_gestion = []
coef_notes_sport = []

coef_maths = 2
coef_francais = 2
coef_histoire_geo = 2
coef_emc = 1
coef_anglais = 2
coef_dnl = 0.5
coef_allemand = 2
coef_physique_chimie = 2
coef_svt = 2
coef_ses = 2
coef_sisl = 0.5
coef_management_gestion = 0.5
coef_sport = 2

def moyenne_matiere(notes, coef):
    if len(notes) == 0:
        return None
    num = 0
    den = 0
    for i in range(len(notes)):
        num = num + notes[i] * coef[i]
        den = den + coef[i]
    return num / den

result_moyenne_maths = moyenne_matiere(notes_maths, coef_notes_maths)
result_moyenne_francais = moyenne_matiere(notes_francais, coef_notes_francais)
result_moyenne_histoire_geo = moyenne_matiere(notes_histoire_geo, coef_notes_histoire_geo)
result_moyenne_emc = moyenne_matiere(notes_emc, coef_notes_emc)
result_moyenne_anglais = moyenne_matiere(notes_anglais, coef_notes_anglais)
result_moyenne_dnl = moyenne_matiere(notes_dnl, coef_notes_dnl)
result_moyenne_allemand = moyenne_matiere(notes_allemand, coef_notes_allemand)
result_moyenne_physique_chimie = moyenne_matiere(notes_physique_chimie, coef_notes_physique_chimie)
result_moyenne_svt = moyenne_matiere(notes_svt, coef_notes_svt)
result_moyenne_ses = moyenne_matiere(notes_ses, coef_notes_ses)
result_moyenne_sisl = moyenne_matiere(notes_sisl, coef_notes_sisl)
result_moyenne_management_gestion = moyenne_matiere(notes_management_gestion, coef_notes_management_gestion)
result_moyenne_sport = moyenne_matiere(notes_sport, coef_notes_sport)

liste_moyennes = []
liste_moyennes.append(result_moyenne_maths)
liste_moyennes.append(result_moyenne_francais)
liste_moyennes.append(result_moyenne_histoire_geo)
liste_moyennes.append(result_moyenne_emc)
liste_moyennes.append(result_moyenne_anglais)
liste_moyennes.append(result_moyenne_dnl)
liste_moyennes.append(result_moyenne_allemand)
liste_moyennes.append(result_moyenne_physique_chimie)
liste_moyennes.append(result_moyenne_svt)
liste_moyennes.append(result_moyenne_ses)
liste_moyennes.append(result_moyenne_sisl)
liste_moyennes.append(result_moyenne_management_gestion)
liste_moyennes.append(result_moyenne_sport)

liste_coefs = []
liste_coefs.append(coef_maths)
liste_coefs.append(coef_francais)
liste_coefs.append(coef_histoire_geo)
liste_coefs.append(coef_emc)
liste_coefs.append(coef_anglais)
liste_coefs.append(coef_dnl)
liste_coefs.append(coef_allemand)
liste_coefs.append(coef_physique_chimie)
liste_coefs.append(coef_svt)
liste_coefs.append(coef_ses)
liste_coefs.append(coef_sisl)
liste_coefs.append(coef_management_gestion)
liste_coefs.append(coef_sport)

def moyenne_g(moyennes, coefs):
    num = 0
    den = 0
    for i in range(len(moyennes)):
        moy = moyennes[i]
        coef = coefs[i]
        if moy != None:
            num = num + moy * coef
            den = den + coef
    if den == 0:
        return None
    return num / den

def affichage_result():
    print("MOYENNE GENERALE :", round(moyenne_g(liste_moyennes, liste_coefs), 3))
    print("Moyenne Maths :", round(result_moyenne_maths, 3))
    print("Moyenne Francais :", result_moyenne_francais)
    print("Moyenne Histoire-Geo :", result_moyenne_histoire_geo)
    print("Moyenne EMC :", result_moyenne_emc)
    print("Moyenne Anglais :", round(result_moyenne_anglais, 3))
    print("Moyenne DNL :", result_moyenne_dnl)
    print("Moyenne Allemand :", result_moyenne_allemand)
    print("Moyenne Physique-Chimie :", round(result_moyenne_physique_chimie, 3))
    print("Moyenne SVT :", result_moyenne_svt)
    print("Moyenne SES :", result_moyenne_ses)
    print("Moyenne SISL :", result_moyenne_sisl)
    print("Moyenne ECO :", result_moyenne_management_gestion)
    print("Moyenne Sport :", result_moyenne_sport)

affichage_result()