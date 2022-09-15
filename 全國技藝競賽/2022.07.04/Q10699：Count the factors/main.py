with open('./input.txt') as file:
    numbers = file.read().splitlines()

def is_prime(n):
    if n == 2 or n == 3:
        return 1
    if (_:=n % 6) != 1 and _!=5:
        return 0
    for i in range(5, int(n**.5)+1, 6):
        if not (n%i and n%(i+2)):
            return 0
    return 1

numbers_result = []
for num in numbers[:-1]:
    prime_list = [i for i in range(2, num//2+1) if is_prime(i)]
    factor = {i for i in prime_list if not num % i}
    numbers_result.append(len(factor) + (is_prime(num)))

with open('./output.txt', 'w') as file:
    file.write('\n'.join(f'{a} : {b}' for a, b in zip(numbers, numbers_result)))