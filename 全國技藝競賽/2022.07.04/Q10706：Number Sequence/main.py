"""
string (n) = '1' + '12' + '123' + ... + ''.join(str(i) for i in range(n))
len of string = sum(i//10 for i in range(n))

string (10) = 1 + 12 + 123 + 1234 + 12345 
            + 123456 + 1234567 + 12345678 + 123456789 + 12345678910









"""
from math import log10

with open('./input.txt') as file:
    lines = [int(i.replace('\n', '')) for i in file.readlines()]
runtime, *lines = lines
