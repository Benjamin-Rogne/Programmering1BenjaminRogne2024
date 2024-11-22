from datetime import date, timedelta

def neste_eu_kontroll(bil_info):
    """
    Beregner neste EU-kontroll basert på bilens registreringsdato.
    
    Parametere:
        bil_info (dict): En dictionary med nøkler 'year', 'month', 'day'.
        
    Returnerer:
        str: Datoen for neste EU-kontroll i format 'YYYY-MM-DD'.
    """
    registreringsdato = date(bil_info['year'], bil_info['month'], 1)
    dagens_dato = date.today()
    
    # Første EU-kontroll er 4 år etter registreringsdato
    første_kontroll = registreringsdato.replace(year=registreringsdato.year + 4)
    
    if dagens_dato > første_kontroll:
        # Beregn siste gjennomførte kontroll
        år_siden_første = (dagens_dato.year - første_kontroll.year) // 2
        siste_kontroll = første_kontroll.replace(year=første_kontroll.year + år_siden_første * 2)
        
        # Neste kontroll er to år etter siste kontroll
        neste_kontroll = siste_kontroll.replace(year=siste_kontroll.year + 2)
        
        # Hvis bilens produksjonsmåned er senere enn dagens måned, juster ikke til 2 år frem
        if registreringsdato.month > dagens_dato.month and neste_kontroll.year > dagens_dato.year:
            neste_kontroll = neste_kontroll.replace(year=dagens_dato.year)
    else:
        # Første kontroll er fortsatt fremtidig
        neste_kontroll = første_kontroll

    return neste_kontroll.strftime('%Y-%m-%d')


# Eksempel på bruk
bil = {'year': 2018, 'month': 12, 'day': 15}
print(f"Neste EU-kontroll: {neste_eu_kontroll(bil)}")
