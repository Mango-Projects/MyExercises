length, array = int(input()), [*map(int, input().split())]

max_ = max(array, key=array.count)

if (array.count(max_) > len(array) / 2):
    print(max_)
else:
    print("error")