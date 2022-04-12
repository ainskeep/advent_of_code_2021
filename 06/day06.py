import copy

import helpers

lines = helpers.read_input("input.txt")


lantern_fish = lines[0].split(',')
copy_of_lantern_fish = copy.deepcopy(lantern_fish)

days = 12

for i in range(days):
    new_fish = 0
    for j in range(len(lantern_fish)):
        days_left = int(lantern_fish[j])
        if days_left == 0:
            new_fish += 1
            lantern_fish[j] = 6
        else:
            lantern_fish[j] = days_left - 1

    for k in range(new_fish):
        lantern_fish.append(8)

print(f"Part 1: {len(lantern_fish)}")


# part 2
lantern_fish = copy_of_lantern_fish

#lantern_fish = [6,0,6,4,5,6,7,8,8]

lantern_fish_count = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for fish in lantern_fish:
    int_fish = int(fish)
    lantern_fish_count[int_fish] = lantern_fish_count[int_fish] + 1

print(lantern_fish_count)

days_left = 256

for i in range(days_left):
    zero_count = 0
    for j in range(len(lantern_fish_count)):
        if j == 0:
            zero_count = lantern_fish_count[0]
            lantern_fish_count[0] = 0
        else:
            lantern_fish_count[j-1] = lantern_fish_count[j]

    # Birth new fishies
    lantern_fish_count[8] = zero_count
    # Reset pregnant fish
    lantern_fish_count[6] = lantern_fish_count[6] + zero_count

print(f"Part 2: {sum(lantern_fish_count)}")
