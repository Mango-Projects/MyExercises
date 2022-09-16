from sys import stdin

data = stdin.read()

print(sum(1 for i in set(data) if i.isdigit()))