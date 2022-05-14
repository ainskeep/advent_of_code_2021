import helpers


relation_dict = {}

for line in helpers.read_input("input.txt"):
    begin, end = line.split('-')

    if begin in relation_dict.keys():
        relation_dict[begin].append(end)
    else:
        relation_dict[begin] = [end]

    if end in relation_dict.keys():
            relation_dict[end].append(begin)
    else:
        relation_dict[end] = [begin]

def pprint(node_set):
    for path in sorted(list(node_set)):
        print(path)
    print(f"Number of paths: {len(node_set)}")

def has_been(node_name, current_path):
    if node_name in current_path.split(","):
        return True
    return False


def visit_node(node_name, current_path):
    possible_moves = relation_dict.get(node_name, [])

    move_set = set()

    for move in possible_moves:
        if move == "end":
            move_set.add( current_path + "," + move )
        elif move.islower() and has_been(move, current_path):
            continue
        elif move in ["start"]:
            continue
        else:
            move_set.update(visit_node(move, current_path+","+move))

    return move_set

print("Part 1")
pprint(visit_node("start", "start"))


def can_go_to_small(move, current_path):
    visit_dict = {}
    for node in current_path.split(','):
        if node.islower() and node not in ["start", "end"]:
            if node in visit_dict.keys():
                visit_dict[node] = visit_dict[node] + 1
            else:
                visit_dict[node] = 1

    if move not in visit_dict.keys():
        return True

    for key, val in visit_dict.items():
        if val >= 2:
            return False

    return True

def visit_node_p2(node_name, current_path):
    possible_moves = relation_dict.get(node_name, [])

    move_set = set()

    for move in possible_moves:
        if move == "end":
            move_set.add( current_path + "," + move )
        elif move.islower() and not can_go_to_small(move, current_path):
            continue
        elif move in ["start"]:
            continue
        else:
            move_set.update(visit_node_p2(move, current_path+","+move))

    return move_set

print("Part 2")
pprint(visit_node_p2("start", "start"))