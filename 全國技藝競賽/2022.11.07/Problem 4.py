from sys import stdin, stdout

data_input = stdin.read().splitlines()

for index in range(0, len(data_input), 2):
    data = data_input[index:index+2]
    stdout.write(' '.join(map(str, sorted(map(int, data[1].split()), reverse=True))) + '\n')