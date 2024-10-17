#oppgave 5.1a
#liste med dictionaris 
movie_library = [{"title":"Inception","year":2010,"score":8.7},
                 {"title":"Inside Out","year":2015,"score":8.1},
                 {"title":"Con Air","year":1997,"score":6.9},
]
#oppgave 5.1b
#funksjon for å legge til filmer i filmlisten
def add_movie(title, year, score = 5.0):
    movie = {"title":title,"year":year,"score":score}
    movie_library.append(movie)

#kaller på funksjonen med info til filmene som skal legges til i listen
add_movie("lTreasure Planet", 2002, 7.2)
add_movie("A New Hope", 1977, 8.6)
add_movie("The Dark Knight", 2008, 9.0)

#oppgave 5.2a
#funksjon for å skrive ut listen med formatet: "film" - "år" has a rating of "rangering"
def print_filmer(movie_list):
    for film in movie_list:
        print(f'{film["title"]} - {film["year"]} has a rating of {film["score"]}')

#oppgave 5.2b
#Funksjon som regner ut gjennomsnittsratingen av en liste
def gjennomsnitt_rating(filmliste):
    total_rating = sum(film["score"] for film in filmliste)
    return total_rating / len(filmliste)

#oppgave 5.2c
#Funksjon som returnerer filmer fra og med gitt år
def filmer_fra_aar(filmliste, aar):
    return [film for film in filmliste if film["year"] >= aar]

#gir filmer_fra_2010 verdiene fra funksjon filmer_fra_aar
filmer_fra_2010 = filmer_fra_aar(movie_library, 2010)

#Printer ut filmer fra 2010
print_filmer(filmer_fra_2010)

#oppgave 5.3a
#Funksjon som skriver filmliste til en fil
def skriv_fil(filmliste, filnavn):
    with open(filnavn, 'w') as fil:
        for film in filmliste:
            fil.write(f'{film["title"]} - {film["year"]} has a rating of {film["score"]}\n')

#Skriver filmene til "movies.txt"
skriv_fil(movie_library, "movies.txt")

#oppgave 5.3b
#Funksjon som leser innholdet fra en fil og skriver det ut
def les_fil(filnavn):
    try:
        with open(filnavn, 'r') as fil:
            innhold = fil.read()
            print(innhold)
    except FileNotFoundError:
        print(f"Filen '{filnavn}' ble ikke funnet.")

#Leser og skriver ut innholdet av "movies.txt"
les_fil("movies.txt")