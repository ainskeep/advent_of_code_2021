import helpers

lines = helpers.read_input()

print("Part 1:")

x, y = 0, 0

for line in lines:
    cmd, distance = line.split()

    distance = int(distance)

    if cmd == 'forward':
        x += distance
    elif cmd == 'down':
        y += distance
    elif cmd == 'up':
        y -= distance
    else:
        print("Parse Error. Fix me")

print(f"X: {x}, Y: {y} X*Y: {x*y}")

print("Part 2:")
aim, x, y = 0, 0, 0
for line in lines:
    cmd, distance = line.split()

    distance = int(distance)

    if cmd == 'forward':
        x += distance
        y += distance * aim
    elif cmd == 'down':
        aim += distance
    elif cmd == 'up':
        aim -= distance
    else:
        print("Parse Error. Fix me")

print(f"X: {x}, Y: {y} X*Y: {x*y}")