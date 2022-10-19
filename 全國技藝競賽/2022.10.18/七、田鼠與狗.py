"""
2022.10.19 finish

d = 狗到洞的距離
m = 田鼠到洞的距離
無法逃走：d<2m
"""
values = []
while True:
    try:
        value = tuple(input().split(' '))
    except EOFError:
        break
    if value[0] == '':
        continue
    times, *xys = value
    values.append([xys, tuple(input().split(' ') for _ in range(int(times)))])
# values = [[['1.000', '1.000', '2.000', '2.00'], (['1.500', '1.500'],)], [['2.000', '2.000', '1.000', '1.000'], (['1.500', '1.500'], ['2.500', '2.500'], ['3.500', '3.500'])]] # testdata

for value in values:
    flag = False
    mouse_x, mouse_y, dog_x, dog_y = map(float, value[0])
    for hole_x, hole_y in value[1]:
        x, y = map(float, (hole_x, hole_y))
        distance_mouse_hole = ((x-mouse_x)**2+(y-mouse_y)**2)**.5
        distance_dog_hole = ((x-dog_x)**2+(y-dog_y)**2)**.5
        if distance_dog_hole > 2*distance_mouse_hole:
            flag = True
            print(f'田鼠可由({hole_x},{hole_y})的鼠洞逃走')
            break
    if flag == False:
        print('田鼠無法逃走')