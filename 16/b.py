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

    def energized(x, y, direction):
        beams = [(x, y, direction)]
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

        return set((x, y) for x, y, _ in visited)
    
    top_edge = [(x, 0, 'down') for x in range(width)]
    right_edge = [(width - 1, y, 'left') for y in range(height)]
    bottom_edge = [(x, height - 1, 'up') for x in range(width)]
    left_edge = [(0, y, 'right') for y in range(height)]
    all_edges = top_edge + right_edge + bottom_edge + left_edge

    print(max(
        len(energized(x, y, direction)) for x, y, direction in all_edges
    ))
