thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict3 = {
  "brand":{"model": "Mustang",
    "year": 1964
},
  "grand":{"model": "Mustang",
    "year": 1964
},
  "srand":{"model": "Mustang",
    "year": 1964
}
}
print(thisdict3)


def get_car_age(car, current_year = 2022):
    car_release = car['year']
    car_age = current_year - car_release
    return car_age

print(f"{get_car_age(thisdict)}")