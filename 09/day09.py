import helpers

lines = helpers.read_input("input.txt")

#gen array
cave_map = []
for line in lines:
    tmp_arr = []
    for char in line:
        tmp_arr.append(int(char))
    cave_map.append(tmp_arr)

x_len = len(cave_map)
y_len = len(cave_map[0])

def get_adjacents(x, y, cave_map):
    adjacents = []
    if x != 0:
        adjacents.append(cave_map[x - 1][y])
    if x != x_len - 1:
        adjacents.append(cave_map[x + 1][y])
    if y != 0:
        adjacents.append(cave_map[x][y - 1])
    if y != y_len - 1:
        adjacents.append(cave_map[x][y + 1])
    return adjacents

def is_low_point(point, adjacents):
    for num in adjacents:
        if num <= point:
            return False
    return True


low_points = {}
for x in range(x_len):
    for y in range(y_len):
        adjacents = get_adjacents(x, y, cave_map)
        if is_low_point(cave_map[x][y], adjacents):
            low_points[(x, y)] = cave_map[x][y]

risk_level = 0
for val in low_points.values():
    risk_level += val + 1

print(f"Part 1: Risk Levels {risk_level}")

#### Part 2:

def points_in_basin(point, cave_map):
    x = point[0]
    y = point[1]
    points = []

    if x != 0:
        if cave_map[x - 1][y] != 9 and cave_map[x - 1][y] > cave_map[x][y]:
            points = points + points_in_basin((x-1, y), cave_map)

    if x != x_len - 1:
        if cave_map[x + 1][y] != 9 and cave_map[x + 1][y] > cave_map[x][y]:
            points = points + points_in_basin((x + 1, y), cave_map)
    if y != 0:
        if cave_map[x][y - 1 ] != 9 and cave_map[x][y - 1] > cave_map[x][y]:
            points = points + points_in_basin((x, y - 1), cave_map)
    if y != y_len - 1:
        if cave_map[x][y + 1] != 9 and cave_map[x][y + 1] > cave_map[x][y]:
            points = points + points_in_basin((x, y + 1), cave_map)

    points.append(point)

    return points

three_largest = [0, 0, 0]

for low_point in low_points.keys():
    points = points_in_basin(low_point, cave_map)
    size = len(set(points))
    if size > three_largest[0]:
        three_largest[0] = size
        three_largest = sorted(three_largest)


print(f"Three largest basins: {three_largest[0] * three_largest[1] * three_largest[2]}")
