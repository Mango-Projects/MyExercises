with open(file='./input.txt', mode='r', encoding='utf8') as rfile:
    data = rfile.readlines()[0]
    # print(data)

isBin = True if len((data_:=data.split('.'))[0]) == 20 and len(data_[1]) == 10 else False

output_data = int(data, 2) if isBin else bin(data)[2:]

with open(file='./output.txt', mode='w', encoding='utf8') as wfile:
    wfile.writelines(output_data)