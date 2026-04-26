import re

with open('input.txt') as input:
    lines = input.read().splitlines()
    time = int(''.join(re.findall(r'\d+', lines[0])))
    distance = int(''.join(re.findall(r'\d+', lines[1])))

    for i in range(time):
        if i * (time - i) > distance:
            print(time + 1 - i * 2)
            break
