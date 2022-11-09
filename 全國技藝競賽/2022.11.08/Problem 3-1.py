from sys import stdin, stdout
from re import findall

"""testdata
Tom Lin's employee number is A123BSC45
The price is 45 US dollars
The machine code is 65K2
"""

for data in stdin.read().splitlines():
    if findall(r'\d[A-Z]{1,3}\d', data):
        stdout.write('有\n')
    else:
        stdout.write('沒有\n')