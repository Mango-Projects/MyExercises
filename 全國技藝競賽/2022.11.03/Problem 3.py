data_count = int(input())
data_set = []
while len(data_set) != data_count:
    _data = input()
    if _data:
        data_set.append((*map(int, _data.split()),))

for data in data_set:
    sum_value = float('-inf')
    for index, value in enumerate(data):
        for last_index in range(len(data), index, -1):
            if (n:=sum(data[index:last_index])) > sum_value:
                sum_value = n
    print(sum_value)