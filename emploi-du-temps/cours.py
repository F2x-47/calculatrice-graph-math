# Ton emploi du temps. Une ligne par cours :
#   (jour, debut, fin, matiere, salle, semaine)
# jour    : "Lun", "Mar", "Mer", "Jeu", "Ven" ou "Sam"
# debut et fin : l'heure en nombre. 8 = 8h00, 9.5 = 9h30, 10.25 = 10h15
# semaine : "" si le cours a lieu toutes les semaines,
#           "A" ou "B" s'il n'a lieu qu'une semaine sur deux
COURS=(
("Lun",8,9,"Maths","B12",""),
("Lun",9,10,"Francais","A04",""),
("Lun",10,12,"Physique-Chimie","Labo 2","A"),
("Lun",10,12,"SVT","Labo 5","B"),
("Lun",13.5,14.5,"Anglais","C21",""),
("Lun",14.5,16.5,"Sport","Gymnase",""),

("Mar",8,10,"Histoire-Geo","A11",""),
("Mar",10,11,"Allemand","C14",""),
("Mar",11,12,"Maths","B12",""),
("Mar",13.5,15,"SES","A07",""),
("Mar",15,16,"EMC","A11","A"),

("Mer",8,9,"Anglais","C21",""),
("Mer",9,10,"Maths","B12",""),
("Mer",10,12,"Francais","A04",""),

("Jeu",9,10,"Physique-Chimie","B03",""),
("Jeu",10,11,"SVT","B08",""),
("Jeu",11,12,"Allemand","C14",""),
("Jeu",13.5,14.5,"DNL","C21","B"),
("Jeu",14.5,15.5,"Maths","B12",""),
("Jeu",15.5,17,"Eco-Gestion","A09","A"),
("Jeu",15.5,17,"SISL","A09","B"),

("Ven",8,9,"Francais","A04",""),
("Ven",9,10,"Histoire-Geo","A11",""),
("Ven",10,11,"Anglais","C21",""),
("Ven",11,12,"Maths","B12","A"),
("Ven",13.5,15.5,"SES","A07","B"),
)
