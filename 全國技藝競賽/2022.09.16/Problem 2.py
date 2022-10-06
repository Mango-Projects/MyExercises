from sys import stdin

money = int(stdin.read()[:-1])
# money = 78

flowers = [0] * 4
for index, cost in enumerate((50, 10, 5, 1)):
    flowers[index] = money//cost
    money %= cost

for i in flowers:
    print(i)