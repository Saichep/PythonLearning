def hotel_night_cost(city):
    if city == "Charlotte":
        return 140
    elif city == "Tampa":
        return 140
    elif city == "Pittsburgh":
        return 140
    elif city == "Los Angeles":
        return 140
    else:
        return "Nope"


def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    else:
        return "Nope"


def rental_car_cost(days):
    daily_rate = 40.0
    total_cost = 0.0
    if days >= 7:
        total_cost = (days * daily_rate) - 50
    elif 3 <= days < 7:
        total_cost = (days * daily_rate) - 20
    else:
        total_cost = (days * daily_rate)
    return total_cost


def trip_cost(city, days):
    return rental_car_cost(days) + (days * hotel_night_cost(city)) + plane_ride_cost(city)

city = str(input("Enter the city name? \n\tCharlotte \n\tTampa \n\tPittsburgh \n\tLos Angeles \nChoose from above: "))
days = int(input("Enter Number of days: "))
print("Total Trip Cost to %s for %d days = $ %f" %(city, days, trip_cost(city, days)))