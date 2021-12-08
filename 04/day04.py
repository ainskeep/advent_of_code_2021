import helpers
import copy

lines = helpers.read_input()

boards = list()
board_height = 5
board_width = 5

print("Part 1")
pull_list = lines.pop(0).split(',')
lines.pop(0)

def gen_board(lines):
    while len(lines) >= board_height:
        board = []
        for i in range(board_height):
            line = lines.pop(0)
            line = line.strip()
            row = line.split()
            board.append(row)
        if len(lines) > 0:
            lines.pop(0) # pop whitespace line
        yield board

def board_has_won(position_board):
    for y in range(board_height):
        if position_board[y] == ['x' for i in range(board_width)]:
            # Horizontal win
            return True

        # this only works because board_width == board_height
        column_board = [position_board[x][y] for x in range(board_width)]
        if column_board == ['x' for i in range(board_width)]:
            return True

    return False


def score_board(board, pull_list):
    score, win_time = 0, len(pull_list) + 99999
    has_won = False
    last_pull = 0
    position_board = [['0' for x in range(board_width)] for y in range(board_height)]

    for turn, pull_num in enumerate(pull_list):
        for y in range(board_height):
            for x in range(board_width):
                if board[x][y] == pull_num:
                    position_board[x][y] = 'x'

        if board_has_won(position_board):
            has_won = True
            win_time = turn
            last_pull = int(pull_num)
            break

    if not has_won:
        # didn't win, return defaults
        return score, win_time

    for y in range(board_height):
        for x in range(board_width):
            if position_board[x][y] != 'x':
                score += int(board[x][y])

    return score*last_pull, win_time


best_board_data = {
    'position': 0,
    'win_time': 999999,
    'score': 0
}

worst_board_data = {
    'position': 0,
    'win_time': -1,
    'score': 9999999
}

position = [
    ['0' for i in range(board_width)],
    ['0' for i in range(board_width)],
    ['x' for i in range(board_width)],
    ['0' for i in range(board_width)],
    ['0' for i in range(board_width)],
]


for i, board in enumerate(gen_board(lines)):
    score, win_time = score_board(board, pull_list)
    if win_time < best_board_data['win_time']:
        best_board_data['position'] = i
        best_board_data['win_time'] = win_time
        best_board_data['score'] = score
    elif win_time == best_board_data['win_time'] and score >= best_board_data['score']:
        best_board_data['position'] = i
        best_board_data['win_time'] = win_time
        best_board_data['score'] = score

    if win_time > worst_board_data['win_time']:
        worst_board_data['position'] = i
        worst_board_data['win_time'] = win_time
        worst_board_data['score'] = score
    elif win_time == worst_board_data['win_time'] and score <= worst_board_data['score']:
        worst_board_data['position'] = i
        worst_board_data['win_time'] = win_time
        worst_board_data['score'] = score

print(f"Best board: {best_board_data}")

print(f"Part 2")

print(f"Worst board: {worst_board_data}")

