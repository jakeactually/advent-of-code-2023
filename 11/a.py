from itertools import combinations

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

with open('input.txt') as input:
    lines = input.read().splitlines()
    height = len(lines)
    width = len(lines[0])
    galaxies = []
    empty_rows = set(range(height))
    empty_columns = set(range(width))

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '#':
                galaxies.append((x, y))
                empty_rows.discard(y)
                empty_columns.discard(x)

    mapped = []

    for x, y in galaxies:
        empty_columns_before = len([c for c in empty_columns if c < x])
        empty_rows_before = len([r for r in empty_rows if r < y])
        mapped.append((x + empty_columns_before, y + empty_rows_before))

    total = 0

    for g1, g2 in combinations(mapped, 2):
        total += manhattan_distance(g1, g2)

    print(total)
