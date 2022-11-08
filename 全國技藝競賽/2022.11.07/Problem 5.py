from sys import stdin, stdout

data_input = stdin.read().splitlines()
data_count = int(data_input[0])

for data in data_input[1:data_count+1]:
    stdout.write(f'{len([*filter(str.isalpha, data)])}\n')