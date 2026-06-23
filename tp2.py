print("=================================================")
print("bienvenue a sama multi_services")
print("=================================================")

price_bread = float(input("Entrez le prix du pain (en FCFA, nombre seulement) : "))
quantity_bread = float(input("Entrez la quantité de pain : "))
price_b = price_bread * quantity_bread

price_milk = float(input("Entrez le prix du lait (en FCFA, nombre seulement) : "))
quantity_milk = float(input("Entrez la quantité de lait : "))
price_m = price_milk * quantity_milk

price_sugar = float(input("Entrez le prix du sucre (en FCFA, nombre seulement) : "))
quantity_sugar = float(input("Entrez la quantité de sucre : "))
price_s = price_sugar * quantity_sugar

ht = price_b + price_m + price_s
tva = ht * 0.18
ttc = ht + tva

print("=================================================")
print("montant HT: ", ht,"cfa")
print("montant TVA: ", tva,"cfa")
print("montant TTC: ", ttc,"cfa")
print("Merci d'avoir utilisé sama multi_services")