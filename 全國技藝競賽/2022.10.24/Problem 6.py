from itertools import permutations

# times = int(input())
# values = [input() for _ in range(times)]

values = ['213', 'ABC'] # testdata

for value in values:
    print('\n'.join(''.join(i) for i in permutations(sorted(value), len(value))))