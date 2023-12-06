from functions import lines, timer
from functools import reduce
from math import sqrt, ceil


@timer
def load_data(file):
    raw_data = lines(file)
    times = [int(x) for x in raw_data[0].split(":")[1].lstrip().split()]
    distances = [int(x) for x in raw_data[1].split(":")[1].lstrip().split()]
    time = int(raw_data[0].split(":")[1].replace(" ", ""))
    distance = int(raw_data[1].split(":")[1].replace(" ", ""))
    return [times, distances, [time, distance]]


@timer
def star_one(data_in):
    ways = list()
    for boat in range(len(data_in[0])):
        wincons = 0
        for hold in range(data_in[0][boat]):
            if hold * (data_in[0][boat] - hold) > data_in[1][boat]:
                wincons += 1
        ways.append(wincons)
    return reduce(lambda x, y: x*y, ways)


@timer
def star_two(data_in):
    time = data_in[2][0]
    distance = data_in[2][1]
    min_solved = (time - sqrt(time**2 - 4*distance))/2
    max_solved = (time + sqrt(time**2 - 4*distance))/2
    return ceil(max_solved)-ceil(min_solved)


@timer
def main():
    # data = []
    data = load_data("day06input.txt")
    print(data)
    print(star_one(data))
    print(star_two(data))


if __name__ == "__main__":
    main()
