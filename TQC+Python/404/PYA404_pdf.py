n1=input()
c_list=[]

for c in n1:
    c_list.append(n1.count(c))
#print(c_list)
print(n1[c_list.index(max(c_list))])
print(max(c_list)) 