# 2022.10.18

values = []
while (value:=input()) != '0 0 0 0':
    values.append(map(int, value.split()))

for value in values:
    z, i, m, l = value
    start = l
    step = []
    while start not in step:
        l = (z*l+i)%m
        step.append(l)
    print(len(step))