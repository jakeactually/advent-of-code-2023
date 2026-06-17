from collections import deque

diagonals = [
    (1, 1),
    (-1, 1),
    (1, -1),
    (-1, -1),
]

cardinals = [
    (0, 2),
    (0, -2),
    (2, 0),
    (-2, 0),
]

all_dirs = [*diagonals, *cardinals]

with open('input.txt') as input:
    matrix = [list(line) for line in input.read().splitlines()]
    height = len(matrix)
    width = len(matrix[0])
    walkers = deque()

    for y in range(height):
        for x in range(width):
            if matrix[y][x] == 'S':
                walkers.append((x, y, 0))

    visited = set()

    while walkers:
        walker = walkers.popleft()
        wx, wy, distance = walker

        if (wx, wy) in visited or distance > 32:
            continue

        visited.add((wx, wy))

        for ox, oy in all_dirs:
            ax, ay = wx + ox, wy + oy

            if 0 <= ax < width and 0 <= ay < height and matrix[ay][ax] == '.':
                valid = True

                if (ox, oy) in diagonals:
                    if matrix[wy][ax] != '.' and matrix[ay][wx] != '.':
                        valid = False

                if (ox, oy) in cardinals:
                    if matrix[wy + oy // 2][wx + ox // 2] != '.':
                        valid = False

                if valid:
                    walkers.append((ax, ay, distance + 1))

    print(len(visited))
