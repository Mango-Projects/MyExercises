with open('./input.txt') as file:
    data = [tuple(map(int, line.replace('\n', '').split())) for line in file.readlines()]
runtimes = data[0][0]
datas = []
for i in range(runtimes):
    _ = [data[1:][2*i:2*i+2] for i in range(runtimes)]
    datas.append({'L': _[0][0], 'n': _[0][1], 'p': _[1]})
    

for k, v in globals().copy().items():
    print(k, v)