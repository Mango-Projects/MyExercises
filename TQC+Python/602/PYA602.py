a = input()

print("".join(filter(str.isupper, a)),"".join(filter(str.islower, a)),len((*filter(str.isupper, a),)),sep="\n")