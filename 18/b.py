direction_to_delta = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, -1),
    'D': (0, 1)
}

def shoelace(points):
    """
    Compute the area of a polygon using the Shoelace formula.

    points: list of (x, y) tuples in polygon order
    """
    n = len(points)
    area = 0

    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]  # wrap around to first point

        area += x1 * y2
        area -= y1 * x2

    return abs(area) / 2

with open('input.txt') as input:
    steps = [line.split() for line in input.read().splitlines()]
    points = []
    current = (0, 0)
    perimeter = 0

    for (dir, size, _) in steps:
        (ox, oy) = direction_to_delta[dir]
        points.append(current)
        current = (current[0] + int(size) * ox, current[1] + int(size) * oy)
        perimeter += int(size)

    print(shoelace(points) + perimeter // 2 + 1)
