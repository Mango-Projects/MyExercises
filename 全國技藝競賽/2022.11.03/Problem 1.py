data_count = int(input())
data_set = []
while len(data_set) != data_count:
    _data = input()
    if _data:
        data_set.append(_data)

# data = ['He works hard from morning till night. He is a hard worker.',
#         'I once heard him speaking in English. He is a very good speaker of English.']

for value in data_set:
    for char in {'.', ',', ':'}:
        value = value.replace(char, '')
    print(len({*value.lower().split()}))