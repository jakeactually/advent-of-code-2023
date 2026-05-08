# https://www.reddit.com/r/adventofcode/comments/18ge41g/comment/kefgbn7/

import re
from functools import lru_cache

spring_regex = re.compile(r'#+')
springs_regex = re.compile(r'#+\.')

@lru_cache(maxsize=None)
def count_poss(pos, hints):
    if '?' not in pos:
        return tuple(len(s) for s in spring_regex.findall(pos)) == hints
    
    i = pos.index('?')
    sb_matches = springs_regex.finditer(pos[:i + 1])
    springs_before = [{'end': m.end(), 'size': len(m.group()) - 1} for m in sb_matches]
    sbl = len(springs_before)
    old_hints, new_hints = hints[:sbl], hints[sbl:] 

    if tuple(s['size'] for s in springs_before) != old_hints:
        return 0

    j = 0 if sbl == 0 else springs_before[-1]['end']
    before, after = pos[j : i], pos[i + 1:]

    return sum([
        count_poss((before + '.' + after).strip('.'), new_hints),
        count_poss((before + '#' + after).strip('.'), new_hints),
    ])
    
with open('input.txt') as input:
    total = 0

    for line in input:
        [springs, counts] = line.strip().split(' ')
        int_counts = tuple(int(i) for i in counts.split(',')) * 5
        total += count_poss('?'.join([springs] * 5), int_counts)

    print(total)
