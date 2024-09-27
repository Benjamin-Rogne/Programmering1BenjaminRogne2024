tolkins_boker = ['Farmer Giles of Ham', 'Lord of the Rings: The Fellowship of the Ring', 'Lord of the Rings: The Return of the King', 'Lord of the Rings: The Two Towers', 'The Adventures of Tom Bombadil', 'The Hobbit', 'The Silmarillion', 'Tree and Leaf', 'Unfinished Tales ']

LOTR_liste = []

for bok in tolkins_boker:
    if "Lord of the Rings" in bok:
        LOTR_liste.append(bok)
print("Ringenes herre liste:")        
print(LOTR_liste)

