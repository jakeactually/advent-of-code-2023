direction_to_delta = {
    '0': (1, 0),
    '2': (-1, 0),
    '3': (0, -1),
    '1': (0, 1)
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
    hex_numbers = [line[-8:-1] for line in input.read().splitlines()]
    points = []
    current = (0, 0)
    perimeter = 0

    for hex_num in hex_numbers:
        dir = hex_num[-1]
        size = int(hex_num[1:-1], 16)

        (ox, oy) = direction_to_delta[dir]
        points.append(current)
        current = (current[0] + size * ox, current[1] + size * oy)
        perimeter += size

    print(shoelace(points) + perimeter // 2 + 1)
