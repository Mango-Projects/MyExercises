"""
2022.10.19 finish
"""
values = []
while (value:=input()) != '0':
    values.append((int(value), [*map(int, input().split(' '))]))

for value in values:
    target_height = sum(value[1])//value[0]
    move_times = 0
    for item_height in value[1]:
        if item_height > target_height:
            move_times += target_height - item_height
    print(abs(move_times))