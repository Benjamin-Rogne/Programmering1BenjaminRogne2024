zoo_animals = ["Panda", "Lion", "Zebra", "Honey Badger", "Aligator"]
planets = ["Merkur", "Venus", "Jorden", "Jupiter", "Saturn", "Uranus"]
print(planets[2])

planets[3] = "Mars"#bytter ut plass 3 i lista med Mars
print(planets)

random_list = ["Europe", 7, ["ny liste", 23, "med nye elementer"], "bil"]
print(random_list[2][2])

planets.insert(2, "pluto")#sjyver listen til høyre og putter inn pluto på plass 2
planets.append("en planet")#putter inn "en planet" i slutten av lista
print(planets)