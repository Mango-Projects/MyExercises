kb = [['q','w','e','r','t','y','u','I','o','p'],
['a','s','d','f','g','h','j','k','l']
, ['z','x','c','v','b','n','m']]
def find(c):
    global kb
    output_c = ''
    for i in range(len(kb)):
        if c in kb[i]:
            idx = kb[i].index(c)
            # print(idx)
        if idx == len(kb[i]) - 1:
            out= kb[i][idx]
        else:
            out = kb[i][idx + 1]
    return out
inp = input()
out_str = ''
for c in inp:
    if c.isupper():
        c = c.lower()
        # print(c)
        out_str += find(c).upper()
    else:
        out_str += find(c)
print(out_str)