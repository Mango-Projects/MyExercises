# from os import mkdir
# from os.path import isdir

# for i in range(1, 8):
#     if not isdir(f'./Problem {i}'):
#         mkdir(f'./Problem {i}')
#         with open(f'./Problem {i}/main.py', 'w') as file:
#             file.write('from sys import stdin\n')

# =====================================================================

from os import listdir
from os.path import isdir

for dirname in listdir('.'):
    if isdir(f'./{dirname}'):
        with open(f'./{dirname}/main.py', encoding='utf8') as file:
            code_data = file.read()
        with open(f'./{dirname}.py', 'w', encoding='utf8') as file:
            file.write(code_data)