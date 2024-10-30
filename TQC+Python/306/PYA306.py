def compute(n: int) -> int: return 1 if n == 0 else n * compute(n - 1)

a = eval(input())

print(f"{a}!={compute(a)}")