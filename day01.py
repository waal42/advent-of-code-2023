from functions import lines, timer
import re


@timer
def load_data(file):
    return lines(file)


digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

first_letters = set([x[0] for x in digits.keys()])


@timer
def star_one(data_in):
    nums = list()
    for line in data_in:
        num = list()
        for char in line:
            if char in list(digits.values()):
                num.append(char)
        nums.append(int("".join([num[0], num[-1]])))
    return sum(nums)


@timer
def star_two(data_in):
    nums = list()
    for line in data_in:
        pattern = r"(\d|one|two|three|four|five|six|seven|eight|nine)"
        first_match = re.search(pattern, line)
        first = first_match.group(0)
        last_match = re.search(pattern, line[::-1])
        last = last_match.group(0)
        first = first if first.isdigit() else digits[first]
        last = last if last.isdigit() else digits[last]
        nums.append(int("".join([first, last])))
    return sum(nums)



@timer
def main():
    # data = []
    data = load_data("day01input.txt")
    # print(data)
    print(star_one(data))
    print(star_two(data))


if __name__ == "__main__":
    main()
