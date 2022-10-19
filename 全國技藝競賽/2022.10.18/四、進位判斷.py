"""
2022.10.19 finish
"""
values = []
while (value:=input()) != '0 0':
    values.append(sorted(value.split(' '), key=len)) # a < b

print(values)

for value in values:
    """
       a
     + b
    -----
    """
    a, b = value
    sum_ab = str(sum(map(int, value)))
    carry_times = int(len(sum_ab) > len(b))
    for i in range(-1, -len(b), -1):
        if sum_ab[i] < a[i]:
            carry_times += 1
    print(carry_times)