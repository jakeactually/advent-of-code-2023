import os
import sys

TEMPLATE = '''
import re

with open('input.txt') as input:
    print(input)
'''

day = sys.argv[1]
folder = day.zfill(2)

os.makedirs(folder)

for part in (1, 2):
    content = TEMPLATE
    with open(os.path.join(folder, 'a.py' if part == 1 else 'b.py'), 'w') as f:
        f.write(content)

with open(os.path.join(folder, 'input.txt'), 'w') as f:
    f.write('')
