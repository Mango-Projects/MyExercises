from sys import stdin, stdout

data_input = stdin.read().splitlines()
data_count = int(data_input[0])
for data in data_input[1:data_count+1]:
    score = 0
    for hit in data.split():
        hit = hit.replace('-', '0')
        if 'X' in hit:
            score += 30*hit.count('X')
        elif hit[1] == '/':
            score += int(hit[0])+10
        else:
            score += sum(map(int, hit))
    stdout.write(f'{score}\n')