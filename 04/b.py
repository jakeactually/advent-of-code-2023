import re

with open('input.txt') as input:
    total = 0
    cache = {}

    for line in input:
        digits = re.findall(r'\d+', line)
        winning = digits[1:11]
        candidates = digits[11:]
        common = set(winning) & set(candidates)
        cache[digits[0]] = len(common)

    def get_value(key):
        if key in cache:
            start = int(key) + 1
            end = start + cache[key]
            return 1 + sum(
                get_value(f'{k}') for k in range(start, end)
            )
        return 0
    
    print(sum(get_value(k) for k in cache))
