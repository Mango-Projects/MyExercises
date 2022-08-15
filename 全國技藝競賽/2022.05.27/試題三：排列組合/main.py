import itertools

with open(file='./input.txt', mode='r', encoding='utf8') as rfile:
    data = rfile.readlines()[0]

output_data = '\n'.join(f"{index+1}.　　　{''.join(value)}" for index, value in enumerate(itertools.permutations(data)))

with open(file='./output.txt', mode='w', encoding='utf8') as wfile:
    wfile.write(output_data)