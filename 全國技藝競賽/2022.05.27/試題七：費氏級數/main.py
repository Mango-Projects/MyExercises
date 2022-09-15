with open(file='./input.txt', mode='r', encoding='utf8') as rfile:
    data: list[str] = rfile.readlines()

def fib(n: int) -> int:
    return n if n < 2 else fib(n-1) + fib(n-2)

output_data: str = '\n'.join(f'({index+1}) {value}' for index, value in enumerate([fib(i) for i in range(1, int(data)+1+3)][3:])) # +3 -> start with 3

with open(file='./output.txt', mode='w', encoding='utf8') as wfile:
    wfile.write(output_data)