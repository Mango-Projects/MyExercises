from random import randint, random

with open(file="./input.txt", mode="r", encoding="utf8") as file:
    min_, max_, count, digit = map(int, file.readlines())

nums = [f'{randint(min_, max_)}.{str(random())[2:digit+2]}' for _ in range(count)]

with open(file="./output.txt", mode="w", encoding="utf8") as file:
    file.write(' '.join(nums))