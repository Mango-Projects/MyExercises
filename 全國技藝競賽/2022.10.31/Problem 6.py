from sys import stdin

# _input = stdin.read().splitlines()
# values = [(*_input[i:i+1],) for i in range(0, len(_input), 2)]

values = [(36, 2), (64, 8)] # testdata

for value in values:
    print(len([i for i in range(1, value[0]//2+1) if not (value[0] % i or i % value[1])]))