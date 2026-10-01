# Messages preenregistres de Claudette
# (mot-cle, reponse). | = retour a la ligne, une ligne qui commence par $$ = formule LaTeX
# Tu peux ajouter tes propres messages en suivant le meme modele.
R=[
("bonjour","Bonjour ! Comment puis-je t'aider aujourd'hui ?"),
("salut","Salut ! Qu'est-ce que je peux faire pour toi ?"),
("merci","Avec plaisir ! N'hesite pas si tu as d'autres questions."),
("qui es","Je suis Claudette, un assistant qui t'aide a reviser les maths, la physique et la chimie."),
("second degre",r"Pour resoudre ax^2+bx+c=0, on calcule le discriminant :|$$\Delta=b^2-4ac|Si Delta > 0, deux solutions :|$$x_1=\frac{-b-\sqrt{\Delta}}{2a}|$$x_2=\frac{-b+\sqrt{\Delta}}{2a}|Si Delta = 0, une solution : x = -b/(2a).|Si Delta < 0, pas de solution reelle."),
("derivee",r"Les derivees a connaitre :|$$(x^n)'=n x^{n-1}|$$(\frac{1}{x})'=-\frac{1}{x^2}|$$(\sqrt{x})'=\frac{1}{2\sqrt{x}}|$$(e^x)'=e^x|Et (uv)' = u'v + uv'."),
("maths","En maths, je peux t'aider sur :|- le second degre (tape : second degre)|- les derivees (tape : derivee)|- les suites (tape : suite)|Que veux-tu revoir ?"),
("suite",r"Suite arithmetique de raison r :|$$u_n=u_0+n r|Suite geometrique de raison q :|$$u_n=u_0\times q^n"),
("physique",r"Quelques formules essentielles :|$$v=\frac{d}{\Delta t}|$$E_c=\frac{1}{2}m v^2|$$P=U\times I|Tu veux un chapitre en particulier ? (energie, ondes, electricite)"),
("energie","L'energie mecanique est la somme des energies cinetique et potentielle :|$$E_m=E_c+E_{pp}|avec Epp = mgz. Sans frottements, Em se conserve."),
("ondes",r"Pour une onde periodique :|$$\lambda=v T=\frac{v}{f}|lambda en m, v en m/s, T en s et f en Hz."),
("electricite",r"Loi d'Ohm et puissance :|$$U=R\times I|$$P=U\times I|U en volts, R en ohms, I en amperes, P en watts."),
("chimie",r"Les relations de base :|$$n=\frac{m}{M}|$$C=\frac{n}{V}|n en mol, m en g, M en g/mol, V en L."),
]
DEFAUT="Je n'ai pas bien compris ta demande. Peux-tu preciser ? Je peux t'aider en maths, physique ou chimie."
SUGG=["bonjour","maths","physique","chimie"]

# Resultats de recherche de Gogole : (mot-cle, [(titre, adresse, extrait), ...])
S=[
("claudette",[("Claudette - Assistant","claudette.app","Discute avec Claudette, ton assistant de revision."),("Telecharger Claudette","claudette.app/download","Disponible sur ta calculatrice.")]),
("maths",[("Cours de maths - Lycee","maths-lycee.fr","Fiches de cours, exercices corriges et methodes."),("Second degre : le cours","maths-lycee.fr/second-degre","Discriminant, racines et factorisation.")]),
("physique",[("Physique-Chimie au lycee","physique-lycee.fr","Formules, cours et exercices pour le bac."),("Tableau periodique","physique-lycee.fr/tableau","Les 118 elements et leurs proprietes.")]),
]
