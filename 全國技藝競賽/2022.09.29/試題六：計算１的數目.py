from sys import stdin

num = int(stdin.read()[:-1])

nums = {i: str(i).count('1') for i in range(1, num+1) if '1' in str(i)}

string = '\n'.join(f'({i}) {v}' for i, v in enumerate(nums, 1))
print(f'１的個數：{sum(nums.values())}\n{string}')