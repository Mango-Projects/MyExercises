"""
value = 012345678
x, y = 0, 0

012
783
654

(0, 0) -> (0, 1) -> (0, 2) -> (1, 2) -> (2, 2) -> (2, 1) -> (2, 0) -> (1, 0) -> (1, 1)
     (0, +) -> (0, +) -> (+, 2) -> (+, 2) -> (2, -) -> (2, -) -> (-, 0) -> (1, -)
"""

from math import ceil

values = ['0123456789ABCDE', '111111111111111122222222']

for value in values:
    height = ceil(len(value)**.5)
    box = [[None] * height for _ in range(height)]
    _range = range(1, height+1)
    x, y = 0, 0
    x_move, y_move = 1, 0
    while value:
        box[x][y] = value[0]
        value = value[1:]
        if not box[x][y] is None:
            
        if x not in _range:
            if x > height:
                ...
            else:
                ...
        if x not in _range:
            if x > height:
                ...
            else:
                ...