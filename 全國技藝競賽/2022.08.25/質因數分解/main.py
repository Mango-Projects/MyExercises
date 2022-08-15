from functools import reduce
from math import sqrt, ceil

with open('./input.txt') as file:
    number = int(file.readline())

def prime_factorization(n):
    def factors(n): # https://stackoverflow.com/a/6800214
        return set(reduce(list.__add__,
                          ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    primes = [j for j in range(2, int(n//2)+1) if factors(j) == {1, j}]
    table = {i: 0 for i in primes}
    for k in table:
        while not n % k:
            n //= k
            table[k] += 1
    return '*'.join(str(k) for k, v in table.items() for i in range(v))

with open('./output.txt', 'w') as file:
    file.write(f'{number}= {prime_factorization(number)}')