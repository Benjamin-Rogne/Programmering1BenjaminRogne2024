pakke_liste = []

loop = 0 #verdi brukt for å lage en while loop

def view_lsit(): #funkjon for å se listen
    print(pakke_liste)

def add_item(): # funksjon for å legge noe til listen 
    new_item = input("legg til en ting: ")
    pakke_liste.append(new_item)
    print(new_item, "er lagt til listen")

def remove_item(): #funksjon for å fjerne noe fra listen
    print(pakke_liste)#viser listen for å gi brukeren oversikt over hva som står i listen
    delete_item = input("skriv hva du vil fjerne fra listen")
    if delete_item not in pakke_liste:#hvis det som skal fjernes ikke er i listen blir bruker sent til kommando oversikten
        print(delete_item,"er ikke i listen prøv igjen")
    else:
        pakke_liste.remove(delete_item)
        print(delete_item, "er fjernet fra listen")

while loop == 0: #lager loop
    print("")
    print("kommandoer:")#kommando oversikt
    print("list, for å se din liste")
    print("add, for å legge noe til listen")
    print("remove, for å fjerne noe fra listen")
    kommando = str(input())#her velger du hviken kommando / funkjson du vil bruke
    
    if kommando == "list":# sjekker hviken kommando som ble brukt
        view_lsit()
    
    elif kommando == "add":
        add_item()
    
    elif kommando == "remove":
        remove_item()
    
    else:
        print("ukjent kommando prøv igjen")