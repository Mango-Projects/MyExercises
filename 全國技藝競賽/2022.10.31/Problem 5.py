values = [(5, 0, 7, 6, 1, 0, 2, 3),
         (5, 0, 7, 6, 3, -6, 4, -3),
         (2, 0, 2, 27, 1, 5, 18, 5)]

for value in values:
    L1, L2 = value[:4], value[4:]
    a1, b1, c1 = (L1[3]-L1[1], L1[0]-L1[2], L1[2]*L1[1]-L1[0]*L1[3])
    a2, b2, c2 = (L2[3]-L2[1], L2[0]-L2[2], L2[2]*L2[1]-L2[0]*L2[3])
    print(L1, L2, ' | ', (a1, b1, c1), (a2, b2, c2))
    if (_a:=a1/a2) == b1/b2:
        if c1/c2 == _a:
            print('L')
        else:
            print('N')
    else:
        print('I')