from sys import stdin, stdout

data_input = stdin.read().splitlines()

line, start_number = [*map(int, data_input[0].replace(',', ' ').split())], int(data_input[1])

"""
5, 3, 7, 11, 4, 2, 1, 8, 9
8
"""

class CircleList(list):
    def get(self, i):
        item = self.__getitem__(i % self.__len__())
        return item

circle_list = CircleList(line)
first_index = circle_list.index(start_number)

for i in range(len(circle_list)-1):
    item = circle_list.get(first_index+i)
    circle_list.remove(item)
stdout.write(f'{circle_list[0]}')