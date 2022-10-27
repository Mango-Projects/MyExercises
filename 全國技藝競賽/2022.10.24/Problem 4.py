from itertools import permutations

times = int(input())


data = (5, 7, 4)
target = 3

flag = True
for i in permutations(('+', '-', '*', '/')*len(data), len(data)-1):
    n, N = 0, ''
    for a, b in zip(data, ('',)+i):
        N += b + str(a)
        exec(f'n {b}= {a}')
        if n % 1 != 0 or abs(n) > 32000:
            continue
    if n == target:
        flag = False
        print(f'{N} = {n}')
        break
if flag:
    print('nan')