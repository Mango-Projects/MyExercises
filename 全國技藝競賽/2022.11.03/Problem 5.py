data_count = int(input())
data_set = []
while len(data_set) != data_count:
    _data = input()
    if _data:
        data_set.append(int(_data))

for data in data_set:
    print(bin(data).count('1'))