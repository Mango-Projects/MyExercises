from datetime import datetime
from os import listdir

# Python Files
for i in range(8):
    with open(f'Problem {i+1}.py', 'w', encoding='utf8') as file:
        file.write('''from sys import stdin, stdout

data_input = stdin.read().splitlines()
data_count = int(data_input[0])
data_set = data_input[1:data_count+1]''')

# README.md
base = f'''# {datetime.strftime(datetime.now(), r'%Y.%m.%d')}

| Title     | File                               | Finish? |
| --------- | ---------------------------------- | :-----: |
'''
base += '\n'.join(f'| {filename.removesuffix(".py")} | [./{filename}](./{filename.replace(" ", "%20")}) | :x: |' for filename in listdir() if filename.endswith('.py') and filename != 'script.py')
with open('README.md', 'w', encoding='utf8') as file:
    file.write(base)