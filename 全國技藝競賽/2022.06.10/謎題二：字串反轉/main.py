with open(file="./input.txt", mode="r", encoding="utf8") as file:
    string = " ".join(file.read().split()[::-1])

with open(file="./output.txt", mode="w", encoding="utf8") as file:
    file.write(string)