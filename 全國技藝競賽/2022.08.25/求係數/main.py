with open('./input.txt') as file:
    numbers = map(int, file.readlines())

def pascal_triangle(n):
    L = [1]
    new = []
    for i in range(n):
        new.append(L)
        L = [sum(i) for i in zip([0]+L, L+[0])]
    return new

with open('./output.txt', 'w') as file:
    file.write('\n'.join(', '.join(map(str, pascal_triangle(n+1)[n])) for n in numbers))