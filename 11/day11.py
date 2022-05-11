import helpers

octopus_board = []
sample_state = []
flash_total = 0
steps = 100

max_row_len = 0
max_col_len = 0

for line in helpers.read_input("input.txt"):
    octopus_board.append([int(char) for char in line])
    max_col_len = len(line)

for line in helpers.read_input("sample_state.txt"):
    sample_state.append([int(char) for char in line])

max_row_len = len(octopus_board)

def increment_all(board):
    for row_num, row in enumerate(board):
        for col_num, value in enumerate(row):
            board[row_num][col_num] = board[row_num][col_num] + 1
    return

def flash(point, board):
    row_num, col_num = point
    points_to_inc = set()

    if row_num != 0:
        # top
        points_to_inc.add((row_num - 1, col_num))

    if row_num > 0 and col_num > 0:
        # top left
        points_to_inc.add((row_num - 1, col_num - 1))

    if col_num > 0:
        # left
        points_to_inc.add((row_num, col_num - 1))

    if row_num < max_row_len - 1 and col_num > 0:
        # bottom left
        points_to_inc.add((row_num + 1, col_num - 1))

    if row_num < max_row_len - 1:
        # bottom
        points_to_inc.add((row_num + 1, col_num))

    if row_num < max_row_len - 1 and col_num < max_col_len - 1:
        # bottom right
        points_to_inc.add((row_num + 1, col_num + 1))

    if col_num < max_col_len - 1:
        # right
        points_to_inc.add((row_num, col_num + 1))

    if col_num < max_col_len - 1 and row_num > 0:
        # top right
        points_to_inc.add((row_num - 1, col_num + 1))

    for point in points_to_inc:
        board[point[0]][point[1]] = board[point[0]][point[1]] + 1

    board[row_num][col_num] = -99999999999




for step_count in range(steps):

    # First, the energy level of each octopus increases by 1.
    increment_all(octopus_board)
    # Then Flash
    flashed_last = True

    while flashed_last:
        flashed_last = False

        for row_num, row in enumerate(octopus_board):
            for col_num, value in enumerate(row):
                if value > 9:
                    flash((row_num, col_num), octopus_board)
                    flash_total += 1
                    flashed_last = True

    for row_num, row in enumerate(octopus_board):
        for col_num, value in enumerate(row):
            if value < 0:
                octopus_board[row_num][col_num] = 0

print(flash_total)


# part 2
# reload data
octopus_board = []
for line in helpers.read_input("input.txt"):
    octopus_board.append([int(char) for char in line])

flash_total = 0
step_total = 0
goal_board = [[ 0 for col in octopus_board[0] ] for row in octopus_board]

while True:
    # First, the energy level of each octopus increases by 1.
    increment_all(octopus_board)
    # Then Flash
    flashed_last = True
    step_total += 1

    while flashed_last:
        flashed_last = False

        for row_num, row in enumerate(octopus_board):
            for col_num, value in enumerate(row):
                if value > 9:
                    flash((row_num, col_num), octopus_board)
                    flash_total += 1
                    flashed_last = True

    for row_num, row in enumerate(octopus_board):
        for col_num, value in enumerate(row):
            if value < 0:
                octopus_board[row_num][col_num] = 0

    print(f"Finished Step {step_total}")

    if octopus_board == goal_board:
        print(f"All flashed after step {step_total}")
        break