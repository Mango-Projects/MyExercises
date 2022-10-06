from sys import stdin

string = stdin.read()[:-1]
# string = 'a9sj2k13ckdi7'

print(len(tuple(filter(str.isdigit, string))))