import helpers
import heapq as heap
from collections import defaultdict

board = []
for line in helpers.read_input("input.txt"):
    board.append([int(char) for char in line])

x_max = len(board[0]) - 1
y_max = len(board) - 1

board_dict = {}

for y, y_line in enumerate(board):
    for x, cost in enumerate(board):
        board_dict[(x, y)] = board[x][y]


def get_adjNodes(node, cost_dict):
    x, y = node
    adj_nodes = [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1)
    ]

    return [node for node in adj_nodes if node in cost_dict.keys()]


def dijkstra(cost_dict, starting_node=(0,0)):
    visited = set()
    priority_queue = []
    parentsMap = {}
    cost_to_node = defaultdict(lambda: float('inf'))
    cost_to_node[starting_node] = 0
    heap.heappush(priority_queue, (0, starting_node))

    while priority_queue:
        _, node = heap.heappop(priority_queue)
        visited.add(node)
        for adjNode in get_adjNodes(node, cost_dict):
            weight = cost_dict[adjNode]
            newCost = cost_to_node[node] + weight
            if cost_to_node[adjNode] > newCost:
                parentsMap[adjNode] = node
                cost_to_node[adjNode] = newCost
                heap.heappush(priority_queue, (newCost, adjNode))

    return parentsMap, cost_to_node


parentsMap, cost_to_node = dijkstra(board_dict, (0,0))

print(f"Part 1: Cost to {(x_max, y_max)}: {cost_to_node[(x_max, y_max)]}")

# Part 2

# Gen data and run through dijkstra again

new_board_dict = {}
for y_increase in range(5):
    for x_increase in range(5):
        for node, cost in board_dict.items():
            x, y = node
            cost = cost + x_increase + y_increase
            while cost > 9:
                cost = cost - 9
            new_board_dict[(x + x_increase * (x_max + 1 ), y + y_increase * (y_max + 1 ))] = cost

parentsMap, cost_to_node = dijkstra(new_board_dict, (0,0))
max_node = ( (x_max+1)*5 - 1, (y_max+1)*5 - 1 )
print(f"Part 1: Cost to {max_node}: {cost_to_node[max_node]}")