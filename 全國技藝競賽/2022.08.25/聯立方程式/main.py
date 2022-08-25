from typing import Iterable

def equation(coef: Iterable[int]) -> tuple[int, int]:
    a, b, c, d, e, f = coef
    if (_:=a / d) != b / e:
        return (-(c*e-b*f)/(a*e-b*d), -(c*d-a*f)/(b*d-a*e))
    if _ == c/e:
        return "inf"
    return "no result"

with open('./input.txt') as file:
    coefficient = map(int, file.readline().split(','))

with open('./output.txt', 'w') as file:
    X, Y = map(int, equation(coef=coefficient))
    file.write(f'{X=}, {Y=}')