from sys import stdin, stdout

'''
testdata

3
A123456789
A123456788
A223499999
*--------------*
2
A107386817
A116673574
'''

data_input = stdin.read().splitlines() 
data_count = int(data_input[0])
for data in data_input[1:data_count+1]:
    data = data.replace(data[0], f'{ord(data[0])-55}')
    _sum = 0
    for char, multiple_number in zip(data, (1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1)):
        _sum += int(char) * multiple_number
    stdout.write(f'{int(not _sum % 10)}\n')