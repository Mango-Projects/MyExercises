def get_factor(num):
    return [(i, num//i) for i in range(2, int(num**.5)+2) if num % i == 0] + [(1, num), (num, 1)]

with open(file="./input.txt", mode="r", encoding="utf8") as input_file:
    _, *data = [i.replace("\n", "") for i in input_file.readlines()]

result = []
for range_ in data:
    # print(list(range(*map(int, range_.split()))))
    factor_nums = (0, 0)
    min_, max_ = map(int, range_.split())
    for num in range(min_, max_+1):
        n = len(get_factor(num))
        if n > factor_nums[1]:
            factor_nums = (num, n)
        # print(num, n, factor_nums)
    result.append((range_.split(), factor_nums))

# print(result)

with open(file="./output.txt", mode="w", encoding="utf8") as output_file:
    output_file.writelines("\n".join([f'Between {i[0]} and {i[1]}, {j[0]} has a maxium of {j[1]} divisors' for i, j in result]))