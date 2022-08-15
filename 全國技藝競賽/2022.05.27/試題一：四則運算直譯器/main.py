with open(file='./input.txt', mode='r', encoding='utf8') as rfile:
    string = rfile.readlines()[0]
    # print(string)

# string_slice = [v if i%2 else float(v) for i, v in enumerate(string.split())]
# print(string_slice)
# print()

# while True:
#     if any(i in string_slice for i in '*/+-'):
#         for symbol in '*/+-':
#             for i in range(string_slice.count(symbol)):
#                 index = string_slice.index(symbol)
#                 print(string_slice)
#                 print(f'{index}, {string_slice[index-1]} {symbol} {string_slice[index+1]} = {eval(f"{string_slice[index-1]} {symbol} {string_slice[index+1]}")}')
#                 string_slice = string_slice[:index-1] + \
#                                [eval(f'{string_slice[index-1]} {symbol} {string_slice[index+1]}')] + \
#                                string_slice[index+2:]
#                 print(string_slice, '\n')
#     else:
#         break

with open(file='./output.txt', mode='w', encoding='utf8') as wfile:
    wfile.write(str(round(eval(string), 5)))

for k, v in globals().copy().items():
    if k[:2] == '__' and k[-2:] == '__':
        continue
    print(f'{k}: {v}')