from sys import stdin, stdout
from re import sub, findall

"""
testdata

true==false==a==true!=false
a!=false==true!=false==true
false==true==true!=false!=true!=false==a==true
true==false==true!=false==a
"""

for data in stdin.read().splitlines():
    data = data.replace('t', 'T').replace('f', 'F')
    data = '('*len(findall(r'==|!=', data)) + sub(r'(==|!=)', r')\1', data)
    for i in (True, False):
        a = i
        if eval(data) == True:
            stdout.write(f'{a}\n'.upper())