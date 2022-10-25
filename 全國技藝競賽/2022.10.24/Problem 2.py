times = int(input())

lengths = (len(tuple(filter(str.isdigit, input()))) for _ in range(times))

print('\n'.join(map(str, lengths)))