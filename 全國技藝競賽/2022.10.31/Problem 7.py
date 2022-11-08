from math import sin, cos

values = [(2, 2000), (10, 3000)]

pi = 3.14
for value in values:
    r, n = value
    angle = (90-360/2)*n
    triangle = sin(angle)*cos(angle)*n
    print(triangle)