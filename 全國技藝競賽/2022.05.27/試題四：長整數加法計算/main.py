with open(file='./input.txt', mode='r', encoding='utf8') as rfile:
    data: list[str] = [line.replace('\n','').rjust(29) for line in rfile.readlines()]

output_data: str = f'  {data[0]}\n+ {data[1]}\n{"-"*31}\n  ' + str(int(data[0]) + int(data[1]))

with open(file='./output.txt', mode='w', encoding='utf8') as wfile:
    wfile.write(output_data)