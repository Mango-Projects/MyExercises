with open(file='./input.txt', mode='r', encoding='utf8') as rfile:
    string: list[str] = rfile.readlines()

with open(file='./output.txt', mode='w', encoding='utf8') as wfile:
    wfile.write(str(round(eval(string), 5)))