"""
x = b^p, max(b) = 1

x          | p
-----------|----
17         | 1
1073741824 | 30
25         | 2
-25        | 1
64         | 6
-64        | 3
"""
from sys import stdin
from math import ceil

for input_num in map(int, stdin.read().splitlines()):
    powers = 1
    for num in range(1, input_num+1):
        ...