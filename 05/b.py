import re
from itertools import batched

with open('input.txt') as input:
    lines = input.readlines()
    seeds = re.findall(r'\d+', lines[0])
    sections = []

    for line in lines[1:]:
        if line.strip() == '':
            continue

        if 'map' in line:
            sections.append([])
            continue

        sections[-1].append(
            [int(n) for n in re.findall(r'\d+', line)]
        )
    
    locations = []
    seed_ranges = [
        (start, start + length) for (start, length) in batched(map(int, seeds), 2)
    ]

    for range_list in sections:
        next_seed_ranges = []

        while seed_ranges:
            seed_start, seed_end = seed_ranges.pop()
            next_seed_ranges_len = len(next_seed_ranges)

            for (dst_start, src_start, length) in range_list:
                src_end = src_start + length
                dst_end = dst_start + length
                next_start = dst_start + (seed_start - src_start)
                next_end = dst_end - (src_end - seed_end)

                if src_start <= seed_start < src_end:
                    if seed_end <= src_end:
                        next_seed_ranges.append((next_start, next_end))
                    else:
                        next_seed_ranges.append((next_start, dst_end))
                        seed_ranges.append((src_end, seed_end))
                        break
                elif src_start < seed_end < src_end:
                    next_seed_ranges.append((dst_start, next_end))
                    seed_ranges.append((seed_start, src_start))
                    break
            
            if len(next_seed_ranges) == next_seed_ranges_len:
                next_seed_ranges.append((seed_start, seed_end))
        
        seed_ranges = next_seed_ranges

    print(min(fst for (fst, _) in seed_ranges))
