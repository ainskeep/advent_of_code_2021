import helpers

lines = helpers.read_input("input.txt")

cords_dict = {}

def get_points(start, end):
    points = []
    if start[0] == end[0]:
        # X is the same. Vertical line
        for y in range(min(start[1], end[1]), max(start[1], end[1]) + 1 ):
            points.append((start[0], y))
        return points

    if start[1] == end[1]:
        # Y is the same. Horizontal line
        for x in range(min(start[0], end[0]), max(start[0], end[0]) + 1 ):
            points.append((x, start[1]))
        return points

    # Diagonal line
    # Assume only a Diagonal line could be here
    if start[0] > end[0]:
        x_range = range(start[0], end[0] -1, -1 )
    else:
        x_range = range(min(start[0], end[0]), max(start[0], end[0]) + 1 )

    if start[1] > end[1]:
        y_range = range(start[1], end[1] -1, -1 )
    else:
        y_range = range(min(start[1], end[1]), max(start[1], end[1]) + 1 )

    for i in range(len(x_range)):
        point = (x_range[i], y_range[i])
        points.append(point)

    return points

for line in lines:
    start, direction, end = line.split()

    start_tuple = tuple([int(x) for x in start.split(',')])
    end_tuple = tuple([int(x) for x in end.split(',')])

    points = get_points(start_tuple, end_tuple)

    for point in points:
        if point not in cords_dict:
            cords_dict[point] = 1
        else:
            cords_dict[point] = 1 + cords_dict[point]

print("Part 1")

counter = 0
for val in cords_dict.values():
    if val >= 2:
        counter +=1

print(counter)

pass