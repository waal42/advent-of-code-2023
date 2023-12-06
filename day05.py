from functions import blocks_of_lines, timer
from pprint import pprint
from math import inf


@timer
def load_data(file):
    raw_input = blocks_of_lines(file)
    structured_input = dict()
    structured_input["s"] = [int(x) for x in raw_input[0][0].split(": ")[1].split()]
    structured_input["ss"] = [[int(y) for y in x.split()] for x in raw_input[1][1:]]
    structured_input["sf"] = [[int(y) for y in x.split()] for x in raw_input[2][1:]]
    structured_input["fw"] = [[int(y) for y in x.split()] for x in raw_input[3][1:]]
    structured_input["wl"] = [[int(y) for y in x.split()] for x in raw_input[4][1:]]
    structured_input["lt"] = [[int(y) for y in x.split()] for x in raw_input[5][1:]]
    structured_input["th"] = [[int(y) for y in x.split()] for x in raw_input[6][1:]]
    structured_input["hl"] = [[int(y) for y in x.split()] for x in raw_input[7][1:]]
    return structured_input


order = ["ss", "sf", "fw", "wl", "lt", "th", "hl"]


@timer
def star_one(data_in):
    lowest = inf
    for seed in data_in["s"]:
        current_index = seed
        for conversion in order:
            for interval in data_in[conversion]:
                if interval[1] <= current_index <= interval[1] + interval[2]:
                    current_index = current_index - interval[1] + interval[0]
                    break
        lowest = min(lowest, current_index)
    return lowest

"""
@timer
def star_two(data_in):
    lowest = inf
    seed_intervals = data_in["s"]
    for i in range(0, len(seed_intervals), 2):
        for seed in range(seed_intervals[i], seed_intervals[i] + seed_intervals[i+1]):
            current_index = seed
            for conversion in order:
                for interval in data_in[conversion]:
                    if current_index in range(interval[1], interval[1] + interval[2]):
                        current_index = current_index - interval[1] + interval[0]
                        break
            lowest = min(lowest, current_index)
    return lowest
"""

@timer
def star_two(data_in):
    lowest = 0
    found = False
    while not found:
        # print(lowest)
        current_index = lowest
        for conversion in order[::-1]:
            for interval in data_in[conversion]:
                if interval[0] <= current_index <= interval[0] + interval[2]:
                    current_index = current_index - interval[0] + interval[1]
                    break
        for i in range(0, len(data_in["s"]), 2):
            if data_in["s"][i] <= current_index <= data_in["s"][i] + data_in["s"][i+1]:
                found = True
                return lowest
        lowest += 1

@timer
def main():
    # data = []
    data = load_data("day05input.txt")
    # pprint(data)
    print(star_one(data))
    print(star_two(data))


if __name__ == "__main__":
    main()
