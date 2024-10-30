a = eval(input())

print("error" if a not in range(0, 101) else a + 10 if a > 60 else a + 5)