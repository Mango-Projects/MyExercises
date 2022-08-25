from typing import Generator
from math import factorial as f

def binomial(n: int) -> Generator:
    for k in range(n+1):
        yield int(f(n)/(f(k)*f(n-k)))

with open('./input.txt') as file:
    numbers = map(int, file.readlines())

with open('./output.txt', 'w') as file:
    for i in numbers:
        file.write(', '.join(map(str, binomial(i)))+'\n')