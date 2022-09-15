with open(file='./input.txt', mode='r', encoding='utf8') as rfile:
    data: list[str] = rfile.readlines()

output_data: str = str(''.join(map(str,range(1,int(data)+1))).count('1'))
output_data += ('\n' + '\n'.join(f'({index}) {value}' for index, value in enumerate(str(i) for i in range(1, int(data)+1) if '1' in (str(i)))))

with open(file='./output.txt', mode='w', encoding='utf8') as wfile:
    wfile.write(output_data)