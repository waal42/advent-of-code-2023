from functions import blocks_of_lines, timer
from pprint import pprint
from functools import reduce
from math import lcm


@timer
def load_data(file):
    raw_data = blocks_of_lines(file)
    directions = dict()
    directions["instructions"] = raw_data[0][0]
    directions["starting_nodes"] = list()
    last_letters = dict()
    last_letters_left = dict()
    last_letters_right = dict()
    for node_index in range(len(raw_data[1])):
        node, l_r = raw_data[1][node_index].split(" = ")
        directions[node] = l_r.replace(")", "").replace("(", "").split(", ")
        if node[2] == "A":
            directions["starting_nodes"].append(node)
        '''if node[2] in last_letters:
            last_letters[node[2]] += 1
        else:
            last_letters[node[2]] = 1
        if directions[node][0][2] in last_letters_left:
            last_letters_left[directions[node][0][2]] += 1
        else:
            last_letters_left[directions[node][0][2]] = 1
        if directions[node][1][2] in last_letters_right:
            last_letters_right[directions[node][1][2]] += 1
        else:
            last_letters_right[directions[node][1][2]] = 1
    pprint(last_letters)
    pprint(last_letters_left)
    pprint(last_letters_right)'''
    return directions
        


@timer
def star_one(data_in):
    position = "AAA"
    steps = 0
    while position != "ZZZ":
        # print(steps, position, data_in[position])
        if data_in["instructions"][steps % len(data_in["instructions"])] == "L":
            position = data_in[position][0]
        else:
            position = data_in[position][1]
        steps += 1
    return steps


@timer
def star_two(data_in):
    positions = data_in["starting_nodes"]
    counter = [0 for x in positions]
    cycle_length = list()
    for position in positions:
        z_found = False
        new_position = position
        steps = 0
        while not z_found:
            if data_in["instructions"][steps % len(data_in["instructions"])] == "L":
                new_position = data_in[new_position][0]
            else:
                new_position = data_in[new_position][1]
            steps += 1
            if new_position[2] == "Z":
                cycle_length.append(steps)
                z_found = True
    return reduce(lcm, cycle_length)


@timer
def main():
    # data = []
    data = load_data("day08input.txt")
    # pprint(data)
    print(star_one(data))
    print(star_two(data))


if __name__ == "__main__":
    main()
