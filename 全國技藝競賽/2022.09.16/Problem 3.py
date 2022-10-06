from sys import stdin

_a, _b, _c = [map(int, i.split()) for i in stdin.read().splitlines()]
a1, b1, a2, b2, a3, b3 = *_a, *_b, *_c
# a1, b1, a2, b2, a3, b3 = 3, 2, 1, 4, 1, 2

a, b = a1*(b2*b3+a3), b1*(b2*b3+a3)+a2*b3

print(a, b)