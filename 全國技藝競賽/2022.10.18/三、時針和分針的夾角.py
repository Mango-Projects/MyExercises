"""
2022.10.19 finish

angle_minute = minute * 6
angle_hour = hour * 30
if minute != 0:
    angle_hour += minute/2
"""

values = []
while (value:=input()) != '0:00':
    values.append(tuple(map(int, value.split(':'))))

# values = [(12, 0), (9, 0), (8, 10)] # testdata

print()

for value in values:
    hour, minute = value
    angle_minute = minute * 6
    angle_hour = hour * 30
    if minute != 0:
        angle_hour += minute/2
    
    delta_angle = _ if (_:=abs(angle_hour-angle_minute)) < 180 else 360 - _
    print(f'{delta_angle:.3f}')

