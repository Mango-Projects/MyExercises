with open('./input.txt') as file:
    coefficient = file.readline().split(',')
    # a1, b1, c1, a2, b2, c2

def check_solution(coef):
    a, b, c = coef[0]/coef[3], coef[1]/coef[4], coef[2]/coef[5]
    if a != b: # a != b
        return 1
    if a == c: # a == b + a == c
        return 0
    return -1 # a == b + a != c

"""
1, 1, -2
3, 1, -4
ax + by + c = 0 -> y = -(a/b)x-c/b = -(1/1)x-(-2)/1 = -x+2
dx + ey + f = 0 -> x = -f/(d+e(-(a/b)x-c/b)) = 4/(3+1(1/1)x-2) = 4/(4x-2) = 4



"""

for k, v in globals().copy().items():
    if k[:2] != '__' and k[-2:] != '__':
        print(f'{k}: {v}')