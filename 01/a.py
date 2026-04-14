import re

with open('input.txt') as input:
    sum = 0
    for line in input:
        digits = re.findall(r'\d', line)
        number = int(digits[0] + digits[-1])
        sum += number
    print(sum)
