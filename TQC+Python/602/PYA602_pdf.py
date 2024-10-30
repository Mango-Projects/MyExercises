inp = input()
U, L = '', ''
for i in inp:
    if i.isupper():
        U += i
    else:
        L += i
print(U)
print(L)
print(len(U))