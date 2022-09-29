from sys import stdin
from random import uniform

num, min_, max_, digit = map(int, stdin.read().split(' '))

print('、'.join(map(str, [format(uniform(min_, max_), f'.{digit}f') for _ in range(num)])))