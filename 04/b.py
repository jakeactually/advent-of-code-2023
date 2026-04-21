import re

with open('input.txt') as input:
    total = 0

    for line in input:
        digits = re.findall(r'\d+', line)
        winning = digits[1:11]
        candidates = digits[11:]
        common = set(winning) & set(candidates)
        value = pow(2, len(common) - 1) if common else 0
        total += value

    print(total)
