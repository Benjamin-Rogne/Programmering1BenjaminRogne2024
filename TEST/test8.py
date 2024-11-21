all_wares = {
    "amd_processor": {
        "name": "AMD Ryzen 9 5900X Processor",
        "price": 5590.0,
        "number_in_stock": 50,
        "ratings": [4.5, 4.0, 5.0, 5.0, 4.5, 3.0],
        "description": "All the cores and threads you'll need!",
    },

    "playstation_5": {
        "name": "PlayStation 5",
        "price": 5999.0,
        "number_in_stock": 0,
        "ratings": [5.0, 5.0, 4.5, 2.0, 5.0, 4.5, 4.0],
        "description": "Next generation console, never in stock!",
    },
    "hdmi_cable": {
        "name": "Belkin Ultra High Speed HDMI Cable - 2m",
        "price": 349.0,
        "number_in_stock": 3,
        "ratings": [0,0,0,0,0,0,0,0],
        "description": "A high speed overprices HDMI cable!",
    }
}

def calculate_shopping_cart_price(shopping_cart, all_wares, tax = 1.25):
    total_cart_price = 0
    for ware in shopping_cart:
        ware_amount = shopping_cart[ware]
        ware_price = all_wares[ware]['price']
        total_cart_price = total_cart_price + (ware_amount * ware_price)
    total_cart_price = total_cart_price * tax
    return total_cart_price

def add_number_of_ware_to_shopping_cart(ware_key = "", ware = {}, shopping_cart = {}, number_of_ware = 1):
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