#------------------------------------------
#Oppgaver
#------------------------------------------
def print_ware_information(ware):
    print(f"Name: {ware['name']}")
    print(f"Price: {int(ware['price'])},-")
    print(f"Number in stock: {ware['number_in_stock']}")
    print(f"Description: {ware['description']}")

def calculate_average_ware_rating(ware):
    try:
        average_rating = sum(ware['ratings']) / len(ware['ratings'])
        average_rating = round(average_rating, 1)
        return average_rating
    
    except ZeroDivisionError:
        return "Error: Ratings not found"

def get_all_wares_in_stock(all_wares):
    all_wares = {
    key: value for key, value in all_wares.items() if value.get("number_in_stock") != 0
    }
    return all_wares

def is_number_of_ware_in_stock(all_wares, number_of_ware = 0 ,ware = {}):
    ware = all_wares[input('enter ware:')]
    number_of_ware =  int(input('enter number'))
    if ware['number_in_stock'] - number_of_ware >= 0:
        return True
    else:
        return False

def add_number_or_ware_to_shopping_cart(number_of_ware = 1, ware = {}, shopping_cart = {}, ware_key = ""):
    ware_key = str(input('enter ware'))
    number_of_ware = int(input('enter number'))
    if ware[ware_key]['number_in_stock'] == 0:
        print(f"we dont have any {ware[ware_key]['name']}s in stock ")

    elif ware[ware_key]['number_in_stock'] - number_of_ware < 0:
        print(f"we only have {ware[ware_key]['number_in_stock']}s in stock and it is now addet to your cart")
        if ware_key in shopping_cart:
            shopping_cart[ware_key] = shopping_cart[ware_key] + ware[ware_key]['number_in_stock']
        else:
            shopping_cart[ware_key] = ware[ware_key]['number_in_stock']

    else:
        print(f"{number_of_ware} {ware[ware_key]['name']}s is now added to your cart")
        if ware_key in shopping_cart:
            shopping_cart[ware_key] = shopping_cart[ware_key] + number_of_ware
        else:
            shopping_cart[ware_key] = number_of_ware
    
    return shopping_cart

def calculate_shopping_cart_price(shopping_cart, all_wares, tax):
    '''Returnerer prisen av en handlevogn basert på varene i den.'''

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