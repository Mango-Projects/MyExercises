with open(file='./input.txt', mode='r', encoding='utf8') as rfile:
    commands = [i.replace('\n', '') for i in rfile.readlines()]
    print(commands)
    command_table = {}