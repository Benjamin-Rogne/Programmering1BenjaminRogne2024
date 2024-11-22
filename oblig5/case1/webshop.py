#------------------------------------------
#Oppgaver
#------------------------------------------

#denne funksjonen er en utskrift for vare verdier.
def print_ware_information(ware):
    print(f"Name: {ware['name']}")
    print(f"Price: {int(ware['price'])},-")
    print(f"Number in stock: {ware['number_in_stock']}")
    print(f"Description: {ware['description']}")

# regner ut vare rating med error melding dersom varen ikke har ratings
def calculate_average_ware_rating(ware):
    try:
        average_rating = sum(ware['ratings']) / len(ware['ratings'])
        average_rating = round(average_rating, 1)
        return average_rating
    
    except ZeroDivisionError:
        return "Error: Ratings not found"

#denne funksjonen luker ut alle varer som ikke lenger finnes på lager
def get_all_wares_in_stock(all_wares):
    all_wares = {
    key: value for key, value in all_wares.items() if value.get("number_in_stock") != 0
    }
    return all_wares

#sjekker om antallet varer som skrives inn finnes eller ikke
def is_number_of_ware_in_stock(all_wares, number_of_ware = 0 ,ware = {}):
    ware = all_wares[input('enter ware:')]
    number_of_ware =  int(input('enter number'))
    if ware['number_in_stock'] - number_of_ware >= 0:
        return True
    else:
        return False

# legger til varer i handlekurv med senarioer for lager status 
def add_number_of_ware_to_shopping_cart(ware_key = "", ware = {}, shopping_cart = {}, number_of_ware = 1):
    current_number_in_stock = ware['number_in_stock']
    if ware['number_in_stock'] == 0:
        print(f"Sorry, we dont have any {ware['name']}s in stock ")

    elif ware['number_in_stock'] - number_of_ware < 0:
        print(f"we only have {ware['number_in_stock']} {ware['name']}s in stock and it is now addet to your cart")
        if ware_key in shopping_cart:
            shopping_cart[ware_key] = shopping_cart[ware_key] + current_number_in_stock
        else:
            shopping_cart[ware_key] = current_number_in_stock

    else:
        print(f"{number_of_ware} {ware['name']}s is now added to your cart")
        if ware_key in shopping_cart:
            shopping_cart[ware_key] = shopping_cart[ware_key] + number_of_ware
        else:
            shopping_cart[ware_key] = number_of_ware
    
    return shopping_cart

# regner ut verdien av varer i handlekurv og retunerer verdien med tax lagt til
def calculate_shopping_cart_price(shopping_cart, all_wares, tax = 1.25):
    total_cart_price = 0
    for ware in shopping_cart:
        ware_amount = shopping_cart[ware]
        ware_price = all_wares[ware]['price']
        total_cart_price = total_cart_price + (ware_amount * ware_price)
    total_cart_price = total_cart_price * tax
    return total_cart_price

def can_afford_shopping_cart(shopping_cart_price, wallet):
    '''Returnerer en Boolean-verdi basert på om det er nok penger i en gitt
    lommebok for å kjøpe en handlevogn.'''
    
def buy_shopping_cart():

    '''Kjøper varene i en handlevogn. Parameterene defineres i oppgaven.'''

#------------------------------------------
# Predefinerte funksjoner
#------------------------------------------
def is_ware_in_stock(ware):
    '''Returnerer en Boolean-verdi som representerer om en vare er på lager.'''
    if ware["number_in_stock"] >= 1:
        return True
    else:
        return False
    def clear_shopping_cart(shopping_cart):
        '''Tømmer en handlevogn.'''
    shopping_cart.clear()