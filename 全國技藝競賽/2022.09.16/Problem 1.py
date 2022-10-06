from sys import stdin

# count, *students = map(int, stdin.read().splitlines())
count, *students = [3, 8, 12, 48]
students = students[:count]

table_of_times = 1

for item in range(1, min(students)+1):
    if all([not (i % item) for i in students]):
        table_of_times = item

print(table_of_times)