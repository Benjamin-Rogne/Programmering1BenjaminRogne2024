import random
def dart_spill():
    # Hver kast kan gi en poengsum mellom 0 og 60
    score = sum(random.randrange(0, 61) for _ in range(3))
    return score

# Input for antall spillere
antall_spillere = int(input("Hvor mange spillere skal spille? "))

# Simuler spillet for hver spiller
for spiller in range(1, antall_spillere + 1):
    resultat = dart_spill()
    print(f"Spiller", spiller ,"sin poengsum er:" ,resultat)