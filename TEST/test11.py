from datetime import date, timedelta

def next_eu_control(car):
    car_production_date = date(car['year'], car['month'], 1)
    today = date.today()
    
    # Første EU-kontroll er 4 år etter registreringsdato
    first_control = car_production_date.replace(year=car_production_date.year + 4)
    
    if today > first_control:
        # Beregn siste gjennomførte kontroll
        year_since_first = (today.year - first_control.year) // 2
        last_control = first_control.replace(year=first_control.year + year_since_first * 2)
        
        # Neste kontroll er to år etter siste kontroll
        next_control = last_control.replace(year=last_control.year + 2)
        
        # Hvis bilens produksjonsmåned er senere enn dagens måned, juster ikke til 2 år frem
        if car_production_date.month > today.month and next_control.year > today.year:
            next_control = next_control.replace(year=today.year)
    else:
        # Første kontroll er fortsatt fremtidig
        next_control = first_control

    return next_control.strftime('%Y-%m-%d')


# Eksempel på bruk
car = {'year': 2011, 'month': 11, 'day': 30}
print(f"Neste EU-kontroll: {next_eu_control(car)}")
