from math import ceil, log

with open('./input.txt') as file:
    lines = [int(i.removesuffix('\n')) for i in file.readlines()]
    nums = [lines[2*i:2*i+2] for i in range(int(len(lines)/2))]

for n, p in nums:
    print(log(p, n))