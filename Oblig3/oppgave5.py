#oppgave 5.1a
movie_library = [{"title":"Inception","year":2010,"score":8.7},
                 {"title":"Inside Out","year":2015,"score":8.1},
                 {"title":"Con Air","year":1997,"score":6.9},
]

#oppgave 5.1b
def add_movie(title, year, score = 5.0):
    movie = {"title":title,"year":year,"score":score}
    movie_library.append(movie)

add_movie("lTreasure Planet", 2002, 7.2)
add_movie("A New Hope", 1977, 8.6)
add_movie("The Dark Knight", 2008, 9.0)

#oppgave 5.2a
def print_filmer(movie_list):
    for film in movie_list:
        print(f'{film["title"]} - {film["year"]} has a rating of {film["score"]}')
