with open('./input.txt') as file:
    strings = [i.split() for i in file.readlines()]

def new_string(strings: list[str]) -> str:
    string = strings[0][:3]
    _ = 0
    for i in strings[1]:
        if _ == 5:
            break
        if i not in string[:3]:
            string += i
            _ += 1
    return string

with open('./output.txt', 'w') as file:
    file.writelines('\n'.join(new_string(i) for i in strings))