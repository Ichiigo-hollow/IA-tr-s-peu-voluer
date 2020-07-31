from datetime import datetime
import random

fic = open('liste.txt', 'a')

#Comment demander l'heure
Quelle_heure_est_il = "Quelle heure est il"
Quelle_heure_est_il_ = "Quelle heure est il ?"
quelle_heure_est_il_ = "quelle heure est il ?"
quelle_heure_est_il = "quelle heure est il"

#demander comment s'appelle roger
Comment_appelle_tu_ = "Comment t'appelle tu ?"
Comment_tu_appelle_ = "Comment tu t'appelle ?"
comment_tu_appelle = "comment tu t'appelle"
comment_appelle_tu = "comment t'appelle tu"
Comment_appelle_tu = "Comment t'appelle tu"
Comment_tu_appelle = "Comment tu t'appelle"
comment_tu_appelle_ = "comment tu t'appelle ?"
comment_appelle_tu_ = "Comment t'appelle tu ?"

#les blagues de Roger

blague1 = "quel est le comble d’un boucher ? --- C’est d’avoir un caractère de cochon."
blague2 = "Quel est le comble d’un jardinier ? --- C’est de raconter des salades."
blague3 = "Pourquoi les marins ne peuvent-ils pas écrire ? --- Parce-qu’ils ont jeté l’ancre !"
blague4 = "Papa, qu’est-ce que ça fait d’avoir un fils aussi beau ? --- Je ne sais pas mon fils, demande à ton grand-père."
blague5 = "que dit un fantôme qui en rencontre un autre ? --- Toi aussi tu es dans de beaux draps."
blague6 = "Où se cache Mozart ? --- Dans le frigo….Car Mozzarella…"
blague7 = "Un œuf attend un autre œuf : --- Si dans 5 minutes, il n’est pas là, j’me casse !"
blague8 = "Quelle est la chanteuse préférée des serruriers ? --- Alicia Keys."
blague9 = "2 vaches discutent : – Ça te fait pas peur toi ces histoires de « vache folle » ? --- Ben j’m’en fous j’suis un lapin !"
blague10 = "Comment tu fais pour sauver Donald Trump de la noyade ? --- Tu ne sais pas ? Tant mieux !"
blague11 = "Qu’est-ce qu’un nem avec des écouteurs ? --- Un NemP3…"
blague12 = "Comment ramasse-t-on la papaye? --- Avec une foufourche"
blague13 = "Est-ce que faire des gâteaux d’instinct... C ‘est avoir la pate à tarte innée ?"
blague14 = "Quel est le comble pour un acteur obèse ? --- Faire un bide"
blague15 = "J’ai raconté une blague à un Parisien… Il a pas ri…"
blague16 = "Pourquoi Napoléon n’ a jamais déménagé? --- Parce qu’il avait un Bonaparte"
blague17 = "Docteur, j’ai mal au dos quand je me lève le matin… Et bien, levez-vous l’après-midi !"
blague18 = "Que faire pour sauver la vie d’une mouche qui se noie ? --- Du mouche à mouche"
blague19 = "Quel est le comble pour un électricien ? --- D’avoir des ampoules aux pieds"
blague20 = "Que dit un zéro quand il rencontre un huit ? --- « T’as mis une ceinture ? »"
raconte_moi_une_blague = "raconte moi une blague"
Raconte_moi_une_blague = "Raconte moi une blague"
blague = 0


#liste de cours
class list_de_cours():
    def __init__(self):
        self.object1 = input("1ère objet : ")
        self.object2 = input("2ème objet : ")
        self.object3 = input("3ème objet : ")
        self.object4 = input("4ème objet : ")
        self.object5 = input("5ème objet : ")
        self.object6 = input("6ème objet : ")
        self.object7 = input("7ème objet : ")
        self.object8 = input("8ème objet : ")
        self.object9 = input("9ème objet : ")
        self.object10 = input("10ème objet : ")
        self.object11 = input("11ère objet : ")
        self.object12 = input("12ème objet : ")
        self.object13 = input("13ème objet : ")
        self.object14 = input("14ème objet : ")
        self.object15 = input("15ème objet : ")
        self.object16 = input("16ème objet : ")
        self.object17 = input("17ème objet : ")
        self.object18 = input("18ème objet : ")
        self.object19 = input("19ème objet : ")
        self.object20 = input("20ème objet : ")
        print("Votre liste de course est : ")
        print(self.object1)
        print(self.object2)
        print(self.object3)
        print(self.object4)
        print(self.object5)
        print(self.object6)
        print(self.object7)
        print(self.object8)
        print(self.object9)
        print(self.object10)
        print(self.object11)
        print(self.object12)
        print(self.object13)
        print(self.object14)
        print(self.object15)
        print(self.object16)
        print(self.object17)
        print(self.object18)
        print(self.object19)
        print(self.object20)
        fic.write(self.object1)
        fic.write("\n")
        fic.write(self.object2)
        fic.write("\n")
        fic.write(self.object3)
        fic.write("\n")
        fic.write(self.object4)
        fic.write("\n")
        fic.write(self.object5)
        fic.write("\n")
        fic.write(self.object6)
        fic.write("\n")
        fic.write(self.object7)
        fic.write("\n")
        fic.write(self.object8)
        fic.write("\n")
        fic.write(self.object9)
        fic.write("\n")
        fic.write(self.object10)
        fic.write("\n")
        fic.write(self.object11)
        fic.write("\n")
        fic.write(self.object12)
        fic.write("\n")
        fic.write(self.object13)
        fic.write("\n")
        fic.write(self.object14)
        fic.write("\n")
        fic.write(self.object15)
        fic.write("\n")
        fic.write(self.object16)
        fic.write("\n")
        fic.write(self.object17)
        fic.write("\n")
        fic.write(self.object18)
        fic.write("\n")
        fic.write(self.object19)
        fic.write("\n")
        fic.write(self.object20)


#comment demander a liste de course
creer_moi_une_liste_de_course = "créer moi une liste de course"
Creer_moi_une_liste_de_course = "Créer moi une liste de course"
creer_moi_une_liste_de_course_ = "creer moi une liste de course"
Creer_moi_une_liste_de_course_ = "Creer moi une liste de course"



b = random.randint(0, 1)
if b == 0:
    print("Bonjour")
else:
    print("salut")

run = True

while run:
    choix = input("Que voulez-vous faire : ")

    if choix == Quelle_heure_est_il or choix == Quelle_heure_est_il_ or choix == quelle_heure_est_il_ or choix == quelle_heure_est_il:
        print("il est : " + str(datetime.now()))

    if choix == Comment_appelle_tu or choix == Comment_appelle_tu_ or choix == Comment_tu_appelle or choix == Comment_tu_appelle_ or choix == comment_appelle_tu or choix == comment_appelle_tu_ or choix == comment_tu_appelle_ or choix == comment_tu_appelle:
        print("Je m'appelle Roger : https://www.youtube.com/channel/UCpu0d1JHqLwZwZsHX9Lyo1w")

    if choix == raconte_moi_une_blague or choix == Raconte_moi_une_blague:
        blague = random.randint(1, 20)
        if blague == 1:
            print(blague1)
        if blague == 2:
            print(blague2)
        if blague == 3:
            print(blague3)
        if blague == 4:
            print(blague4)
        if blague == 5:
            print(blague5)
        if blague == 6:
            print(blague6)
        if blague == 7:
            print(blague7)
        if blague == 8:
            print(blague8)
        if blague == 9:
            print(blague9)
        if blague == 10:
            print(blague10)
        if blague == 11:
            print(blague11)
        if blague == 12:
            print(blague12)
        if blague == 13:
            print(blague13)
        if blague == 14:
            print(blague14)
        if blague == 15:
            print(blague15)
        if blague == 16:
            print(blague16)
        if blague == 17:
            print(blague17)
        if blague == 18:
            print(blague18)
        if blague == 19:
            print(blague19)
        if blague == 20:
            print(blague20)
    if choix == creer_moi_une_liste_de_course or choix == creer_moi_une_liste_de_course_ or choix == Creer_moi_une_liste_de_course or choix == Creer_moi_une_liste_de_course_:
        list_de_cours.__init__(self=list_de_cours)
        fic.close()