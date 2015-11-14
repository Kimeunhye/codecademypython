# 8.1
def answer():
    return 42

# 8.2
def hotel_cost(nights):
    return nights * 140

# 8.3
def hotel_cost(nights):
    return nights * 140

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    else:
        return 475

# 8.4
def rental_car_cost(days):
    p = 40
    total = p * days
    if days >= 7:
        total -= 50
    elif days >= 3:
        total -= 20
    return total

# 8.5
def trip_cost(city, days):
    return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days)

# 8.6
def trip_cost(city, days, spending_money):
    return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_money

# 8.7 !-- 다 한꺼번에 묶어놓은것--
def hotel_cost(nights):
    return nights * 140

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    else:
        return 475

def rental_car_cost(days):
    p = 40
    total = p * days
    if days >= 7:
        total -= 50
    elif days >= 3:
        total -= 20
    return total

def trip_cost(city, days, spending_money):
    return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_money

print trip_cost("Los Angeles", 5, 600)
