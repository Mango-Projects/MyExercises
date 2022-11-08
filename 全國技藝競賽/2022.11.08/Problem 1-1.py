from sys import stdin, stdout
from re import findall
from collections import Counter
from string import ascii_uppercase

"""
Just ask a Chinese fruit farmer who now has to pay people to pollinate apple trees because there are no
longer enough bees to do the job. And it's not just the number of bees that are rapidly dwindling. As a
direct result of human activity, species are becoming extinct at a rate 1,000 times greater than the natural
average.
"""

data_input = stdin.read().splitlines()
data_count = int(data_input[0])

data = findall(r'[A-Z]', ''.join(data_input[1:data_count+1]).upper())
counter = Counter(data)

for index in range(0, len(ascii_uppercase), 5):
    stdout.write(f'{" ".join(f"({char}, {counter[char]})" for char in ascii_uppercase[index:index+5])}\n')