import re

with open('input.txt') as input:
    lines = input.readlines()
    seeds = re.findall(r'\d+', lines[0])
    ranges = []

    for line in lines[1:]:
        if line.strip() == '':
            continue

        if 'map' in line:
            ranges.append([])
            continue

        ranges[-1].append(
            [int(n) for n in re.findall(r'\d+', line)]
        )
    
    locations = []

    for seed in seeds:
        current = int(seed)

        for rangelist in ranges:
            for (dst, src, length) in rangelist:
                if current in range(src, src + length):
                    current = dst + (current - src)
                    break
        
        locations.append(current)

    print(min(locations))
