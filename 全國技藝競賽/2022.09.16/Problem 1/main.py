from rich import print

from sys import stdin

data = tuple(map(int, stdin.read().splitlines()))[1:]

data_divisors = {}
for num in data:
    if num in {2, 3, 5, 7}:
        num_divs = [num]
    else:
        num_divs = []
        for i in range(2, num//2+1):
            for j in range(2, int(i**.5)+1):
                if not i % j:
                    break
            else:
                n = num
                while not n % i:
                    n /= i
                    num_divs.append(i)
    data_divisors[num] = set(num_divs)

print(data_divisors)