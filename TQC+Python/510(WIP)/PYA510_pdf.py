s=input().split(' ')
h,w=int(s[0]), int(s[1])
m=[]
# input
for i in range(h):
    inp=input().split(' ')
    r_list=[]
    for j in range(len(inp)):
        r_list.append(inp[j])
    m.append(r_list)
# generate output
for i in range(h):
    out=''
    for j in range(w):
        if m[i][j] == '1':
            if (i == 0) or (j == 0) or (i == h-1) or (j == w-1):
                out+='*'
            else:
                if m[i-1][j] == '0' or m[i+1][j] == '0' or m[i][j-1] == '0' or m[i][j+1] == '0':
                    out += '*'
                else:
                    out += ' '
        else:
            out += ' '
    print(out)