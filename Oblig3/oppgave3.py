#funksjon skriver ut liste med hvert verdi under hverandre
def print_list(list):
    for food in list:
        print(f"{food}")

#lager listen og kaller på funksjonen med listen som parameter
favorite_food = ["hamburger", "taco", "pizza"]
print_list(favorite_food) 