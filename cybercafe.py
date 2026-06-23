print("============Bienvenue dans le cybercafe la vie ================")

client_name = input("Entrez votre nom : ")
heure_arrivee = int(input("Entrez l'heure d'arrivée : "))
heure_depart = int(input("Entrez l'heure de départ : "))

prix_par_heure = 250
duree = heure_depart - heure_arrivee
montant_total = duree * prix_par_heure

if duree < 3:
    montant_total = montant_total * 0.10

print("=================================================")
print("Client : ", client_name)
print("Durée de la session : ", duree, " heures")
print("Montant total : ", montant_total, " F CFA")