import helpers
import copy

dot_chart = set()
instructions = []



for line in helpers.read_input("input.txt"):

    if line.startswith("fold along "):
        instructions.append(line.split()[-1])
    elif line:
        x, y = line.split(',')
        dot_chart.add((int(x), int(y)))


def pprint_dotchart(dot_chart):
    # find largest x and y
    largest_x, largest_y = 0, 0
    for chord in dot_chart:
        if chord[0] > largest_x:
            largest_x = chord[0]
        elif chord[1] > largest_y:
            largest_y = chord[1]

    square_board_size = max(largest_y + 1, largest_x + 1 )

    for y in range(square_board_size):
        for x in range(square_board_size):
            if (x, y) in dot_chart:
                print('#', end='')
            else:
                print(' ', end='')
        print("")

def do_translation(dot_chart, instruction):
    translation_direction, translation_point = instruction.split('=')
    translation_point = int(translation_point)

    new_dot_chart = set()

    if translation_direction == 'y':
        for cord in dot_chart:
            if cord[1] < translation_point:
                new_dot_chart.add(cord)
            elif cord[1] == translation_point:
                continue
            elif cord[1] > translation_point:
                y_cord = translation_point - (cord[1] - translation_point)
                new_dot_chart.add((cord[0], y_cord))

    elif translation_direction == 'x':
        for cord in dot_chart:
            if cord[0] < translation_point:
                new_dot_chart.add(cord)
            elif cord[0] == translation_point:
                continue
            elif cord[0] > translation_point:
                x_cord = translation_point - (cord[0] - translation_point)
                new_dot_chart.add((x_cord, cord[1]))


    return new_dot_chart


print(f"Part 1 {len(do_translation(copy.deepcopy(dot_chart), instructions[0]))}")

for instruction in instructions:
    dot_chart = do_translation(copy.deepcopy(dot_chart), instruction)

pprint_dotchart(dot_chart)

print(f"Part 2 {len(dot_chart)}")

