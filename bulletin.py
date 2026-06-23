last_name = input("Entrez votre nom : ")
first_name = input("Entrez votre prenom : ")


course_1 = input("Entrez le nom du premier cours : ")
grade_1 = float(input("Entrez la note du devoir(40%) : "))
exam_1 = float(input("Entrez la note de l'examen (60%) : "))

course_2 = input("Entrez le nom du deuxième cours : ")
grade_2 = float(input("Entrez la note du devoir(40%) : "))
exam_2 = float(input("Entrez la note de l'examen (60%) : "))

course_3 = input("Entrez le nom du troisième cours : ")
grade_3 = float(input("Entrez la note du devoir(40%) : "))
exam_3 = float(input("Entrez la note de l'examen (60%) : "))

course_4 = input("Entrez le nom du quatrième cours : ")
grade_4 = float(input("Entrez la note du devoir(40%) : "))
exam_4 = float(input("Entrez la note de l'examen (60%) : "))    

course_5 = input("Entrez le nom du cinquième cours : ")
grade_5 = float(input("Entrez la note du devoir(40%) : "))
exam_5 = float(input("Entrez la note de l'examen (60%) : "))

avrage_1 = round(grade_1 * 0.4 + exam_1 * 0.6, 2)
avrage_2 = round(grade_2 * 0.4 + exam_2 * 0.6, 2)
avrage_3 = round(grade_3 * 0.4 + exam_3 * 0.6, 2)
avrage_4 = round(grade_4 * 0.4 + exam_4 * 0.6, 2)
avrage_5 = round(grade_5 * 0.4 + exam_5 * 0.6, 2)   

total_average = round((avrage_1 + avrage_2 + avrage_3 + avrage_4 + avrage_5) / 5, 2)

print("=============bulletin de ",last_name, first_name, " =================")


print(course_1, " devoir ", grade_1, " note examen ", exam_1, )
print(course_2, " devoir ", grade_2, " note examen ", exam_2, )
print(course_3, " devoir ", grade_3, " note examen ", exam_3, )
print(course_4, " devoir ", grade_4, " note examen ", exam_4, )
print(course_5, " devoir ", grade_5, " note examen ", exam_5, )

print("------------------------------------------------------")

print("la moyenne est :  ",total_average, "/20")