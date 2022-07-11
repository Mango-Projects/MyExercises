with open('./input.txt') as file:
    nums = [int(j) for i in [i.replace('\n', '').split() for i in file.readlines()] for j in i]

nums_table = []
while (i:=nums[0]) != 0:
    nums_table.append(nums[1:i+1])
    for _ in range(i+1):
        nums.pop(0)

length = len(nums_table)
wins = []

for idx, nums in enumerate(nums_table):
    _ = -1
    for i in range(len(nums)):
        for j in range(i+1, len(nums)+1):
            if (n:=sum(nums[i:j])) >= _:
                _ = n
    wins.append(_)

with open('./output.txt', 'w') as file:
    file.writelines(
        '\n'.join(
            f'The maximum winning streak is {result}.' if result > 0 else 'Losing streak.' for result in wins
            )
        )