from sys import stdin

fib = lambda n: n if n<2 else fib(n-1) + fib(n-2)

num = int(stdin.read()[:-1])

for i in range(1, num+1):
    print(f'({i}) {fib(i+3)}')