import helpers

lines = helpers.read_input()

# Part 1

increasing = 0
decreasing = 0

for i, window in enumerate(lines):
    if i == 0:
        print(window)
        continue
    if int(window) > int(lines[i - 1]):
        increasing += 1
    else:
        decreasing += 1

print("\nPart 1:")
print(f"Total increasing: {increasing}")
print(f"Total decreasing: {decreasing}")

# Part 2
print("\nPart 2:")

def depth_window(depths):
    for i, measurement in enumerate(depths):
        if i in [0, 1]:
            continue
        yield int(measurement) + int(depths[i-1]) + int(depths[i-2])

increasing = 0
decreasing = 0

window_list = [ window_measurement for window_measurement in depth_window(lines)]

for i, window in enumerate(window_list):
    if i == 0:
        print(window)
        continue
    if int(window) > int(window_list[i - 1]):
        print(f"{window} (increasing)")
        increasing += 1
    else:
        print(f"{window} (decreasing)")
        decreasing += 1


print(f"Total increasing: {increasing}")
print(f"Total decreasing: {decreasing}")