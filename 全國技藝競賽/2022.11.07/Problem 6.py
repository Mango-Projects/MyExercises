from sys import stdin, stdout

data_input = stdin.read().splitlines()
data_count = int(data_input[0])

for data in data_input[1:data_count+1]:
    even_number = sum(map(int, data[::2]))
    odd_number = sum(map(int, data[1::2]))
    stdout.write(f'{int((delta:=even_number - odd_number) == 0 or not delta % 11)}'+'\n')