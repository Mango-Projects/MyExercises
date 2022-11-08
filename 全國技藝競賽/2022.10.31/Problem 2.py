from itertools import combinations
from sys import stdin

_input = stdin.read().splitlines()

values = [(*map(int, _input[i].split()), _input[i+1]) for i in range(0, len(_input), 2)]

# values = [(6, 4, '268574'), (5, 2, '41235')] # testdata

for value in values:
    print(max(int(''.join(i)) for i in combinations(value[2], value[0]-value[1])))