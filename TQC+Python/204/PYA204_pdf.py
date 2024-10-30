a=eval(input())
b=eval(input())
op=input()
if op == "+":
    ans=a+b
    print("{:d}+{:d}={:d}".format(a,b,ans))
elif op == "-":
    ans=a-b
    print("{:d}-{:d}={:d}".format(a,b,ans))
elif op == "*":
    ans=a*b
    print("{:d}*{:d}={:d}".format(a,b,ans))
else:
    print("error")