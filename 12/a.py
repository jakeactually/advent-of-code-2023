
def count_groups(chars):
    count = 0

    for char in chars:
        if char == '#':
            count += 1
        else:
            if count > 0:
                yield count
            count = 0
    if count > 0:
        yield count

def multiplex(springs):
    if not springs:
        return [[]]

    [x, *xs] = springs

    match x:
        case '?':
            return [['#'] + s for s in multiplex(xs)] + [['.'] + s for s in multiplex(xs)]
        case _:
            return [[x] + s for s in multiplex(xs)]

with open('input.txt') as input:
    total = 0

    for line in input:
        [springs, counts] = line.strip().split(' ')
        list_springs = list(springs)
        int_counts = [int(i) for i in counts.split(',')]
        
        for m in multiplex(list_springs):
            if list(count_groups(m)) == int_counts:
                total += 1                

    print(total)
