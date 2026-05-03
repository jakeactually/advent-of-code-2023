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
    matrix = [list(line.rstrip('\n')) for line in input]
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

    current, *goals = candidates
    path = set([start, current])

    while not any(current == goal for goal in goals):
        cx, cy = current
        current_char = matrix[cy][cx]

        for ox, oy, direction in cardinals:
            mx, my = cx + ox, cy + oy

            if is_point_in_bounds(mx, my, width, height):
                next_char = matrix[my][mx]

                if (mx, my) not in path and can_connect(current_char, next_char, direction):
                    current = (mx, my)
                    path.add(current)
                    break

    # https://www.reddit.com/r/adventofcode/comments/18evyu9/comment/keaz25j/

    territory = 0
    is_inside = False
    starting_joint = None
    matrix[start[1]][start[0]] = 'L'

    for y in range(height):
        for x in range(width):
            tile = matrix[y][x]

            if (x, y) not in path:
                if is_inside:
                    territory += 1
            else:
                if tile == '|':
                    is_inside = not is_inside
                elif tile in ('F', 'L'):
                    starting_joint = tile
                elif tile == 'J':
                    if starting_joint == 'F':
                        is_inside = not is_inside
                    starting_joint = None
                elif tile == '7':
                    if starting_joint == 'L':
                        is_inside = not is_inside
                    starting_joint = None

    print(territory)
