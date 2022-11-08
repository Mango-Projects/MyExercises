# values = []
# while (value:=input()) != '0':
#     values.append(*map(int, input().split()))

values = [(8, 20, 27, 17, 13, 28, 35, 31), (13, 14, 55, 21, 66, 72, 23, 73, 1, 2, 88, 83, 84, 24, 7)] # testdata

for value in values:
    min_distance, flag = float('inf'), 0
    for index, a in enumerate(value):
        if index == len(value)-1:
            break
        distance = abs(a-value[index+1])
        if distance < min_distance:
            min_distance = distance
        if distance <= 1:
            flag = 1
            break
    if flag:
        print(distance)
    else:
        print(min_distance)