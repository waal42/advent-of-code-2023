from functions import lines, timer


@timer
def load_data(file):
    clean_data = list()
    for line in lines(file):
        card = int(line.split(": ")[0].split()[1])
        winning = [int(x) for x in line.split(": ")[1].split(" | ")[0].split()]
        mine = [int(x) for x in line.split(": ")[1].split(" | ")[1].split()]
        clean_data.append([card, winning, mine])
    return clean_data


@timer
def star_one(data_in):
    points = 0
    for card in data_in:
        mine_winning = 0
        for mine in card[2]:
            if mine in card[1]:
                mine_winning += 1
        if mine_winning:
            points += 2 ** (mine_winning - 1)
    return points


@timer
def star_two(data_in):
    cards = dict()
    for card in data_in:
        if card[0] not in cards:
            cards[card[0]] = 1
        else:
            cards[card[0]] += 1
        mine_winning = 0
        for mine in card[2]:
            if mine in card[1]:
                mine_winning += 1
        if mine_winning:
            for i in range(card[0] + 1, mine_winning + card[0] + 1):
                if i in cards.keys():
                    cards[i] += cards[card[0]]
                else:
                    cards[i] = cards[card[0]]
    return sum(cards.values())


@timer
def main():
    # data = []
    data = load_data("day04input.txt")
    # print(data)
    print(star_one(data))
    print(star_two(data))


if __name__ == "__main__":
    main()
