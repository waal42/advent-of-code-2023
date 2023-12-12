from functions import lines_of_numbers, timer


@timer
def load_data(file):
    return lines_of_numbers(file, " ")


@timer
def star_one(data_in):
    extrapolated = 0
    for seq in data_in:
        last_values = [seq[-1]]
        seq_diffs = seq
        zeroes = False
        while not zeroes:
            seq_diffs = sequence_diffs(seq_diffs)
            last_values.append(seq_diffs[-1])
            if seq_diffs.count(seq_diffs[0]) == len(seq_diffs) and seq_diffs[0] == 0:
                zeroes = True
        for i, val in enumerate(reversed(last_values)):
            if i == 0:
                add = 0
            else:
                add = add + val
        extrapolated += add
    return extrapolated


def sequence_diffs(seq):
    out = list()
    for i in range(len(seq) - 1):
        out.append(seq[i+1] - seq[i])
    return out


@timer
def star_two(data_in):
    extrapolated = 0
    for seq in data_in:
        first_values = [seq[0]]
        seq_diffs = seq
        zeroes = False
        while not zeroes:
            seq_diffs = sequence_diffs(seq_diffs)
            first_values.append(seq_diffs[0])
            if seq_diffs.count(seq_diffs[0]) == len(seq_diffs) and seq_diffs[0] == 0:
                zeroes = True
        for i, val in enumerate(reversed(first_values)):
            if i == 0:
                add = 0
            else:
                add = val - add
        extrapolated += add
    return extrapolated


@timer
def main():
    # data = []
    data = load_data("day09input.txt")
    # print(data)
    print(star_one(data))
    print(star_two(data))


if __name__ == "__main__":
    main()
