n=input()
inp=input().split(' ')
for i in range(len(inp)):
    if inp.count(inp[i]) > len(inp)/2:
        print(inp[i])
        exit()
print('error')