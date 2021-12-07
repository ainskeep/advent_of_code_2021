IN_FILE = 'input.txt'


def read_input(file_name=IN_FILE):
    lines = []
    with open(file_name, 'r') as infile:
        lines = infile.read().splitlines()
    return lines


