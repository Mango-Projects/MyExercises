def compute(x):
    cnt = 1
    for i in range(2, x+1):
        cnt *= i
    return cnt

x = int(input())
print("{:d}!={:d}".format(x,compute(x)))