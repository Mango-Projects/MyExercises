data_count = int(input())
data_set = []
while len(data_set) != data_count:
    _data = input()
    if _data:
        data_set.append((*map(int, _data.split()), ))

for B, P, M in data_set:
    print(B**P%M)