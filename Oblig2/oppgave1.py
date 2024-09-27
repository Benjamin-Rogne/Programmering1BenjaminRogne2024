svar = int(input("Hva er svaret på det ultimate spørsmålet om livet, universet og alle ting? Hint: Det er et tall."))
riktig_svar = 42
if svar == riktig_svar:#sjekker om svaret er riktig
    print("Det stemmer, meningen med livet er 42!")
elif svar > 30 and svar < 50:#sjekker om svaret er mellom 30 og 50
    print("Nærme, men feil.")
else:#gjør dette hvis ingen av kravene over er oppfyllt
    print("feil")