# from sys import stdin

# num = int(stdin.read()[:-1])

# add_nums = []

def f(n: int) -> tuple[int]:
    if n > 1:
        return (f(n-1) + f(n-2))
    return (n,)


print(f(5))