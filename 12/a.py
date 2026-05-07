
import re

def out(springs, in_group, groups, counts):
    if not springs or not counts:
        print(groups, springs, counts)
        return

    [x, *xs] = springs

    match x:
        case '#':
            [*gs, g] = groups if in_group else [*groups, 0]
            if g < counts[0]:
                out(xs, True, [*gs, g + 1], counts)
        case '.':
            if in_group:
                if groups[-1] == counts[0]:
                    out(xs, False, groups + [], counts[1:])
            else:
                out(xs, False, groups.copy(), counts)
        case '?':
            out(['.', *xs], in_group, groups.copy(), counts)
            out(['#', *xs], in_group, groups.copy(), counts)

with open('12/input.txt') as input:
    springs = list('?###????????')
    counts = [3,2,1]

    out(springs, False, [], counts)
