with open('./input.txt') as file:
    n = number = int(file.readlines()[0])

prime_factor = []

for i in range(2, n//2+1):
    for j in range(2, int(i**.5)+1):
        if not i % j:
            break
    else:
        while not n % i:
            n /= i
            prime_factor.append(i)

with open('./output.txt', 'w') as file:
    file.write(f'{number}= {"*".join(map(str, prime_factor))}')