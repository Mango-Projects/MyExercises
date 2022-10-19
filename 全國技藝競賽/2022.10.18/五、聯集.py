"""
2022.10.19 finish
"""
values = []
while (value:=input()) != '0 0':
    values.append([int(i) for i in value.split(' ')])

for value in values:
    range_value = range(value[0], value[1]+1)
    sets = {number: {*filter(lambda i: not i % number, range_value)} for number in (2, 3, 5)}
    print(len([i for i in sets[2]|sets[3]|set[5]]))