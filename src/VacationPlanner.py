list_of_cities = ["Charlotte", "Tampa", "Pittsburgh", "Los Angeles"];
plane_costs = [1183, 1220, 2222, 3475];
hotel_costs_per_night = [140, 240, 200, 475];

def calculate_hotel_cost(city_code: int, days: int):
    """Returns hotel cost for the selected city and days"""
    return days * hotel_costs_per_night[city_code]


def calculate_car_cost(days: int):
    """Returns cost of car rental for the selected days"""
    daily_rate = 40.0
    if days >= 7:
        return (days * daily_rate) - 50
    elif 3 <= days < 7:
        return (days * daily_rate) - 20
    elif 1 <= days < 3:
        return (days * daily_rate)
    else:
        exit(-1)


def calculate_plane_cost(city_code: int):
    """Returns flight cost to-and-fro for the selected city"""
    return plane_costs[city_code]


def trip_cost(city_code: int, days: int, expenditure: int):
    """Returns total trip cost"""
    return calculate_car_cost(days) + calculate_hotel_cost(city_code, days) + calculate_plane_cost(city_code) + expenditure


def print_cities():
    index = 0
    city_iterator = iter(list_of_cities)
    print("+++---+---+---+---+---+---+---+---+++")
    for city in city_iterator:
        index = index + 1
        print(index, ")", city)


print_cities()
chosen_city_code = int(input("Choose city number from above: "))
if 1 <= chosen_city_code <= len(list_of_cities):
    chosen_city_code = chosen_city_code - 1
    days = int(input("Enter Number of days: "))
    trip_additional_expense = int(input("Enter your estimated expenditure: "))
    print("\nTotal Trip Cost to \'%s\' for \'%d\' days = $ %f" %(list_of_cities[chosen_city_code], days, trip_cost(chosen_city_code, days, trip_additional_expense)))
else:
    print("Invalid Selection of city. Try again !!")