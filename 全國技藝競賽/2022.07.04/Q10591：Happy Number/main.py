with open('./input.txt') as file:
    times, *numbers = [int(i.replace('/n', '')) for i in file.readlines()]

isHappy = [0] * len(numbers)
for i in range(times):
    _, n = -1, numbers[i]
    while (n:=sum(int(i)**2 for i in list(str(n)))) != 1:
        if n == numbers[i]:
            _ += 1
        if _ == 1:
            break
    else:
        isHappy[i] = 1

with open('./output.txt', 'w') as file:
    file.writelines('\n'.join(f'Case #{i+1}: {k} is {"a Happy" if v else "an Unhappy"} number.' for i, k, v in zip(range(len(numbers)), numbers, isHappy)))