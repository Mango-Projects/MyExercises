with open('./input.txt') as file:
    nums = (int(i) for i in file.readlines()[0].replace(' ','').split(',') if i != '0')

avg = sum(nums) / len(nums)
