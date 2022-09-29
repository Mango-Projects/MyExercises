from sys import stdin

num = int(stdin.read()[:-1])

lst = []
while num not in lst:
    print(f'{num}\t{num**2}')
    lst.append(num)
    _ = tuple(map(int, list(str(num**2))))
    num = int(f'{min(_)}{max(_)}')
print(f'*{num}\t{num**2}')