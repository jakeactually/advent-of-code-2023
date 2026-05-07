
import re

def count_groups(chars):
    count = 0

    for char in chars:
        if char == '#':
            count += 1
        else:
            yield count
            count = 0

    yield count

def validate(springs, counts):
    for group, count in zip(count_groups(springs), counts):
        if group != count:
            return False

    return True

def multiplex(springs):
    [x, *xs] = springs

    match x:
        case '?':
            return (['.', *xs], ['#', *xs])

with open('input.txt') as input:
    springs = list('???.###')
    counts = [1,1,3]

    print(validate(list('##.##.###'), [2,2]))
