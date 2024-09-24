svar = int(input("Hva er svaret på det ultimate spørsmålet om livet, universet og alle ting? Hint: Det er et tall."))
riktig_svar = 42
if svar == riktig_svar:
    print("Det stemmer, meningen med livet er 42!")
elif svar > 30 and svar < 50:
    print("Nærme, men feil.")
else:
    print("feil")