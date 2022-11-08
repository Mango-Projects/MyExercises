from typing import Union

def insert(box: list, x: int) -> list:
    # print('>> 0')
    return sorted(box + [x])
    # return box + [x]

def inquire(box: list, k: int) -> Union[list, int]:
    # print('>> 1')
    if k > len(box):
        return sorted(box)
        # return box
    print(sorted(box, reverse=True)[k-1])
    return sorted(box)
    # return box

def clean(box: list=None, *unused) -> list:
    # print('>> 2')
    return []

def end(box: list=None, *unused) -> None:
    # print('>> 3')
    return None

cmd_table = {
    "Insert": insert,
    "Inquire": inquire,
    "Clean": clean,
    "End": end
}

# box = clean()
# while True:
#     cmd, *arg = input().split()
#     box = cmd_table.get(cmd)(box, arg)
#     if box is None:
#         break

## test code
input_cmd = [("Insert", 4), ("Inquire", 1), ("Insert", 1), ("Inquire", 2), ("Insert", -3), 
             ("Insert", 3), ("Insert", 7), ("Insert", -99), ("Inquire", 4), ("Clean", ), 
             ("Insert", 3), ("Inquire", 2), ("Inquire", 1), ("End", )]

box = clean()
i = 0
while True:
    cmd, *arg = input_cmd[i]
    # print(cmd, arg, '\t', box, end='\t-> ')
    box = cmd_table.get(cmd)(box, *arg)
    # print(box)
    if box is None:
        break
    i += 1