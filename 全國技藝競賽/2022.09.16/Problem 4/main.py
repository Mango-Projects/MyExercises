from sys import stdin

count, *heights = 10, 82, 53, 74, 84, 45, 46, 57, 67, 43, 47
heights = heights[:count]

length = len(heights)
heights = sorted(heights)
for a, b in zip(heights[:length//2+1], heights[-1:length//2-1:-1]):
    print(f'{a+b} = {a} + {b}')