with open('./input.txt') as file:
    lines = [int(i.removesuffix('\n')) for i in file.readlines()]
    nums = [lines[2*i:2*i+2] for i in range(int(len(lines)/2))]

with open('./output.txt', 'w') as file:
    file.writelines('\n'.join(round(p**(1/n)) for n, p in nums))