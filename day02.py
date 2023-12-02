from functions import lines, timer


@timer
def load_data(file):
    # return lines(file)
    clean_data = list()
    for line in lines(file):
        game_data = list()
        game_split = line.split(":")
        game_data.append(int(game_split[0].split(" ")[1]))
        revealed = game_split[1].split("; ")
        reveals = list()
        for reveal in revealed:
            red, green, blue = 0, 0, 0
            for colour in reveal.strip().split(", "):
                if colour.split(" ")[1] == "red":
                    red = int(colour.split(" ")[0])
                elif colour.split(" ")[1] == "green":
                    green = int(colour.split(" ")[0])
                elif colour.split(" ")[1] == "blue":
                    blue = int(colour.split(" ")[0])
            reveals.append([red, green, blue])
        game_data.append(reveals)
        clean_data.append(game_data)
    return clean_data

r_max, g_max, b_max = 12, 13, 14


@timer
def star_one(data_in):
    total = 0
    for game in data_in:
        possible = True
        for reveal in game[1]:
            if r_max >= reveal[0] and g_max >= reveal[1] and b_max >= reveal[2]:
                continue
            else:
                possible = False
                break
        if possible:
            total += game[0]
    return total


@timer
def star_two(data_in):
    total = 0
    for game in data_in:
        r_min, g_min, b_min = 0, 0, 0
        for reveal in game[1]:
            r_min = max(r_min, reveal[0])
            g_min = max(g_min, reveal[1])
            b_min = max(b_min, reveal[2])
        total += r_min * g_min * b_min
    return total


@timer
def main():
    # data = []
    data = load_data("day02input.txt")
    print(star_one(data))
    print(star_two(data))


if __name__ == "__main__":
    main()
