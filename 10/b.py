
from collections import deque

tags = {
    'F': ['top', 'left'],
    'L': ['bottom', 'left'],
    'J': ['bottom', 'right'],
    '7': ['top', 'right'],
    '|': ['top', 'bottom'],
    '-': ['left', 'right'],
}

opposite_direction = {
    'top': 'bottom',
    'bottom': 'top',
    'left': 'right',
    'right': 'left',
}

cardinals = [
    (0, -1, 'top'),
    (0, 1, 'bottom'),
    (-1, 0, 'left'),
    (1, 0, 'right'),
]

def is_point_in_bounds(x, y, width, height):
    return 0 <= x < width and 0 <= y < height

def can_connect(char1, char2, direction):
    return char2 in tags and direction in tags[char2] and opposite_direction[direction] in tags[char1]

with open('input.txt') as input:
    matrix = [list(line) for line in input]
    height = len(matrix)
    width = len(matrix[0])
    start = (0, 0)

    for y, col in enumerate(matrix):
        for x, char in enumerate(col):
            if char == 'S':
                start = (x, y)

    candidates = []

    for x, y, direction in cardinals:
        mx, my = start[0] + x, start[1] + y
        if is_point_in_bounds(mx, my, width, height):
            char = matrix[my][mx]
            if char in tags and direction in tags[char]:
                candidates.append((mx, my))

    dq = deque(candidates)

    for _ in range(len(dq)):
        current, *goals = list(dq)
        path = [start, current]

        while not any(current == goal for goal in goals):
            cx, cy = current
            current_char = matrix[cy][cx]

            for ox, oy, direction in cardinals:
                mx, my = cx + ox, cy + oy

                if is_point_in_bounds(mx, my, width, height):
                    next_char = matrix[my][mx]

                    if (mx, my) not in path and can_connect(current_char, next_char, direction):
                        current = (mx, my)
                        path.append(current)
                        break                    
            else:
                break

        print(len(path) / 2)
        dq.rotate(1)
        break
