"""
this is a book -> book a is this
"""
from sys import stdin

print(' '.join(stdin.read()[:-1].split(' ')[::-1]))