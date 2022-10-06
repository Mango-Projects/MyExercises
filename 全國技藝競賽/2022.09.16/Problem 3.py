from sys import stdin

# a1, b1, a2, b2, a3, b3 = map(int, stdin.read().splitlines())
a1, b1, a2, b2, a3, b3 = 3, 2, 1, 4, 1, 2

a, b = a1*(b2*b3+a3), b1*(b2*b3+a3)+a2*b3

print(a, b)