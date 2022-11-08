from sys import stdin, stdout

data_input = stdin.read().splitlines()
data_count = int(data_input[0])

for data in data_input[1:data_count+1]:
    data_split = data.split()
    stdout.write(f'{len([char for char in data_split if data_split.count(char) == 1])}\n')