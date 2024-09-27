tolkins_boker = ["The Hobbit", "Farmer Giles of Ham", "The Fellowship of the Ring", "The Two Towers", "The Return of the King", "The Adventures of Tom Bombadil", "Tree and Leaf"]

#printer ut de to føreste og to siste bøkene i listen
print(tolkins_boker[0], tolkins_boker[1], tolkins_boker[5], tolkins_boker[6])

#legger til bøker bakerst i listen
tolkins_boker.append("The Silmarillion")
tolkins_boker.append("Unfinished Tales ")

#legger til Lord of the Rings forran bøkene på plass 2,3 og 4 i listen
tolkins_boker[2] = "Lord of the Rings: " + tolkins_boker[2]
tolkins_boker[3] = "Lord of the Rings: " + tolkins_boker[3]
tolkins_boker[4] = "Lord of the Rings: " + tolkins_boker[4]

print(sorted(tolkins_boker))#sorterer listen og skriver ut den sorterte listen