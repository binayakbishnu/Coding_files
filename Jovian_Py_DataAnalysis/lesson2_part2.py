def total_cost(days, place):
    total = 0
    if place == "Paris":
        total += 200
        total += (20*days)
        total += 200
    elif place == "London":
        total += 250
        total += (30*days)
        total += 120
    elif place == "Dubai":
        total += 370
        total += (15*days)
        total += 80
    else:
        total += 450
        total += (10*days)
        total += 70

    return total


def decide_place(days, list_places):
    cost_list = []
    for place in list_places:
        t_cost = total_cost(days, place)
        cost_list.append(t_cost)

    return cost_list


N = int(input("Enter number of days: "))
places_list = ["Paris", "London", "Dubai", "Mumbai"]

return_value = decide_place(N, places_list)

# print(return_value)
print(places_list[
    return_value.index(
        min(return_value)
    )
])
