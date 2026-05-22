direction_deltas = {
    'up': (0, -1),
    'down': (0, 1),
    'left': (-1, 0),
    'right': (1, 0)
}

forward_slash_directions = {
    'up': 'right',
    'down': 'left',
    'left': 'down',
    'right': 'up'
}

backslash_directions = {
    'up': 'left',
    'down': 'right',
    'left': 'up',
    'right': 'down'
}

def next_directions(direction, cell):
    match cell:
        case '.':
            return [direction]
        case '-':
            return ['left', 'right'] if direction in ['up', 'down'] else [direction]
        case '|':
            return ['up', 'down'] if direction in ['left', 'right'] else [direction]
        case '/':
            return [forward_slash_directions[direction]]
        case '\\':
            return [backslash_directions[direction]]

with open('input.txt') as input:
    matrix = [list(line) for line in input.read().splitlines()]
    height = len(matrix)
    width = len(matrix[0])

    beams = [(0, 0, 'right')]
    visited = set()

    while beams:
        x, y, direction = beams.pop()

        if (x, y, direction) in visited:
            continue

        if not (0 <= x < width and 0 <= y < height):
            continue

        for nd in next_directions(direction, matrix[y][x]):
            dx, dy = direction_deltas[nd]
            beams.append((x + dx, y + dy, nd))
        
        visited.add((x, y, direction))

    coords = set((x, y) for x, y, _ in visited)
    print(len(coords))
