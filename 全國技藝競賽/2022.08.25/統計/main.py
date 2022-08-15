with open('./input.txt') as file:
    numbers = []
    for i in map(int, file.readline().split(', ')):
        if i == 0:
            break
        numbers.append(i)
    print(numbers)

def statistics(numbers: list[int]) -> tuple[int]:
    _len = len(numbers)
    average = round(sum(numbers) / _len, 1)
    variance = round(1/_len*sum((i-average)**2 for i in numbers), 2)
    _ = _len//2
    median = numbers[_:_+1] if _len % 2 else [numbers[_]]
    _ = {numbers.count(i): set() for i in numbers}
    for i in numbers:
        _[numbers.count(i)].add(i)
    mode = _[max(_)]
    return {'平均數': average, '變異數': variance, '中位數': median, '眾　數': mode}

with open('./output.txt', 'w', encoding='utf8') as file:
    file.writelines('\n'.join(f'{k}：{v if isinstance(v, int | float) else " ".join(map(str, v))}' for k, v in statistics(numbers).items()))