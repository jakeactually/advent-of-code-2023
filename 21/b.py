# https://www.reddit.com/r/adventofcode/comments/18nevo3/comment/l02tjtl/

from collections import deque
from itertools import product
from operator import itemgetter

OFFSETS = sorted(product((-1, 0, 1), repeat=2), key=itemgetter(1))

def add_points(a, b):
    return a[0] + b[0], a[1] + b[1]

def neighbors(
    center,
    num_directions=8,
    *,
    max_size = None,
    max_x_size = None,
    max_y_size = None,
    diagonals=False,
):
    assert num_directions in {4, 8, 9}
    if diagonals:
        assert num_directions == 4, "diagonals can only be used in 4-directional mode"

    # one or the other
    if max_size:
        assert not (max_x_size or max_y_size), "specify only max_size OR max_DIM_size"
    if max_x_size or max_y_size:
        assert not max_size, "specify only max_size OR max_DIM_size"

    is_bounded = max_size or max_x_size or max_y_size

    for offset_x, offset_y in OFFSETS:
        if diagonals and not (offset_x and offset_y):
            continue

        if num_directions == 4 and not diagonals and offset_x and offset_y:
            # diagonal; skip
            continue

        if num_directions != 9 and not (offset_x or offset_y):
            # skip self
            continue

        next_x, next_y = add_points(center, (offset_x, offset_y))

        if is_bounded and (next_x < 0 or next_y < 0):
            continue

        if max_size and (next_x > max_size or next_y > max_size):
            continue

        if max_x_size and (next_x > max_x_size):
            continue

        if max_y_size and (next_y > max_y_size):
            continue

        yield (next_x, next_y)

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

    def num_points_where(f) -> int:
        return sum(f(v) for v in visited.values())

    while queue:
        distance, point = queue.popleft()

        if point in visited:
            continue

        visited[point] = distance

        for n in neighbors(point, num_directions=4):
            if n in visited or n not in plot_locations:
                continue

            queue.append((distance + 1, n))

    distance_to_edge = grid_size // 2
    assert (
        distance_to_edge == 65
    ), f"unexpected distance to edge, got {distance_to_edge}"

    part_1 = num_points_where(lambda v: v < distance_to_edge and v % 2 == 0)

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