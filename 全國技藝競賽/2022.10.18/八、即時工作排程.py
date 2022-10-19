"""
2022.10.1 finish
"""
# times = int(input())
# data = []
# for i in range(times):
#     name, *value = input().split(' ')
#     data.append((name, *map(int, value)))
data = [('A1', 3, 3, 30, 8), ('A2', 6, 4, 25, 4), ('A3', 4, 5, 30, 4), ('A4', 8, 3, 30, 1)] # testdata

waiting = sorted(data, key=lambda item: item[4])
finish = []
step = 1
working = []
while step:=step+1:
    print(f'\n{"-"*50}\n{waiting}\n{finish}\n{step}\n{working}')
    if not (waiting or working):
        print('no waiting')
        break
    if working:
        print('has working')
        if working[1]+working[2] < step:
            print(f'working {working}')
            continue
        print(f'finish {working}')
        finish.append(working)
        working = []
        continue
    for index, task in enumerate(waiting):
        if step >= task[1]:
            working = task
            waiting.pop(index)
            print(f'find task {working}, start:{working[1]}, runtime:{working[2]}, deadline:{working[3]}, priority:{working[4]}')
            break
print(f'\n{"-"*50}\n')
print(' '.join(item[0] for item in finish))