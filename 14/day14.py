import helpers
import time


starting_chain = ""
rules = {}

for line in helpers.read_input("input.txt"):

    if "->" in line:
        rule, insert = line.split(" -> ")
        rules[rule] = insert

    elif line:
        starting_chain = line.strip()

def do_step(chain):
    new_chain = ""

    for i in range(len(chain) + 1):
        if i > 1:
            pair = chain[i-2:i]
            if pair in rules.keys():
                insert = rules[pair]
                new_chain = new_chain + pair[0] + insert

    new_chain = new_chain + chain[-1]
    return new_chain

def score_chain(chain):
    counts = {}
    for char in chain:
        if char not in counts.keys():
            counts[char] = 1
        else:
            counts[char] = counts[char] + 1

    least_common, most_common = 9999999999, 0
    for key, val in counts.items():
        if val < least_common:
            least_common = val
        if val > most_common:
            most_common = val

    return most_common - least_common

chain = starting_chain
for i in range(10):
    chain = do_step(chain)

print(f"Part 1 {score_chain(chain)}")


# Part 2
def score_dict(count_dict):
    least_common, most_common = 9999999999999999999999999999999, 0
    for key, val in count_dict.items():
        if val < least_common:
            least_common = val
        if val > most_common:
            most_common = val

    return most_common - least_common

def add_to_dict(diction, key, amount):
    if key not in diction.keys():
        diction[key] = amount
    else:
        diction[key] = diction[key] + amount

def break_down_template(template):
    pair_dict = {}
    count_dict= {}

    for i in range(len(template) + 1):
        if i < len(template):
            letter = template[i]
            add_to_dict(count_dict, letter, 1)
        if i > 1:
            pair = template[i-2:i]
            if pair in pair_dict.keys():
                pair_dict[pair] = pair_dict[pair] + 1
            else:
                pair_dict[pair] = 1
    return pair_dict, count_dict

def do_step_part_two(pair_dict, count_dict):
#todo, track count seprately?
#todo dont have 3 var, just split into 2

    new_pair_dict = {}
    for key, val in pair_dict.items():
        insert = rules[key]
        add_to_dict(count_dict, insert, val)
        add_to_dict(new_pair_dict, key[0]+insert, val)
        add_to_dict(new_pair_dict, insert+key[1], val)

    return new_pair_dict


chain = starting_chain
pair_dict, count_dict = break_down_template(chain)

start = time.time()
for i in range(40):
    last_start = time.time()
    pair_dict = do_step_part_two(pair_dict, count_dict)

print(f"Part 2 {score_dict(count_dict)} Took { time.time() - start }")
