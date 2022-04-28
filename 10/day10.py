import helpers
import math

lines = helpers.read_input("input.txt")

stack = []
opening_brackets = ['[', '{', '(', '<']
closing_brackets = [']', '}', ')', '>']

point_map = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

point_map_part_two = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}
compliment_map = {
    '[': ']',
    '(': ')',
    '{': '}',
    '<': '>',
}

def process_line(line):
    stack = []
    for char in line:
        if char in opening_brackets:
            stack = [char] + stack
        if char in closing_brackets:
            compliment = stack.pop(0)
            if compliment == '(' and char == ')':
                continue
            elif compliment == '[' and char == ']':
                continue
            elif compliment == '{' and char == '}':
                continue
            elif compliment == '<' and char == '>':
                continue
            else:
                return point_map[char]
    return 0

total_points = 0
for line in lines:
    total_points += process_line(line)

print(f"Total Points: {total_points}")

# part 2

def process_line_part_two(line):
    stack = []
    points = 0
    for char in line:
        if char in opening_brackets:
            stack = [char] + stack
        if char in closing_brackets:
            compliment = stack.pop(0)
            if compliment == '(' and char == ')':
                continue
            elif compliment == '[' and char == ']':
                continue
            elif compliment == '{' and char == '}':
                continue
            elif compliment == '<' and char == '>':
                continue
            else:
                return 0
    if stack:
        for i in range(len(stack)):
            compliment = stack.pop(0)
            points = 5 * points
            points += point_map_part_two[compliment_map[compliment]]

    return points

scores = []
for line in lines:
    score = process_line_part_two(line)
    if score:
        scores.append(score)

scores.sort()
middle_index = math.floor(len(scores)/2)

print(f"Part 2: {scores[middle_index]}")