a = input()

print(["No", "Yes"][a[:len(a)//2] == a[len(a)//2 + (len(a) & 1):][::-1]])