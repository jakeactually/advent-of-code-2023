# https://www.reddit.com/r/adventofcode/comments/18nevo3/comment/l02tjtl/

from collections import deque

cardinals = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]

def parse_grid(raw_grid, ignore_chars):
    result = {}
    ignore = set(ignore_chars)

    for row, line in enumerate(raw_grid):
        for col, c in enumerate(line):
            if c in ignore:
                continue

            result[row, col] = c

    return result

with open('input.txt') as input_file:
    input = input_file.read().splitlines()
    grid_size = len(input)
    grid = parse_grid(input, ignore_chars="#")
    plot_locations = set(grid)

    visited = {}
    queue = deque(
        [(0, next(k for k, v in grid.items() if v == "S"))]
    )

    def num_points_where(f):
        return sum(f(v) for v in visited.values())

    while queue:
        distance, point = queue.popleft()

        if point in visited:
            continue

        visited[point] = distance
        px, py = point

        for n in [(px + ox, py + oy) for ox, oy in cardinals]:
            if n in visited or n not in plot_locations:
                continue

            queue.append((distance + 1, n))

    distance_to_edge = grid_size // 2
    assert (
        distance_to_edge == 65
    ), f"unexpected distance to edge, got {distance_to_edge}"

    n = (26501365 - distance_to_edge) // grid_size
    assert n == 202300, f"n calc wrong, got {n}"
    num_odd_tiles = (n + 1) ** 2
    num_even_tiles = n**2

    odd_corners = num_points_where(lambda v: v > distance_to_edge and v % 2 == 1)
    even_corners = num_points_where(lambda v: v > distance_to_edge and v % 2 == 0)

    part_2 = (
        num_odd_tiles * num_points_where(lambda v: v % 2 == 1)
        + num_even_tiles * num_points_where(lambda v: v % 2 == 0)
        - ((n + 1) * odd_corners)
        + (n * even_corners)
    )

    print(part_2)
