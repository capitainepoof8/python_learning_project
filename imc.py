weight=input("Entrez votre poids en kg : ")
height=input("Entrez votre taille en m : ")
imc = float(weight) / (float(height) ** 2)

print("Votre poids est : ", weight, "kg")
print("Votre taille est : ", height, "m")
print("Votre IMC est : ", imc)