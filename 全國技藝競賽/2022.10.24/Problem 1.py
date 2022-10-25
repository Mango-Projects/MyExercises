values = []
while (value:=input()) != '0 0':
    values.append([*map(int, value.split())])

for a, b in values:
    while all((a, b)):
        if a > b:
            a %= b
        else:
            b %= a
    print(max((a, b)))