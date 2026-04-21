from enum import Enum

class State(Enum):
    IDLE = 0
    PARSING = 1
    INVALID = 2

neighbors_offsets = [
    (-1, -1), (0, -1), (1, -1),
    (-1, 0),           (1, 0),
    (-1, 1),  (0, 1),  (1, 1)
]

def is_coord_in_limits(x, y, width, height):
    return 0 <= x < width and 0 <= y < height

with open('input.txt') as input:
    matrix = [list(line.strip()) for line in input]
    height = len(matrix)
    state = State.IDLE
    buffer = ''
    total = 0

    for y in range(height):
        width = len(matrix[y])

        for x in range(width):
            chr = matrix[y][x]

            if chr.isdigit() and state != State.INVALID:
                state = State.PARSING

                neighbors = [
                    matrix[y + dy][x + dx] for dx, dy in neighbors_offsets if is_coord_in_limits(x + dx, y + dy, width, height)
                ]

                if not all(neighbor == '.' or neighbor.isdigit() for neighbor in neighbors):
                    state = State.INVALID

                buffer += chr
            
            if not chr.isdigit():
                if state == State.PARSING:
                    total += int(buffer)
                
                buffer = ''
                state = State.IDLE
    
    print(total)
