data_count = int(input())
data_set = []
while len(data_set) != data_count:
    data_set.append((*map(int, input().split()),)[1:])

for data in data_set:
    print(f'{round(sum(data)/len(data), 2):.2f}')