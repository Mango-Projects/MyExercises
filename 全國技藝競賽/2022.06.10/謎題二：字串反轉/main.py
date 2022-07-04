# string = input().split()
# print(" ".join(string[::-1]))

with open(file="./input.txt", mode="r", encoding="utf8") as input_file:
    string = " ".join(input_file.readlines()[0].split()[::-1])

with open(file="./output.txt", mode="w", encoding="utf8") as output_file:
    output_file.write(string)