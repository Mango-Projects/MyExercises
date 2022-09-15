from re import sub

with open(file='./input.txt', mode='r', encoding='utf8') as rfile:
    lines = [i for i in rfile.read().splitlines() if i]

times = lines[0]
count = [len(set(sub(r'[:,.]', '', i))) for i in lines[1:]]

with open(file='./output.txt', mode='w', encoding='utf8') as wfile:
    wfile.write('\n'.join(str(i) for i in count))