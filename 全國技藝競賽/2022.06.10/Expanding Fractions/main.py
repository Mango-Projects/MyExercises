a, b = map(int, input().split())

nums = str(a/b)[2:]

print(nums)

if len(nums) < b:
    print(a/b)

# with open(file="./input.txt", mode="r", encoding="utf8") as file:
#     ...

# with open(file="./output.txt", mode="w", encoding="utf8") as file:
#     ...