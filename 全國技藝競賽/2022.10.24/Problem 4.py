from itertools import permutations
from functools import reduce

# times = int(input())
# values = []
# for _ in range(times):
#     c, *d, t = map(int, input().split())
#     values.append((c, d, t))

values = [(3, (5, 7, 4), 3), (2, (1, 1), 2000), (5, (12, 2, 5, 1, 2), 4)] # testdata

for count, data, target in values:
    flag = True
    if reduce(int.__mul__, data) < target:
        print('無解')
        continue
    for i in permutations(('+', '-', '*', '/')*count, count-1):
        n, N = 0, ''
        for a, b in zip(data, ('',)+i):
            N += b + str(a)
            exec(f'n {b}= {a}')
            if n % 1 != 0 or abs(n) > 32000:
                continue
        if n == target:
            flag = False
            print(f'{N} = {int(n)}')
            break
    if flag:
        print('無解')