from sys import stdin, stdout

k, i = int(stdin.read().splitlines()[0]), 1
for i in (2, 3, 5, 7):
    n = 2**(i-1)*(2**i-1)
    if n > k:
        break
    stdout.write(f'{n}\n')