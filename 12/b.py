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
    ranges = [(m.start(), m.end()) for m in springs_regex.finditer(pos[:i + 1])]
    lr = len(ranges)
    diffs = [e - s - 1 for s, e in ranges]

    if len(hints) < lr or any(d != h for d, h in zip(diffs, hints)):
        return 0

    j = 0 if lr == 0 else ranges[-1][1]
    new_hints = hints[lr:]    
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
