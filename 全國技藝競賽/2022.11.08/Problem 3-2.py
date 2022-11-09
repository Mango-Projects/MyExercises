from sys import stdin, stdout
from re import findall

"""testdata
His ID number is A120441768
Her ID number is B272857734
Their ID number is E286585485, E282467997, and E195445887
"""

def print(*strings, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, strings))+end)

def replace(string, /, **target_map):
    for target, value in target_map.items():
        string = string.replace(target, value)
    return string

for data in stdin.read().splitlines():
    ID_numbers = findall(r'[ABE][12]\d{8}', data)
    if ID_numbers:
        flag = False
        for ID_number in ID_numbers:
            ID_number = replace(ID_number, A='10', B='11', E='14')
            sum_number = 0
            for digit, multiple_number in zip(map(int, ID_number), (1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1)):
                sum_number += digit*multiple_number
            if not sum_number % 10:
                flag = True
        print('有' if flag else '沒有')
    else:
        print('沒有')