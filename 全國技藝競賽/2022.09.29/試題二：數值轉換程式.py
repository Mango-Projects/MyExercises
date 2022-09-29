from sys import stdin

num = stdin.read().removesuffix('\n').split('.')
print(int(num[0], 2) + int(num[1], 2) / 2.**len(num[1]))