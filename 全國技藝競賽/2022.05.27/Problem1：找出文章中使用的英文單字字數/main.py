with open(file='./input.txt', mode='r', encoding='utf8') as rfile:
    lines = [i_.lower() for i in rfile.readlines() if (i_:=i.replace('\n', ''))]
    for index, line in enumerate(lines):
        for symbol in ',.:':
            line = line.replace(symbol, '')
        lines[index] = line
    # print(lines)

output_lines = []
for line in lines[1:int(lines[0])+1]:
    output_lines.append(len(set(line.split())))
# print(output_lines)

with open(file='./output.txt', mode='w', encoding='utf8') as wfile:
    wfile.writelines(str(v) + ('\n' if i+1 != len(output_lines) else '') for i, v in enumerate(output_lines))