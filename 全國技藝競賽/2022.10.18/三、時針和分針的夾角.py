values = []
while (value:=input()) != '0:00':
    values.append(tuple(map(int, value.split(':'))))

hour_angle_delta = 360/12
minute_angle_delta = 360/12

for value in values:
    hour, minute = value
    hour_angle, minute_angle = (hour-(12*(hour>12)))*(360/12), minute*(360/60)
    print(round(abs(hour_angle-minute_angle), 4))