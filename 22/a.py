import re
from itertools import combinations

def points_in_line(bounds):
    _, start, end = bounds
    x1, y1, _ = start
    x2, y2, _ = end

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            yield x, y

with open('input.txt') as input:
    bricks = []

    for i, line in enumerate(input.readlines()):
        start, end = (list(map(int, re.findall(r'\d+', part))) for part in line.split('~'))
        bricks.append((chr(i + 97), start, end))

    supported = {}
    supporting = {}

    for c in combinations(bricks, 2):
        a, b = c

        a_points = set(points_in_line(a))
        b_points = set(points_in_line(b))

        if a_points & b_points:
            tag = a[0]

            if tag not in supported:
                supported[tag] = []

            supported[tag].append(b)

    for k in supported:
        print(k, supported[k])
