from sys import stdin

count, *data = stdin.read().splitlines()
# print(count, data, sep='\n')
# # count, data = 5 ,['160 165', '175 180', '170 173', '174 178', '165 171']
# print(data[:count])
data = {dad: son for dad, son in [map(int, i.split(' ')) for i in data[:int(count)]]}

# data = {160: 165,
#         175: 180,
#         170: 173,
#         174: 178,
#         165: 171}

X, Y = data.keys(), data.values()
length = len(data)
x_ = sum(X)/length
y_ = sum(Y)/length

r = sum((x-x_)*(y-y_) for x, y in zip(X, Y))/(sum((x-x_)**2 for x in X)**.5*sum((y-y_)**2 for y in Y)**.5)

print(round(r, 3))