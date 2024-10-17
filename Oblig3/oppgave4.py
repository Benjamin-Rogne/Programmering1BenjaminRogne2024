#funksjon for utregning av lengde, bredde og høyde, som skriver ut utregningen
def volum_kalkulator(lengde, bredde, høyde):
    volum = (lengde*bredde*høyde)
    volumutregning = (f"lengde {lengde} * bredde {bredde} * høyde {høyde} = volum {volum}")
    print(volumutregning)

#kaller på funksjonen med tall verdier for lengde, bredde og høyde
volum_kalkulator(1,4,6)
volum_kalkulator(6,10,7)
volum_kalkulator(13,3,8)
