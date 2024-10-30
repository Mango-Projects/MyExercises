a = input()

max_ = max(a, key=a.count)

print(max_,a.count(max_),sep="\n")