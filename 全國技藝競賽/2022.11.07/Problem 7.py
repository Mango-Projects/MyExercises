from sys import stdin, stdout

data_input = stdin.read().splitlines()
data_count = int(data_input[0])

"""
5  9
9  5
----
4  4

"""

for data in data_input[1:data_count+1]:
    a, b = map(int, data.split())
    sum_ab = f'{a+b}'
    median = 0
    for raw_digit, sum_digit in enumerate(sum_ab[int(len(sum_ab) > len(f'{a}')):]):
        raw_digit = int(max(f'{a}'[raw_digit], f'{b}'[raw_digit]))
        if int(sum_digit) < raw_digit:
            median += 1
    stdout.write(f'{median}\n')