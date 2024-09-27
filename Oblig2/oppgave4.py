tolkins_boker = ['Farmer Giles of Ham', 'Lord of the Rings: The Fellowship of the Ring', 'Lord of the Rings: The Return of the King', 'Lord of the Rings: The Two Towers', 'The Adventures of Tom Bombadil', 'The Hobbit', 'The Silmarillion', 'Tree and Leaf', 'Unfinished Tales ']

LOTR_liste = []

#leser av listen: tolkins bøker, så legger den til lord of the rings bøkene i listen LOTR_liste
for bok in tolkins_boker:
    if "Lord of the Rings" in bok:
        LOTR_liste.append(bok)

#skriver ut bøkene i LOTR_liste
print("lord of the rings bøker")
for bok in LOTR_liste:
    print(bok)

#skriver ut bøkene i LOTR_liste
print("")
print("lord of the rings bøker")
for i in range(len(LOTR_liste)):
    print(LOTR_liste[i])