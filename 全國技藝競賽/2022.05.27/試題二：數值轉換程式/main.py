with open(file='./input.txt', mode='r', encoding='utf8') as rfile:
    data: list[str] = rfile.readlines()

output_data: int = int(data, 2) if len((data_:=data.split('.'))[0]) == 20 and len(data_[1]) == 10 else bin(data)[2:]

with open(file='./output.txt', mode='w', encoding='utf8') as wfile:
    wfile.writelines(output_data)