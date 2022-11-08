# times = int(input())
# values = [(*map(int, input().split()),) for _ in range(times)]

values = [(2, 4, 6, 8), (2, 4, 8, 16)] # testdata

for val in values:
    a = g = 0
    _a, _g = val[1] - val[0], val[1] / val[0]
    if all([val[i+1] - val[i] == _a for i in range(3)]):
        print(f'A {_a}')
        continue
    print(f'G {(_g, int(_g))[_g.is_integer()]}')