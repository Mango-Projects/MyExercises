from sys import stdin

money = map(int, stdin.read().splitlines())
# money = [10, 5, 20, 30]

keys = (1000, 500, 200, 100)
values = []

for item in range(1, min(list(money))+1):
    if any(new:=[i % item for i in money]):
        values = new

print(len(new))
for key, value in zip(keys, values):
    print(key, value, sep='\t')