from pathlib import Path

CWD = Path(__file__).parent

with open(CWD / "read.txt") as file:
    file_data = [*map(int, file.read().splitlines())]

input_data = [int(input()) for _ in range(4)]

output = "\n".join(map(str, sorted(file_data + input_data)))

print(output)

with open(CWD / "write.txt", "w") as file:
    file.write(output)