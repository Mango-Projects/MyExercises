def compute(n):
    A= []
    for i in range(1, n):
        s = str(i)
        k = len(s)
        cnt = 0
        for j in range(k):
            cnt += int(s[j]) ** k
        if cnt == i:
            A.append(i)
    return A

n = int(input())
A = compute(n)
sum = 0
for x in A:
    print(x)
sum += x
print(sum)