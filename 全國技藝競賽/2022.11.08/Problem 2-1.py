from sys import stdin, stdout

data_input = stdin.read().splitlines()

def step(number_array: list[int]) -> bool:
    while True:
        number_array.sort(reverse=True)
        for index, number in enumerate(number_array[1:]):
            number = number-number_array[0]
            print()
            if number < 0:
                return False
            number_array[index+1] = number
        number_array.pop(0)
        if set(number_array) == {0}:
            return True

for data in data_input:
    data = [*map(int, data.replace(',', '').split())]
    if step(data):
        stdout.write('正確\n')
    else:
        stdout.write('不正確\n')