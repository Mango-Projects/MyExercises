from sys import stdin
from itertools import permutations

chars = stdin.read()[:-1]

print('、'.join(''.join(i) for i in permutations(chars, len(chars))))