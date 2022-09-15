card_map = dict(*zip(range(2, 10), range(2, 10))) + {}

with open(file="./input.txt", mode="r", encoding="utf8") as file:
    start, card1, card2, _ = [i.replace("\n", "") for i in file.readlines()]

with open(file="./output.txt", mode="w", encoding="utf8") as file:
    ...