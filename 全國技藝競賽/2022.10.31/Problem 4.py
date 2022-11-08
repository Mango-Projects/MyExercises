from sys import stdin

values = [*map(str.split, stdin.read().splitlines())]

# values = [('1', '36', '3647'), ('8', '79', '797', '799')] # testdata

for value in values:
    print(''.join(sorted(value)))