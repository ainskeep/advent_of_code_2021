import helpers
import copy

lines = helpers.read_input()

grid = []

x_len = 0
y_len = len(lines)

for line in lines:
    grid.append([char for char in line])
    x_len = len(line)

print("Part 1")

gama_rate = ""
epsilon_rate = ""

for x in range(x_len):
    one_count, zero_count = 0, 0
    for y in range(y_len):
        char = grid[y][x]
        if char == '1':
            one_count += 1
        else:
            zero_count += 1

    if one_count > zero_count:
        gama_rate += "1"
        epsilon_rate += "0"
    else:
        gama_rate += "0"
        epsilon_rate += "1"

print(f"Gama: {int(gama_rate, 2)}, epsilon: {int(epsilon_rate, 2)}, Gama x Epsilon: {int(epsilon_rate, 2) * int(gama_rate, 2)}")

print("Part 2")

generator_list = copy.deepcopy(grid)
scrubber_list = copy.deepcopy(grid)

x = 0
while x < x_len:
    one_count, zero_count = 0, 0

    for y in range(len(generator_list)):
        char = generator_list[y][x]
        if char == '1':
            one_count += 1
        else:
            zero_count += 1

    remove_char = '1' if one_count >= zero_count else '0'

    generator_list = list(filter(lambda number: number[x] == remove_char, generator_list))

    # generator handle
    if len(generator_list) == 1:
        break
    x += 1

x = 0
while x < x_len:
    one_count, zero_count = 0, 0

    for y in range(len(scrubber_list)):
        char = scrubber_list[y][x]
        if char == '1':
            one_count += 1
        else:
            zero_count += 1

    remove_char = '1' if one_count < zero_count else '0'

    scrubber_list = list(filter(lambda number: number[x] == remove_char, scrubber_list))

    # scrubber handle
    if len(scrubber_list) == 1:
        break
    x += 1


generator_num = int(''.join(generator_list[0]), 2)
scrubber_num = int(''.join(scrubber_list[0]), 2)

print(f"Generator: {generator_num}, Scrubber: {scrubber_num}. Life Support Rating: {generator_num * scrubber_num}")
