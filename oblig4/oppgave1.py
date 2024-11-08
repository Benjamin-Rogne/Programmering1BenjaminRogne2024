class Film:
    def __init__(self, tittel, utgivelsesår, score):
        self.tittel = tittel
        self.utgivelsesår = utgivelsesår
        self.score = score

    
    def hentInformasjon(self):
        return f"{self.tittel} was released in {self.utgivelsesår} and currently has a score of {self.score}"

# Oppretter filmene som objekter
film1 = Film("Inception", 2010, 8.8)
film2 = Film("The Martian", 2015, 8.0)
film3 = Film("Joker", 2019, 8.4)

# Skrive ut informasjon om hver film ved å bruke metoden hentInformasjon
print(film1.hentInformasjon())
print(film2.hentInformasjon())
print(film3.hentInformasjon())