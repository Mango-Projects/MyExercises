from itertools import permutations

with open(file='./input.txt', mode='r', encoding='utf8') as rfile:
    data: list[str] = rfile.readlines()

output_data: str = '\n'.join(f"{index+1}.　　　{''.join(value)}" for index, value in enumerate(permutations(data)))

with open(file='./output.txt', mode='w', encoding='utf8') as wfile:
    wfile.write(output_data)