with open('./input.txt') as file:
    nums = [int(j) for i in [i.replace('\n', '').split() for i in file.readlines()] for j in i]

nums_table = []
while (i:=nums[0]) != 0:
    nums_table.append(nums[1:i+1])
    for _ in range(i+1):
        nums.pop(0)

length = len(nums_table)
wins = [0] * length

for idx, nums in enumerate(nums_table):
    _ = []
    for i in range(1, length):
        lst = []
        max_ = length - i + 1
        for j in range(max_):
            lst.append(sum(nums[j:j+i]))
            print(lst)
        _.append(lst)
    wins[idx] = max(_)
    print()

print(wins)