"""
2022.10.18 finish
"""
input_times = int(input())
values = [input() for _ in range(input_times)]

for value in values:
    old = value
    while True:
        new = old.replace('()', '').replace('[]', '')
        if old == new:
            break
        old = new
    print(('Yes', 'No')[bool(len(old))])