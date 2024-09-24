tolkins_boker = ["The Hobbit", "Farmer Giles of Ham", "The Fellowship of the Ring", "The Two Towers", "The Return of the King", "The Adventures of Tom Bombadil", "Tree and Leaf"]

print(tolkins_boker[0], tolkins_boker[1], tolkins_boker[5], tolkins_boker[6])

tolkins_boker.append("The Silmarillion")
tolkins_boker.append("Unfinished Tales ")

tolkins_boker[2] = "Lord of the Rings: " + tolkins_boker[2]
tolkins_boker[3] = "Lord of the Rings: " + tolkins_boker[3]
tolkins_boker[4] = "Lord of the Rings: " + tolkins_boker[4]

print(sorted(tolkins_boker))