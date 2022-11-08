data_set = []
while (_data := input()) != '0':
    data_set.append((int(data), {'too high': 1, 'too low': -1}.get(input(), 0)))

answer = [(item[0], index) for index, item in enumerate(data_set) if item[1] == 'right on']