

loop = 0


pakke_liste = []

def view_lsit():
    print(pakke_liste)

def add_item():
    new_item = input("legg til en ting")
    pakke_liste.append(new_item)
    print(new_item, "er lagt til listen")

def remove_item():
    print(pakke_liste)
    delete_item = input("skriv hva du vil fjerne fra listen")
    pakke_liste.remove(delete_item)
    print(delete_item, "er fjernet fra listen")

#while loop == 0:
print("kommandoer:")
print("list, for å se din liste")
print("add, for å legge noe til listen")
print("remove, for å fjerne noe fra listen")
kommando = str(input("skriv kommando"))
if kommando == "list":
    view_lsit()
elif kommando == "add":
    add_item()
elif kommando == "remove":
    remove_item()
else:
    print("ukjent kommando prøv igjen")