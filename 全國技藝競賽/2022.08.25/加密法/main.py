with open('./input.txt') as file:
    data = file.readline()

def encryption(string: str, digit: int = 3) -> str:
    for item in string:
        yield chr(ord(item) ^ 2**digit-1)

with open('./output.txt', 'w') as file:
    for i in encryption(data):
        file.write(i)