card_map = dict(*zip(range(2, 10), range(2, 10))) + {}

with open(file="./input.txt", mode="r", encoding="utf8") as input_file:
    start, card1, card2, _ = [i.replace("\n", "") for i in input_file.readlines()]

with open(file="./output.txt", mode="w", encoding="utf8") as output_file:
    ...