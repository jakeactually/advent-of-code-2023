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
    is_part_number = False
    buffer = ''
    total = 0

    for y in range(height):
        width = len(matrix[y])

        for x in range(width):
            chr = matrix[y][x]

            if chr.isdigit():
                neighbors = [
                    matrix[y + dy][x + dx] for dx, dy in neighbors_offsets if is_coord_in_limits(x + dx, y + dy, width, height)
                ]

                if not all(neighbor == '.' or neighbor.isdigit() for neighbor in neighbors):
                    is_part_number = True

                buffer += chr
            
            if not chr.isdigit():
                if is_part_number:
                    total += int(buffer)
                
                buffer = ''
                is_part_number = False
    
    print(total)
