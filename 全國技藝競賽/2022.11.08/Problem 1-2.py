from sys import stdin, stdout

data_input = stdin.read().splitlines()
data_count = int(data_input[0])

"""
Just ask a Chinese fruit farmer who now has to pay people to pollinate apple trees because there are no
longer enough bees to do the job. And it's not just the number of bees that are rapidly dwindling. As a
direct result of human activity, species are becoming extinct at a rate 1,000 times greater than the natural
average.
"""

words = set()
for word in ' '.join(data_input[1:data_count+1]).split():
    if word.lower().startswith('a') and word not in words:
        stdout.write(f'{word}\n')
        words.add(word)