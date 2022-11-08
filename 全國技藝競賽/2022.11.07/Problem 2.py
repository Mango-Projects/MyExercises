from sys import stdin, stdout
from math import ceil

data_input = stdin.read().splitlines()
data_count = int(data_input[0])

prime_list = [i for i in range(3, 5000, 2)] # Generate Prime List
for number in prime_list:
    for factor in range(2, ceil(number/2)):
        if not number % factor:
            # print(f'REMOVE > {number} ? {factor}')
            prime_list.remove(number)
            break

for data in data_input[1:data_count+1]:
    data = int(data)
    for number in prime_list:
        if data - number in prime_list:
            a, b = number, data-number
            break
    stdout.write(f'{a} {b}\n')