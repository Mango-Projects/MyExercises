a, b, c = (input() for _ in range(3))

print("error" if c not in "+-*" else eval(a+c+b))