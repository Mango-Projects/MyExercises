# values = []
# while (value:=input()) != '0':
#     values.append((value, (*map(int, input().split()),)))

values = [(3, (1, 2, 3)), (3, (2, 3, 1))] # testdata

def InsertionSort(data):
    n = len(data)
    for i in range(n-1):
        key = data[i+1]
        j = i
        while j >=0 and key < data[j] :
                data[j+1] = data[j]
                j -= 1
        data[j+1] = key
    return data

for value in values:
    lst = [*value[1]]
    
    if sorted(lst) == lst:
        print(0)
        continue
    
    step = 0
    n = len(lst)
    for i in range(n-1):
        key = lst[i+1]
        j = i
        while j >=0 and key < lst[j] :
            lst[j+1] = lst[j]
            j -= 1
            step += 1
        lst[j+1] = key
    
    print(step)