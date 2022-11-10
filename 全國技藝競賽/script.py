from datetime import datetime
from os import listdir

# Python Files
for i in range(1, 3):
    for j in range(1, 5):
        with open(f'Problem {j}-{i}.py', 'w', encoding='utf8') as file:
            file.write('''from sys import stdin, stdout

\'\'\'
testdata

...
\'\'\'

for data in stdin.read().splitlines():
    ...
''')

# README.md
base = f'''# {datetime.strftime(datetime.now(), r'%Y.%m.%d')}

| Title       | File                                   | Finish? |
| ----------- | -------------------------------------- | :-----: |
'''
base += '\n'.join(f'| {filename.removesuffix(".py")} | [./{filename}](./{filename.replace(" ", "%20")}) |   :x:   |' for filename in listdir() if filename.endswith('.py') and filename != 'script.py')
with open('README.md', 'w', encoding='utf8') as file:
    file.write(base)