from sys import stdin, stdout
from re import sub, findall

"""
testdata

true==false!=false
true!=true==false==true==false
false==false!=true!=true!=false==true
false!=false==true==false==true!=false==true!=false
"""

for data in stdin.read().splitlines():
    data = data.replace('t', 'T').replace('f', 'F')
    data = '('*len(findall(r'==|!=', data)) + sub(r'(==|!=)', r')\1', data)
    stdout.write(f'{("FALSE","TRUE")[eval(data)]}\n')