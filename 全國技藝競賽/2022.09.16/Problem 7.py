from sys import stdin

# count, *strings = stdin.read().splitlines()
count, *strings = 5, 858, 792, 459, 574, 762
strings = strings[:count]

strings = tuple(map(str, strings))
print('、'.join(strings))
for i in range(3):
    print('、'.join(sorted(strings, key=lambda x: int(x[-(i+1)]))))