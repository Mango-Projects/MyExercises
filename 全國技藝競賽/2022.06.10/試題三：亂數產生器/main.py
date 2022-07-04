import random

# min_, max_ = map(int, input().split())
# count = int(input())
# digit = int(input())

# nums = [f'{random.randint(min_, max_)}.{str(random.random())[2:digit+2]}' for i in range(count)]

# print(*nums)

with open(file="./input.txt", mode="r", encoding="utf8") as input_file:
    min_, max_, count, digit = [int(i) for i in input_file.readlines()]

nums = [f'{random.randint(min_, max_)}.{str(random.random())[2:digit+2]}' for i in range(count)]

with open(file="./output.txt", mode="w", encoding="utf8") as output_file:
    output_file.write(' '.join(nums))