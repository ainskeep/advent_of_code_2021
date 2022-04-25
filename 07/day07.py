import copy

import helpers



lines = helpers.read_input("input.txt")

positions = lines[0]

position_dict = {}  # key: crab position, Val: Number of crabs at that position

for position in positions.split(','):
    if int(position) not in position_dict:
        position_dict[int(position)] = 1
    else:
        position_dict[int(position)] = position_dict[int(position)] + 1

# calc wrong
# also they can go to any position

def calc_fuel_cost(position_dict, position):
    cost = 0
    for key, val in position_dict.items():
        cost += abs(key - position) * val

    return cost

position_range = range(min(position_dict.keys()), max(position_dict.keys()) + 1)

lowest_fuel_cost = 9999999999
lowest_cost_position = 0
for position in position_range:
    current_position_cost = calc_fuel_cost(position_dict, position)
    if current_position_cost < lowest_fuel_cost:
        lowest_cost_position = position
        lowest_fuel_cost = current_position_cost


print(f"P1: Fuel Cost: {lowest_fuel_cost} at position {lowest_cost_position}")


def calc_fuel_cost_p2(position_dict, position):
    cost = 0
    for key, val in position_dict.items():
        n = abs(key - position)
        cost += (n * n + n)/2 * val

    return cost

position_range = range(min(position_dict.keys()), max(position_dict.keys()) + 1)

lowest_fuel_cost = 9999999999
lowest_cost_position = 0
for position in position_range:
    current_position_cost = calc_fuel_cost_p2(position_dict, position)
    if current_position_cost < lowest_fuel_cost:
        lowest_cost_position = position
        lowest_fuel_cost = current_position_cost


print(f"P2: Fuel Cost: {lowest_fuel_cost} at position {lowest_cost_position}")
