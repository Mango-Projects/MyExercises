s1 = [int(x) for x in input().split(' ')]
m1 = []
for i in range(s1[0]):
    row = [int(x) for x in input().split(' ')]
    m1.append(row)
# read matrix 2
s2 = [int(x) for x in input().split(' ')]
m2 = []
for i in range(s2[0]):
    row = [int(x) for x in input().split(' ')]
    m2.append(row)
# check size
if s1[1] != s2[0]:
    print('error')
    exit()
# count
out=[]
for i in range(s1[0]):
    row=[]
    for j in range(s2[1]):
        cnt=0
        for k in range(s1[1]):
            cnt += m1[i][k] * m2[k][j]
        row.append(cnt)
    out.append(row)
# print
for i in range(len(out)):
    for j in range(len(out [0])):
        if j != len(out [0]) - 1:
            print(out[i][j], end = ' ')
        else:
            print(out[i][j])