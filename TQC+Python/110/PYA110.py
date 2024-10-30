a, b, c = (eval(input()) for _ in range(3))

print(+(60 < a < 100))
print(f"{round((b+1)/10,2):.2f}")
print(a if a >= c else c)