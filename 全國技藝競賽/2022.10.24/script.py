from datetime import datetime
from os import listdir

# Python Files
for i in range(7):
    with open(f'Problem {i+1}.py', 'w', encoding='utf8'):
        pass

# README.md
base = f'''# {datetime.strftime(datetime.now(), r'%Y.%m.%d')}

|Title|File|Finish?|
|---|---|:-:|
'''
base += '\n'.join(f'|{filename.removesuffix(".py")}|[./{filename}](./{filename.replace(" ", "%20")})|:x:|' for filename in listdir() if filename.endswith('.py'))
with open('README.md', 'w', encoding='utf8') as file:
    file.write(base)