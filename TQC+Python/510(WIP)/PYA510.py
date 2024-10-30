a, b = map(int, input().split(" "))

lines = [input().split(" ")[:b] for _ in range(a)]
new_lines = [i[::] for i in lines]

for row_index, row in enumerate(lines):
    for col_index, element in enumerate(row):
        try:
            if (
                lines[row_index+1][col_index] == "1" and
                lines[row_index-1][col_index] == "1" and
                lines[row_index][col_index+1] == "1" and
                lines[row_index][col_index-1] == "1"
            ):
                new_lines[row_index][col_index] = "0"
        except: pass

print("\n".join("".join([" ","*"][col] for col in map(int, row)) for row in new_lines))