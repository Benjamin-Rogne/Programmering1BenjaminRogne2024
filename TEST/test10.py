from datetime import date

def next_eu_control():
    car_production_date = date(1981, 12, 1)
    today = date.today()
    current_month = today.month
    years_since_production = today.year - car_production_date.year

    last_control_year = car_production_date.year + (years_since_production // 2) * 2
    last_eu_control = date(last_control_year, car_production_date.month, car_production_date.day)
    
    if car_production_date.year % 2 == 0 and last_control_year % 2 == 0 and car_production_date.month > current_month:
        next_eu_control = last_eu_control
    
    elif car_production_date.year % 2 != 0 and last_control_year % 2 != 0 and car_production_date.month > current_month and (today - last_eu_control) < (2,0,0):
        next_eu_control = last_eu_control

    else:
        next_control_year = last_control_year + 2
        next_eu_control = date(next_control_year, car_production_date.month, car_production_date.day)
    
    
    return next_eu_control


print(next_eu_control())