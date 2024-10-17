#importerer bibliotek for random funksjoner
import random
#funksjon for å skrive ut tilfeldig tall med fin utskrift
def fin_utskrift():
    number = random.randrange(0, 100)
    print("********")
    print(f"***{number}***")
    print("********")

#kaller på funksjonen fin_utskrift
fin_utskrift()
fin_utskrift()
fin_utskrift()