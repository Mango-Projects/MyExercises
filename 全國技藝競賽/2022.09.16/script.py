from os import mkdir
from os.path import isdir

for i in range(1, 8):
    if not isdir(f'./Problem {i}'):
        mkdir(f'./Problem {i}')
        with open(f'./Problem {i}/main.py', 'w') as file:
            file.write('from sys import stdin\n')