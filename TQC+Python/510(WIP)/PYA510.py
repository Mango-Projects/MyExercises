a, b = map(int, input().split(" "))

lines = [[*map(int, input().split(" "))][:b] for _ in range(a)]
new_lines = [i[::] for i in lines]
line_str = ""

for row_index, row in enumerate(lines):
    for col_index, element in enumerate(row):
        try:
            if (((row_index == 0 or row_index == b-1) or (col_index == 0 or col_index == a - 1)) and element == 1):
                new_lines[row_index][col_index] = 1
            elif (
                lines[row_index+1][col_index] == 0 or
                lines[row_index-1][col_index] == 0 or
                lines[row_index][col_index+1] == 0 or
                lines[row_index][col_index-1] == 0
            ):
                new_lines[row_index][col_index] = 1
        except: pass

print("\n".join("".join([" ","*"][col] for col in map(int, row)) for row in new_lines))