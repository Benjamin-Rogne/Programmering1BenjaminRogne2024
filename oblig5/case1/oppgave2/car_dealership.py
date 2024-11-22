from datetime import date, timedelta
car_register = {
"toyotaBZ4X": {
"brand": "Toyota",
"model": "Corolla",
"price": 96_000,
"year": 2012,
"month": 8,
"new": False,
"km": 163_000
},
"pugeot408": {
"brand": "Pugeot",
"model": "408",
"price": 330_000,
"year": 2019,
"month": 1,
"new": False,
"km": 40_000
},
"audiRS3": {
"brand": "Audi",
"model": "RS3",
"price": 473_000,
"year": 2022,
"month": 2,
"new": True,
"km": 0
},
}

NEW_CAR_REGISTRATION_FEE = 8745
RENT_CAR_PERCENTAGE = 0.4
RENT_NEW_CAR__FEE = 1000

# funksjon for utskrift av bil informasjon
def print_car_information(car):
    print(f"Brand: {car['brand']}")
    print(f"Model: {car['model']}")
    print(f"Price. {car['price']},-")
    print(f"Manufactured: {car['year']}-{car['month']}")
    if car['new'] == True:
        print("Condition: New")
    else:
        print("Condition: Used")
# Oppgave 3.1

# denne funksjonen brukes for å legge til en ny bil i car_register
def create_car(car_register, brand, model, price, year, month, new, km):
    car_key = brand + model
    car_register[car_key] = {
        "brand": brand,
        "model": model,
        "price": price,
        "year": year,
        "month": month,
        "year": year,
        "new": new,
        "km": km
    }
    return car_register
# Oppgave 3.2

# regner ut bilens alder
def get_car_age(car, current_year = 2024):
    car_release = car['year']
    car_age = current_year - car_release
    return car_age  
# Oppgave 3.3

# månedlig leiepris for bil
def rent_car_monthly_price(car):
    car_total_price = car['price']
    price_pr_month = (car_total_price * 0.40)/12
    if car['new'] == True:
        price_pr_month = price_pr_month + 1000
    price_pr_month = round(price_pr_month, 2)
    return price_pr_month
# Oppgave 3.4

# sjekker når neste eu kontroll er
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
# Oppgave 3.5

# regner ut den totale kjøpsprisen på en bil
def calculate_total_price(car):
    total_price = car['price']
    if car['new'] == True:
        total_price = total_price + 10783
    else:
        car_age = get_car_age(car)
        if car_age in range(0,4):
            total_price = total_price + 6681
        elif car_age in range(4,12):
            total_price = total_price + 4034
        elif car_age in range(12,30):
            total_price = total_price + 1729
        else:
            total_price = total_price
    return total_price
    # Oppgave 3.6

def is_new(car):
    return car['new']

if __name__ == '__main__':
    create_car(car_register, "Volvo", "V90", 850_000, 2021, 12, True, 0)

    toyota = car_register['toyotaBZ4X']

    print_car_information(toyota)

    print(f"\nThe total price for this {toyota['brand']} {toyota['model']} is {calculate_total_price(toyota)}kr.")

    print(f"Next EU-control for the {toyota['brand']} {toyota['model']} is {next_eu_control(toyota)}")

    print(f"If you want to rent the {toyota['brand']} {toyota['model']} the monthly fee will be {rent_car_monthly_price(toyota)}.")

    audi = car_register['audiRS3']

    print_car_information(audi)

    print(f"\nThe total price for this {audi['brand']} {audi['model']} is {calculate_total_price(audi)}kr.")

    print(f"Next EU-control for the {audi['brand']} {audi['model']} is {next_eu_control(audi)}")

    print(f"If you want to rent the {audi['brand']} {audi['model']} the monthly fee will be {rent_car_monthly_price(audi)}kr.")


# oppgave 7
class Car:
    def __init__(self, name, brand, model, price, year, month, new, km):
        self.name = name
        self.suit = brand
        self.value = model
        self.name = price
        self.suit = year
        self.value = month
        self.name = new
        self.suit = km

    def car_information():
        "skriver ut informasjon om bilen"
    
    def make_car():
        "dette kunne vært en effektiv løsning for å forenkle prosessen å lage en bil"
    # jeg tror disse to kan være effektive som class funksjoner for å implementere et
    # tettere sammarbeid mellom funksjonen og bil classen.
